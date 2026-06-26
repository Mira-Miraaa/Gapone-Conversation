# **1\. Tổng quan**

## **1.1 Kiến trúc Tool Calling**

Trong kiến trúc Tool Calling  (LangChain / LangGraph), LLM (Large Language Model) không chỉ trả lời bằng text mà còn chủ động gọi các hàm (tools) để truy xuất dữ liệu thật, thực hiện hành động và kết hợp nhiều bước logic trong một hội thoại. Mỗi tool được mô tả bằng docstring \+ constraints, và LLM tự quyết định gọi tool nào, khi nào, với tham số gì.

![][image1]

**Luồng xử lý chính:** Conversation → AI Orchestrator → Tool Calls → Database/Services → Response

## **1.2 Nguyên tắc chung**

* **Không bịa dữ liệu:** Giá, tồn kho, trạng thái đơn chỉ được trả lời SAU KHI gọi tool tương ứng. Đây là hard constraint.

* **Multi-intent:** LLM có thể gọi nhiều tools trong cùng 1 turn (ví dụ: vừa search SP vừa tra đơn).

* **Hỏi làm rõ trước:** Khi thiếu thông tin để gọi tool, hỏi khách trước thay vì đoán.

* **Graceful fallback:** Khi tool lỗi, thông báo lịch sự \+ đề xuất handoff hoặc thử lại.

* **Tiếng Việt tự nhiên:** Mọi response từ bot phải ngắn gọn, dễ hiểu, gợi ý bước tiếp theo.

## **1.3 Danh sách tất cả tools (MVP)**

| \# | Tool name | Nhóm | Mô tả ngắn |
| ----- | :---- | :---- | :---- |
| 1 | search\_product | Product | Semantic search SP theo ngôn ngữ tự nhiên \+ bộ lọc |
| 2 | get\_product\_detail | Product | Lấy thông tin đầy đủ 1 variant |
| 3 | add\_to\_cart | Order | Thêm SP vào giỏ hàng |
| 4 | remove\_from\_cart | Order | Xóa 1 SP khỏi giỏ |
| 5 | view\_cart | Order | Xem nội dung giỏ hàng |
| 6 | clear\_cart | Order | Xóa toàn bộ giỏ hàng |
| 7 | start\_order\_flow | Order | Khởi động checkout multi-step |
| 8 | get\_order\_status | Order | Tra cứu trạng thái đơn hàng |
| 9 | list\_orders | Order | Liệt kê lịch sử đơn hàng |
| 10 | get\_store\_info | Info / FAQ | Truy xuất thông tin cửa hàng |
| 11 | escalate\_to\_human | Human Handoff | Chuyển sang nhân viên hỗ trợ |

## **1.4. So sánh: Intent Classification vs Tool Calling**

| Khía cạnh | Intent Classification | Tool Calling |
| :---- | :---- | :---- |
| **Triết lý** | Top-down: con người định nghĩa intent trước, LLM chỉ phân loại vào đúng hộp | Bottom-up: LLM tự chọn hành động dựa trên tools và docstring |
| **Vai trò LLM** | Classifier — bị giới hạn trong label space | Orchestrator — reasoning \+ decision-making |
| **Multi-intent** | 1 intent/turn — “xem quần và kiểm tra đơn” chỉ xử lý 1 việc | Gọi nhiều tools liên tiếp, trả lời cả hai |
| **Câu mơ hồ** | Dễ route sai — “mua quần” bị route sang ORDER agent | Tự xử lý: hỏi thêm hoặc search trước khi hành động |
| **Thêm tính năng** | Sửa 4–5 chỗ: classifier prompt, route\_map, agent, graph node, edge | Sửa 1 chỗ: thêm @tool function \+ docstring |
| **Hallucination** | Trung bình — LLM có thể bịa nếu agent không gọi tool | Thấp — data luôn từ tool thật, safety check code-level |
| **Coupling** | Tight — intent ↔ agent ↔ graph phụ thuộc chặt | Loose — tools độc lập, dễ thêm/xóa/thay thế |
| **Latency** | Thấp hơn — ít LLM reasoning | Cao hơn \~200–500ms — có reasoning \+ tool calls |
| **Control** | Deterministic routing, dễ predict | Phụ thuộc docstring, cần viết chặt |

**Case thực tế:** *User nói “tôi muốn mua quần” — Intent Classification match keyword “mua” → route sang ORDER agent (SAI vì chưa có SP cụ thể). Tool Calling đọc docstring “KHÔNG gọi khi chưa add\_to\_cart” → gọi search\_products trước (ĐÚNG).*

# 

# **2\. Product Tools**

Nhóm tools phục vụ việc tìm kiếm, xem chi tiết và gợi ý sản phẩm. Đây là nhóm được gọi thường xuyên nhất, là đầu vào cho toàn bộ funnel chuyển đổi.

**search\_products**

**Mô tả:** Tìm kiếm sản phẩm sử dụng Semantic Search (vector similarity) thay vì keyword match cứng. Khi khách hỏi bằng ngôn ngữ tự nhiên (ví dụ: “đồ gia dụng”, “quà tặng cho bạn gái”), tool sẽ tìm các sản phẩm có ngữ nghĩa liên quan (loosely overlapping) thay vì chỉ khớp chính xác category. Các bộ lọc cứng (màu, size, giá…) được áp dụng phÍa SAU semantic ranking để thu hẹp kết quả. Kết quả trả về danh sách variants còn hàng, sắp xếp theo độ phù hợp (relevance score).

| Input | query: string (câu hỏi / mô tả tự nhiên của khách — BẮT BUỘC), filters?: { category?: string, color?: string, size?: string, brand?: string, min\_price?: number, max\_price?: number }, top\_k?: number (số kết quả trả về, mặc định \= 5\) |
| :---- | :---- |
| **Output** | Array of { variant\_id: string, product\_name: string, color: string, size: string, price: number, stock\_quantity: number, image\_url: string, relevance\_score: float (0–1) } |
| **Error handling** | Không tìm thấy: hỏi thêm tiêu chí, gợi ý từ khác hoặc đề xuất SP phổ biến. DB/embedding service lỗi: thông báo lỗi \+ đề xuất thử lại hoặc handoff. |

**Trigger ví dụ**

* *“Tôi muốn mua quần đen Nike size M”*

* *“Có giày nào dưới 1 triệu không?”*

* *“Cho xem áo thun trắng”*

* *“Đồ gia dụng có gì?”*

* *“Quà tặng cho bạn gái”*

* *“Có gì mặc đi biển không?”*

* *“Sản phẩm phù hợp cho mùa đông”*

**Ví dụ hội thoại**

**KH: Tôi muốn mua quần đen Nike size M dưới 500k**

*\[Orchestrator gọi search\_products(query="quần đen Nike size M", filters={color:"đen", brand:"Nike", size:"M", max\_price:500000})\]*

**Bot: Mình tìm được 2 sản phẩm phù hợp:**

**Bot: 1\. \[var-001-1\] Quần Jean Nam Slim Fit — đen, M — 450,000đ — Còn 15**

**Bot: 2\. \[var-003-2\] Quần Jean Nam Regular — đen, M — 480,000đ — Còn 8**

**Bot: Bạn muốn xem chi tiết sản phẩm nào?**

Khác với keyword search truyền thống (khớp chính xác từ khóa vào tên/category), search\_products sử dụng semantic search để hiểu ý định của khách hàng và tìm các sản phẩm có ngữ nghĩa liên quan, kể cả khi không khớp keyword hay category.

**Vì sao cần Semantic Search?**

| Keyword Search (truyền thống) | Semantic Search (GAPCon) |
| :---- | :---- |
| Khách hỏi “đồ gia dụng” → tìm category \= “đồ gia dụng”. Nếu không có category này → 0 kết quả. | Khách hỏi “đồ gia dụng” → hiểu ngữ nghĩa → tìm được máy giặt, máy hút bụi, nồi chiên… dù chúng thuộc category “electronics” hay “kitchen”. |
| Khách hỏi “quà tặng cho bạn gái” → không match bất kỳ keyword/category nào. | Hiểu “quà tặng bạn gái” ≈ phụ kiện, thời trang nữ, mỹ phẩm… → trả về SP phù hợp. |
| Khách hỏi “đồ mặc đi biển” → không có category “đi biển”. | Hiểu ngữ cảnh → tìm được quần short, áo tank top, dép, kính mát… |

**Cách hoạt động**

* **Bước 1 — Embedding:** Biến query của khách và thông tin SP (tên \+ mô tả \+ category \+ tags) thành vector bằng mô hình embedding (ví dụ: multilingual-e5, BGE-M3, hoặc OpenAI text-embedding).

* **Bước 2 — Vector similarity:** Tìm top-K vectors gần nhất (cosine similarity) trong vector store (Qdrant, Pinecone, pgvector…).

* **Bước 3 — Post-filter:** Áp dụng các bộ lọc cứng (color, size, brand, min/max\_price) lên kết quả semantic để thu hẹp.

* **Bước 4 — Stock filter:** Loại bỏ các variants hết hàng (stock\_quantity \= 0).

* **Bước 5 — Return:** Trả về danh sách còn lại, sắp xếp theo relevance\_score giảm dần.

Query của khách là **ngôn ngữ tự nhiên tiếng Việt***. Embedding model phải hỗ trợ multilingual để hiểu đúng ngữ nghĩa tiếng Việt và các biến thể (“quần bò” \= “jean”, “đồ gia dụng” ≈ “appliance”…).*

**Ví dụ: Semantic search vượt category**

**KH: Có đồ gia dụng gì không?**

*\[Orchestrator gọi search\_products(query="đồ gia dụng")\]*

*\[Semantic search: "đồ gia dụng" ≈ appliance, household → match SP từ nhiều category\]*

**Bot: Mình tìm được mấy sản phẩm gia dụng nè:**

**Bot: 1\. \[var-101\] Máy giặt Samsung 8kg — 12,500,000đ (category: electronics)**

**Bot: 2\. \[var-205\] Máy hút bụi Dyson V8 — 8,900,000đ (category: electronics)**

**Bot: 3\. \[var-310\] Nồi chiên không dầu Philips — 2,800,000đ (category: kitchen)**

**Bot: 4\. \[var-412\] Bàn ủi hơi nước Tefal — 1,200,000đ (category: home)**

**Bot: Bạn quan tâm cái nào? Mình có thể xem chi tiết nhé\!**

**Lưu ý:** Kết quả trên đến từ 3 category khác nhau (electronics, kitchen, home) — keyword search truyền thống sẽ không tìm được vì không có category “đồ gia dụng” nào match.

**Ví dụ: Semantic search theo intent**

**KH: Gợi ý cho tôi quà tặng cho bạn gái dưới 500k**

*\[Orchestrator gọi search\_products(query="quà tặng cho bạn gái", filters={max\_price: 500000})\]*

*\[Semantic: "quà tặng bạn gái" ≈ phụ kiện nữ, thời trang nữ, mỹ phẩm, trang sức\]*

**Bot: Mình gợi ý mấy món quà phù hợp:**

**Bot: 1\. \[var-501\] Khăn lụa Hermes mini — 450,000đ (category: accessories)**

**Bot: 2\. \[var-502\] Son MAC Ruby Woo — 380,000đ (category: beauty)**

**Bot: 3\. \[var-503\] Vòng tay bạc 925 — 320,000đ (category: jewelry)**

**Lưu ý:** “Quà tặng cho bạn gái” không phải là category hay keyword nào — nhưng semantic search hiểu được intent và tìm SP phù hợp từ nhiều category.

**Hybrid approach: Semantic \+ Filters**

search\_products kết hợp 2 cơ chế:

| Thành phần | Mô tả | Ví dụ |
| :---- | :---- | :---- |
|   | Embedding query \+ cosine similarity để tìm SP có ngữ nghĩa liên quan. Cho phép loosely overlapping vượt category. | query \= "đồ gia dụng" → match máy giặt (electronics), nồi chiên (kitchen) |
|   | Áp dụng sau semantic ranking: color, size, brand, min/max\_price, stock \> 0\. Thu hẹp kết quả chính xác. | filters \= {max\_price: 500000} → loại SP \> 500k khỏi kết quả semantic |

**Thứ tự ưu tiên:** Semantic ranking trước (tìm đúng ý định) → Filters sau (thu hẹp đúng điều kiện). Nếu Orchestrator truyền cả query và filters, pipeline là: embed(query) → vector search top-K → apply filters → remove out-of-stock → return.

**Xử lý tình huống đặc biệt**

| Tình huống | Xử lý |
| :---- | :---- |
| **Query quá chung (“coi có gì hay”)** | Trả về SP bán chạy / mới nhất. Gợi ý khách nói rõ hơn. |
| **Semantic match nhưng relevance thấp (\< 0.3)** | Thông báo kết quả có thể không chính xác lắm, hỏi khách xác nhận hoặc mô tả rõ hơn. |
| **Filters loại hết kết quả semantic** | Thông báo không có SP khớp cả ý định và bộ lọc. Gợi ý nới lỏng (ví dụ: bỏ filter giá hoặc đổi size). |
| **Tiếng Việt lóng / viết tắt** | Embedding model multilingual xử lý: “quần bò” \= “jean”, “đt” \= “điện thoại”. Nếu không hiểu, hỏi làm rõ. |
| **Mix semantic \+ exact keyword** | Khách nói “Nike đen”: “Nike” match exact brand filter, “đen” match exact color, nhưng toàn bộ câu cũng được embed để semantic ranking. |

**get\_product\_detail**

**Mô tả:** Lấy thông tin đầy đủ của một variant cụ thể: mô tả sản phẩm, hình ảnh, giá hiện tại, số lượng tồn kho. Thường được gọi sau khi search trả về nhiều kết quả và khách muốn xem kỹ một sản phẩm.

| Input | variant\_id: string (BẮT BUỘC) |
| :---- | :---- |
| **Output** | { variant\_id, product\_name, sku, color, size, price, stock\_quantity, description, image\_urls: string\[\] } |
| **Error handling** | Variant không tồn tại: thông báo và gợi ý gọi search\_products lại. |

**Trigger ví dụ**

* *“Cho tôi xem chi tiết cái đầu tiên”*

* *“Mô tả sản phẩm var-001-1”*

* *“Còn bao nhiêu cái?”*

* *“Xem ảnh sản phẩm này”*

**Ví dụ hội thoại**

**KH: Cho xem chi tiết cái đầu tiên**

*\[Orchestrator gọi get\_product\_detail(variant\_id=var-001-1)\]*

**Bot: Quần Jean Nam Slim Fit**

**Bot: SKU: QJN-DEN-28 | Màu: đen | Size: 28**

**Bot: Giá: 450,000đ | Còn: 15 cái**

**Bot: Mô tả: Denim co giãn 4 chiều, thoáng mát, phù hợp mặc hàng ngày**

**Bot: Bạn muốn thêm vào giỏ hàng không?**

# **3\. Order Tools**

Nhóm tools quản lý giỏ hàng. Giỏ hàng được hiển thực dưới dạng draft order trong hệ thống GapOne. Mỗi session có tối đa 1 giỏ hàng.

**add\_to\_cart**

**Mô tả:** Thêm một variant vào giỏ hàng (draft order). Tự động tạo draft order nếu chưa có. Nếu variant đã có trong giỏ thì cộng dồn số lượng. Tự động recompute total\_amount sau mỗi lần thêm.

| Input | variant\_id: string (BẮT BUỘC), quantity: number (mặc định \= 1\) |
| :---- | :---- |
| **Output** | { success: boolean, cart\_summary: { total\_items: number, total\_amount: number }, added\_item: { name, qty, unit\_price } } |
| **Side effects** | Tạo draft order nếu chưa có. Cập nhật line\_items và total\_amount. |
| **Error handling** | Hết hàng: thông báo \+ gọi search\_products(). Số lượng yêu cầu \> tồn kho: thông báo số còn lại và hỏi khách có muốn lấy số còn không. |

**Trigger ví dụ**

* *“Thêm vào giỏ hàng”*

* *“Lấy cho tôi 2 cái”*

* *“Mua luôn cái này”*

* *“(Khách đã chọn variant cụ thể \+ đồng ý mua)”*

**Ví dụ hội thoại**

**KH: Lấy cho tôi 2 cái**

*\[Orchestrator gọi add\_to\_cart(variant\_id=var-001-1, quantity=2)\]*

**Bot: Đã thêm 2 x Quần Jean Nam Slim Fit (đen, 28\) vào giỏ.**

**Bot: Tổng giỏ hàng: 900,000đ (2 sản phẩm)**

**Bot: Bạn muốn tiếp tục mua hay đặt hàng luôn?**

**remove\_from\_cart**

**Mô tả:** Xóa một product variant khỏi giỏ hàng. Yêu cầu xác nhận từ khách hàng trước khi thực hiện và variant\_id phải hợp lệ (tồn tại trong giỏ).

| Input | variant\_id: string (BẮT BUỘC) |
| :---- | :---- |
| **Output** | { success: boolean, removed\_item: { name, qty, unit\_price }, cart\_summary: { total\_items, total\_amount } } |
| **Side effects** | Cập nhật line\_items và total\_amount của draft order. |
| **Error handling** | Variant không có trong giỏ: thông báo và hiển thị nội dung giỏ hiện tại. Giỏ trống: thông báo giỏ đang trống. |

**Trigger ví dụ**

* *“Bỏ cái quần ra khỏi giỏ”*

* *“Xóa sản phẩm đầu tiên”*

* *“Không lấy cái đó nữa”*

**Ví dụ hội thoại**

**KH: Bỏ cái áo thun ra nhé**

**Bot: Bạn muốn xóa Áo Thun Nam Basic (trắng, M) khỏi giỏ đúng không?**

**KH: Đúng rồi**

*\[Orchestrator gọi remove\_from\_cart(variant\_id=var-002-1)\]*

**Bot: Đã xóa\! Giỏ còn 1 SP, tổng: 450,000đ.**

**view\_cart**

**Mô tả:** Xem nội dung giỏ hàng hiện tại. Hiển thị live price từ ProductVariant (lấy giá mới nhất, không dùng giá cũ), tính subtotal từng item và tổng cộng. Trả về “Giỏ hàng trống.” nếu chưa có gì.

| Input | (không có tham số) |
| :---- | :---- |
| **Output** | { items: \[{ variant\_id, name, variant\_label, qty, unit\_price, subtotal }\], total\_amount } hoặc { empty: true } |

**Trigger ví dụ**

* *“Giỏ hàng của tôi có gì?”*

* *“Tổng tiền bao nhiêu?”*

* *“Xem giỏ hàng”*

* *“(Tự động gọi trước khi bắt đầu checkout)”*

**Ví dụ hội thoại**

**KH: Giỏ hàng của tôi có gì?**

*\[Orchestrator gọi view\_cart()\]*

**Bot: Giỏ hàng của bạn:**

**Bot: 1\. Quần Jean Nam Slim Fit | đen, 28 — 450,000đ × 1 \= 450,000đ**

**Bot: 2\. Áo Thun Nam Basic | trắng, M — 199,000đ × 2 \= 398,000đ**

**Bot: Tổng cộng: 848,000đ**

**Bot: Bạn muốn đặt hàng hay mua thêm?**

**clear\_cart**

**Mô tả:** Xóa TOÀN BỘ sản phẩm trong giỏ hàng cùng lúc. Dùng khi khách muốn làm trống hoặc bắt đầu lại giỏ hàng.

| Input | (không có tham số) |
| :---- | :---- |
| **Output** | { success: boolean, cleared\_items\_count: number } |
|  |  |
| **Side effects** | Xóa toàn bộ line\_items của draft order. Reset total\_amount \= 0\. |
| **Error handling** | Giỏ đã trống: thông báo giỏ đang trống, không cần xóa. |

**Trigger ví dụ**

* *“Xóa hết giỏ hàng”*

* *“Làm trống giỏ”*

* *“Bỏ hết đi, tôi muốn chọn lại”*

**Ví dụ hội thoại**

**KH: Xóa hết giỏ hàng đi**

**Bot: Giỏ hàng của bạn có 3 sản phẩm. Bạn chắc chắn muốn xóa hết không?**

**KH: Ʈ̀, xóa đi**

*\[Orchestrator gọi clear\_cart()\]*

**Bot: Đã xóa toàn bộ 3 sản phẩm. Giỏ hàng đang trống.**

**Bot: Bạn muốn tìm sản phẩm mới không?**

**start\_order\_flow**

**Mô tả:** Khởi động luồng đặt hàng multi-step. Kiểm tra giỏ hàng và trả về signal để orchestrator chuyển sang checkout state machine: thu thập tên → SĐT → địa chỉ → xác nhận. Trả về NEED\_NAME nếu giỏ có hàng, NEED\_ITEMS nếu giỏ trống.

| Input | (không có tham số) |
| :---- | :---- |
| **Output** | Giỏ có hàng: { signal: "NEED\_NAME", cart\_summary: { items\[\], total\_amount } }Giỏ trống: { signal: "NEED\_ITEMS" } |
|  |  |
| **Side effects** | Tạo order thật trong DB khi khách xác nhận. Cập nhật session state (checkout step, shipping info). Idempotency key chống tạo đơn trùng. |
| **Error handling** | Giỏ trống: trả về NEED\_ITEMS và thông báo cho khách. SĐT sai định dạng: hỏi nhập lại. |

**Trigger ví dụ**

* *“Đặt hàng ngay”*

* *“Checkout”*

* *“Xác nhận đơn hàng”*

* *“Mua luôn”*

* *“(Sau khi add\_to\_cart thành công và khách muốn đặt)”*

**Ví dụ hội thoại**

**KH: Đặt hàng luôn nhé**

*\[Orchestrator gọi start\_order\_flow()\]*

*\[Signal: NEED\_NAME \+ cart\_summary\]*

**Bot: Đơn hàng của bạn:**

**Bot: • Quần Jean Slim Fit (x1) \= 450,000đ**

**Bot: • Áo Thun Basic (x2) \= 398,000đ**

**Bot: Tổng: 848,000đ**

**Bot: Cho mình xin tên người nhận nhé?**

**KH: Nguyễn Văn A**

*\[current\_step → NEED\_PHONE\]*

**Bot: Cảm ơn anh A\! Số điện thoại nhận hàng là gì ạ?**

**KH: 0901234567**

*\[current\_step → NEED\_ADDRESS\]*

**Bot: Địa chỉ giao hàng là ở đâu ạ?**

**KH: 123 Lê Lợi, Quận 1, TP.HCM**

*\[current\_step → NEED\_CONFIRM\]*

**Bot: Xác nhận đơn hàng:**

**Bot: • Quần Jean Slim Fit x1 \= 450,000đ**

**Bot: • Áo Thun Basic x2 \= 398,000đ**

**Bot: Tổng: 848,000đ**

**Bot: Giao cho: Nguyễn Văn A — 0901234567**

**Bot: Địa chỉ: 123 Lê Lợi, Q1, HCM**

**Bot: Bạn xác nhận đặt đơn không?**

**KH: OK xác nhận**

*\[Tạo order trong hệ thống → DONE\]*

**Bot: Đơn hàng đã tạo thành công\! Mã đơn: \#7DE649BB**

**Bot: Giao hàng trong 2–3 ngày. Cảm ơn bạn\!**

## **4.1 Checkout State Machine**

**Transitions:** NEED\_NAME → NEED\_PHONE → NEED\_ADDRESS → NEED\_CONFIRM → DONE

| Session State Field | Type | Mô tả |
| :---- | :---- | :---- |
|  | enum | Bước hiện tại của checkout flow |
|  | UUID | ID của giỏ hàng / draft order |
|  | string | Tên người nhận hàng |
|  | string | SĐT (định dạng VN: 10 số) |
|  | string | Địa chỉ giao hàng |
|  | string | Variant cuối cùng khách chọn (context) |

**get\_order\_status**

**Mô tả:** Tra cứu trạng thái đơn hàng. Nếu không truyền order\_id thì lấy đơn hàng gần nhất (đơn mới nhất không phải DRAFT). Trả về đầy đủ trạng thái, tổng tiền, địa chỉ giao hàng và danh sách sản phẩm.

| Input | order\_id: string (Tùy chọn — nếu None lấy đơn gần nhất) |
| :---- | :---- |
| **Output** | { order\_id, status, total\_amount, shipping\_name, shipping\_phone, shipping\_address, created\_at, items: \[{ name, qty, price, subtotal }\] } |
|  |  |
| **Error handling** | Không tìm thấy đơn: thông báo không có đơn hàng nào. Mã đơn sai: gợi ý kiểm tra lại mã. |

**Trigger ví dụ**

* *“Đơn hàng của tôfi đang ở đâu?”*

* *“Kiểm tra đơn \#ORD-001”*

* *“Bao giờ giao hàng?”*

* *“Đơn hôm qua của tôi thế nào rồi?”*

**Ví dụ hội thoại**

**KH: Đơn hàng hôm qua của tôi đang ở đâu rồi?**

*\[Orchestrator gọi get\_order\_status() — không có order\_id → lấy đơn gần nhất\]*

**Bot: Đơn \#7DE649BB của bạn:**

**Bot: Trạng thái: Chờ xác nhận**

**Bot: Tổng tiền: 848,000đ**

**Bot: Giao cho: Nguyễn Văn A — 0901234567**

**Bot: Địa chỉ: 123 Lê Lợi, Q1, HCM**

**Bot: Ngày đặt: 09/04/2026**

**Bot: Sản phẩm: Quần Jean Nam ×1 \= 450,000đ**

**list\_orders**

**Mô tả:** Liệt kê tất cả đơn hàng của customer (bỏ qua DRAFT), sắp xếp theo ngày đặt mới nhất trước. Hiển thị tóm tắt: mã đơn, trạng thái, tổng tiền, số lượng sản phẩm, ngày đặt.

| Input | (không có tham số — tự động dùng customer\_id từ session) |
| :---- | :---- |
| **Output** | Array of { order\_id, status, total\_amount, item\_count, created\_at } |
| **Error handling** | Không có đơn nào: thông báo chưa có đơn hàng và gợi ý tìm sản phẩm. |

**Trigger ví dụ**

* *“Tôi có bao nhiêu đơn hàng?”*

* *“Lịch sử mua hàng của tôi”*

* *“Xem tất cả đơn hàng”*

**Ví dụ hội thoại**

**KH: Xem lịch sử mua hàng của tôi**

*\[Orchestrator gọi list\_orders()\]*

**Bot: Bạn có 4 đơn hàng:**

**Bot: 1\. \#7DE649BB | Chờ xác nhận | 848,000đ | 2 sp | 09/04/2026**

**Bot: 2\. \#ORD-001 | Chờ xác nhận | 649,000đ | 2 sp | 09/04/2026**

**Bot: 3\. \#ORD-002 | Đang giao | 1,200,000đ | 1 sp | 07/04/2026**

**Bot: 4\. \#ORD-003 | Hoàn thành | 398,000đ | 1 sp | 02/04/2026**

**Bot: Bạn muốn xem chi tiết đơn nào không?**

# **4\. FAQ Tool**

**get\_store\_info**

**Mô tả:** Truy xuất thông tin cửa hàng từ FAQ tĩnh (knowledge base). Nhận topic string và trả về câu trả lời tương ứng. Dùng cho mọi câu hỏi về vận hành cửa hàng không liên quan đến sản phẩm hay đơn hàng.

| Input | topic: string (hours | address | shipping | return | payment | general) |
| :---- | :---- |
| **Output** | { topic: string, answer: string } |
| **Error handling** | Topic không tìm thấy: dùng RAG fallback để tìm câu trả lời gần đúng nhất. Nếu vẫn không có: thông báo và đề xuất handoff. |

**Trigger ví dụ**

* *“Cửa hàng mở đến mấy giờ? → hours”*

* *“Địa chỉ ở đâu? → address”*

* *“Ship có mất phí không? → shipping”*

* *“Đổi trả như thế nào? → return”*

* *“Thanh toán bằng gì? → payment”*

**Ví dụ hội thoại**

**KH: Cửa hàng mở đến mấy giờ?**

*\[Orchestrator gọi get\_store\_info(topic="hours")\]*

**Bot: Cửa hàng mở cửa 8:00–22:00 tất cả các ngày kể cả lễ tết.**

**KH: Ship về tỉnh mất bao nhiêu ngày?**

*\[Orchestrator gọi get\_store\_info(topic="shipping")\]*

**Bot: Miễn phí đơn từ 500,000đ. Giao 2–3 ngày nội thành, 4–5 ngày tỉnh.**

## **4.1 Topic Mapping**

| Topic | Ví dụ câu hỏi | Nguồn dữ liệu |
| :---- | :---- | :---- |
|  | Giờ mở cửa, ngày nghỉ, lễ tết | FAQ tĩnh (admin cập nhật) |
|  | Địa chỉ cửa hàng, bản đồ | FAQ tĩnh |
|  | Phí ship, thời gian giao, khu vực | FAQ tĩnh |
|  | Chính sách đổi trả, thời hạn, điều kiện | FAQ tĩnh \+ RAG |
|  | Phương thức thanh toán, COD, chuyển khoản | FAQ tĩnh |
|  | Câu hỏi khác không thuộc nhóm trên | RAG retrieval |

# **5\. Handoff Tool**

**escalate\_to\_human**

**Mô tả:** Chuyển cuộc hội thoại sang nhân viên hỗ trợ. Ghi lại lý do escalate để nhân viên nắm bắt ngay tình huống. Trong production: set Session.status \= HANDOFF và Session.conversation\_mode \= HUMAN trong DB, ngăn bot tiếp tục reply cho session đó.

| Input | reason: string (Lý do handoff — BẮT BUỘC, có nghĩa và đầy đủ) |
| :---- | :---- |
| **Output** | { escalated: true, reason: string, session\_status: "HANDOFF" } |
|  |  |
| **Side effects** | Session.status → HANDOFF. Session.conversation\_mode → HUMAN. Bot ngừng auto-reply. Gửi context (lý do, mã đơn, SP, shipping info) đến nhân viên. |

**Trigger ví dụ**

* *“Tôi muốn khiếu nại”*

* *“Hoàn tiền cho tôi”*

* *“Cho tôi gặp quản lý”*

* *“Sản phẩm bị lỗi”*

* *“(Bot không hiểu \> N lần)”*

* *“(Tool lỗi liên tiếp)”*

**Ví dụ hội thoại**

**KH: Tôi muốn hoàn tiền đơn hàng vừa rồi**

*\[Orchestrator gọi escalate\_to\_human(reason="khách yêu cầu hoàn tiền đơn \#7DE649BB")\]*

**Bot: Mình đã ghi nhận và chuyển bạn sang nhân viên hỗ trợ.**

**Bot: Bạn sẽ được liên hệ trong 5 phút.**

*\[Session.status \= HANDOFF\]*

*\[Session.conversation\_mode \= HUMAN\]*

*\[Bot ngừng auto-reply cho session này\]*

## **5.1 Trigger tự động**

Ngoài việc khách hàng yêu cầu trực tiếp, escalate\_to\_human còn được gọi tự động trong các trường hợp:

| Tình huống | Hành động |
| :---- | :---- |
| **Khiếu nại / hoàn tiền / hủy đơn** | Escalate ngay lập tức với reason chính xác |
| **Bot không hiểu \> N lần** | N cấu hình được (mặc định \= 3). Escalate với reason “bot không hiểu sau N lần” |
| **Tool lỗi liên tiếp** | \>2 lần cùng tool hoặc \>3 tool bất kỳ. Escalate với reason “hệ thống lỗi” |
| **Tình huống nhạy cảm** | Khách tức giận, yêu cầu gặp quản lý, vấn đề pháp lý |

## **5.2 Context gửi cho nhân viên**

Khi handoff, hệ thống phải gửi đủ thông tin để nhân viên không cần hỏi lại khách hàng:

* **Lý do handoff:** Vì sao chuyển (khiếu nại, hoàn tiền, tool lỗi…)

* **Mã đơn hàng:** Nếu có đơn liên quan

* **Sản phẩm:** SP đang xem/đã mua

* **Thông tin giao hàng:** Nếu đã thu thập trong checkout flow

* **Lịch sử hội thoại:** Toàn bộ messages trong session

[image1]: <data:image/png;base64,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R7qPW7ZsaWbPnm22b99uTjzxRPu8Qt2kSZPsYwW9xYsXm1WrVpkrrrjCTlo/cOBAs3v3bvtcu3btTKdOncxVV11l1q9f7y5XtWpVdznp0KGDqVy5smndurV9rHqFwxo1apjevXubXbt2ufvkGDdunPnpp5+81UkTVhtHXda4r82UeevN4jW7UlcIcEhzBDgAvoQVLrwB7t577zUvvviief755+0Yaddff70NZp9//rk555xz7P2VK1ea9u3bm/322880bdrU1r399tv2tlSpUuaMM86w93v06OEu161bN3c5qVu3rhk8eLCpVauW+e2338yzzz5rn7/kkkvs7d133+3uk+OZZ54xP/zwg7c6acJq46h74s0cAhwQEAEOgC9hhQtvgNPMBApw6nHbunWrvVUoE/WgKVzJyy+/bN555x0zaNAgW/fII4/YWwUz9Z5pvccff7y73MaNG93l1DNXv359M3bsWJOTk2OfO+WUU+x+bN682dSuXTvfPn333XdmwYIFpm/fvuajjz6y98PoiQurjaOOAAcER4AD4EtY4SIxwCk8Va9e3Qawc88910yZMsX8/PPPZp999rHPOwFux44dply5cubkk0+2AU916k3TrQ6pim4rVqzoLrdo0SJ3Oc2AoOCm+3Xq1DEffvihPXR69NFH27HYnOL4xz/+YZe97LLLzD333GPvT5s2zX0+WcJq46gjwAHBEeAA+BJWuFCA05ygOtzpnOMmDRs2NMuXLzcPPPCAW/fQQw/Z+z/++KPZd9997flrl156qa3T+Wu6LVOmjJ3VoGzZsua6665zl/v+++/d5VasWGHatm1r5s2bZ3vwFMa6du1qn9d5bjpfrkWLFom7aXEINRwEOCA4AhwAX8IKF4lXodasWdP2cMlrr71m61q1amWOO+44e56aLm444YQTzJw5c0zPnj1tWLvpppvscrooQbdNmjSxPWlVqlQxX331lbucAp2znFSqVMk+Puigg+zjdevW2YsfVKdDr+qh8yLAhYMABwRHgAPgS6aGi1TK1DYmwAHBEeAA+JKp4SKVMrWNCXBAcAQ4AL5karhIpUxt47gGuJ07d3qrgKQhwAHwJVPDRSplahtHMcDp4hfnPEhdDa1zKIOe/6gxDP3Slde6CjvR5MmT8z32QwNXIzMQ4AD4Ela4+OSTT+xAu2F46qmn7Pr35o033rDT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>
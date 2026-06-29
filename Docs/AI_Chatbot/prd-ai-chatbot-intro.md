---
title: PRD AI Chatbot for e-commerce - Introduction
version: 1.0.0
status: verified-by-ba
related_code: F:/Gapone Conversation/Docs/AI_Chatbot/prd-ai-chatbot-intro.md
last_updated: 2026-06-26
---

# Nhật ký thay đổi (Revision History)

| Phiên bản | Ngày | Người cập nhật | Vị trí thay đổi | Lý do chi tiết |
| :--- | :--- | :--- | :--- | :--- |
| 1.0.0 | 2026-06-26 | Mira-Miraaa | Toàn bộ tài liệu | Chuẩn hóa tài liệu từ tệp cũ |

---



GAPIT Communications

GapOne Platform — gapone.vn

**GAPCon AI Chatbot**

Product Requirements Document (PRD)

Trợ lý bán hàng AI đa kênh cho Thương mại điện tử

# **1\. Tóm tắt sản phẩm**

## **1.1 Định nghĩa sản phẩm**

GAPCon AI Chatbot là trợ lý bán hàng và chăm sóc khách hàng tự động, hoạt động trực tiếp trên các kênh messaging phổ biến tại Việt Nam: Zalo OA, Facebook Messenger và Telegram. Sản phẩm cho phép khách hàng thực hiện toàn bộ hành trình mua hàng — từ hỏi thông tin, tìm kiếm sản phẩm, thêm vào giỏ, đặt hàng, đến tra cứu đơn — tất cả ngay trong cuộc hội thoại mà không cần rời ứng dụng nhắn tin.

**Mục tiêu cốt lõi:** *Biến chat thành kênh bán hàng hoàn chỉnh (Conversational Commerce), thay thế các bước thủ công như trả lời FAQ, kiểm kho, nhập đơn và tra cứu trạng thái đơn hàng.*

## **1.2 Kiến trúc chủ đạo**

Giải pháp sử dụng kiến trúc Tool Calling (LLM chọn và gọi tools/API dựa trên docstring \+ context), mang lại các lợi thế:

* **Giảm hallucination:** Dữ liệu quan trọng (giá, tồn kho, trạng thái đơn) luôn lấy từ nguồn thật qua tool call, không bịa.

* **Xử lý multi-intent:** Khách hàng có thể vừa hỏi sản phẩm vừa hỏi đơn trong cùng một tin nhắn, LLM gọi nhiều tools liên tiếp.

* **Dễ mở rộng:** Thêm tool \= mở rộng năng lực. Không cần sửa classifier, router hay graph.

* **Loose coupling:** Tools độc lập, dễ thêm/xóa/thay thế từng tool mà không ảnh hưởng hệ thống.

## **1.3 Bảng tóm tắt năng lực MVP**

| STT | Tính năng | Mô tả chi tiết |
| ----- | :---- | :---- |
| 1 | **FAQ / Policy Q\&A** | Trả lời câu hỏi về cửa hàng (giờ mở cửa, đổi trả, vận chuyển, địa chỉ…) từ tài liệu được tải lên. Sử dụng RAG để đảm bảo chính xác và nhất quán. |
| 2 | **Tìm kiếm sản phẩm** | Lọc theo danh mục, màu, size, thương hiệu, khoảng giá. Hiển thị ảnh, giá, tình trạng tồn kho real-time từ hệ thống. |
| 3 | **Chi tiết sản phẩm** | Mô tả đầy đủ, hình ảnh, giá hiện tại, số lượng tồn kho của từng variant cụ thể. |
| 4 | **Giỏ hàng** | Thêm sản phẩm (cộng dồn nếu đã có), xóa từng sản phẩm, xem giỏ, xóa toàn bộ. Tự động recompute tổng tiền. |
| 5 | **Đặt hàng end-to-end** | Checkout multi-step qua chat: tên người nhận → SĐT → địa chỉ giao hàng → xác nhận đơn → tạo order trong hệ thống và trả mã đơn. |
| 6 | **Tra cứu đơn hàng** | Tra trạng thái đơn gần nhất hoặc theo mã đơn cụ thể. Xem lịch sử toàn bộ đơn hàng. Bỏ qua DRAFT orders. |
| 7 | **Gợi ý tương tự** | Khi sản phẩm hết hàng hoặc khách muốn xem thêm, gợi ý N sản phẩm cùng category. |
| 8 | **Handoff sang nhân viên** | Chuyển hội thoại kèm toàn bộ ngữ cảnh (lý do \+ mã đơn \+ SP \+ địa chỉ). Dừng auto-reply AI cho session đó. |

## **1.4 Điểm khác biệt so với chatbot hiện tại**

| GAPCon chatbot hiện tại | GAPCon AI Chatbot mới |
| :---- | :---- |
| Chỉ trả lời câu hỏi có sẵn (rule-based) | Hiểu câu hỏi tự nhiên bằng LLM, không cần template |
| Không kết nối với kho hàng | Truy vấn kho hàng real-time qua tool call |
| Không thể tạo đơn hàng | Tạo và xử lý đơn hàng hoàn toàn tự động trong chat |
| Mất context khi hỏi nhiều bước | Nhớ toàn bộ lịch sử hội thoại trong session \+ session state |
| Chuyển nhân viên không có context | Handoff có ngữ cảnh đầy đủ (lý do, mã đơn, SP, thông tin giao hàng) |

# **2\. Bối cảnh và cơ hội thị trường**

## **2.1 Vấn đề hiện tại**

Phần lớn cửa hàng SMB tại Việt Nam bán hàng qua Zalo và Facebook nhưng CSKH vẫn xử lý hoàn toàn thủ công:

* Trả lời câu hỏi lặp đi lặp lại về sản phẩm, giá cả, chính sách đổi trả

* Kiểm tra kho và báo tình trạng hàng cho từng khách

* Nhận đơn hàng qua chat rồi nhập thủ công vào hệ thống

* Theo dõi và phản hồi về trạng thái giao hàng

Điều này không chỉ tốn thời gian mà còn dễ xảy ra sai sót, đặc biệt khi lượng tin nhắn lớn vào giờ cao điểm. Peak hours gây quá tải dẫn đến trễ phản hồi, sai sót nhập liệu và rơi rớt cơ hội mua.

## **2.2 Cơ hội thị trường**

Thị trường e-commerce đang chuyển dịch từ Search-based commerce (Google, Shopee search) sang AI-assisted discovery (ChatGPT, TikTok), nhưng đang thiếu mảnh ghép quan trọng: transaction ngay trong conversation. Người dùng khám phá bằng AI hoặc content nhưng vẫn phải rời khỏi chat để checkout — đây là friction lớn nhất trong funnel.

**Zalo là blue ocean:** *Hơn 30 triệu người dùng hàng tháng, thói quen mua qua messaging mạnh nhưng chưa có nền tảng nào xây full-stack AI chatbot có thể recommend \+ tạo order trực tiếp trên Zalo OA.*

Thị trường conversational commerce toàn cầu dự kiến tăng từ $7.6 tỷ (2024) lên $34.4 tỷ vào 2034, và phần lớn growth đến từ các thị trường mobile-first như Việt Nam.

## **2.3 Bối cảnh cạnh tranh 3 tầng**

Thị trường không chỉ là “chatbot vs chatbot” mà gồm 3 tầng cạnh tranh khác nhau:

**Layer 1: AI Shopping Agents**

ChatGPT Shopping, Amazon Rufus, Perplexity AI Shopping — Tối ưu discovery/so sánh và trải nghiệm hỏi-đáp kiểu search. Điểm nghẽn: execution (inventory, checkout, payment, logistics).

| Giải pháp | Điểm mạnh | Điểm yếu chính |
| :---- | :---- | :---- |
| **ChatGPT Shopping** | User base lớn, discovery & comparison tốt, open ecosystem (multi-merchant) | Không có checkout native → redirect sang website/app khác. Thiếu inventory, tax/payment infra, logistics. |
| **Amazon Rufus** | Tích hợp sâu inventory \+ logistics → execution mạnh trong ecosystem Amazon | Closed ecosystem (chỉ Amazon). Không multi-channel. Không phù hợp SMB ngoài Amazon. |
| **Perplexity Shopping** | Conversational shopping tốt, thử checkout qua đối tác thanh toán | User base nhỏ, không kiểm soát inventory/logistics end-to-end. |

**Layer 2: E-commerce Platforms**

Shopee, Lazada, TikTok Shop — Tối ưu traffic → engagement → conversion trong hệ sinh thái riêng. AI chủ yếu phục vụ CSKH/FAQ hoặc discovery nội bộ, hiếm khi coi “conversation \= checkout”.

| Nền tảng | Điểm mạnh | Điểm yếu chính |
| :---- | :---- | :---- |
| **Shopee (Sophie)** | Market share cao, logistics \+ voucher \+ ecosystem mạnh. Sophie xử lý 18 triệu chat/năm, tự resolve 80% inquiries. | AI chỉ FAQ/CSKH. Chỉ chạy trong app, không qua Zalo/Telegram. Không conversation \= checkout. |
| **Lazada (Lazzie)** | Personalization tốt. Pilot tăng 42% orders và 50% interactions. | Checkout vẫn ngoài chat. Chưa end-to-end chat commerce. |
| **TikTok Shop** | Shoppertainment (video/livestream) → conversion cao. | Discovery phụ thuộc content, không phải intent. AI không phải core. |

**Layer 3: Conversational Platforms / CPaaS**

Zalo, Messenger, WhatsApp, Gupshup — Mạnh về distribution và hành vi người dùng “chat để mua”. Thiếu commerce brain và lớp quyết định (decision layer) để tạo giao dịch end-to-end. Bot thường rule-based/FAQ.

## **2.4 Vị trí chiến lược của GAPCon**

**GAPCon nằm ở giao điểm cả 3 tầng:** *Dùng AI để hiểu nhu cầu (Layer 1\) \+ thực thi giao dịch e-commerce (Layer 2\) \+ phân phối qua messaging (Layer 3).*

Strategic positioning map (2 trục):

* **Open \+ Search:** ChatGPT, Perplexity

* **Closed \+ Transaction:** Amazon

* **Closed \+ Discovery/Conversion:** Shopee, TikTok

* **Open \+ Transaction: KHOẢNG TRỐNG — GAPCon nhắm vào đây**

## **2.5 Competitive Matrix**

| Capability | ChatGPT | Rufus | Lazada | Shopee | TikTok | GAPCon |
| :---- | ----- | ----- | ----- | ----- | ----- | ----- |
| **Product search** | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| **Recommendation** | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| **In-chat checkout** | ❌ | ⚠️ | ❌ | ❌ | ⚠️ | ✅ |
| **Order end-to-end** | ❌ | ⚠️ | ❌ | ❌ | ❌ | ✅ |
| **Multi-channel** | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| **Own inventory** | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ |
| **SMB friendly** | ⚠️ | ❌ | ❌ | ❌ | ⚠️ | ✅ |
| **Zalo/Telegram native** | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |

## **2.6 Vì sao khoảng trống này tồn tại?**

**1\) Độ phức tạp kỹ thuật rất cao**

Không phải bài toán chatbot đơn thuần. Cần: inventory real-time, stateful checkout (state machine nhiều bước), order consistency \+ idempotency, handling edge cases (thiếu thông tin, đổi ý, lỗi tool, handoff…).

**2\) Ecosystem conflict**

Không ai sở hữu đủ cả 3 yếu tố cùng lúc: Amazon \= closed ecosystem; Shopee/Lazada/TikTok \= lock-in marketplace; AI agents \= thiếu commerce infra; Messaging platforms \= thiếu commerce layer.

**3\) UX mismatch**

Checkout truyền thống \= form-based; Chat \= context-based. Cần một paradigm mới: conversational checkout. GAPCon định nghĩa lại stack: Conversation → AI Orchestrator → Tools → Order (thay vì Frontend → Cart → Checkout → Order truyền thống).

## **2.7 Tổng hợp research thực tế**

| Nền tảng | Phân tích thực tế |
| :---- | :---- |
| **TikTok Shop** | Gần như không có ứng dụng AI hoặc rất ít tại VN. Các shop ưu tiên CSKH chat trực tiếp. KH mua đa phần qua trải nghiệm xem video và livestream. |
| **Shopee** | AI được ứng dụng để chào khách, tư vấn thông tin có trong database. Khi không tìm thấy thông tin, AI trực tiếp chuyển tới nhân viên thực. Có AI hỗ trợ xử lý khiếu nại. |
| **Lazada** | AI đa phần trong CSKH như Shopee. Ngoài ra còn AI hỗ trợ nhà bán hàng giải đáp thắc mắc và hướng dẫn xử lý hệ thống. |
| **Zalora** | Chỉ có bot tư vấn khi KH hỏi SP là chủ yếu, human vẫn xử lý chính. |
| **Amazon Rufus** | Trợ lý tư vấn mua hàng mạnh: phân tích hành vi KH (lịch sử mua, chi tiêu, độ tuổi) để đề xuất SP cá nhân hóa cao. Cung cấp lịch sử giá và so sánh giữa các seller. Tuy nhiên vẫn chưa hoàn tất order hoàn toàn qua conversation. |

**Insight chính:** *Không ai làm được order creation end-to-end qua chat. Amazon Rufus chỉ mới add to cart/auto-buy giới hạn. Lazada AI tăng 42% orders nhưng vẫn cần checkout thủ công. GAPCon proposed là duy nhất check đủ 8 capabilities bao gồm Zalo/Telegram native và order creation thực sự.*

# **3\. Mục tiêu và chỉ số thành công**

## **3.1 Mục tiêu sản phẩm**

* **Giảm tải cho CSKH/Sales:** Tự động hóa trả lời FAQ, kiểm kho, nhập đơn — giảm đáng kể công việc thủ công lặp lại.

* **Tăng chuyển đổi:** Tăng tỉ lệ chat → đơn hàng bằng cách loại bỏ friction (rời chat để checkout).

* **Trải nghiệm tự nhiên 24/7:** Mua hàng như nói chuyện với nhân viên, bất kỳ lúc nào.

* **Handoff chất lượng:** Chuyển nhân viên nhanh, đủ ngữ cảnh, giảm thời gian xử lý.

## **3.2 Success metrics chi tiết (đo theo kênh và tổng)**

| Nhóm | Chỉ số | Định nghĩa và cách đo |
| :---- | :---- | :---- |
| **Hiệu quả tự động hóa** | Automation coverage | % sessions bot xử lý hoàn toàn (không handoff). Đo bằng số sessions không có HANDOFF\_TRIGGERED / tổng sessions. |
|  | Deflection rate | % câu hỏi FAQ/policy được bot xử lý thành công. Đo bằng số get\_store\_info calls thành công / tổng câu hỏi FAQ. |
| **Doanh thu / Chuyển đổi** | Conversion rate | % sessions tạo order thành công. Đo bằng số ORDER\_CREATED events / tổng sessions có search\_products. |
|  | Funnel drop-off | Tỉ lệ rơi tại mỗi bước: search → detail → add\_to\_cart → start\_order\_flow → order\_created. |
| **Chất lượng vận hành** | First response time | Thời gian từ lúc KH gửi tin đến khi bot phản hồi. Đo median và p95. |
|  | AHT của CS | Average Handle Time của nhân viên sau handoff. Mục tiêu giảm so với trước khi có bot. |
|  | Handoff quality | % handoff có đủ thông tin: lý do \+ mã đơn \+ sản phẩm \+ địa chỉ giao hàng (nếu có). |
| **Rủi ro / Độ tin cậy** | Hallucination incidents | Số lần bot trả lời sai về giá, tồn kho, chính sách, trạng thái đơn. Mục tiêu: 0\. |
|  | Tool error rate | % tool calls thất bại. Đo và phân loại theo từng tool. |
|  | Tool latency p95 | Thời gian xử lý của từng tool ở percentile 95\. |

# **4\. Phạm vi (Scope)**

## **4.1 In-scope (MVP)**

1. Store FAQ / Policy Q\&A (giờ mở cửa, địa chỉ, shipping, đổi trả)

2. Product discovery: lọc theo danh mục, màu, size, brand, khoảng giá

3. Product detail: mô tả, ảnh, giá, tồn kho real-time của từng variant

4. Gợi ý sản phẩm tương tự (khi hết hàng hoặc khách muốn xem thêm)

5. Giỏ hàng: thêm sản phẩm, xóa sản phẩm, xem giỏ, xóa toàn bộ giỏ

6. Checkout flow multi-step: tên → SĐT → địa chỉ → xác nhận → tạo đơn

7. Order tracking: đơn gần nhất hoặc theo mã đơn

8. Order history: liệt kê toàn bộ đơn hàng (bỏ qua DRAFT)

9. Escalate to human: handoff có ngữ cảnh \+ khóa auto-reply

## **4.2 Out-of-scope (giai đoạn sau)**

* Payment link/QR và thanh toán trực tiếp trong chat

* Hoàn tiền/hủy đơn tự động end-to-end (MVP chỉ handoff)

* Voucher stacking / tối ưu mã giảm giá phức tạp

* Personalization sâu theo lịch sử mua và hành vi đa kênh

* Multi-language (MVP chỉ tiếng Việt)

* Merge/split identity của khách hàng (omni-channel) 

* Tự động prompt khách để hỏi email / SĐT nhằm tạo account trên GapOne khi khách nhắn

## **4.3 Vấn đề sản phẩm cần giải quyết**

**a) Về GAPCon (Conversation platform)**

| Vấn đề | Hướng giải quyết |
| :---- | :---- |
| **Thiếu memory theo session** | Bổ sung session state \+ short-term memory cho Orchestrator |
| **Session đóng/mở thủ công** | Tự động auto-open/auto-close theo timeout hoặc lịch làm việc |
| **Workflow automation khó quản trị** | Thêm workflow categories và hiển thị ở danh sách quản trị |
| **Chưa có quan hệ Conversation ↔ Customer/Order/Product** | Chuẩn hóa mô hình định danh \+ lớp tích hợp dữ liệu (xem mục 9\) |

**b) Định hướng sản phẩm (tránh “trượt” sang full e-commerce)**

GAPCon là nền tảng hội thoại/CSKH, không cạnh tranh trực diện sàn TMĐT. Vai trò rõ ràng:

* **Pre-sale:** Tư vấn sản phẩm, trả lời FAQ, gợi ý sản phẩm phù hợp

* **Transaction:** Tạo đơn nhanh cho SMB qua chat (conversational checkout)

* **Post-sale:** Tracking đơn hàng, handoff khi cần hỗ trợ phức tạp

**c) Kết nối GapOne × GAPCon**

Hiện thiếu integration DB GapOne. Cần xây dựng: tools layer/services giữa 2 hệ thống, domain identity, và contract ổn định cho API giữa GapOne và GAPCon.

# **5\. Personas và Jobs-to-be-done**

## **5.1 Personas chi tiết**

**Persona 1: Khách hàng (Buyer)**

**Mô tả:** Người mua hàng qua kênh messaging (Zalo, Facebook, Telegram). Muốn mua nhanh, không muốn rời app, ưu tiên trải nghiệm tiện lợi.

**Nhu cầu chính:** Tìm sản phẩm nhanh, so sánh giá/tồn kho, đặt hàng trực tiếp trong chat, tra cứu đơn.

**Pain points:** Phải chờ nhân viên trả lời, thông tin không nhất quán, phải rời chat để checkout.

**Persona 2: CS/Sales Agent**

**Mô tả:** Nhân viên chăm sóc khách hàng/bán hàng của shop. Quản lý nhiều cuộc chat cùng lúc.

**Nhu cầu chính:** Giảm câu hỏi lặp lại, nhận handoff có đủ ngữ cảnh để xử lý nhanh.

**Pain points:** Quá tải giờ cao điểm, nhập đơn thủ công dễ sai, không biết khách hỏi gì trước khi handoff.

**Persona 3: Store Admin**

**Mô tả:** Chủ shop hoặc quản lý. Quản trị nội dung FAQ/policy, tone của bot, theo dõi hiệu quả.

**Nhu cầu chính:** Xem dashboard hiệu suất bot, cập nhật chính sách cửa hàng, đảm bảo bot trả lời đúng.

## **5.2 Use cases chi tiết với ví dụ hội thoại**

**UC1: Tìm và mua sản phẩm**

**KH: Tôi muốn mua quần jean đen Nike size M dưới 500k**

*\[Bot gọi search\_products(color=đen, brand=Nike, size=M, max\_price=500000)\]*

**Bot: Mình tìm được 2 sản phẩm phù hợp:**

**Bot: 1\. Quần Jean Nam Slim Fit Nike — đen, M — 450,000đ — Còn 15**

**Bot: 2\. Quần Jean Nam Regular Nike — đen, M — 480,000đ — Còn 8**

**Bot: Bạn muốn xem chi tiết sản phẩm nào?**

**KH: Cho xem cái đầu tiên**

*\[Bot gọi get\_product\_detail(var-001-1)\]*

**Bot: Quần Jean Nam Slim Fit Nike | SKU: QJN-DEN-M | Denim co giãn 4 chiều...**

**KH: Lấy cho tôi 1 cái**

*\[Bot gọi add\_to\_cart(var-001-1, 1)\]*

**Bot: Đã thêm vào giỏ\! Tổng: 450,000đ. Bạn muốn tiếp tục mua hay đặt hàng luôn?**

**UC2: Đặt hàng end-to-end**

**KH: Đặt hàng luôn nhé**

*\[Bot gọi start\_order\_flow()\]*

**Bot: Đơn hàng của bạn: Quần Jean Slim Fit Nike x1 \= 450,000đ. Cho mình xin tên người nhận nhé?**

**KH: Nguyễn Văn A**

**Bot: Cảm ơn anh A\! Số điện thoại nhận hàng là gì ạ?**

**KH: 0901234567**

**Bot: Địa chỉ giao hàng là ở đâu ạ?**

**KH: 123 Lê Lợi, Quận 1, TP.HCM**

**Bot: Xác nhận đơn hàng:**

**Bot: • Quần Jean Slim Fit Nike x1 \= 450,000đ**

**Bot: • Giao cho: Nguyễn Văn A — 0901234567**

**Bot: • Địa chỉ: 123 Lê Lợi, Q1, HCM**

**Bot: Bạn xác nhận đặt đơn không?**

**KH: OK, xác nhận**

*\[Bot tạo order trong hệ thống\]*

**Bot: Đơn hàng đã được tạo thành công\! Mã đơn: \#7DE649BB. Giao hàng trong 2–3 ngày.**

**UC3: Tra cứu đơn hàng**

**KH: Đơn hàng hôm qua của tôi đang ở đâu rồi?**

*\[Bot gọi get\_order\_status()\]*

**Bot: Đơn \#7DE649BB của bạn đang ở trạng thái: Chờ xác nhận.**

**Bot: Tổng tiền: 450,000đ | Giao cho: Nguyễn Văn A | 123 Lê Lợi, Q1**

**UC4: Khiếu nại → Handoff**

**KH: Tôi muốn hoàn tiền đơn hàng vừa rồi**

*\[Bot gọi escalate\_to\_human(reason=“khách yêu cầu hoàn tiền đơn \#7DE649BB”)\]*

**Bot: Mình đã ghi nhận và chuyển bạn sang nhân viên hỗ trợ. Bạn sẽ được liên hệ trong 5 phút.**

*\[Session.status \= HANDOFF, conversation\_mode \= HUMAN\]*

**UC5: Multi-intent**

**KH: Cho tôi xem áo thun trắng, và kiểm tra đơn hàng hôm qua luôn**

*\[Bot gọi search\_products(color=trắng, category=áo thun)\]*

*\[Bot gọi get\_order\_status()\]*

**Bot: Đây là kết quả tìm áo thun trắng: \[danh sách\]**

**Bot: Và đơn hàng gần nhất của bạn: \#7DE649BB — Chờ xác nhận.**

# **6\. UX và luồng hội thoại**

## **6.1 Nguyên tắc thiết kế UX**

* **Ngắn gọn, tự nhiên:** Trả lời tiếng Việt tự nhiên, không dài dòng. Gợi ý bước tiếp theo rõ ràng.

* **Không bịa dữ liệu:** Giá, tồn kho, trạng thái đơn chỉ được trả lời SAU KHI gọi tool tương ứng. Đây là hard constraint.

* **Hỏi làm rõ:** Khi thiếu thông tin để hành động (ví dụ khách nói “mua quần” nhưng không nói màu/size), hỏi làm rõ trước.

* **Hạn chế spam:** Nếu nhiều kết quả, trả top N (3–5) \+ hướng dẫn lọc thêm.

* **Graceful fallback:** Khi tool lỗi, thông báo lịch sự và đề xuất handoff hoặc thử lại sau.

* **Proactive guidance:** Sau mỗi hành động, gợi ý bước tiếp theo phù hợp (ví dụ: sau add\_to\_cart gợi ý “mua thêm hay đặt hàng luôn?”).

## **6.2 Luồng tìm sản phẩm**

1. Nhận nhu cầu từ khách → gọi search\_products với các bộ lọc phù hợp

2. Nhiều kết quả (\>5) → trả top 3–5 \+ hướng dẫn lọc thêm (giá, màu, size)

3. Khách chọn 1 sản phẩm → gọi get\_product\_detail hiển thị đầy đủ thông tin

4. Sản phẩm hết hàng → tự động gọi search\_products() gợi ý thay thế

5. Không tìm thấy gì → hỏi thêm tiêu chí hoặc đề xuất sản phẩm phổ biến

## **6.3 Luồng đặt hàng end-to-end**

**Điều kiện tiên quyết:** Giỏ hàng không trống. Nếu giỏ trống, start\_order\_flow trả về NEED\_ITEMS và thông báo cho khách.

1. “Checkout” / “Đặt hàng” / “Xác nhận đơn” → gọi start\_order\_flow() → trả về NEED\_NAME

2. Thu thập tên người nhận → lưu vào session state → chuyển NEED\_PHONE

3. Thu thập SĐT (validate định dạng cơ bản) → chuyển NEED\_ADDRESS

4. Thu thập địa chỉ giao hàng → chuyển NEED\_CONFIRM

5. Bot gửi tóm tắt đơn (sản phẩm, số lượng, tổng tiền, thông tin giao hàng) để khách xác nhận

6. Khách xác nhận → tạo order trong hệ thống → trả mã đơn \+ tóm tắt → DONE

## **6.4 Luồng tra cứu đơn hàng**

* **get\_order\_status(order\_id?):** Nếu không truyền order\_id, lấy đơn gần nhất (bỏ qua DRAFT). Trả về: trạng thái, tổng tiền, địa chỉ, danh sách SP.

* **list\_orders():** Liệt kê tất cả đơn hàng (bỏ qua DRAFT), sắp xếp theo ngày đặt mới nhất. Hiển thị: mã, trạng thái, tổng tiền, số SP, ngày.

## **6.5 Luồng handoff**

**Trigger tự động:** 

* Khách yêu cầu khiếu nại, hoàn tiền, hủy đơn

* Bot lặp không hiểu \> N lần (cấu hình được, mặc định N=3)

* Tool lỗi liên tiếp (\>2 lần cùng tool hoặc \>3 tool bất kỳ)

* Tình huống nhạy cảm (ví dụ: khách tức giận, yêu cầu gặp quản lý)

**Hành động hệ thống:** 

* Set Session.status \= HANDOFF

* Set Session.conversation\_mode \= HUMAN

* Dừng auto-reply AI cho session đó

* Gửi thông báo cho khách: “Bạn sẽ được nhân viên hỗ trợ trong X phút”

* Gửi context đầy đủ cho nhân viên: lý do handoff, mã đơn, SP liên quan, thông tin giao hàng

# **7\. Yêu cầu chức năng**

## **7.1 Orchestrator (Tool Calling)**

**Input**

* Message hiện tại của khách hàng

* Conversation history (cửa sổ context, cấu hình được)

* Session state (checkout step, draft\_order\_id, shipping info…)

* Tool docstrings \+ constraints (mô tả tool, điều kiện gọi, tham số)

**Behavior**

* 0..N tool calls mỗi turn (đa tool cho multi-intent)

* Tự quyết định tool nào gọi và thứ tự gọi dựa trên reasoning

* Trả lời bằng tiếng Việt tự nhiên, tổng hợp kết quả từ các tool

**Hard constraints (BẮT BUỘC)**

| Constraint | Lý do |
| :---- | :---- |
| **Không gọi start\_order\_flow khi cart trống** | Tránh tạo đơn rỗng, gây nhầm lẫn |
| **Không trả lời giá/tồn kho nếu chưa gọi tool** | Chống hallucination — dữ liệu phải từ nguồn thật |
| **Không trả lời trạng thái đơn nếu chưa gọi get\_order\_status** | Thông tin đơn hàng thay đổi liên tục |
| **Thiếu thông tin → hỏi làm rõ trước** | Tránh gọi tool sai tham số |

## **7.2 Tools contract chi tiết (MVP)**

Dưới đây là đặc tả chi tiết của từng tool, bao gồm: mô tả, tham số đầu vào, đầu ra, trigger ví dụ, và xử lý lỗi.

**Tool 1: search\_products**

| Mô tả | Tìm kiếm sản phẩm trong database theo nhiều tiêu chí. Trả về danh sách variants còn hàng. Nếu hết hàng thì tìm các sản phẩm phù hợp nhất. |
| :---- | :---- |
| **Input** | filters: { category?, color?, size?, brand?, min\_price?, max\_price?, keyword? } |
| **Output** | Array of { variant\_id, product\_name, color, size, price, stock\_quantity, image\_url } |
| **Trigger** | “Tìm quần jean đen”, “Có giày nào dưới 1 triệu?”, “Cho xem áo thun trắng” |
| **Error handling** | Không tìm thấy: hỏi thêm tiêu chí hoặc đề xuất SP phổ biến. DB lỗi: thông báo \+ đề xuất thử lại. |

**Tool 2: get\_product\_detail**

| Mô tả | Lấy thông tin đầy đủ của một variant: mô tả, ảnh, giá, tồn kho. |
| :---- | :---- |
| **Input** | variant\_id: string (bắt buộc) |
| **Output** | { variant\_id, product\_name, sku, color, size, price, stock\_quantity, description, image\_urls\[\] } |
| **Trigger** | “Cho tôi xem chi tiết cái đầu tiên”, “Mô tả sản phẩm var-001”, “Còn bao nhiêu cái?” |
| **Error handling** | Variant không tồn tại: thông báo và gợi ý search lại. |

**Tool 3: add\_to\_cart**

| Mô tả | Thêm variant vào giỏ hàng (draft order). Tự động tạo draft order nếu chưa có. Cộng dồn nếu variant đã có. Recompute total\_amount. |
| :---- | :---- |
| **Input** | variant\_id: string (bắt buộc), quantity: number (mặc định 1\) |
| **Output** | { success, cart\_summary: { total\_items, total\_amount }, added\_item: { name, qty, price } } |
| **Trigger** | “Thêm vào giỏ hàng”, “Lấy cho tôi 2 cái”, khách đã chọn variant \+ đồng ý mua |
| **Error handling** | Hết hàng: thông báo \+ gợi ý tương tự. Số lượng \> tồn kho: thông báo số còn lại. |

**Tool 4: remove\_from\_cart**

| Mô tả | Xóa một variant khỏi giỏ. Yêu cầu xác nhận từ khách và variant\_id hợp lệ. |
| :---- | :---- |
| **Input** | variant\_id: string (bắt buộc) |
| **Output** | { success, removed\_item, cart\_summary } |

**Tool 5: view\_cart**

| Mô tả | Xem nội dung giỏ hàng. Hiển thị live price, subtotal từng item và tổng cộng. Trả “Giỏ hàng trống” nếu chưa có gì. |
| :---- | :---- |
| **Input** | (không có tham số) |
| **Output** | { items: \[{ name, variant, qty, unit\_price, subtotal }\], total\_amount } hoặc { empty: true } |
| **Trigger** | “Giỏ hàng của tôi có gì?”, “Tổng tiền bao nhiêu?”, trước khi checkout |

**Tool 6: clear\_cart**

| Mô tả | Xóa toàn bộ giỏ hàng. Yêu cầu xác nhận từ khách trước khi thực hiện. |
| :---- | :---- |
| **Input** | (không có tham số) |
| **Output** | { success, cleared\_items\_count } |

**Tool 7: start\_order\_flow**

| Mô tả | Khởi động luồng đặt hàng multi-step. Kiểm tra giỏ hàng và trả signal để orchestrator chuyển sang checkout state machine. |
| :---- | :---- |
| **Input** | (không có tham số) |
| **Output** | Cart có hàng: { signal: NEED\_NAME, cart\_summary }. Cart trống: { signal: NEED\_ITEMS }. |
| **HARD CONSTRAINT** | KHÔNG gọi khi khách chưa add\_to\_cart. Đây là constraint cứng trong docstring. |

**Tool 8: get\_order\_status**

| Mô tả | Tra cứu trạng thái đơn hàng. Mặc định lấy đơn gần nhất (bỏ qua DRAFT). |
| :---- | :---- |
| **Input** | order\_id: string (tùy chọn — nếu None lấy đơn gần nhất) |
| **Output** | { order\_id, status, total\_amount, shipping\_address, shipping\_name, shipping\_phone, created\_at, items\[\] } |
| **Trigger** | “Đơn hàng của tôi đang ở đâu?”, “Kiểm tra đơn \#ORD-001”, “Bao giờ giao hàng?” |

**Tool 9: list\_orders**

| Mô tả | Liệt kê toàn bộ đơn hàng của customer (bỏ qua DRAFT), sắp xếp mới nhất trước. |
| :---- | :---- |
| **Input** | (không có tham số — tự động dùng customer\_id từ session) |
| **Output** | Array of { order\_id, status, total\_amount, item\_count, created\_at } |
| **Trigger** | “Tôi có bao nhiêu đơn hàng?”, “Lịch sử mua hàng của tôi” |

**Tool 10: get\_store\_info**

| Mô tả | Truy xuất thông tin cửa hàng từ FAQ/policy từ uploaded files. Nhận topic string và trả câu trả lời tương ứng. |
| :---- | :---- |
| **Input** | topic: string (hours | address | shipping | return | payment | general) |
| **Output** | { topic, answer: string } — nội dung từ knowledge base |
| **Trigger** | “Cửa hàng mở đến mấy giờ?” → hours | “Ship có mất phí không?” → shipping | “Đổi trả như thế nào?” → return |

**Tool 11: escalate\_to\_human**

| Mô tả | Chuyển hội thoại sang nhân viên. Ghi lý do escalate. Set HANDOFF \+ HUMAN mode. |
| :---- | :---- |
| **Input** | reason: string (lý do handoff — bắt buộc) |
| **Output** | { escalated: true, reason, session\_status: HANDOFF } |
| **Side effects** | Session.status \= HANDOFF, Session.conversation\_mode \= HUMAN, ngăn bot tiếp tục reply |
| **Trigger** | “Tôi muốn khiếu nại”, “Hoàn tiền cho tôi”, câu hỏi vượt khả năng bot, tool lỗi liên tục |

## **7.3 Checkout state machine**

Luồng checkout được quản lý bằng state machine với các bước rõ ràng:

**Transitions:** NEED\_NAME → NEED\_PHONE → NEED\_ADDRESS → NEED\_CONFIRM → DONE

**Session state tối thiểu cần lưu:** 

| Field | Mô tả |
| :---- | :---- |
| **current\_step** | Bước hiện tại của checkout flow |
| **draft\_order\_id / cart\_id** | ID của giỏ hàng / draft order |
| **shipping\_name** | Tên người nhận hàng |
| **shipping\_phone** | Số điện thoại người nhận |
| **shipping\_address** | Địa chỉ giao hàng |
| **last\_selected\_variant\_id** | Variant cuối cùng khách chọn (context) |

## **7.4 Knowledge/FAQ management**

* **Single source of truth:** FAQ/policy lưu trong DB/PDF, có versioning

* **Topic mapping:** Map topic (hours, shipping, return, address, payment) đến câu trả lời cụ thể

* **RAG fallback:** Khi topic không match, dùng retrieval để tìm câu trả lời gần đúng nhất

* **Admin cập nhật:** Store admin có thể cập nhật FAQ qua giao diện quản trị

# **8\. Yêu cầu phi chức năng**

| Yêu cầu | Chi tiết | Mục tiêu / Ghi chú |
| :---- | :---- | :---- |
| **Data correctness** | Mọi dữ liệu giao dịch (giá, tồn kho, trạng thái đơn) lấy từ DB/services | Hallucination incidents \= 0 |
| **Latency** | End-to-end response time bao gồm LLM reasoning \+ tool call \+ response generation | Mục tiêu p95 ≤ X giây (cần chốt theo infra) |
| **Reliability** | Graceful degradation khi tool lỗi. Auto-handoff khi cần. | Uptime target: 99.5% |
| **Multi-channel consistency** | Logic thống nhất giữa Zalo, Messenger, Telegram. Chỉ khác adapter UI. | Core engine chia sẻ giữa các kênh |
| **Scalability** | Hệ thống phải xử lý được peak hours không sụp. | Rate limiting \+ queue cho tool calls |
| **Idempotency** | Đảm bảo không tạo đơn trùng khi retry/network issue. | Idempotency key cho order creation |

# **9\. Edge cases chi tiết**

| Tình huống | Xử lý | Ví dụ |
| :---- | :---- | :---- |
| **Không tìm thấy SP** | Hỏi thêm tiêu chí hoặc đề xuất SP phổ biến | “Mình không tìm thấy SP phù hợp. Bạn có muốn xem SP bán chạy?” |
| **SP hết hàng** | Gọi search\_products() gợi ý thay thế | “SP này hết hàng rồi. Mình gợi ý mấy cái tương tự:” |
| **User đổi ý giữa checkout** | Cho phép quay lại view\_cart, thêm/xóa SP | “Bạn muốn sửa giỏ hàng không? Xem lại giỏ nhé” |
| **Tool downtime** | Thông báo lịch sự \+ tự động handoff | “Hệ thống đang bảo trì. Mình chuyển bạn sang NV hỗ trợ” |
| **Giá thay đổi giữa search và checkout** | Recompute tại bước confirm, thông báo nếu khác | “Giá đã cập nhật từ 450k → 470k. Bạn vẫn muốn đặt?” |
| **SĐT/địa chỉ không hợp lệ** | Validate cơ bản, hỏi lại | “SĐT không đúng định dạng. Bạn nhập lại nhé” |
| **Khách gửi ảnh/sticker/file** | Thông báo chưa hỗ trợ, gợi ý dùng text | “Mình chưa đọc được ảnh. Bạn mô tả bằng text nhé” |
| **Multi-session cùng lúc** | Mỗi kênh \= 1 session độc lập, cart riêng | Giỏ hàng trên Zalo và Messenger là riêng biệt |
| **Bot không hiểu \> N lần** | Tự động escalate\_to\_human | “Mình chưa hiểu ý bạn. Để mình chuyển sang NV” |

# **10\. Tiêu chí nghiệm thu chi tiết**

| \# | Tiêu chí | Điều kiện pass | Status |
| ----- | :---- | :---- | :---- |
| 1 | **Trả lời FAQ đúng** | Bot trả lời chính xác ≥5 topics khác nhau từ knowledge base | □ Pending |
| 2 | **Search theo nhiều tiêu chí** | Tìm được SP theo ≥3 tiêu chí kết hợp (màu+size+giá) | □ Pending |
| 3 | **Không checkout khi cart trống** | start\_order\_flow trả về NEED\_ITEMS, không tạo order | □ Pending |
| 4 | **Tạo order thành công** | Sau checkout flow, order được tạo trong DB, trả mã \+ tóm tắt | □ Pending |
| 5 | **Tra đơn hàng** | Tra được đơn gần nhất và theo mã, hiển thị đúng trạng thái | □ Pending |
| 6 | **Handoff hoạt động** | Complaint/refund → HANDOFF \+ dừng auto-reply \+ context đầy đủ | □ Pending |
| 7 | **Giỏ hàng đầy đủ** | Thêm, xóa, xem, clear đều hoạt động, total đúng | □ Pending |
| 8 | **Identity mapping** | KH từ Zalo được link đúng với contact trong GapOne | □ Pending |
| 9 | **Multi-intent** | Câu “xem áo trắng và kiểm tra đơn” → trả lời cả 2 yêu cầu | □ Pending |
| 10 | **Không hallucination** | Giá, tồn kho, trạng thái đơn chỉ từ tool, không bịa | □ Pending |
| 11 | **SP hết hàng** | Tự động gợi ý SP tương tự khi SP được chọn hết hàng | □ Pending |
| 12 | **Error handling** | Tool lỗi → thông báo lịch sự \+ đề xuất handoff hoặc thử lại | □ Pending |


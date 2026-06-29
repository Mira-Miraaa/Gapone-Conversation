---
title: PRD AI Chatbot for e-commerce - Core Specifications
version: 1.0.0
status: verified-by-ba
related_code: F:/Gapone Conversation/Docs/AI_Chatbot/prd-ai-chatbot.md
last_updated: 2026-06-26
---

# Nhật ký thay đổi (Revision History)

| Phiên bản | Ngày | Người cập nhật | Vị trí thay đổi | Lý do chi tiết |
| :--- | :--- | :--- | :--- | :--- |
| 1.0.0 | 2026-06-26 | Mira-Miraaa | Toàn bộ tài liệu | Chuẩn hóa tài liệu từ tệp cũ |

---

Tổng quan
**GAPCon AI Chatbot - Trợ lý mua sắm thông minh cho thương mại điện tử**

## Tổng quan

GAPCon AI Chatbot là một trợ lý mua sắm và CSKH đa kênh cho thương mại điện tử, hoạt động trực tiếp trên Zalo, Facebook Messenger và Telegram. Người dùng có thể hỏi về cửa hàng, tìm sản phẩm, xem chi tiết, thêm vào giỏ, tạo đơn hàng, tra cứu trạng thái đơn và được chuyển sang nhân viên khi cần, tất cả ngay trong hội thoại mà không cần rời ứng dụng nhắn tin.
Mục tiêu cốt lõi của sản phẩm là biến chat thành một kênh bán hàng hoàn chỉnh, thay thế các bước thủ công như trả lời FAQ, kiểm kho, nhập đơn và tra cứu trạng thái đơn, vốn đang tiêu tốn nhiều thời gian của đội CSKH/sales ở các shop bán hàng qua Zalo/Facebook. 

## Chatbot làm được gì?

### 1. Trả lời câu hỏi về cửa hàng

Khách hàng có thể hỏi bất kỳ thông tin chung nào về cửa hàng và nhận được câu trả lời ngay lập tức, 24/7.
*"Cửa hàng mở cửa đến mấy giờ?"* *"Chính sách đổi trả của bạn là gì?"* *"Ship về tỉnh mất bao nhiêu ngày?"*
Chatbot tìm kiếm thông tin từ tài liệu tải lên về chính sách cửa hàng sử dụng RAG, đảm bảo câu trả lời luôn chính xác và nhất quán.

### 2. Tư vấn và tìm kiếm sản phẩm

Chatbot kết nối trực tiếp với kho hàng và có thể tìm kiếm sản phẩm theo nhiều tiêu chí khác nhau - màu sắc, kích thước, thương hiệu, danh mục, hoặc ngân sách.
*"Tôi muốn mua quần jean màu đen, hãng Nike, size M, giá dưới 500 nghìn"* *"Bạn có áo thun cotton không? Tôi đang tìm loại mặc đi làm được"* *"Gợi ý cho tôi vài sản phẩm tương tự cái vừa xem"*
Kết quả trả về bao gồm hình ảnh sản phẩm, giá hiện tại và tình trạng còn hàng - đều được lấy theo thời gian thực từ hệ thống.

### 3. Đặt hàng hoàn toàn qua chat

Đây là tính năng cốt lõi phân biệt GAPCon với các chatbot FAQ thông thường. Khách hàng có thể hoàn tất toàn bộ quy trình mua hàng mà không cần ra khỏi cuộc trò chuyện.
Quy trình diễn ra tự nhiên theo từng bước:
Khách chọn sản phẩm → chatbot thêm vào giỏ hàng
Chatbot hỏi thông tin giao hàng (tên, số điện thoại, địa chỉ)
Chatbot xác nhận lại đơn hàng để khách kiểm tra
Khách xác nhận → đơn hàng được tạo trong hệ thống ngay lập tức
*"Cho tôi đặt cái quần đen vừa xem"* *"Giao đến 123 Lê Lợi, quận 1 nhé"* *"OK, xác nhận đơn"*

### 4. Tra cứu và theo dõi đơn hàng

Khách hàng có thể kiểm tra trạng thái đơn hàng bất cứ lúc nào chỉ bằng một tin nhắn.
*"Đơn hàng hôm qua của tôi đang ở đâu rồi?"* *"Tôi muốn xem lại đơn hàng tuần trước"*
Chatbot truy xuất thông tin trực tiếp từ hệ thống và trả về trạng thái đơn hàng cập nhật nhất - Chờ xác nhận, Đang giao, Hoàn thành, v.v.

### 5. Chuyển sang nhân viên khi cần

Khi gặp khiếu nại, yêu cầu hoàn tiền, hoặc các vấn đề phức tạp nằm ngoài khả năng của chatbot, hệ thống tự động chuyển cuộc hội thoại sang nhân viên hỗ trợ và thông báo cho khách hàng biết.
Toàn bộ lịch sử trò chuyện trước đó được giữ nguyên, giúp nhân viên nắm bắt tình huống mà không cần khách hàng phải kể lại từ đầu.

## Tại sao lại cần chatbot này?

Phần lớn cửa hàng đang bán hàng qua Zalo, Facebook - nhưng việc trả lời tin nhắn khách hàng hoàn toàn thủ công. Nhân viên phải dành nhiều giờ mỗi ngày để:
Trả lời các câu hỏi lặp đi lặp lại về sản phẩm, giá cả, chính sách
Kiểm tra kho và báo tình trạng hàng
Nhận đơn hàng qua chat rồi nhập thủ công vào hệ thống
Theo dõi và phản hồi về trạng thái giao hàng
Điều này không chỉ tốn thời gian mà còn dễ xảy ra sai sót, đặc biệt khi lượng tin nhắn lớn vào giờ cao điểm hoặc cuối tuần.

## Cách hoạt động (đơn giản hóa)

Khi khách hàng gửi một tin nhắn, hệ thống xử lý qua 4 bước:
Bước 1 - Hiểu ý định AI phân tích tin nhắn và xác định khách muốn gì: hỏi thông tin, tìm sản phẩm, đặt hàng, hay có vấn đề cần giải quyết.
Bước 2 - Tìm thông tin Tùy theo ý định, hệ thống tự động tra cứu dữ liệu phù hợp - tìm sản phẩm trong kho, kiểm tra đơn hàng, hoặc tìm trong tài liệu chính sách.
Bước 3 - Thực hiện hành động Nếu khách muốn đặt hàng, hệ thống tạo đơn hàng trực tiếp. Nếu cần thêm thông tin, chatbot hỏi từng bước một cách tự nhiên.
Bước 4 - Trả lời AI tạo ra phản hồi bằng tiếng Việt tự nhiên, kèm gợi ý bước tiếp theo phù hợp với ngữ cảnh của cuộc hội thoại.

## Nền tảng kỹ thuật

Hệ thống được xây dựng trên nền tảng GAPCon - platform quản lý hội thoại và chăm sóc khách hàng đang được sử dụng - với lớp thương mại điện tử được phát triển thêm, bao gồm quản lý sản phẩm, giỏ hàng và đơn hàng.
AI sử dụng các mô hình ngôn ngữ lớn (LLM) thế hệ mới, kết hợp với khả năng truy vấn cơ sở dữ liệu theo thời gian thực để đảm bảo mọi thông tin được cung cấp đều chính xác, không phải dự đoán hay bịa đặt.

PRD

GAPIT Communications
GapOne Platform — gapone.vn

**GAPCon AI Chatbot**
Product Requirements Document (PRD)
Trợ lý bán hàng AI đa kênh cho Thương mại điện tử

# 1. Tóm tắt sản phẩm

## 1.1 Định nghĩa sản phẩm

GAPCon AI Chatbot là trợ lý bán hàng và chăm sóc khách hàng tự động, hoạt động trực tiếp trên các kênh messaging phổ biến tại Việt Nam: Zalo OA, Facebook Messenger và Telegram. Sản phẩm cho phép khách hàng thực hiện toàn bộ hành trình mua hàng — từ hỏi thông tin, tìm kiếm sản phẩm, thêm vào giỏ, đặt hàng, đến tra cứu đơn — tất cả ngay trong cuộc hội thoại mà không cần rời ứng dụng nhắn tin.
**Mục tiêu cốt lõi: ***Biến chat thành kênh bán hàng hoàn chỉnh (Conversational Commerce), thay thế các bước thủ công như trả lời FAQ, kiểm kho, nhập đơn và tra cứu trạng thái đơn hàng.*

## 1.2 Kiến trúc chủ đạo

Giải pháp sử dụng kiến trúc Tool Calling (LLM chọn và gọi tools/API dựa trên docstring + context), mang lại các lợi thế:
**Giảm hallucination: **Dữ liệu quan trọng (giá, tồn kho, trạng thái đơn) luôn lấy từ nguồn thật qua tool call, không bịa.
**Xử lý multi-intent: **Khách hàng có thể vừa hỏi sản phẩm vừa hỏi đơn trong cùng một tin nhắn, LLM gọi nhiều tools liên tiếp.
**Dễ mở rộng: **Thêm tool = mở rộng năng lực. Không cần sửa classifier, router hay graph.
**Loose coupling: **Tools độc lập, dễ thêm/xóa/thay thế từng tool mà không ảnh hưởng hệ thống.

## 1.3 Bảng tóm tắt năng lực MVP

| STT | Tính năng | Mô tả chi tiết |
| --- | --- | --- |
| 1 | FAQ / Policy Q&A | Trả lời câu hỏi về cửa hàng (giờ mở cửa, đổi trả, vận chuyển, địa chỉ…) từ tài liệu được tải lên. Sử dụng RAG để đảm bảo chính xác và nhất quán. |
| 2 | Tìm kiếm sản phẩm | Lọc theo danh mục, màu, size, thương hiệu, khoảng giá. Hiển thị ảnh, giá, tình trạng tồn kho real-time từ hệ thống. |
| 3 | Chi tiết sản phẩm | Mô tả đầy đủ, hình ảnh, giá hiện tại, số lượng tồn kho của từng variant cụ thể. |
| 4 | Giỏ hàng | Thêm sản phẩm (cộng dồn nếu đã có), xóa từng sản phẩm, xem giỏ, xóa toàn bộ. Tự động recompute tổng tiền. |
| 5 | Đặt hàng end-to-end | Checkout multi-step qua chat: tên người nhận → SĐT → địa chỉ giao hàng → xác nhận đơn → tạo order trong hệ thống và trả mã đơn. |
| 6 | Tra cứu đơn hàng | Tra trạng thái đơn gần nhất hoặc theo mã đơn cụ thể. Xem lịch sử toàn bộ đơn hàng. Bỏ qua DRAFT orders. |
| 7 | Gợi ý tương tự | Khi sản phẩm hết hàng hoặc khách muốn xem thêm, gợi ý N sản phẩm cùng category. |
| 8 | Handoff sang nhân viên | Chuyển hội thoại kèm toàn bộ ngữ cảnh (lý do + mã đơn + SP + địa chỉ). Dừng auto-reply AI cho session đó. |

## 1.4 Điểm khác biệt so với chatbot hiện tại

| GAPCon chatbot hiện tại | GAPCon AI Chatbot mới |
| --- | --- |
| Chỉ trả lời câu hỏi có sẵn (rule-based) | Hiểu câu hỏi tự nhiên bằng LLM, không cần template |
| Không kết nối với kho hàng | Truy vấn kho hàng real-time qua tool call |
| Không thể tạo đơn hàng | Tạo và xử lý đơn hàng hoàn toàn tự động trong chat |
| Mất context khi hỏi nhiều bước | Nhớ toàn bộ lịch sử hội thoại trong session + session state |
| Chuyển nhân viên không có context | Handoff có ngữ cảnh đầy đủ (lý do, mã đơn, SP, thông tin giao hàng) |

# 2. Bối cảnh và cơ hội thị trường

## 2.1 Vấn đề hiện tại

Phần lớn cửa hàng SMB tại Việt Nam bán hàng qua Zalo và Facebook nhưng CSKH vẫn xử lý hoàn toàn thủ công:
Trả lời câu hỏi lặp đi lặp lại về sản phẩm, giá cả, chính sách đổi trả
Kiểm tra kho và báo tình trạng hàng cho từng khách
Nhận đơn hàng qua chat rồi nhập thủ công vào hệ thống
Theo dõi và phản hồi về trạng thái giao hàng
Điều này không chỉ tốn thời gian mà còn dễ xảy ra sai sót, đặc biệt khi lượng tin nhắn lớn vào giờ cao điểm. Peak hours gây quá tải dẫn đến trễ phản hồi, sai sót nhập liệu và rơi rớt cơ hội mua.

## 2.2 Cơ hội thị trường

Thị trường e-commerce đang chuyển dịch từ Search-based commerce (Google, Shopee search) sang AI-assisted discovery (ChatGPT, TikTok), nhưng đang thiếu mảnh ghép quan trọng: transaction ngay trong conversation. Người dùng khám phá bằng AI hoặc content nhưng vẫn phải rời khỏi chat để checkout — đây là friction lớn nhất trong funnel.
**Zalo là blue ocean: ***Hơn 30 triệu người dùng hàng tháng, thói quen mua qua messaging mạnh nhưng chưa có nền tảng nào xây full-stack AI chatbot có thể recommend + tạo order trực tiếp trên Zalo OA.*
Thị trường conversational commerce toàn cầu dự kiến tăng từ $7.6 tỷ (2024) lên $34.4 tỷ vào 2034, và phần lớn growth đến từ các thị trường mobile-first như Việt Nam.

## 2.3 Bối cảnh cạnh tranh 3 tầng

Thị trường không chỉ là “chatbot vs chatbot” mà gồm 3 tầng cạnh tranh khác nhau:
**Layer 1: AI Shopping Agents**
ChatGPT Shopping, Amazon Rufus, Perplexity AI Shopping — Tối ưu discovery/so sánh và trải nghiệm hỏi-đáp kiểu search. Điểm nghẽn: execution (inventory, checkout, payment, logistics).

| Giải pháp | Điểm mạnh | Điểm yếu chính |
| --- | --- | --- |
| ChatGPT Shopping | User base lớn, discovery & comparison tốt, open ecosystem (multi-merchant) | Không có checkout native → redirect sang website/app khác. Thiếu inventory, tax/payment infra, logistics. |
| Amazon Rufus | Tích hợp sâu inventory + logistics → execution mạnh trong ecosystem Amazon | Closed ecosystem (chỉ Amazon). Không multi-channel. Không phù hợp SMB ngoài Amazon. |
| Perplexity Shopping | Conversational shopping tốt, thử checkout qua đối tác thanh toán | User base nhỏ, không kiểm soát inventory/logistics end-to-end. |

**Layer 2: E-commerce Platforms**
Shopee, Lazada, TikTok Shop — Tối ưu traffic → engagement → conversion trong hệ sinh thái riêng. AI chủ yếu phục vụ CSKH/FAQ hoặc discovery nội bộ, hiếm khi coi “conversation = checkout”.

| Nền tảng | Điểm mạnh | Điểm yếu chính |
| --- | --- | --- |
| Shopee (Sophie) | Market share cao, logistics + voucher + ecosystem mạnh. Sophie xử lý 18 triệu chat/năm, tự resolve 80% inquiries. | AI chỉ FAQ/CSKH. Chỉ chạy trong app, không qua Zalo/Telegram. Không conversation = checkout. |
| Lazada (Lazzie) | Personalization tốt. Pilot tăng 42% orders và 50% interactions. | Checkout vẫn ngoài chat. Chưa end-to-end chat commerce. |
| TikTok Shop | Shoppertainment (video/livestream) → conversion cao. | Discovery phụ thuộc content, không phải intent. AI không phải core. |

**Layer 3: Conversational Platforms / CPaaS**
Zalo, Messenger, WhatsApp, Gupshup — Mạnh về distribution và hành vi người dùng “chat để mua”. Thiếu commerce brain và lớp quyết định (decision layer) để tạo giao dịch end-to-end. Bot thường rule-based/FAQ.

## 2.4 Vị trí chiến lược của GAPCon

**GAPCon nằm ở giao điểm cả 3 tầng: ***Dùng AI để hiểu nhu cầu (Layer 1) + thực thi giao dịch e-commerce (Layer 2) + phân phối qua messaging (Layer 3).*
Strategic positioning map (2 trục):
**Open + Search: **ChatGPT, Perplexity
**Closed + Transaction: **Amazon
**Closed + Discovery/Conversion: **Shopee, TikTok
**Open + Transaction: KHOẢNG TRỐNG — GAPCon nhắm vào đây**

## 2.5 Competitive Matrix

| Capability | ChatGPT | Rufus | Lazada | Shopee | TikTok | GAPCon |
| --- | --- | --- | --- | --- | --- | --- |
| Product search | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| Recommendation | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| In-chat checkout | ❌ | ⚠️ | ❌ | ❌ | ⚠️ | ✅ |
| Order end-to-end | ❌ | ⚠️ | ❌ | ❌ | ❌ | ✅ |
| Multi-channel | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| Own inventory | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ |
| SMB friendly | ⚠️ | ❌ | ❌ | ❌ | ⚠️ | ✅ |
| Zalo/Telegram native | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |

## 2.6 Vì sao khoảng trống này tồn tại?

**1) Độ phức tạp kỹ thuật rất cao**
Không phải bài toán chatbot đơn thuần. Cần: inventory real-time, stateful checkout (state machine nhiều bước), order consistency + idempotency, handling edge cases (thiếu thông tin, đổi ý, lỗi tool, handoff…).
**2) Ecosystem conflict**
Không ai sở hữu đủ cả 3 yếu tố cùng lúc: Amazon = closed ecosystem; Shopee/Lazada/TikTok = lock-in marketplace; AI agents = thiếu commerce infra; Messaging platforms = thiếu commerce layer.
**3) UX mismatch**
Checkout truyền thống = form-based; Chat = context-based. Cần một paradigm mới: conversational checkout. GAPCon định nghĩa lại stack: Conversation → AI Orchestrator → Tools → Order (thay vì Frontend → Cart → Checkout → Order truyền thống).

## 2.7 Tổng hợp research thực tế

| Nền tảng | Phân tích thực tế |
| --- | --- |
| TikTok Shop | Gần như không có ứng dụng AI hoặc rất ít tại VN. Các shop ưu tiên CSKH chat trực tiếp. KH mua đa phần qua trải nghiệm xem video và livestream. |
| Shopee | AI được ứng dụng để chào khách, tư vấn thông tin có trong database. Khi không tìm thấy thông tin, AI trực tiếp chuyển tới nhân viên thực. Có AI hỗ trợ xử lý khiếu nại. |
| Lazada | AI đa phần trong CSKH như Shopee. Ngoài ra còn AI hỗ trợ nhà bán hàng giải đáp thắc mắc và hướng dẫn xử lý hệ thống. |
| Zalora | Chỉ có bot tư vấn khi KH hỏi SP là chủ yếu, human vẫn xử lý chính. |
| Amazon Rufus | Trợ lý tư vấn mua hàng mạnh: phân tích hành vi KH (lịch sử mua, chi tiêu, độ tuổi) để đề xuất SP cá nhân hóa cao. Cung cấp lịch sử giá và so sánh giữa các seller. Tuy nhiên vẫn chưa hoàn tất order hoàn toàn qua conversation. |

**Insight chính: ***Không ai làm được order creation end-to-end qua chat. Amazon Rufus chỉ mới add to cart/auto-buy giới hạn. Lazada AI tăng 42% orders nhưng vẫn cần checkout thủ công. GAPCon proposed là duy nhất check đủ 8 capabilities bao gồm Zalo/Telegram native và order creation thực sự.*

# 3. Mục tiêu và chỉ số thành công

## 3.1 Mục tiêu sản phẩm

**Giảm tải cho CSKH/Sales: **Tự động hóa trả lời FAQ, kiểm kho, nhập đơn — giảm đáng kể công việc thủ công lặp lại.
**Tăng chuyển đổi: **Tăng tỉ lệ chat → đơn hàng bằng cách loại bỏ friction (rời chat để checkout).
**Trải nghiệm tự nhiên 24/7: **Mua hàng như nói chuyện với nhân viên, bất kỳ lúc nào.
**Handoff chất lượng: **Chuyển nhân viên nhanh, đủ ngữ cảnh, giảm thời gian xử lý.

## 3.2 Success metrics chi tiết (đo theo kênh và tổng)

| Nhóm | Chỉ số | Định nghĩa và cách đo |
| --- | --- | --- |
| Hiệu quả tự động hóa | Automation coverage | % sessions bot xử lý hoàn toàn (không handoff). Đo bằng số sessions không có HANDOFF_TRIGGERED / tổng sessions. |
|  | Deflection rate | % câu hỏi FAQ/policy được bot xử lý thành công. Đo bằng số get_store_info calls thành công / tổng câu hỏi FAQ. |
| Doanh thu / Chuyển đổi | Conversion rate | % sessions tạo order thành công. Đo bằng số ORDER_CREATED events / tổng sessions có search_products. |
|  | Funnel drop-off | Tỉ lệ rơi tại mỗi bước: search → detail → add_to_cart → start_order_flow → order_created. |
| Chất lượng vận hành | First response time | Thời gian từ lúc KH gửi tin đến khi bot phản hồi. Đo median và p95. |
|  | AHT của CS | Average Handle Time của nhân viên sau handoff. Mục tiêu giảm so với trước khi có bot. |
|  | Handoff quality | % handoff có đủ thông tin: lý do + mã đơn + sản phẩm + địa chỉ giao hàng (nếu có). |
| Rủi ro / Độ tin cậy | Hallucination incidents | Số lần bot trả lời sai về giá, tồn kho, chính sách, trạng thái đơn. Mục tiêu: 0. |
|  | Tool error rate | % tool calls thất bại. Đo và phân loại theo từng tool. |
|  | Tool latency p95 | Thời gian xử lý của từng tool ở percentile 95. |

# 4. Phạm vi (Scope)

## 4.1 In-scope (MVP)

Store FAQ / Policy Q&A (giờ mở cửa, địa chỉ, shipping, đổi trả)
Product discovery: lọc theo danh mục, màu, size, brand, khoảng giá
Product detail: mô tả, ảnh, giá, tồn kho real-time của từng variant
Gợi ý sản phẩm tương tự (khi hết hàng hoặc khách muốn xem thêm)
Giỏ hàng: thêm sản phẩm, xóa sản phẩm, xem giỏ, xóa toàn bộ giỏ
Checkout flow multi-step: tên → SĐT → địa chỉ → xác nhận → tạo đơn
Order tracking: đơn gần nhất hoặc theo mã đơn
Order history: liệt kê toàn bộ đơn hàng (bỏ qua DRAFT)
Escalate to human: handoff có ngữ cảnh + khóa auto-reply

## 4.2 Out-of-scope (giai đoạn sau)

Payment link/QR và thanh toán trực tiếp trong chat
Hoàn tiền/hủy đơn tự động end-to-end (MVP chỉ handoff)
Voucher stacking / tối ưu mã giảm giá phức tạp
Personalization sâu theo lịch sử mua và hành vi đa kênh
Multi-language (MVP chỉ tiếng Việt)
Merge/split identity của khách hàng (omni-channel) 
Tự động prompt khách để hỏi email / SĐT nhằm tạo account trên GapOne khi khách nhắn

## 4.3 Vấn đề sản phẩm cần giải quyết

**a) Về GAPCon (Conversation platform)**

| Vấn đề | Hướng giải quyết |
| --- | --- |
| Thiếu memory theo session | Bổ sung session state + short-term memory cho Orchestrator |
| Session đóng/mở thủ công | Tự động auto-open/auto-close theo timeout hoặc lịch làm việc |
| Workflow automation khó quản trị | Thêm workflow categories và hiển thị ở danh sách quản trị |
| Chưa có quan hệ Conversation ↔ Customer/Order/Product | Chuẩn hóa mô hình định danh + lớp tích hợp dữ liệu (xem mục 9) |

**b) Định hướng sản phẩm (tránh “trượt” sang full e-commerce)**
GAPCon là nền tảng hội thoại/CSKH, không cạnh tranh trực diện sàn TMĐT. Vai trò rõ ràng:
**Pre-sale: **Tư vấn sản phẩm, trả lời FAQ, gợi ý sản phẩm phù hợp
**Transaction: **Tạo đơn nhanh cho SMB qua chat (conversational checkout)
**Post-sale: **Tracking đơn hàng, handoff khi cần hỗ trợ phức tạp
**c) Kết nối GapOne × GAPCon**
Hiện thiếu integration DB GapOne. Cần xây dựng: tools layer/services giữa 2 hệ thống, domain identity, và contract ổn định cho API giữa GapOne và GAPCon.

# 5. Personas và Jobs-to-be-done

## 5.1 Personas chi tiết

**Persona 1: Khách hàng (Buyer)**
**Mô tả: **Người mua hàng qua kênh messaging (Zalo, Facebook, Telegram). Muốn mua nhanh, không muốn rời app, ưu tiên trải nghiệm tiện lợi.
**Nhu cầu chính: **Tìm sản phẩm nhanh, so sánh giá/tồn kho, đặt hàng trực tiếp trong chat, tra cứu đơn.
**Pain points: **Phải chờ nhân viên trả lời, thông tin không nhất quán, phải rời chat để checkout.
**Persona 2: CS/Sales Agent**
**Mô tả: **Nhân viên chăm sóc khách hàng/bán hàng của shop. Quản lý nhiều cuộc chat cùng lúc.
**Nhu cầu chính: **Giảm câu hỏi lặp lại, nhận handoff có đủ ngữ cảnh để xử lý nhanh.
**Pain points: **Quá tải giờ cao điểm, nhập đơn thủ công dễ sai, không biết khách hỏi gì trước khi handoff.
**Persona 3: Store Admin**
**Mô tả: **Chủ shop hoặc quản lý. Quản trị nội dung FAQ/policy, tone của bot, theo dõi hiệu quả.
**Nhu cầu chính: **Xem dashboard hiệu suất bot, cập nhật chính sách cửa hàng, đảm bảo bot trả lời đúng.

## 5.2 Use cases chi tiết với ví dụ hội thoại

**UC1: Tìm và mua sản phẩm**
**KH: Tôi muốn mua quần jean đen Nike size M dưới 500k**
*[Bot gọi search_products(color=đen, brand=Nike, size=M, max_price=500000)]*
**Bot: Mình tìm được 2 sản phẩm phù hợp:**
**Bot: 1. Quần Jean Nam Slim Fit Nike — đen, M — 450,000đ — Còn 15**
**Bot: 2. Quần Jean Nam Regular Nike — đen, M — 480,000đ — Còn 8**
**Bot: Bạn muốn xem chi tiết sản phẩm nào?**
**KH: Cho xem cái đầu tiên**
*[Bot gọi get_product_detail(var-001-1)]*
**Bot: Quần Jean Nam Slim Fit Nike | SKU: QJN-DEN-M | Denim co giãn 4 chiều...**
**KH: Lấy cho tôi 1 cái**
*[Bot gọi add_to_cart(var-001-1, 1)]*
**Bot: Đã thêm vào giỏ! Tổng: 450,000đ. Bạn muốn tiếp tục mua hay đặt hàng luôn?**
**UC2: Đặt hàng end-to-end**
**KH: Đặt hàng luôn nhé**
*[Bot gọi start_order_flow()]*
**Bot: Đơn hàng của bạn: Quần Jean Slim Fit Nike x1 = 450,000đ. Cho mình xin tên người nhận nhé?**
**KH: Nguyễn Văn A**
**Bot: Cảm ơn anh A! Số điện thoại nhận hàng là gì ạ?**
**KH: 0901234567**
**Bot: Địa chỉ giao hàng là ở đâu ạ?**
**KH: 123 Lê Lợi, Quận 1, TP.HCM**
**Bot: Xác nhận đơn hàng:**
**Bot: • Quần Jean Slim Fit Nike x1 = 450,000đ**
**Bot: • Giao cho: Nguyễn Văn A — 0901234567**
**Bot: • Địa chỉ: 123 Lê Lợi, Q1, HCM**
**Bot: Bạn xác nhận đặt đơn không?**
**KH: OK, xác nhận**
*[Bot tạo order trong hệ thống]*
**Bot: Đơn hàng đã được tạo thành công! Mã đơn: #7DE649BB. Giao hàng trong 2–3 ngày.**
**UC3: Tra cứu đơn hàng**
**KH: Đơn hàng hôm qua của tôi đang ở đâu rồi?**
*[Bot gọi get_order_status()]*
**Bot: Đơn #7DE649BB của bạn đang ở trạng thái: Chờ xác nhận.**
**Bot: Tổng tiền: 450,000đ | Giao cho: Nguyễn Văn A | 123 Lê Lợi, Q1**
**UC4: Khiếu nại → Handoff**
**KH: Tôi muốn hoàn tiền đơn hàng vừa rồi**
*[Bot gọi escalate_to_human(reason=“khách yêu cầu hoàn tiền đơn #7DE649BB”)]*
**Bot: Mình đã ghi nhận và chuyển bạn sang nhân viên hỗ trợ. Bạn sẽ được liên hệ trong 5 phút.**
*[Session.status = HANDOFF, conversation_mode = HUMAN]*
**UC5: Multi-intent**
**KH: Cho tôi xem áo thun trắng, và kiểm tra đơn hàng hôm qua luôn**
*[Bot gọi search_products(color=trắng, category=áo thun)]*
*[Bot gọi get_order_status()]*
**Bot: Đây là kết quả tìm áo thun trắng: [danh sách]**
**Bot: Và đơn hàng gần nhất của bạn: #7DE649BB — Chờ xác nhận.**

# 6. UX và luồng hội thoại

## 6.1 Nguyên tắc thiết kế UX

**Ngắn gọn, tự nhiên: **Trả lời tiếng Việt tự nhiên, không dài dòng. Gợi ý bước tiếp theo rõ ràng.
**Không bịa dữ liệu: **Giá, tồn kho, trạng thái đơn chỉ được trả lời SAU KHI gọi tool tương ứng. Đây là hard constraint.
**Hỏi làm rõ: **Khi thiếu thông tin để hành động (ví dụ khách nói “mua quần” nhưng không nói màu/size), hỏi làm rõ trước.
**Hạn chế spam: **Nếu nhiều kết quả, trả top N (3–5) + hướng dẫn lọc thêm.
**Graceful fallback: **Khi tool lỗi, thông báo lịch sự và đề xuất handoff hoặc thử lại sau.
**Proactive guidance: **Sau mỗi hành động, gợi ý bước tiếp theo phù hợp (ví dụ: sau add_to_cart gợi ý “mua thêm hay đặt hàng luôn?”).

## 6.2 Luồng tìm sản phẩm

Nhận nhu cầu từ khách → gọi search_products với các bộ lọc phù hợp
Nhiều kết quả (>5) → trả top 3–5 + hướng dẫn lọc thêm (giá, màu, size)
Khách chọn 1 sản phẩm → gọi get_product_detail hiển thị đầy đủ thông tin
Sản phẩm hết hàng → tự động gọi search_products() gợi ý thay thế
Không tìm thấy gì → hỏi thêm tiêu chí hoặc đề xuất sản phẩm phổ biến

## 6.3 Luồng đặt hàng end-to-end

**Điều kiện tiên quyết: **Giỏ hàng không trống. Nếu giỏ trống, start_order_flow trả về NEED_ITEMS và thông báo cho khách.
“Checkout” / “Đặt hàng” / “Xác nhận đơn” → gọi start_order_flow() → trả về NEED_NAME
Thu thập tên người nhận → lưu vào session state → chuyển NEED_PHONE
Thu thập SĐT (validate định dạng cơ bản) → chuyển NEED_ADDRESS
Thu thập địa chỉ giao hàng → chuyển NEED_CONFIRM
Bot gửi tóm tắt đơn (sản phẩm, số lượng, tổng tiền, thông tin giao hàng) để khách xác nhận
Khách xác nhận → tạo order trong hệ thống → trả mã đơn + tóm tắt → DONE

## 6.4 Luồng tra cứu đơn hàng

**get_order_status(order_id?): **Nếu không truyền order_id, lấy đơn gần nhất (bỏ qua DRAFT). Trả về: trạng thái, tổng tiền, địa chỉ, danh sách SP.
**list_orders(): **Liệt kê tất cả đơn hàng (bỏ qua DRAFT), sắp xếp theo ngày đặt mới nhất. Hiển thị: mã, trạng thái, tổng tiền, số SP, ngày.

## 6.5 Luồng handoff

**Trigger tự động: **
Khách yêu cầu khiếu nại, hoàn tiền, hủy đơn
Bot lặp không hiểu > N lần (cấu hình được, mặc định N=3)
Tool lỗi liên tiếp (>2 lần cùng tool hoặc >3 tool bất kỳ)
Tình huống nhạy cảm (ví dụ: khách tức giận, yêu cầu gặp quản lý)
**Hành động hệ thống: **
Set Session.status = HANDOFF
Set Session.conversation_mode = HUMAN
Dừng auto-reply AI cho session đó
Gửi thông báo cho khách: “Bạn sẽ được nhân viên hỗ trợ trong X phút”
Gửi context đầy đủ cho nhân viên: lý do handoff, mã đơn, SP liên quan, thông tin giao hàng

# 7. Yêu cầu chức năng

## 7.1 Orchestrator (Tool Calling)

**Input**
Message hiện tại của khách hàng
Conversation history (cửa sổ context, cấu hình được)
Session state (checkout step, draft_order_id, shipping info…)
Tool docstrings + constraints (mô tả tool, điều kiện gọi, tham số)
**Behavior**
0..N tool calls mỗi turn (đa tool cho multi-intent)
Tự quyết định tool nào gọi và thứ tự gọi dựa trên reasoning
Trả lời bằng tiếng Việt tự nhiên, tổng hợp kết quả từ các tool
**Hard constraints (BẮT BUỘC)**

| Constraint | Lý do |
| --- | --- |
| Không gọi start_order_flow khi cart trống | Tránh tạo đơn rỗng, gây nhầm lẫn |
| Không trả lời giá/tồn kho nếu chưa gọi tool | Chống hallucination — dữ liệu phải từ nguồn thật |
| Không trả lời trạng thái đơn nếu chưa gọi get_order_status | Thông tin đơn hàng thay đổi liên tục |
| Thiếu thông tin → hỏi làm rõ trước | Tránh gọi tool sai tham số |

## 7.2 Tools contract chi tiết (MVP)

Dưới đây là đặc tả chi tiết của từng tool, bao gồm: mô tả, tham số đầu vào, đầu ra, trigger ví dụ, và xử lý lỗi.

**Tool 1: search_products**

| Mô tả | Tìm kiếm sản phẩm trong database theo nhiều tiêu chí. Trả về danh sách variants còn hàng. Nếu hết hàng thì tìm các sản phẩm phù hợp nhất. |
| --- | --- |
| Input | filters: { category?, color?, size?, brand?, min_price?, max_price?, keyword? } |
| Output | Array of { variant_id, product_name, color, size, price, stock_quantity, image_url } |
| Trigger | “Tìm quần jean đen”, “Có giày nào dưới 1 triệu?”, “Cho xem áo thun trắng” |
| Error handling | Không tìm thấy: hỏi thêm tiêu chí hoặc đề xuất SP phổ biến. DB lỗi: thông báo + đề xuất thử lại. |

**Tool 2: get_product_detail**

| Mô tả | Lấy thông tin đầy đủ của một variant: mô tả, ảnh, giá, tồn kho. |
| --- | --- |
| Input | variant_id: string (bắt buộc) |
| Output | { variant_id, product_name, sku, color, size, price, stock_quantity, description, image_urls[] } |
| Trigger | “Cho tôi xem chi tiết cái đầu tiên”, “Mô tả sản phẩm var-001”, “Còn bao nhiêu cái?” |
| Error handling | Variant không tồn tại: thông báo và gợi ý search lại. |

**Tool 3: add_to_cart**

| Mô tả | Thêm variant vào giỏ hàng (draft order). Tự động tạo draft order nếu chưa có. Cộng dồn nếu variant đã có. Recompute total_amount. |
| --- | --- |
| Input | variant_id: string (bắt buộc), quantity: number (mặc định 1) |
| Output | { success, cart_summary: { total_items, total_amount }, added_item: { name, qty, price } } |
| Trigger | “Thêm vào giỏ hàng”, “Lấy cho tôi 2 cái”, khách đã chọn variant + đồng ý mua |
| Error handling | Hết hàng: thông báo + gợi ý tương tự. Số lượng > tồn kho: thông báo số còn lại. |

**Tool 4: remove_from_cart**

| Mô tả | Xóa một variant khỏi giỏ. Yêu cầu xác nhận từ khách và variant_id hợp lệ. |
| --- | --- |
| Input | variant_id: string (bắt buộc) |
| Output | { success, removed_item, cart_summary } |

**Tool 5: view_cart**

| Mô tả | Xem nội dung giỏ hàng. Hiển thị live price, subtotal từng item và tổng cộng. Trả “Giỏ hàng trống” nếu chưa có gì. |
| --- | --- |
| Input | (không có tham số) |
| Output | { items: [{ name, variant, qty, unit_price, subtotal }], total_amount } hoặc { empty: true } |
| Trigger | “Giỏ hàng của tôi có gì?”, “Tổng tiền bao nhiêu?”, trước khi checkout |

**Tool 6: clear_cart**

| Mô tả | Xóa toàn bộ giỏ hàng. Yêu cầu xác nhận từ khách trước khi thực hiện. |
| --- | --- |
| Input | (không có tham số) |
| Output | { success, cleared_items_count } |

**Tool 7: start_order_flow**

| Mô tả | Khởi động luồng đặt hàng multi-step. Kiểm tra giỏ hàng và trả signal để orchestrator chuyển sang checkout state machine. |
| --- | --- |
| Input | (không có tham số) |
| Output | Cart có hàng: { signal: NEED_NAME, cart_summary }. Cart trống: { signal: NEED_ITEMS }. |
| HARD CONSTRAINT | KHÔNG gọi khi khách chưa add_to_cart. Đây là constraint cứng trong docstring. |

**Tool 8: get_order_status**

| Mô tả | Tra cứu trạng thái đơn hàng. Mặc định lấy đơn gần nhất (bỏ qua DRAFT). |
| --- | --- |
| Input | order_id: string (tùy chọn — nếu None lấy đơn gần nhất) |
| Output | { order_id, status, total_amount, shipping_address, shipping_name, shipping_phone, created_at, items[] } |
| Trigger | “Đơn hàng của tôi đang ở đâu?”, “Kiểm tra đơn #ORD-001”, “Bao giờ giao hàng?” |

**Tool 9: list_orders**

| Mô tả | Liệt kê toàn bộ đơn hàng của customer (bỏ qua DRAFT), sắp xếp mới nhất trước. |
| --- | --- |
| Input | (không có tham số — tự động dùng customer_id từ session) |
| Output | Array of { order_id, status, total_amount, item_count, created_at } |
| Trigger | “Tôi có bao nhiêu đơn hàng?”, “Lịch sử mua hàng của tôi” |

**Tool 10: get_store_info**

| Mô tả | Truy xuất thông tin cửa hàng từ FAQ/policy từ uploaded files. Nhận topic string và trả câu trả lời tương ứng. |
| --- | --- |
| Input | topic: string (hours | address | shipping | return | payment | general) |
| Output | { topic, answer: string } — nội dung từ knowledge base |
| Trigger | “Cửa hàng mở đến mấy giờ?” → hours | “Ship có mất phí không?” → shipping | “Đổi trả như thế nào?” → return |

**Tool 11: escalate_to_human**

| Mô tả | Chuyển hội thoại sang nhân viên. Ghi lý do escalate. Set HANDOFF + HUMAN mode. |
| --- | --- |
| Input | reason: string (lý do handoff — bắt buộc) |
| Output | { escalated: true, reason, session_status: HANDOFF } |
| Side effects | Session.status = HANDOFF, Session.conversation_mode = HUMAN, ngăn bot tiếp tục reply |
| Trigger | “Tôi muốn khiếu nại”, “Hoàn tiền cho tôi”, câu hỏi vượt khả năng bot, tool lỗi liên tục |

## 7.3 Checkout state machine

Luồng checkout được quản lý bằng state machine với các bước rõ ràng:
**Transitions: **NEED_NAME → NEED_PHONE → NEED_ADDRESS → NEED_CONFIRM → DONE

**Session state tối thiểu cần lưu: **

| Field | Mô tả |
| --- | --- |
| current_step | Bước hiện tại của checkout flow |
| draft_order_id / cart_id | ID của giỏ hàng / draft order |
| shipping_name | Tên người nhận hàng |
| shipping_phone | Số điện thoại người nhận |
| shipping_address | Địa chỉ giao hàng |
| last_selected_variant_id | Variant cuối cùng khách chọn (context) |

## 7.4 Knowledge/FAQ management

**Single source of truth: **FAQ/policy lưu trong DB/PDF, có versioning
**Topic mapping: **Map topic (hours, shipping, return, address, payment) đến câu trả lời cụ thể
**RAG fallback: **Khi topic không match, dùng retrieval để tìm câu trả lời gần đúng nhất
**Admin cập nhật: **Store admin có thể cập nhật FAQ qua giao diện quản trị

# 8. Yêu cầu phi chức năng

| Yêu cầu | Chi tiết | Mục tiêu / Ghi chú |
| --- | --- | --- |
| Data correctness | Mọi dữ liệu giao dịch (giá, tồn kho, trạng thái đơn) lấy từ DB/services | Hallucination incidents = 0 |
| Latency | End-to-end response time bao gồm LLM reasoning + tool call + response generation | Mục tiêu p95 ≤ X giây (cần chốt theo infra) |
| Reliability | Graceful degradation khi tool lỗi. Auto-handoff khi cần. | Uptime target: 99.5% |
| Multi-channel consistency | Logic thống nhất giữa Zalo, Messenger, Telegram. Chỉ khác adapter UI. | Core engine chia sẻ giữa các kênh |
| Scalability | Hệ thống phải xử lý được peak hours không sụp. | Rate limiting + queue cho tool calls |
| Idempotency | Đảm bảo không tạo đơn trùng khi retry/network issue. | Idempotency key cho order creation |

# 9. Edge cases chi tiết

| Tình huống | Xử lý | Ví dụ |
| --- | --- | --- |
| Không tìm thấy SP | Hỏi thêm tiêu chí hoặc đề xuất SP phổ biến | “Mình không tìm thấy SP phù hợp. Bạn có muốn xem SP bán chạy?” |
| SP hết hàng | Gọi search_products() gợi ý thay thế | “SP này hết hàng rồi. Mình gợi ý mấy cái tương tự:” |
| User đổi ý giữa checkout | Cho phép quay lại view_cart, thêm/xóa SP | “Bạn muốn sửa giỏ hàng không? Xem lại giỏ nhé” |
| Tool downtime | Thông báo lịch sự + tự động handoff | “Hệ thống đang bảo trì. Mình chuyển bạn sang NV hỗ trợ” |
| Giá thay đổi giữa search và checkout | Recompute tại bước confirm, thông báo nếu khác | “Giá đã cập nhật từ 450k → 470k. Bạn vẫn muốn đặt?” |
| SĐT/địa chỉ không hợp lệ | Validate cơ bản, hỏi lại | “SĐT không đúng định dạng. Bạn nhập lại nhé” |
| Khách gửi ảnh/sticker/file | Thông báo chưa hỗ trợ, gợi ý dùng text | “Mình chưa đọc được ảnh. Bạn mô tả bằng text nhé” |
| Multi-session cùng lúc | Mỗi kênh = 1 session độc lập, cart riêng | Giỏ hàng trên Zalo và Messenger là riêng biệt |
| Bot không hiểu > N lần | Tự động escalate_to_human | “Mình chưa hiểu ý bạn. Để mình chuyển sang NV” |

# 10. Tiêu chí nghiệm thu chi tiết

| # | Tiêu chí | Điều kiện pass | Status |
| --- | --- | --- | --- |
| 1 | Trả lời FAQ đúng | Bot trả lời chính xác ≥5 topics khác nhau từ knowledge base | □ Pending |
| 2 | Search theo nhiều tiêu chí | Tìm được SP theo ≥3 tiêu chí kết hợp (màu+size+giá) | □ Pending |
| 3 | Không checkout khi cart trống | start_order_flow trả về NEED_ITEMS, không tạo order | □ Pending |
| 4 | Tạo order thành công | Sau checkout flow, order được tạo trong DB, trả mã + tóm tắt | □ Pending |
| 5 | Tra đơn hàng | Tra được đơn gần nhất và theo mã, hiển thị đúng trạng thái | □ Pending |
| 6 | Handoff hoạt động | Complaint/refund → HANDOFF + dừng auto-reply + context đầy đủ | □ Pending |
| 7 | Giỏ hàng đầy đủ | Thêm, xóa, xem, clear đều hoạt động, total đúng | □ Pending |
| 8 | Identity mapping | KH từ Zalo được link đúng với contact trong GapOne | □ Pending |
| 9 | Multi-intent | Câu “xem áo trắng và kiểm tra đơn” → trả lời cả 2 yêu cầu | □ Pending |
| 10 | Không hallucination | Giá, tồn kho, trạng thái đơn chỉ từ tool, không bịa | □ Pending |
| 11 | SP hết hàng | Tự động gợi ý SP tương tự khi SP được chọn hết hàng | □ Pending |
| 12 | Error handling | Tool lỗi → thông báo lịch sự + đề xuất handoff hoặc thử lại | □ Pending |

Kiến trúc

# 1. Tổng quan

## 1.1 Kiến trúc Tool Calling

Trong kiến trúc Tool Calling  (LangChain / LangGraph), LLM (Large Language Model) không chỉ trả lời bằng text mà còn chủ động gọi các hàm (tools) để truy xuất dữ liệu thật, thực hiện hành động và kết hợp nhiều bước logic trong một hội thoại. Mỗi tool được mô tả bằng docstring + constraints, và LLM tự quyết định gọi tool nào, khi nào, với tham số gì.

**Luồng xử lý chính: **Conversation → AI Orchestrator → Tool Calls → Database/Services → Response

## 1.2 Nguyên tắc chung

**Không bịa dữ liệu: **Giá, tồn kho, trạng thái đơn chỉ được trả lời SAU KHI gọi tool tương ứng. Đây là hard constraint.
**Multi-intent: **LLM có thể gọi nhiều tools trong cùng 1 turn (ví dụ: vừa search SP vừa tra đơn).
**Hỏi làm rõ trước: **Khi thiếu thông tin để gọi tool, hỏi khách trước thay vì đoán.
**Graceful fallback: **Khi tool lỗi, thông báo lịch sự + đề xuất handoff hoặc thử lại.
**Tiếng Việt tự nhiên: **Mọi response từ bot phải ngắn gọn, dễ hiểu, gợi ý bước tiếp theo.

## 1.3 Danh sách tất cả tools (MVP)

| # | Tool name | Nhóm | Mô tả ngắn |
| --- | --- | --- | --- |
| 1 | search_product | Product | Semantic search SP theo ngôn ngữ tự nhiên + bộ lọc |
| 2 | get_product_detail | Product | Lấy thông tin đầy đủ 1 variant |
| 3 | add_to_cart | Order | Thêm SP vào giỏ hàng |
| 4 | remove_from_cart | Order | Xóa 1 SP khỏi giỏ |
| 5 | view_cart | Order | Xem nội dung giỏ hàng |
| 6 | clear_cart | Order | Xóa toàn bộ giỏ hàng |
| 7 | start_order_flow | Order | Khởi động checkout multi-step |
| 8 | get_order_status | Order | Tra cứu trạng thái đơn hàng |
| 9 | list_orders | Order | Liệt kê lịch sử đơn hàng |
| 10 | get_store_info | Info / FAQ | Truy xuất thông tin cửa hàng |
| 11 | escalate_to_human | Human Handoff | Chuyển sang nhân viên hỗ trợ |

## 1.4. So sánh: Intent Classification vs Tool Calling

| Khía cạnh | Intent Classification | Tool Calling |
| --- | --- | --- |
| Triết lý | Top-down: con người định nghĩa intent trước, LLM chỉ phân loại vào đúng hộp | Bottom-up: LLM tự chọn hành động dựa trên tools và docstring |
| Vai trò LLM | Classifier — bị giới hạn trong label space | Orchestrator — reasoning + decision-making |
| Multi-intent | 1 intent/turn — “xem quần và kiểm tra đơn” chỉ xử lý 1 việc | Gọi nhiều tools liên tiếp, trả lời cả hai |
| Câu mơ hồ | Dễ route sai — “mua quần” bị route sang ORDER agent | Tự xử lý: hỏi thêm hoặc search trước khi hành động |
| Thêm tính năng | Sửa 4–5 chỗ: classifier prompt, route_map, agent, graph node, edge | Sửa 1 chỗ: thêm @tool function + docstring |
| Hallucination | Trung bình — LLM có thể bịa nếu agent không gọi tool | Thấp — data luôn từ tool thật, safety check code-level |
| Coupling | Tight — intent ↔ agent ↔ graph phụ thuộc chặt | Loose — tools độc lập, dễ thêm/xóa/thay thế |
| Latency | Thấp hơn — ít LLM reasoning | Cao hơn ~200–500ms — có reasoning + tool calls |
| Control | Deterministic routing, dễ predict | Phụ thuộc docstring, cần viết chặt |

**Case thực tế: ***User nói “tôi muốn mua quần” — Intent Classification match keyword “mua” → route sang ORDER agent (SAI vì chưa có SP cụ thể). Tool Calling đọc docstring “KHÔNG gọi khi chưa add_to_cart” → gọi search_products trước (ĐÚNG).*

# 2. Product Tools

Nhóm tools phục vụ việc tìm kiếm, xem chi tiết và gợi ý sản phẩm. Đây là nhóm được gọi thường xuyên nhất, là đầu vào cho toàn bộ funnel chuyển đổi.
**search_products**
**Mô tả: **Tìm kiếm sản phẩm sử dụng Semantic Search (vector similarity) thay vì keyword match cứng. Khi khách hỏi bằng ngôn ngữ tự nhiên (ví dụ: “đồ gia dụng”, “quà tặng cho bạn gái”), tool sẽ tìm các sản phẩm có ngữ nghĩa liên quan (loosely overlapping) thay vì chỉ khớp chính xác category. Các bộ lọc cứng (màu, size, giá…) được áp dụng phÍa SAU semantic ranking để thu hẹp kết quả. Kết quả trả về danh sách variants còn hàng, sắp xếp theo độ phù hợp (relevance score).

| Input | query: string (câu hỏi / mô tả tự nhiên của khách — BẮT BUỘC), filters?: { category?: string, color?: string, size?: string, brand?: string, min_price?: number, max_price?: number }, top_k?: number (số kết quả trả về, mặc định = 5) |
| --- | --- |
| Output | Array of { variant_id: string, product_name: string, color: string, size: string, price: number, stock_quantity: number, image_url: string, relevance_score: float (0–1) } |
| Error handling | Không tìm thấy: hỏi thêm tiêu chí, gợi ý từ khác hoặc đề xuất SP phổ biến. DB/embedding service lỗi: thông báo lỗi + đề xuất thử lại hoặc handoff. |

**Trigger ví dụ**
*“**Tôi muốn mua quần đen Nike size M**”*
*“**Có giày nào dưới 1 triệu không?**”*
*“**Cho xem áo thun trắng**”*
*“**Đồ gia dụng có gì?**”*
*“**Quà tặng cho bạn gái**”*
*“**Có gì mặc đi biển không?**”*
*“**Sản phẩm phù hợp cho mùa đông**”*
**Ví dụ hội thoại**
**KH: Tôi muốn mua quần đen Nike size M dưới 500k**
*[Orchestrator gọi search_products(query="quần đen Nike size M", filters={color:"đen", brand:"Nike", size:"M", max_price:500000})]*
**Bot: Mình tìm được 2 sản phẩm phù hợp:**
**Bot: 1. [var-001-1] Quần Jean Nam Slim Fit — đen, M — 450,000đ — Còn 15**
**Bot: 2. [var-003-2] Quần Jean Nam Regular — đen, M — 480,000đ — Còn 8**
**Bot: Bạn muốn xem chi tiết sản phẩm nào?**

Khác với keyword search truyền thống (khớp chính xác từ khóa vào tên/category), search_products sử dụng semantic search để hiểu ý định của khách hàng và tìm các sản phẩm có ngữ nghĩa liên quan, kể cả khi không khớp keyword hay category.
**Vì sao cần Semantic Search?**

| Keyword Search (truyền thống) | Semantic Search (GAPCon) |
| --- | --- |
| Khách hỏi “đồ gia dụng” → tìm category = “đồ gia dụng”. Nếu không có category này → 0 kết quả. | Khách hỏi “đồ gia dụng” → hiểu ngữ nghĩa → tìm được máy giặt, máy hút bụi, nồi chiên… dù chúng thuộc category “electronics” hay “kitchen”. |
| Khách hỏi “quà tặng cho bạn gái” → không match bất kỳ keyword/category nào. | Hiểu “quà tặng bạn gái” ≈ phụ kiện, thời trang nữ, mỹ phẩm… → trả về SP phù hợp. |
| Khách hỏi “đồ mặc đi biển” → không có category “đi biển”. | Hiểu ngữ cảnh → tìm được quần short, áo tank top, dép, kính mát… |

**Cách hoạt động**
**Bước 1 — Embedding: **Biến query của khách và thông tin SP (tên + mô tả + category + tags) thành vector bằng mô hình embedding (ví dụ: multilingual-e5, BGE-M3, hoặc OpenAI text-embedding).
**Bước 2 — Vector similarity: **Tìm top-K vectors gần nhất (cosine similarity) trong vector store (Qdrant, Pinecone, pgvector…).
**Bước 3 — Post-filter: **Áp dụng các bộ lọc cứng (color, size, brand, min/max_price) lên kết quả semantic để thu hẹp.
**Bước 4 — Stock filter: **Loại bỏ các variants hết hàng (stock_quantity = 0).
**Bước 5 — Return: **Trả về danh sách còn lại, sắp xếp theo relevance_score giảm dần.
Query của khách là **ngôn ngữ tự nhiên tiếng Việt***. Embedding model phải hỗ trợ multilingual để hiểu đúng ngữ nghĩa tiếng Việt và các biến thể (“quần bò” = “jean”, “đồ gia dụng” ≈ “appliance”…).*
**Ví dụ: Semantic search vượt category**
**KH: Có đồ gia dụng gì không?**
*[Orchestrator gọi search_products(query="đồ gia dụng")]*
*[Semantic search: "đồ gia dụng" ≈ appliance, household → match SP từ nhiều category]*
**Bot: Mình tìm được mấy sản phẩm gia dụng nè:**
**Bot: 1. [var-101] Máy giặt Samsung 8kg — 12,500,000đ (category: electronics)**
**Bot: 2. [var-205] Máy hút bụi Dyson V8 — 8,900,000đ (category: electronics)**
**Bot: 3. [var-310] Nồi chiên không dầu Philips — 2,800,000đ (category: kitchen)**
**Bot: 4. [var-412] Bàn ủi hơi nước Tefal — 1,200,000đ (category: home)**
**Bot: Bạn quan tâm cái nào? Mình có thể xem chi tiết nhé!**

**Lưu ý: **Kết quả trên đến từ 3 category khác nhau (electronics, kitchen, home) — keyword search truyền thống sẽ không tìm được vì không có category “đồ gia dụng” nào match.

**Ví dụ: Semantic search theo intent**
**KH: Gợi ý cho tôi quà tặng cho bạn gái dưới 500k**
*[Orchestrator gọi search_products(query="quà tặng cho bạn gái", filters={max_price: 500000})]*
*[Semantic: "quà tặng bạn gái" ≈ phụ kiện nữ, thời trang nữ, mỹ phẩm, trang sức]*
**Bot: Mình gợi ý mấy món quà phù hợp:**
**Bot: 1. [var-501] Khăn lụa Hermes mini — 450,000đ (category: accessories)**
**Bot: 2. [var-502] Son MAC Ruby Woo — 380,000đ (category: beauty)**
**Bot: 3. [var-503] Vòng tay bạc 925 — 320,000đ (category: jewelry)**

**Lưu ý: **“Quà tặng cho bạn gái” không phải là category hay keyword nào — nhưng semantic search hiểu được intent và tìm SP phù hợp từ nhiều category.
**Hybrid approach: Semantic + Filters**
search_products kết hợp 2 cơ chế:

| Thành phần | Mô tả | Ví dụ |
| --- | --- | --- |
|  | Embedding query + cosine similarity để tìm SP có ngữ nghĩa liên quan. Cho phép loosely overlapping vượt category. | query = "đồ gia dụng" → match máy giặt (electronics), nồi chiên (kitchen) |
|  | Áp dụng sau semantic ranking: color, size, brand, min/max_price, stock > 0. Thu hẹp kết quả chính xác. | filters = {max_price: 500000} → loại SP > 500k khỏi kết quả semantic |

**Thứ tự ưu tiên: **Semantic ranking trước (tìm đúng ý định) → Filters sau (thu hẹp đúng điều kiện). Nếu Orchestrator truyền cả query và filters, pipeline là: embed(query) → vector search top-K → apply filters → remove out-of-stock → return.
**Xử lý tình huống đặc biệt**

| Tình huống | Xử lý |
| --- | --- |
| Query quá chung (“coi có gì hay”) | Trả về SP bán chạy / mới nhất. Gợi ý khách nói rõ hơn. |
| Semantic match nhưng relevance thấp (< 0.3) | Thông báo kết quả có thể không chính xác lắm, hỏi khách xác nhận hoặc mô tả rõ hơn. |
| Filters loại hết kết quả semantic | Thông báo không có SP khớp cả ý định và bộ lọc. Gợi ý nới lỏng (ví dụ: bỏ filter giá hoặc đổi size). |
| Tiếng Việt lóng / viết tắt | Embedding model multilingual xử lý: “quần bò” = “jean”, “đt” = “điện thoại”. Nếu không hiểu, hỏi làm rõ. |
| Mix semantic + exact keyword | Khách nói “Nike đen”: “Nike” match exact brand filter, “đen” match exact color, nhưng toàn bộ câu cũng được embed để semantic ranking. |

**get_product_detail**
**Mô tả: **Lấy thông tin đầy đủ của một variant cụ thể: mô tả sản phẩm, hình ảnh, giá hiện tại, số lượng tồn kho. Thường được gọi sau khi search trả về nhiều kết quả và khách muốn xem kỹ một sản phẩm.

| Input | variant_id: string (BẮT BUỘC) |
| --- | --- |
| Output | { variant_id, product_name, sku, color, size, price, stock_quantity, description, image_urls: string[] } |
| Error handling | Variant không tồn tại: thông báo và gợi ý gọi search_products lại. |

**Trigger ví dụ**
*“**Cho tôi xem chi tiết cái đầu tiên**”*
*“**Mô tả sản phẩm var-001-1**”*
*“**Còn bao nhiêu cái?**”*
*“**Xem ảnh sản phẩm này**”*
**Ví dụ hội thoại**
**KH: Cho xem chi tiết cái đầu tiên**
*[Orchestrator gọi get_product_detail(variant_id=var-001-1)]*
**Bot: Quần Jean Nam Slim Fit**
**Bot: SKU: QJN-DEN-28 | Màu: đen | Size: 28**
**Bot: Giá: 450,000đ | Còn: 15 cái**
**Bot: Mô tả: Denim co giãn 4 chiều, thoáng mát, phù hợp mặc hàng ngày**
**Bot: Bạn muốn thêm vào giỏ hàng không?**

# 3. Order Tools

Nhóm tools quản lý giỏ hàng. Giỏ hàng được hiển thực dưới dạng draft order trong hệ thống GapOne. Mỗi session có tối đa 1 giỏ hàng.
**add_to_cart**
**Mô tả: **Thêm một variant vào giỏ hàng (draft order). Tự động tạo draft order nếu chưa có. Nếu variant đã có trong giỏ thì cộng dồn số lượng. Tự động recompute total_amount sau mỗi lần thêm.

| Input | variant_id: string (BẮT BUỘC), quantity: number (mặc định = 1) |
| --- | --- |
| Output | { success: boolean, cart_summary: { total_items: number, total_amount: number }, added_item: { name, qty, unit_price } } |
| Side effects | Tạo draft order nếu chưa có. Cập nhật line_items và total_amount. |
| Error handling | Hết hàng: thông báo + gọi search_products(). Số lượng yêu cầu > tồn kho: thông báo số còn lại và hỏi khách có muốn lấy số còn không. |

**Trigger ví dụ**
*“**Thêm vào giỏ hàng**”*
*“**Lấy cho tôi 2 cái**”*
*“**Mua luôn cái này**”*
*“**(Khách đã chọn variant cụ thể + đồng ý mua)**”*
**Ví dụ hội thoại**
**KH: Lấy cho tôi 2 cái**
*[Orchestrator gọi add_to_cart(variant_id=var-001-1, quantity=2)]*
**Bot: Đã thêm 2 x Quần Jean Nam Slim Fit (đen, 28) vào giỏ.**
**Bot: Tổng giỏ hàng: 900,000đ (2 sản phẩm)**
**Bot: Bạn muốn tiếp tục mua hay đặt hàng luôn?**

**remove_from_cart**
**Mô tả: **Xóa một product variant khỏi giỏ hàng. Yêu cầu xác nhận từ khách hàng trước khi thực hiện và variant_id phải hợp lệ (tồn tại trong giỏ).

| Input | variant_id: string (BẮT BUỘC) |
| --- | --- |
| Output | { success: boolean, removed_item: { name, qty, unit_price }, cart_summary: { total_items, total_amount } } |
| Side effects | Cập nhật line_items và total_amount của draft order. |
| Error handling | Variant không có trong giỏ: thông báo và hiển thị nội dung giỏ hiện tại. Giỏ trống: thông báo giỏ đang trống. |

**Trigger ví dụ**
*“**Bỏ cái quần ra khỏi giỏ**”*
*“**Xóa sản phẩm đầu tiên**”*
*“**Không lấy cái đó nữa**”*
**Ví dụ hội thoại**
**KH: Bỏ cái áo thun ra nhé**
**Bot: Bạn muốn xóa Áo Thun Nam Basic (trắng, M) khỏi giỏ đúng không?**
**KH: Đúng rồi**
*[Orchestrator gọi remove_from_cart(variant_id=var-002-1)]*
**Bot: Đã xóa! Giỏ còn 1 SP, tổng: 450,000đ.**

**view_cart**
**Mô tả: **Xem nội dung giỏ hàng hiện tại. Hiển thị live price từ ProductVariant (lấy giá mới nhất, không dùng giá cũ), tính subtotal từng item và tổng cộng. Trả về “Giỏ hàng trống.” nếu chưa có gì.

| Input | (không có tham số) |
| --- | --- |
| Output | { items: [{ variant_id, name, variant_label, qty, unit_price, subtotal }], total_amount } hoặc { empty: true } |

**Trigger ví dụ**
*“**Giỏ hàng của tôi có gì?**”*
*“**Tổng tiền bao nhiêu?**”*
*“**Xem giỏ hàng**”*
*“**(Tự động gọi trước khi bắt đầu checkout)**”*
**Ví dụ hội thoại**
**KH: Giỏ hàng của tôi có gì?**
*[Orchestrator gọi view_cart()]*
**Bot: Giỏ hàng của bạn:**
**Bot: 1. Quần Jean Nam Slim Fit | đen, 28 — 450,000đ × 1 = 450,000đ**
**Bot: 2. Áo Thun Nam Basic | trắng, M — 199,000đ × 2 = 398,000đ**
**Bot: Tổng cộng: 848,000đ**
**Bot: Bạn muốn đặt hàng hay mua thêm?**

**clear_cart**
**Mô tả: **Xóa TOÀN BỘ sản phẩm trong giỏ hàng cùng lúc. Dùng khi khách muốn làm trống hoặc bắt đầu lại giỏ hàng.

| Input | (không có tham số) |
| --- | --- |
| Output | { success: boolean, cleared_items_count: number } |
|  |  |
| Side effects | Xóa toàn bộ line_items của draft order. Reset total_amount = 0. |
| Error handling | Giỏ đã trống: thông báo giỏ đang trống, không cần xóa. |

**Trigger ví dụ**
*“**Xóa hết giỏ hàng**”*
*“**Làm trống giỏ**”*
*“**Bỏ hết đi, tôi muốn chọn lại**”*
**Ví dụ hội thoại**
**KH: Xóa hết giỏ hàng đi**
**Bot: Giỏ hàng của bạn có 3 sản phẩm. Bạn chắc chắn muốn xóa hết không?**
**KH: Ʈ̀, xóa đi**
*[Orchestrator gọi clear_cart()]*
**Bot: Đã xóa toàn bộ 3 sản phẩm. Giỏ hàng đang trống.**
**Bot: Bạn muốn tìm sản phẩm mới không?**

**start_order_flow**
**Mô tả: **Khởi động luồng đặt hàng multi-step. Kiểm tra giỏ hàng và trả về signal để orchestrator chuyển sang checkout state machine: thu thập tên → SĐT → địa chỉ → xác nhận. Trả về NEED_NAME nếu giỏ có hàng, NEED_ITEMS nếu giỏ trống.

| Input | (không có tham số) |
| --- | --- |
| Output | Giỏ có hàng: { signal: "NEED_NAME", cart_summary: { items[], total_amount } }Giỏ trống: { signal: "NEED_ITEMS" } |
|  |  |
| Side effects | Tạo order thật trong DB khi khách xác nhận. Cập nhật session state (checkout step, shipping info). Idempotency key chống tạo đơn trùng. |
| Error handling | Giỏ trống: trả về NEED_ITEMS và thông báo cho khách. SĐT sai định dạng: hỏi nhập lại. |

**Trigger ví dụ**
*“**Đặt hàng ngay**”*
*“**Checkout**”*
*“**Xác nhận đơn hàng**”*
*“**Mua luôn**”*
*“**(Sau khi add_to_cart thành công và khách muốn đặt)**”*
**Ví dụ hội thoại**
**KH: Đặt hàng luôn nhé**
*[Orchestrator gọi start_order_flow()]*
*[Signal: NEED_NAME + cart_summary]*
**Bot: Đơn hàng của bạn:**
**Bot: • Quần Jean Slim Fit (x1) = 450,000đ**
**Bot: • Áo Thun Basic (x2) = 398,000đ**
**Bot: Tổng: 848,000đ**
**Bot: Cho mình xin tên người nhận nhé?**

**KH: Nguyễn Văn A**
*[current_step → NEED_PHONE]*
**Bot: Cảm ơn anh A! Số điện thoại nhận hàng là gì ạ?**

**KH: 0901234567**
*[current_step → NEED_ADDRESS]*
**Bot: Địa chỉ giao hàng là ở đâu ạ?**

**KH: 123 Lê Lợi, Quận 1, TP.HCM**
*[current_step → NEED_CONFIRM]*
**Bot: Xác nhận đơn hàng:**
**Bot: • Quần Jean Slim Fit x1 = 450,000đ**
**Bot: • Áo Thun Basic x2 = 398,000đ**
**Bot: Tổng: 848,000đ**
**Bot: Giao cho: Nguyễn Văn A — 0901234567**
**Bot: Địa chỉ: 123 Lê Lợi, Q1, HCM**
**Bot: Bạn xác nhận đặt đơn không?**

**KH: OK xác nhận**
*[Tạo order trong hệ thống → DONE]*
**Bot: Đơn hàng đã tạo thành công! Mã đơn: #7DE649BB**
**Bot: Giao hàng trong 2–3 ngày. Cảm ơn bạn!**

## 4.1 Checkout State Machine

**Transitions: **NEED_NAME → NEED_PHONE → NEED_ADDRESS → NEED_CONFIRM → DONE

| Session State Field | Type | Mô tả |
| --- | --- | --- |
|  | enum | Bước hiện tại của checkout flow |
|  | UUID | ID của giỏ hàng / draft order |
|  | string | Tên người nhận hàng |
|  | string | SĐT (định dạng VN: 10 số) |
|  | string | Địa chỉ giao hàng |
|  | string | Variant cuối cùng khách chọn (context) |

**get_order_status**
**Mô tả: **Tra cứu trạng thái đơn hàng. Nếu không truyền order_id thì lấy đơn hàng gần nhất (đơn mới nhất không phải DRAFT). Trả về đầy đủ trạng thái, tổng tiền, địa chỉ giao hàng và danh sách sản phẩm.

| Input | order_id: string (Tùy chọn — nếu None lấy đơn gần nhất) |
| --- | --- |
| Output | { order_id, status, total_amount, shipping_name, shipping_phone, shipping_address, created_at, items: [{ name, qty, price, subtotal }] } |
|  |  |
| Error handling | Không tìm thấy đơn: thông báo không có đơn hàng nào. Mã đơn sai: gợi ý kiểm tra lại mã. |

**Trigger ví dụ**
*“**Đơn hàng của tôi đang ở đâu?**”*
*“**Kiểm tra đơn #ORD-001**”*
*“**Bao giờ giao hàng?**”*
*“**Đơn hôm qua của tôi thế nào rồi?**”*
**Ví dụ hội thoại**
**KH: Đơn hàng hôm qua của tôi đang ở đâu rồi?**
*[Orchestrator gọi get_order_status() — không có order_id → lấy đơn gần nhất]*
**Bot: Đơn #7DE649BB của bạn:**
**Bot: Trạng thái: Chờ xác nhận**
**Bot: Tổng tiền: 848,000đ**
**Bot: Giao cho: Nguyễn Văn A — 0901234567**
**Bot: Địa chỉ: 123 Lê Lợi, Q1, HCM**
**Bot: Ngày đặt: 09/04/2026**
**Bot: Sản phẩm: Quần Jean Nam ×1 = 450,000đ**

**list_orders**
**Mô tả: **Liệt kê tất cả đơn hàng của customer (bỏ qua DRAFT), sắp xếp theo ngày đặt mới nhất trước. Hiển thị tóm tắt: mã đơn, trạng thái, tổng tiền, số lượng sản phẩm, ngày đặt.

| Input | (không có tham số — tự động dùng customer_id từ session) |
| --- | --- |
| Output | Array of { order_id, status, total_amount, item_count, created_at } |
| Error handling | Không có đơn nào: thông báo chưa có đơn hàng và gợi ý tìm sản phẩm. |

**Trigger ví dụ**
*“**Tôi có bao nhiêu đơn hàng?**”*
*“**Lịch sử mua hàng của tôi**”*
*“**Xem tất cả đơn hàng**”*
**Ví dụ hội thoại**
**KH: Xem lịch sử mua hàng của tôi**
*[Orchestrator gọi list_orders()]*
**Bot: Bạn có 4 đơn hàng:**
**Bot: 1. #7DE649BB | Chờ xác nhận | 848,000đ | 2 sp | 09/04/2026**
**Bot: 2. #ORD-001 | Chờ xác nhận | 649,000đ | 2 sp | 09/04/2026**
**Bot: 3. #ORD-002 | Đang giao | 1,200,000đ | 1 sp | 07/04/2026**
**Bot: 4. #ORD-003 | Hoàn thành | 398,000đ | 1 sp | 02/04/2026**
**Bot: Bạn muốn xem chi tiết đơn nào không?**

# 4. FAQ Tool

**get_store_info**
**Mô tả: **Truy xuất thông tin cửa hàng từ FAQ tĩnh (knowledge base). Nhận topic string và trả về câu trả lời tương ứng. Dùng cho mọi câu hỏi về vận hành cửa hàng không liên quan đến sản phẩm hay đơn hàng.

| Input | topic: string (hours | address | shipping | return | payment | general) |
| --- | --- |
| Output | { topic: string, answer: string } |
| Error handling | Topic không tìm thấy: dùng RAG fallback để tìm câu trả lời gần đúng nhất. Nếu vẫn không có: thông báo và đề xuất handoff. |

**Trigger ví dụ**
*“**Cửa hàng mở đến mấy giờ? → hours**”*
*“**Địa chỉ ở đâu? → address**”*
*“**Ship có mất phí không? → shipping**”*
*“**Đổi trả như thế nào? → return**”*
*“**Thanh toán bằng gì? → payment**”*
**Ví dụ hội thoại**
**KH: Cửa hàng mở đến mấy giờ?**
*[Orchestrator gọi get_store_info(topic="hours")]*
**Bot: Cửa hàng mở cửa 8:00–22:00 tất cả các ngày kể cả lễ tết.**

**KH: Ship về tỉnh mất bao nhiêu ngày?**
*[Orchestrator gọi get_store_info(topic="shipping")]*
**Bot: Miễn phí đơn từ 500,000đ. Giao 2–3 ngày nội thành, 4–5 ngày tỉnh.**

## 4.1 Topic Mapping

| Topic | Ví dụ câu hỏi | Nguồn dữ liệu |
| --- | --- | --- |
|  | Giờ mở cửa, ngày nghỉ, lễ tết | FAQ tĩnh (admin cập nhật) |
|  | Địa chỉ cửa hàng, bản đồ | FAQ tĩnh |
|  | Phí ship, thời gian giao, khu vực | FAQ tĩnh |
|  | Chính sách đổi trả, thời hạn, điều kiện | FAQ tĩnh + RAG |
|  | Phương thức thanh toán, COD, chuyển khoản | FAQ tĩnh |
|  | Câu hỏi khác không thuộc nhóm trên | RAG retrieval |

# 5. Handoff Tool

**escalate_to_human**
**Mô tả: **Chuyển cuộc hội thoại sang nhân viên hỗ trợ. Ghi lại lý do escalate để nhân viên nắm bắt ngay tình huống. Trong production: set Session.status = HANDOFF và Session.conversation_mode = HUMAN trong DB, ngăn bot tiếp tục reply cho session đó.

| Input | reason: string (Lý do handoff — BẮT BUỘC, có nghĩa và đầy đủ) |
| --- | --- |
| Output | { escalated: true, reason: string, session_status: "HANDOFF" } |
|  |  |
| Side effects | Session.status → HANDOFF. Session.conversation_mode → HUMAN. Bot ngừng auto-reply. Gửi context (lý do, mã đơn, SP, shipping info) đến nhân viên. |

**Trigger ví dụ**
*“**Tôi muốn khiếu nại**”*
*“**Hoàn tiền cho tôi**”*
*“**Cho tôi gặp quản lý**”*
*“**Sản phẩm bị lỗi**”*
*“**(Bot không hiểu > N lần)**”*
*“**(Tool lỗi liên tiếp)**”*
**Ví dụ hội thoại**
**KH: Tôi muốn hoàn tiền đơn hàng vừa rồi**
*[Orchestrator gọi escalate_to_human(reason="khách yêu cầu hoàn tiền đơn #7DE649BB")]*
**Bot: Mình đã ghi nhận và chuyển bạn sang nhân viên hỗ trợ.**
**Bot: Bạn sẽ được liên hệ trong 5 phút.**
*[Session.status = HANDOFF]*
*[Session.conversation_mode = HUMAN]*
*[Bot ngừng auto-reply cho session này]*

## 5.1 Trigger tự động

Ngoài việc khách hàng yêu cầu trực tiếp, escalate_to_human còn được gọi tự động trong các trường hợp:

| Tình huống | Hành động |
| --- | --- |
| Khiếu nại / hoàn tiền / hủy đơn | Escalate ngay lập tức với reason chính xác |
| Bot không hiểu > N lần | N cấu hình được (mặc định = 3). Escalate với reason “bot không hiểu sau N lần” |
| Tool lỗi liên tiếp | >2 lần cùng tool hoặc >3 tool bất kỳ. Escalate với reason “hệ thống lỗi” |
| Tình huống nhạy cảm | Khách tức giận, yêu cầu gặp quản lý, vấn đề pháp lý |

## 5.2 Context gửi cho nhân viên

Khi handoff, hệ thống phải gửi đủ thông tin để nhân viên không cần hỏi lại khách hàng:
**Lý do handoff: **Vì sao chuyển (khiếu nại, hoàn tiền, tool lỗi…)
**Mã đơn hàng: **Nếu có đơn liên quan
**Sản phẩm: **SP đang xem/đã mua
**Thông tin giao hàng: **Nếu đã thu thập trong checkout flow
**Lịch sử hội thoại: **Toàn bộ messages trong session
Database schema

# Định hướng kiến trúc dữ liệu GAPCon (E-commerce AI Chatbot)

Hiện tại hệ thống đang có 2 schema chính:
**public**** (GapOne)**:
 Chứa dữ liệu nghiệp vụ cốt lõi:
Khách hàng (contact) (lưu ý, khách hàng ở đây là người đặt hàng chứ không phải người nhận hàng)
Sản phẩm (product, product_variant)
Đơn hàng (deal, line_items)

**conversation**** (GAPCon)**:
 Chứa dữ liệu hội thoại:
Conversations: 1 cuộc nói chuyện với khách hàng trên 1 nền tảng nhất định
Sessions: 1 phiên hội thoại. Hiện tại, cơ chế đóng / mở đang làm thủ công do người
Messages: 1 tin nhắn từ người, AI agent hoặc human agent (GapCon user)

Hiện tại cần nối GapOne và GapCon với nhau để chung một khách hàng / contact, enforce 1-1 bởi 1 số điện thoại hoặc 1 email.
Các câu hỏi mẫu

Reminder Agent

# Reminder Agent

## 1.1 Vấn đề

Hiện tại, GAPCon AI Chatbot hoạt động theo mô hình session-based: khi khách hàng gửi tin, bot trả lời và orchestrate các tools. Hết session, bot tự refresh. Tuy nhiên không có cơ chế nào để:
**Nhắc nhở khách quay lại: **Khi khách đang giữa chừng mua hàng (có SP trong giỏ, đang checkout) nhưng không phản hồi, session chỉ im lặng chờ. Khách có thể quên hoàn toàn.
**Tự động đóng session: **Sessions không bao giờ được đóng tự động. Dẫn đến sessions zombie tiêu tốn tài nguyên và làm sai lệch metrics.
**Phục hồi doanh thu: **Giỏ hàng bị bỏ rơi (abandoned cart) là nguồn mất doanh thu lớn nhất trong conversational commerce.

## 1.2 Giải pháp: Reminder Agent

Xây dựng một worker độc lập chạy song song với chatbot chính, chịu trách nhiệm nhắc nhở và tự động đóng sessions:

| Giai đoạn | Trigger | Hành động |
| --- | --- | --- |
|  | KH gửi tin cuối cùng | Bot trả lời bình thường. Timer bắt đầu. |
|  | 48h không có reply từ KH | Gửi reminder context-aware (4 loại template). Set status = REMINDED. |
|  | 48h sau reminder, KH vẫn không reply | Gửi goodbye message. Auto-close session. Giữ lại giỏ hàng. |
|  | KH reply (dù đang REMINDED) | Reset về ACTIVE. Timer 48h bắt đầu lại. Tiếp tục bình thường. |

## 1.3 Mục tiêu

| Mục tiêu | Chi tiết |
| --- | --- |
| Phục hồi abandoned cart | Tăng % khách quay lại hoàn tất mua hàng sau reminder. Mục tiêu: >8% cart recovery. |
| Giảm sessions zombie | 100% sessions được đóng tự động sau 96h. Metrics chính xác hơn. |
| Cải thiện trải nghiệm | KH cảm nhận được quan tâm. Checkout gián đoạn được nhắc đúng chỗ. |
| Không làm phiền | Tối đa 1 reminder/session. |

# 2. Session Lifecycle

**ACTIVE**  ── [48h idle] ──>  **REMINDED**  ── [48h idle] ──>  **CLOSED**
*KH reply bất cứ lúc nào trong REMINDED → quay về ACTIVE, timer reset.*

# 3. Nội dung Reminder theo Context

Tin nhắn reminder PHỤ THUỘC vào trạng thái session. Reminder Agent capture context và chọn template:

## 3.1 Context A: Abandoned cart

**Trigger: **Session có DRAFT order với 1 hoặc nhiều order_item.
Chào bạn! Mình thấy bạn còn **{N} sản phẩm** trong giỏ hàng (tổng **{total}**). Bạn muốn tiếp tục đặt hàng không? Mình vẫn giữ giỏ cho bạn nhé!

## 3.2 Context B: Checkout bị gián đoạn

**Trigger: **order_step khác null và khác DONE (VD: NEED_PHONE, NEED_ADDRESS, CONFIRMING).
Chào bạn! Đơn hàng của bạn chỉ còn thiếu **{missing_field}**. Bạn gửi thông tin để mình hoàn tất nhé!

## 3.3 Context C: Browsing (xem SP, giỏ trống)

**Trigger: **last_products không trống nhưng giỏ hàng trống.
Chào bạn! Lần trước bạn đang xem **{product_name}**. Bạn có muốn mình tìm thêm hoặc thêm vào giỏ không?

## 3.4 Context D: General

**Trigger: **Giỏ hàng trống, không có last_products.
Chào bạn! Bạn có cần mình hỗ trợ thêm gì không? Mình luôn sẵn sàng tư vấn nhé!

## 3.5 Goodbye message (T+96h)

**Có giỏ hàng**
Mình tạm đóng cuộc trò chuyện nhé. Giỏ hàng của bạn (**{N} SP, {total}**) sẽ được giữ lại. Bất cứ lúc nào bạn muốn tiếp tục, cứ nhắn tin cho mình nhé!
**Không có giỏ hàng**
Mình tạm đóng cuộc trò chuyện nhé. Bất cứ lúc nào bạn cần, cứ nhắn tin cho mình. Hẹn gặp lại!

## 3.6 Giỏ hàng khi đóng session

**Quyết định: **GIỮ lại DRAFT order. Khi KH quay lại (session mới), bot thông báo: “Bạn còn giỏ hàng từ lần trước. Tiếp tục đặt hay chọn lại?” — Tăng khả năng phục hồi doanh thu.

# 4. Kiến trúc

## 4.1 Tổng quan

Reminder Agent và Chatbot Agent là 2 processes độc lập, giao tiếp qua Database:

| Chatbot Agent (hiện tại) | Reminder Agent (mới) |
| --- | --- |
| Xử lý tin nhắn đến từ khách (event-driven) | Gửi tin proactive, không có trigger từ khách |
| Orchestrate 12 tools, LLM reasoning | Chỉ gửi message + cập nhật session state. Không dùng LLM. |
| Khi KH reply sau reminder: reset status về ACTIVE | Khi auto-close: set CLOSED, gửi goodbye |

# 5. Ví dụ luồng hoàn chỉnh

## 5.1 KH quay lại sau reminder → mua hàng

*[Ngày 1, 14:00] KH thêm 2 SP vào giỏ (850,000đ)*
**Bot: Đã thêm! Tổng: 850,000đ. Bạn muốn đặt hàng luôn?**
*[KH không reply. 48 giờ trôi qua...]*

*[Ngày 3, 14:00 — Reminder Agent quét]*
*[Detect: ACTIVE, 48h idle, DRAFT có 2 items, total=850k]*
*[Context: abandoned_cart → gửi template A]*
**Bot: Chào bạn! Bạn còn 2 SP trong giỏ (850,000đ). Tiếp tục đặt hàng không?**
*[Set reminder_sent=true, session_status=REMINDED]*

*[Ngày 3, 20:00 — KH reply]*
**KH: Ơ đúng rồi, đặt hàng luôn nhé**
*[Chatbot: reset reminder_sent=false, session_status=ACTIVE]*
*[Chatbot: start_order_flow() → checkout bình thường]*
**Bot: Tên người nhận là gì ạ?**

## 5.2 KH không quay lại → auto-close

*[Ngày 1, 10:00] KH hỏi shipping*
**Bot: Miễn phí đơn từ 500k. Giao 2–3 ngày nội thành.**
*[48h không reply...]*

*[Ngày 3, 10:00 — Reminder Agent]*
*[Detect: ACTIVE, 48h idle, giỏ trống, không có SP context]*
*[Context: general → gửi template D]*
**Bot: Bạn có cần mình hỗ trợ thêm không?**
*[Set reminder_sent=true, session_status=REMINDED]*

*[48h nữa không reply...]*

*[Ngày 5, 10:00 — Reminder Agent]*
*[Detect: REMINDED, 48h sau reminder, KH vẫn không reply]*
*[Auto-close]*
**Bot: Mình tạm đóng nhé. Hẹn gặp lại!**
*[Set session_status=CLOSED, closed_reason=auto_timeout]*

## 5.3 Checkout gián đoạn → nhắc nhở → tiếp tục

*[14:00] KH đang checkout: đã có tên + SĐT*
**Bot: Địa chỉ giao hàng đầy đủ là gì ạ?**
*[KH không reply. 48h...]*

*[Reminder Agent: detect order_step=NEED_ADDRESS]*
*[Context: checkout_interrupted → missing_field=địa chỉ giao hàng]*
**Bot: Đơn của bạn chỉ còn thiếu địa chỉ giao hàng. Gửi địa chỉ nhé!**

*[12h sau — KH reply]*
**KH: 123 Lê Lợi, Q1, HCM**
*[Reset reminder, tiếp tục state machine NEED_ADDRESS → CONFIRMING]*
**Bot: Xác nhận: Quần Jean x1, 450k | A | 0901234567 | 123 Lê Lợi. Đặt không?**

Đọc hình ảnh
**Upload Ảnh & Đánh giá Khả thi Kỹ thuật**

# 1. Mục tiêu

Liệt kê toàn bộ use case khi khách hàng upload ảnh lên chatbot e-commerce GAPCon, và đánh giá tính khả thi về mặt technical execution cho từng use case. Mục tiêu là xác định nhóm use case nên đưa vào MVP và nhóm để giai đoạn sau. 

## Nguyên tắc

**Tách perception khỏi action: **VLM “đọc” ảnh thành mô tả (description), rồi mới đưa vào pipeline Tool Calling hiện có.
**Xác nhận trước hành động: **Mọi field trích từ OCR (SĐT, địa chỉ, mã đơn) phải đọc lại cho khách xác nhận trước khi gọi tool.

# 2. Nhóm Pre-sale - Tìm kiếm & tư vấn

| Use case | Mô tả | Tool | Khả thi | Ghi chú |
| --- | --- | --- | --- | --- |
| Tìm sản phẩm giống ảnh (visual search) | Khách chụp ảnh SP thật / screenshot web hoặc đối thủ → “có cái này không?” | search_products | Cao | VLM mô tả ảnh thành query tiếng Việt -> đẩy vào semantic search đã có. |
| Tìm theo phong cách / cảm hứng | Gửi ảnh outfit, ảnh phòng → “tìm đồ giống set này” | search_products (nhiều lần) | Trung bình | VLM trích nhiều thuộc tính Khả thi nhưng kết quả phối đồ phụ thuộc độ phong phú của catalog |
| Hỏi chi tiết SP trong ảnh | Chụp 1 món → “còn size M không? giá bao nhiêu?” | search_products → get_product_detail | Cao | Nhận diện ảnh để định vị SP, nhưng giá/tồn kho LẤY TỪ TOOL. Rủi ro thấp nếu match đúng variant. |
| Gợi ý SP đi kèm / phối hợp | Gửi ảnh món đã có → “phụ kiện nào hợp?” | search_products | Trung bình | Cần tinh chỉnh để sinh query cho sản phẩm bổ trợ khả thi; chất lượng gợi ý phụ thuộc vào catalog. |

# 3. Nhóm Post-sale - Tra cứu & hỗ trợ

| Use case | Mô tả | Tool | Khả thi | Ghi chú kỹ thuật |
| --- | --- | --- | --- | --- |
| Chụp mã vận đơn / tem giao hàng | Chụp kiện hàng để tra trạng thái giao | OCR → get_order_status | Thấp | Phụ thuộc tích hợp đơn vị vận chuyển. Mã vận đơn không nằm trong hệ thống GapOne hiện tại. |
| Khiếu nại sản phẩm lỗi/hỏng | Chụp hàng rách/vỡ/giao sai + lời than | escalate_to_human (kèm ảnh) | Cao | VLM mô tả tình trạng -> human handoff có context + đính kèm ảnh cho nhân viên. Không cần phán đoán đúng/sai, chỉ chuyển tiếp. |

### 4. Kiến trúc tổng thể

Khách gửi ảnh lên hệ thống
        ↓
[1] Ingestion Layer - nén ảnh (VD: tối đa 1024px 1 cạnh)
        ↓
[2] VLM (GPT-4o-mini API) - "đọc" ảnh -> mô tả/field có cấu trúc
        ↓
[3] AI Orchestrator - nhận text mô tả 
        ↓
[5] Tool Calls (search_products, get_order_status, escalate_to_human...)
        ↓
[6] Trả lời khách

### 5. Các mô hình VLM sử dụng

### a) VLM qua API  - triển khai cho MVP

| Model | Đặc điểm | Phù hợp Gapcon |
| --- | --- | --- |
| GPT-4o-mini (OpenAI) | Vision + function calling, $0.15/$0.60 per 1M token | Lựa chọn mặc định cho MVP: rẻ, đủ tốt cho mô tả sản phẩm & OCR cơ bản |
| GPT-4o (OpenAI) | Mạnh hơn mini, $2.50/$10 | Khi cần độ chính xác cao hơn cho ảnh khó/OCR phức tạp |
| Gemini 2.5 Flash / Pro (Google) | Gemini 2.5 Pro nổi bật trong nhóm proprietary; Price Per Token Flash rẻ và nhanh | Mạnh về OCR/document; Flash là đối thủ trực tiếp của GPT-4o-mini về giá |
| Claude (Sonnet/Haiku) (Anthropic) | Thiên về hiểu và phân tích hơn là sinh ảnh, hợp tác vụ trích xuất OpenAI | Tốt cho mô tả sản phẩm chính xác, ít "bịa" |

### Ưu điểm: không cần GPU, tích hợp vài dòng code, chất lượng OCR tiếng Việt tốt.

### Nhược điểm: chi phí per-image, dữ liệu rời hệ thống.

### b) VLM open-source (tự host) - khi volume lớn / cần kiểm soát dữ liệu

| Model | Đặc điểm | Ghi chú |
| --- | --- | --- |
| Qwen3-VL / Qwen2.5-VL (Alibaba) | Qwen2.5-VL-72B dẫn đầu nhóm open-weight, ~70.2% MMMU và ~888 OCRBench | Lựa chọn số 1 open-source; có bản nhỏ 7B/32B chạy nhẹ hơn. Hỗ trợ 29 ngôn ngữ, mạnh OCR đa ngữ và trích xuất dữ liệu có cấu trúc |
| Gemma 3 (Google) | 4B–27B, đa ngôn ngữ, context 128k PE Collective | Nhẹ, dễ host, license Google |
| Llama 4 multimodal (Meta) | Tích hợp hiểu ảnh natively vào dòng Llama 4 Price Per Token | Hệ sinh thái lớn |

### Đề xuất Gapcon

**MVP: GPT-4o-mini** qua API - rẻ, nhanh, đủ tốt cho visual search + mô tả sản phẩm. 
**Khi scale / lo dữ liệu: chuyển sang Qwen2.5-VL tự host** - chất lượng OCR top open-source, chi phí thấp khi volume cao,

Đọc file
**Đọc & Xử lý File**

File ở đây gồm tài liệu có cấu trúc (PDF, Word, Excel/CSV)

### 2 cách LLM đọc file

**Cách 1: LLM đọc trực tiếp (native file input):** Nhiều LLM/VLM hiện nhận thẳng file PDF hoặc ảnh làm input, tự "nhìn" và hiểu cả text lẫn layout, nên không cần thư viện trích xuất riêng.
**Cách 2: Trích text bằng thư viện trước, rồi đưa text vào LLM** pdfplumber/python-docx/pandas lấy text ra -> đưa chuỗi text vào LLM để hiểu ý định.

### Tại sao Cách 1 phù hợp hơn

**1. Đơn giản hóa kiến trúc
** Cách 2 cần một router rẽ nhánh theo từng loại file (PDF text → pdfplumber, PDF scan → OCR, Word → python-docx, Excel → pandas) cộng thư viện riêng và xử lý lỗi cho mỗi nhánh. Cách 1 gộp tất cả về một đường: file vào thẳng LLM. 
**2. Xử lý được file scan và ảnh chụp tài liệu
** Đây là điểm quyết định với bối cảnh Việt Nam. Khách thường **chụp ảnh** hóa đơn, đơn cũ, danh sách viết tay thay vì gửi file số. Cách 2 với file scan buộc phải thêm OCR - vốn yếu với tiếng Việt có dấu. Cách 1 để LLM/VLM "nhìn" trực tiếp, xử lý cả ảnh lẫn PDF số trong cùng một luồng.
**3. Hiểu được layout phức tạp
** Hóa đơn, báo giá, brochure có bảng và bố cục rối. Khi pdfplumber trích text thô, cấu trúc bảng thường vỡ (cột lẫn vào nhau). LLM đọc trực tiếp giữ được ngữ cảnh không gian - biết số nào thuộc dòng nào, cột nào.
**4. Một pipeline cho mọi định dạng
** Thay vì bảo trì nhiều nhánh trích xuất, chỉ cần một interface gọi LLM. Dễ phát triển, dễ test, dễ mở rộng khi có loại file mới.

### Kiến trúc tổng thể

Khách gửi file (PDF/Word/Excel/CSV)

[1] Trích xuất → text/bảng có cấu trúc
        ↓
[2] AI Orchestrator - nhận nội dung như input bình thường
        ↓
[3] Tool Calls (search_products, add_to_cart, get_order_status, escalate_to_human)
        ↓
[4] Đọc lại cho khách xác nhận
**Upload Ảnh & Đánh giá Khả thi Kỹ thuật**

# **1\. Mục tiêu** 

Liệt kê toàn bộ use case khi khách hàng upload ảnh lên chatbot e-commerce GAPCon, và đánh giá tính khả thi về mặt technical execution cho từng use case. Mục tiêu là xác định nhóm use case nên đưa vào MVP và nhóm để giai đoạn sau. 

## **Nguyên tắc**

* **Tách perception khỏi action:** VLM “đọc” ảnh thành mô tả (description), rồi mới đưa vào pipeline Tool Calling hiện có.

* **Xác nhận trước hành động:** Mọi field trích từ OCR (SĐT, địa chỉ, mã đơn) phải đọc lại cho khách xác nhận trước khi gọi tool.

# **2\. Nhóm Pre-sale \- Tìm kiếm & tư vấn**

| Use case | Mô tả | Tool | Khả thi | Ghi chú |
| ----- | ----- | ----- | :---: | ----- |
| Tìm sản phẩm giống ảnh (visual search) | Khách chụp ảnh SP thật / screenshot web hoặc đối thủ → “có cái này không?” | search\_products | **Cao** | VLM mô tả ảnh thành query tiếng Việt \-\> đẩy vào semantic search đã có. |
| Tìm theo phong cách / cảm hứng | Gửi ảnh outfit, ảnh phòng → “tìm đồ giống set này” | search\_products (nhiều lần) | **Trung bình** | VLM trích nhiều thuộc tính Khả thi nhưng kết quả phối đồ phụ thuộc độ phong phú của catalog |
| Hỏi chi tiết SP trong ảnh | Chụp 1 món → “còn size M không? giá bao nhiêu?” | search\_products → get\_product\_detail | **Cao** | Nhận diện ảnh để định vị SP, nhưng giá/tồn kho LẤY TỪ TOOL. Rủi ro thấp nếu match đúng variant. |
| Gợi ý SP đi kèm / phối hợp | Gửi ảnh món đã có → “phụ kiện nào hợp?” | search\_products | **Trung bình** | Cần tinh chỉnh để sinh query cho sản phẩm bổ trợ khả thi; chất lượng gợi ý phụ thuộc vào catalog. |

# 

# **3\. Nhóm Post-sale \- Tra cứu & hỗ trợ**

| Use case | Mô tả | Tool | Khả thi | Ghi chú kỹ thuật |
| ----- | ----- | ----- | :---: | ----- |
| Chụp mã vận đơn / tem giao hàng | Chụp kiện hàng để tra trạng thái giao | OCR → get\_order\_status | **Thấp** | Phụ thuộc tích hợp đơn vị vận chuyển. Mã vận đơn không nằm trong hệ thống GapOne hiện tại. |
| Khiếu nại sản phẩm lỗi/hỏng | Chụp hàng rách/vỡ/giao sai \+ lời than | escalate\_to\_human (kèm ảnh) | **Cao** | VLM mô tả tình trạng \-\> human handoff có context \+ đính kèm ảnh cho nhân viên. Không cần phán đoán đúng/sai, chỉ chuyển tiếp. |

### **4\. Kiến trúc tổng thể**

Khách gửi ảnh lên hệ thống  
        ↓  
\[1\] Ingestion Layer \- nén ảnh (VD: tối đa 1024px 1 cạnh)  
        ↓  
\[2\] VLM (GPT-4o-mini API) \- "đọc" ảnh \-\> mô tả/field có cấu trúc  
        ↓  
\[3\] AI Orchestrator \- nhận text mô tả   
        ↓  
\[5\] Tool Calls (search\_products, get\_order\_status, escalate\_to\_human...)  
        ↓  
\[6\] Trả lời khách

### **5\. Các mô hình VLM sử dụng**

### **a) VLM qua API  \- triển khai cho MVP**

| Model | Đặc điểm | Phù hợp Gapcon |
| ----- | ----- | ----- |
| **GPT-4o-mini (OpenAI)** | Vision \+ function calling, $0.15/$0.60 per 1M token | Lựa chọn mặc định cho MVP: rẻ, đủ tốt cho mô tả sản phẩm & OCR cơ bản |
| **GPT-4o (OpenAI)** | Mạnh hơn mini, $2.50/$10 | Khi cần độ chính xác cao hơn cho ảnh khó/OCR phức tạp |
| **Gemini 2.5 Flash / Pro (Google)** | Gemini 2.5 Pro nổi bật trong nhóm proprietary; [Price Per Token](https://pricepertoken.com/pricing-page/model/openai-gpt-4.1) Flash rẻ và nhanh | Mạnh về OCR/document; Flash là đối thủ trực tiếp của GPT-4o-mini về giá |
| **Claude (Sonnet/Haiku) (Anthropic)** | Thiên về hiểu và phân tích hơn là sinh ảnh, hợp tác vụ trích xuất [OpenAI](https://openai.com/api/pricing/) | Tốt cho mô tả sản phẩm chính xác, ít "bịa" |

### **Ưu điểm**: không cần GPU, tích hợp vài dòng code, chất lượng OCR tiếng Việt tốt. 

### **Nhược điểm**: chi phí per-image, dữ liệu rời hệ thống.

### **b) VLM open-source (tự host) \- khi volume lớn / cần kiểm soát dữ liệu**

| Model | Đặc điểm | Ghi chú |
| ----- | ----- | ----- |
| **Qwen3-VL / Qwen2.5-VL (Alibaba)** | Qwen2.5-VL-72B dẫn đầu nhóm open-weight, \~70.2% MMMU và \~888 OCRBench | Lựa chọn số 1 open-source; có bản nhỏ 7B/32B chạy nhẹ hơn. Hỗ trợ 29 ngôn ngữ, mạnh OCR đa ngữ và trích xuất dữ liệu có cấu trúc |
| **Gemma 3 (Google)** | 4B–27B, đa ngôn ngữ, context 128k [PE Collective](https://pecollective.com/tools/gpt-4o-pricing/) | Nhẹ, dễ host, license Google |
| **Llama 4 multimodal (Meta)** | Tích hợp hiểu ảnh natively vào dòng Llama 4 [Price Per Token](https://pricepertoken.com/pricing-page/model/openai-gpt-4o) | Hệ sinh thái lớn |

### **Đề xuất Gapcon**

1. **MVP: GPT-4o-mini** qua API \- rẻ, nhanh, đủ tốt cho visual search \+ mô tả sản phẩm.   
2. **Khi scale / lo dữ liệu: chuyển sang Qwen2.5-VL tự host** \- chất lượng OCR top open-source, chi phí thấp khi volume cao,


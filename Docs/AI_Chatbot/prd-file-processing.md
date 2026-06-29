---
title: PRD AI Chatbot for e-commerce - File Processing Specification
version: 1.0.0
status: verified-by-ba
related_code: F:/Gapone Conversation/Docs/AI_Chatbot/prd-file-processing.md
last_updated: 2026-06-26
---

# Nhật ký thay đổi (Revision History)

| Phiên bản | Ngày | Người cập nhật | Vị trí thay đổi | Lý do chi tiết |
| :--- | :--- | :--- | :--- | :--- |
| 1.0.0 | 2026-06-26 | Mira-Miraaa | Toàn bộ tài liệu | Chuẩn hóa tài liệu từ tệp cũ |

---

**Đọc & Xử lý File**

File ở đây gồm tài liệu có cấu trúc (PDF, Word, Excel/CSV)

### **2 cách LLM đọc file**

**Cách 1: LLM đọc trực tiếp (native file input):** Nhiều LLM/VLM hiện nhận thẳng file PDF hoặc ảnh làm input, tự "nhìn" và hiểu cả text lẫn layout, nên không cần thư viện trích xuất riêng.

**Cách 2: Trích text bằng thư viện trước, rồi đưa text vào LLM** pdfplumber/python-docx/pandas lấy text ra \-\> đưa chuỗi text vào LLM để hiểu ý định.

### **Tại sao Cách 1 phù hợp hơn**

**1\. Đơn giản hóa kiến trúc**  
 Cách 2 cần một router rẽ nhánh theo từng loại file (PDF text → pdfplumber, PDF scan → OCR, Word → python-docx, Excel → pandas) cộng thư viện riêng và xử lý lỗi cho mỗi nhánh. Cách 1 gộp tất cả về một đường: file vào thẳng LLM. 

**2\. Xử lý được file scan và ảnh chụp tài liệu**  
 Đây là điểm quyết định với bối cảnh Việt Nam. Khách thường **chụp ảnh** hóa đơn, đơn cũ, danh sách viết tay thay vì gửi file số. Cách 2 với file scan buộc phải thêm OCR \- vốn yếu với tiếng Việt có dấu. Cách 1 để LLM/VLM "nhìn" trực tiếp, xử lý cả ảnh lẫn PDF số trong cùng một luồng.

**3\. Hiểu được layout phức tạp**  
 Hóa đơn, báo giá, brochure có bảng và bố cục rối. Khi pdfplumber trích text thô, cấu trúc bảng thường vỡ (cột lẫn vào nhau). LLM đọc trực tiếp giữ được ngữ cảnh không gian \- biết số nào thuộc dòng nào, cột nào.

**4\. Một pipeline cho mọi định dạng**  
 Thay vì bảo trì nhiều nhánh trích xuất, chỉ cần một interface gọi LLM. Dễ phát triển, dễ test, dễ mở rộng khi có loại file mới.

### **Kiến trúc tổng thể**

Khách gửi file (PDF/Word/Excel/CSV)

\[1\] Trích xuất → text/bảng có cấu trúc  
        ↓  
\[2\] AI Orchestrator \- nhận nội dung như input bình thường  
        ↓  
\[3\] Tool Calls (search\_products, add\_to\_cart, get\_order\_status, escalate\_to\_human)  
        ↓  
\[4\] Đọc lại cho khách xác nhận
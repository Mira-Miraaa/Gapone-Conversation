---
name: jira-story-writer-skill
description: Writes Jira story descriptions based on provided documents with 4 main sections: Objective, Business Requirements (Channels, Format, Features), Acceptance Criteria (Happy Path, Edge Cases, Out of Scope), and Anti-Hallucination Rules.
---

# SKILL: Jira Story Description Writer

> **Kích hoạt:** Skill này chạy khi người dùng yêu cầu viết story Jira **kèm theo file tài liệu**.

---

## Điều kiện kích hoạt

Skill được kích hoạt khi người dùng nói một trong các dạng sau (không nhất thiết phải giống từng chữ):

- "Viết story Jira cho [tên tính năng] từ file [tên file]"
- "Tạo mô tả story từ tài liệu này..."
- "Phân tích file và viết story Jira..."
- "Write Jira story based on [file]..."

> **Bắt buộc:** Phải có ít nhất 1 file tài liệu. Nếu không có file, AI hỏi: *"Bạn có thể cung cấp file tài liệu (PRD, SRS, BRD, spec...) để tôi viết story không?"*

---

## Quy tắc xử lý của AI

### Bước 1 — Đọc tài liệu

- Đọc **toàn bộ** file được cung cấp trước khi viết bất cứ điều gì.
- Nếu tài liệu tham chiếu file khác ("xem Appendix", "flow diagram đính kèm", v.v.) → Hỏi người dùng có muốn cung cấp không.

### Bước 2 — Đánh giá đủ thông tin

Nếu tài liệu **thiếu** một trong các yếu tố sau, AI hỏi người dùng trước khi tiếp tục:

| Thông tin thiếu                    | Cách hỏi                                                            |
| ------------------------------------ | --------------------------------------------------------------------- |
| Kênh/luồng nghiệp vụ không rõ  | "Tính năng này áp dụng cho kênh nào (Facebook, Zalo, Web...)?" |
| Actor chưa xác định              | "Ai là người dùng chính của tính năng này?"                  |
| Điều kiện thành công/thất bại | "Bạn có tài liệu mô tả flow lỗi hoặc edge case không?"       |
| Tài liệu quá tóm tắt            | "Bạn có bản SRS/spec chi tiết hơn không?"                       |

> Nếu người dùng không cung cấp thêm → đánh dấu điểm thiếu bằng **`⚠️ Cần làm rõ`** trong output.

### Bước 3 — Viết story theo template

Sử dụng template bên dưới. Giữ đủ 3 section chính, điều chỉnh số mục tùy độ phức tạp.

### Bước 4 — Tự review trước khi output

Chạy Quality Checklist ở cuối file này trước khi xuất kết quả.

---

## Output Template

 [Story ID nếu có] [Tên story: Động từ + đối tượng, ≤ 10 từ]

**Mục tiêu:**
[1–3 câu. Trả lời: Tại sao làm? Ai hưởng lợi? Kết quả mong muốn?]
Không đề cập chi tiết kỹ thuật ở đây.

**Yêu cầu nghiệp vụ:**

**Kênh / Luồng nghiệp vụ:**
- Kênh: [Chỉ liệt kê kênh có trong tài liệu]
- Luồng: [Mô tả bước theo thứ tự: Bước 1 → Bước 2 → ... → Kết quả]

**Định dạng / Tài liệu liên quan** *(bỏ qua nếu không áp dụng)*:
- Đầu vào: [Loại dữ liệu: JSON, file ảnh, text, form...]
- Đầu ra: [Kết quả trả về hoặc trạng thái thay đổi]
- Tham chiếu: [Tên file / link tài liệu nếu có]

**Tính năng chính:**
1. [Tính năng 1 — mô tả hành vi cụ thể]
2. [Tính năng 2]
3. [Tính năng N]
   ⚠️ Chỉ liệt kê tính năng có trong tài liệu hoặc được yêu cầu, KHÔNG thêm tính năng suy đoán.

⚠️ Cần làm rõ:
- [Điểm A còn mơ hồ trong tài liệu]
- [Điểm B chưa được đề cập]
(Xóa section này nếu không có điểm nào cần làm rõ)

**Acceptance Criteria:**

**Happy Path (Luồng thành công):**
- [ ] AC1: [Điều kiện cụ thể + kết quả đo lường được]
- [ ] AC2: [...]

**Edge Cases / Luồng ngoại lệ:**
- [ ] AC: [Khi [điều kiện ngoại lệ], hệ thống [làm gì]]
- [ ] AC: [...]

**Out of Scope** *(nếu cần tránh scope creep)*:
- [Thứ gì KHÔNG thuộc story này]

---

## Hướng dẫn chi tiết từng section

### Mục tiêu

- Mẫu câu: *"Để [đạt được gì], [actor] cần [làm gì]."*
- Tối đa 3 câu. Không dùng thuật ngữ kỹ thuật.
- Phải trả lời được: **"Tại sao story này tồn tại?"**

### Yêu cầu nghiệp vụ

- **Kênh**: Chỉ ghi kênh được đề cập trực tiếp trong tài liệu
- **Định dạng**: Chỉ điền khi story xử lý file, dữ liệu có cấu trúc, hoặc tích hợp API
- **Tính năng chính**: Viết theo thứ tự thực thi hoặc mức độ ưu tiên; dùng động từ hành động

### Acceptance Criteria

- Mỗi AC phải **testable** — có thể viết test case từ AC đó
- ❌ Tránh: *"Hệ thống hoạt động đúng"*
- ✅ Nên: *"Khi user upload ảnh JPG < 5MB, hệ thống phản hồi trong vòng 3 giây và hiển thị preview"*
- Số lượng AC hợp lý: **3–8 per story**. Nếu > 8 → cân nhắc split story và gợi ý cho người dùng.

---

## Anti-Hallucination Rules (BẮT BUỘC)

| ❌ KHÔNG làm                                                | ✅ PHẢI làm                                                |
| ------------------------------------------------------------- | ------------------------------------------------------------ |
| Tự thêm tính năng không có trong tài liệu             | Chỉ viết những gì có trong tài liệu                   |
| Bịa số liệu, SLA, tên API, tên hệ thống                | Dùng đúng số liệu từ tài liệu hoặc đánh dấu ⚠️ |
| Suy diễn chi tiết kỹ thuật không có căn cứ            | Ghi rõ "⚠️ Cần làm rõ" cho phần mơ hồ               |
| Copy nguyên tài liệu mà không diễn giải                | Tóm tắt ngắn gọn, cô đọng, đúng nghĩa              |
| Giả định kênh, actor, hoặc flow không được đề cập | Hỏi người dùng trước                                   |

---

## Quality Checklist (AI tự review trước khi output)

- [ ] Mỗi thông tin trong output đều có nguồn từ tài liệu được đọc?
- [ ] Không có số liệu, tên hệ thống, hoặc API nào được tự bịa?
- [ ] Mục tiêu trả lời được câu hỏi "Tại sao làm story này"?
- [ ] Tất cả kênh được liệt kê đều xuất hiện trong tài liệu?
- [ ] Mỗi AC có thể viết test case được không?
- [ ] Các phần còn mơ hồ đã được đánh dấu ⚠️?
- [ ] Story có scope hợp lý (nếu quá lớn → đề xuất split)?

---

## 📖 Ví dụ mẫu (Reference Output)

```
 US-001 Nhận và lưu trữ tin nhắn hình ảnh đa kênh

Mục tiêu

Hệ thống cần nhận và lưu trữ tin nhắn hình ảnh từ các kênh Facebook, Telegram, 
và Zalo để phục vụ tra cứu lịch sử hội thoại và xử lý tiếp theo bởi các module khác.

Yêu cầu nghiệp vụ

**Kênh / Luồng nghiệp vụ:**
- Kênh: Facebook Messenger, Telegram Bot, Zalo OA
- Luồng: User gửi ảnh → Webhook nhận event → Parse metadata → Lưu DB → Trả ACK

**Định dạng / Tài liệu liên quan:**
- Đầu vào: Webhook payload JSON từ từng platform
- Đầu ra: Bản ghi DB với URL ảnh + metadata (sender_id, timestamp, channel, message_id)
- Tham chiếu: SRS_Messenger_v1.2.pdf – Appendix A: Webhook Schema

**Tính năng chính:**
1. Parse webhook payload từ 3 kênh (Facebook, Telegram, Zalo)
2. Tải xuống hoặc lưu URL ảnh vào storage
3. Lưu metadata tin nhắn vào database
4. Trả acknowledgment HTTP 200 cho platform trong vòng 5 giây

⚠️ Cần làm rõ:
- Giới hạn kích thước file ảnh tối đa chưa được định nghĩa trong tài liệu

Acceptance Criteria

**Happy Path:**
- [ ] Khi nhận ảnh từ Facebook, hệ thống lưu URL ảnh và metadata vào DB thành công
- [ ] Khi nhận ảnh từ Telegram, hệ thống gọi API lấy file_path và lưu đúng cấu trúc
- [ ] Khi nhận ảnh từ Zalo, hệ thống parse đúng payload Zalo OA format
- [ ] Hệ thống trả HTTP 200 trong vòng 5 giây sau khi nhận webhook

**Edge Cases:**
- [ ] Khi payload thiếu trường bắt buộc, hệ thống log lỗi chi tiết và trả HTTP 400
- [ ] Khi URL ảnh không truy cập được, hệ thống retry tối đa 3 lần rồi đánh dấu trạng thái lỗi

**Out of Scope:**
- Phân tích nội dung ảnh (OCR, nhận diện đối tượng) thuộc story riêng
```

---

*Skill version: 1.0 | Created: 2026-05-12 | Ngôn ngữ: Tiếng Việt*

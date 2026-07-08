# Story: AI Tự Động Tóm Tắt Phiên Hội Thoại Sau Khi Đóng

---

## US-01 · Tự động tóm tắt nội dung phiên hội thoại khi đóng

**Mục tiêu:**
Để Agent/Admin nhanh chóng nắm bắt ngữ cảnh mà không cần đọc lại toàn bộ lịch sử, AI cần tự động tạo ra bản tóm tắt có cấu trúc ngay khi một phiên hội thoại được đóng. Bản tóm tắt này đồng thời là nguồn dữ liệu đầu vào cho tính năng AI Ghi nhớ lịch sử phiên (AI Memory).

---

**Yêu cầu nghiệp vụ:**

**Kênh / Luồng nghiệp vụ:**
- Kênh: Zalo OA, Facebook Messenger, Telegram, Website Livechat
- Đường dẫn cấu hình (Admin): `Cài đặt > Kênh > tab Cấu hình AI > sub-tab Tóm tắt hội thoại`
- Đường dẫn xem kết quả (Agent): `Trang chủ > Hội thoại > Chi tiết cuộc hội thoại` (Timeline & tab Lịch sử phiên)
- Luồng tự động:
  1. Agent đóng thủ công hoặc hệ thống auto-close session (timeout) → Session chuyển sang `Closed`
  2. Hệ thống đẩy job `summarize_session` (payload: `session_id`) vào Job Queue bất đồng bộ
  3. AI Summary Worker lấy toàn bộ tin nhắn của phiên và đọc cấu hình
  4. Kiểm tra điều kiện loại trừ: số tin nhắn `< N` (mặc định `N = 3`) hoặc chỉ có tin nhắn hệ thống → **bỏ qua**, không tạo tóm tắt
  5. Đủ điều kiện → gọi LLM API → nhận kết quả JSON (intent, resolution_status, summary, next_steps)
  6. Lưu vào bảng `conversation.session_summaries` → emit event `summary_created` → hiển thị trên Timeline

**Định dạng / Tài liệu liên quan:**
- Đầu vào: Lịch sử tin nhắn của phiên (`session_id`), cấu hình Admin (Provider, Model, Prompt)
- Đầu ra: Bản ghi `session_summaries` gồm `summary_content`, `intent_detected`, `resolution_status`, `model_used`, `input_tokens`, `output_tokens`, `cost_estimation`; Event Message trên Timeline
- Tham chiếu: `Docs/AI_Chatbot/srs-conversation-summary.md`, `Docs/AI_Chatbot/prd-conversation-memory.md`

**Tính năng chính:**
1. **Trigger tự động khi đóng phiên**: Lắng nghe sự kiện `session.status_changed` với `new_status = 'Closed'`; hoạt động với cả 2 trường hợp: Agent đóng thủ công và hệ thống auto-close (timeout)
2. **Điều kiện loại trừ**: Không gọi LLM nếu tổng tin nhắn của phiên `< N` (có thể cấu hình, mặc định `3`) hoặc phiên chỉ gồm tin hệ thống không có tin thực tế từ khách
3. **Gọi LLM với Structured Output (JSON Mode)**: Gửi system prompt + lịch sử tin nhắn lên model đã cấu hình; yêu cầu trả về JSON 4 trường bắt buộc: `intent`, `resolution_status` (enum: `Order_Created` / `Escalated_to_Human` / `FAQ_Resolved` / `Abandoned` / `Other`), `summary` (≤ 150 từ), `next_steps`
4. **Event Message trên Timeline**: Sau khi lưu thành công, hệ thống chèn một tin nhắn sự kiện đặc biệt (background xanh nhạt, icon 🤖) vào timeline hiển thị đủ 4 phần tóm tắt — **chỉ hiển thị nội bộ, không gửi tới kênh của khách hàng**
5. **Tab Lịch sử phiên**: Tại bảng thông tin khách hàng (cột phải) thêm sub-tab `Lịch sử phiên`; mỗi phiên cũ hiển thị icon tóm tắt; hover/click → Popover/Modal hiển thị nội dung tóm tắt AI
6. **Retry tự động khi lỗi API**: Thực hiện Exponential backoff 3 lần (sau 5s → 15s → 45s); nếu vẫn thất bại → ghi log lỗi, hiển thị event *"Không thể tạo tóm tắt AI cho phiên này (Lỗi kết nối AI)"* trên Timeline, gửi thông báo cảnh báo đến Admin

---

**Acceptance Criteria:**

**Happy Path (Luồng thành công):**
- [ ] **AC-01**: Agent nhấn đóng session có ≥ 3 tin nhắn thực tế → sau tối đa 10 giây, Timeline chat xuất hiện Event Message chứa tóm tắt AI đầy đủ 4 phần (Ý định, Nội dung, Kết quả, Hành động tiếp theo)
- [ ] **AC-02**: Hệ thống auto-close session sau timeout → Job tóm tắt vẫn được kích hoạt và lưu thành công vào `session_summaries`
- [ ] **AC-03**: Tab Lịch sử phiên tại bảng thông tin khách hàng hiển thị icon tóm tắt; click vào → Popover/Modal hiển thị đúng nội dung tóm tắt AI của phiên đó
- [ ] **AC-04**: Kiểm tra DB bảng `conversation.session_summaries` — các trường `input_tokens`, `output_tokens`, `model_used`, `cost_estimation` đều có giá trị thực tế hợp lệ sau mỗi lượt tóm tắt
- [ ] **AC-05**: Nội dung tóm tắt **không** được gửi sang kênh của khách hàng (Zalo/FB/Telegram/Website)

**Edge Cases / Luồng ngoại lệ:**
- [ ] **AC-06**: Đóng session chỉ có 2 tin nhắn → hệ thống đóng session bình thường nhưng **không** gọi LLM và **không** tạo bản ghi trong `session_summaries`
- [ ] **AC-07**: Lỗi API (timeout/key không hợp lệ) → hệ thống thử lại 3 lần, sau đó ghi sự kiện lỗi trên Timeline và gửi cảnh báo đến Admin; hệ thống không bị treo hay crash
- [ ] **AC-08**: LLM trả về JSON sai schema → Worker tự động fallback parse text thô, bản tóm tắt vẫn hiển thị dưới dạng text thường

**Out of Scope:**
- Agent chỉnh sửa nội dung tóm tắt AI → V1 chỉ hỗ trợ read-only
- Tóm tắt đa ngôn ngữ (đầu ra linh hoạt) → xem xét ở Phase 2
- Phân tích Sentiment (Angry/Happy/Neutral) → Phase 2
- Tóm tắt các phiên đang `Open` hoặc `In Progress`

---

## US-02 · Cấu hình tính năng AI Tóm Tắt (Admin Dashboard)

**Mục tiêu:**
Để kiểm soát chất lượng, chi phí và hành vi của tính năng tóm tắt tự động, Admin cần có giao diện cấu hình tập trung cho phép bật/tắt tính năng, chọn model AI phù hợp và tùy chỉnh prompt theo đặc thù nghiệp vụ của doanh nghiệp.

---

**Yêu cầu nghiệp vụ:**

**Kênh / Luồng nghiệp vụ:**
- Kênh: Toàn bộ kênh tích hợp (cấu hình áp dụng đồng nhất)
- Đường dẫn: `Cài đặt > Kênh > tab Cấu hình AI > sub-tab Tóm tắt hội thoại`
- Luồng:
  1. Admin truy cập trang cấu hình → bật Toggle Switch
  2. Chọn Provider, nhập API Key → click **[Kiểm tra kết nối]** xác nhận kết nối thành công
  3. Chọn Model, đặt ngưỡng số tin nhắn tối thiểu, tùy chỉnh System Prompt (nếu cần)
  4. Click **[Lưu cấu hình]** → cấu hình có hiệu lực ngay với các session đóng tiếp theo

**Định dạng / Tài liệu liên quan:**
- Đầu vào: Toggle, Dropdown (Provider, Model), Input Password (API Key), Input Number (ngưỡng tin nhắn), Textarea (System Prompt)
- Đầu ra: Cấu hình được lưu, áp dụng ngay cho job tóm tắt kế tiếp
- Tham chiếu: `Docs/AI_Chatbot/srs-conversation-summary.md`

**Tính năng chính:**
1. **Toggle Bật/Tắt**: Nhãn `Bật tự động tóm tắt bằng AI`; khi Off, Worker bỏ qua toàn bộ job tóm tắt
2. **Cấu hình Provider & Model**: Dropdown chọn Provider (`OpenAI`, `Google Gemini`, `GAPIT AI Gateway`); Input Password nhập API Key (có icon ẩn/hiện); nút **[Kiểm tra kết nối]** xác nhận API Key hợp lệ; Dropdown chọn Model (VD: `gpt-4o-mini`, `gemini-2.5-flash` — mặc định gợi ý `gpt-4o-mini`)
3. **Ngưỡng số tin nhắn tối thiểu**: Input Number, mặc định `3`; session có số tin nhắn thấp hơn ngưỡng này sẽ không được tóm tắt
4. **Tùy chỉnh System Prompt**: Textarea hiển thị prompt mặc định của hệ thống; Admin có thể chỉnh sửa và nhấn **[Khôi phục mặc định]** nếu cần

---

**Acceptance Criteria:**

**Happy Path (Luồng thành công):**
- [ ] **AC-01**: Admin bật toggle, chọn Provider `OpenAI`, nhập API Key hợp lệ, nhấn **[Kiểm tra kết nối]** → hệ thống báo kết nối thành công
- [ ] **AC-02**: Admin chọn model `gpt-4o-mini`, đặt ngưỡng tin nhắn = `3`, nhấn **[Lưu cấu hình]** → session đóng sau đó áp dụng đúng model và ngưỡng đã cấu hình
- [ ] **AC-03**: Admin đổi model sang `gemini-2.5-flash` và lưu → session đóng tiếp theo lưu đúng `gemini-2.5-flash` vào trường `model_used` trong DB

**Edge Cases / Luồng ngoại lệ:**
- [ ] **AC-04**: Admin nhập API Key không hợp lệ và nhấn **[Kiểm tra kết nối]** → hệ thống hiển thị thông báo lỗi kết nối, không lưu API Key
- [ ] **AC-05**: Admin tắt Toggle → các session đóng sau đó không kích hoạt job tóm tắt, không tạo bản ghi trong `session_summaries`
- [ ] **AC-06**: Admin nhấn **[Hủy]** → giao diện trở về thiết lập đã lưu trước đó, không áp dụng thay đổi

**Out of Scope:**
- Cấu hình riêng theo từng kênh (Zalo/FB/Telegram) → áp dụng đồng nhất toàn hệ thống ở V1
- Xem lịch sử thay đổi cấu hình (Audit log) → xem xét ở phiên bản sau

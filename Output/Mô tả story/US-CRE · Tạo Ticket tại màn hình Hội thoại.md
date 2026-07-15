US-CRE Tạo Ticket tại màn hình Hội thoại

**Mục tiêu:**
Để nhanh chóng ghi nhận và theo dõi các yêu cầu phức tạp từ khách hàng ngay trong khi đang nhắn tin, nhân viên CSKH (Agent) cần có khả năng tạo nhanh Ticket trực tiếp từ màn hình Hội thoại mà không phải chuyển phân hệ hay nhập lại dữ liệu thủ công.

**Yêu cầu nghiệp vụ:**

**Kênh / Luồng nghiệp vụ:**
- Kênh: GapOne Conversation (Hội thoại)
- Luồng: Agent truy cập cuộc hội thoại → Click nút "Tạo Ticket" → Hệ thống kiểm tra điều kiện (BR-CRE-01) → Hiển thị Form tạo nhanh → Agent điền và submit form → Hệ thống tạo Ticket thành công, ghi log Timeline & cập nhật Sidebar.

**Định dạng / Tài liệu liên quan:**
- Đầu vào: Form tạo Ticket gồm Tiêu đề (bắt buộc), Mô tả (tùy chọn), Độ ưu tiên (bắt buộc), Người xử lý (tùy chọn), thông tin Khách hàng và Mã cuộc hội thoại (tự động điền).
- Đầu ra: Bản ghi Ticket trong Database ở trạng thái `Open`, Event message trên timeline chat, cập nhật danh sách ở sidebar.
- Tham chiếu: [SRS Create Ticket at Conversation v1.2.0](file:///home/mira/repositories/gitlab.com/Gapone-Conversation/Docs/SRS%20Create%20Ticket%20at%20Conversation.md)

**Tính năng chính:**
1. **Nút kích hoạt:** Tích hợp nút tạo Ticket tại 2 vị trí: Chat Toolbar (`btn-create-ticket-chat`) và Sidebar thông tin bên phải (`btn-create-ticket-sidebar`).
2. **Kiểm tra quyền tạo (BR-CRE-01):** Chỉ cho phép Agent tạo Ticket khi cuộc hội thoại ở trạng thái "In process" và đang được gán cho chính Agent đó. Admin không bị giới hạn bởi quy tắc này.
3. **Form tạo nhanh (`create-ticket-modal`):** Hiển thị Popup tự động pre-fill thông tin Khách hàng (dạng `[Tên] - [SĐT]`) và mã cuộc hội thoại. Cho phép nhập Tiêu đề, Mô tả, chọn Độ ưu tiên và chọn Người xử lý.
4. **Validation tiêu đề:** Bắt buộc nhập tiêu đề (tối đa 255 ký tự). Nếu không hợp lệ, disabled nút "Xác nhận", hiển thị nhãn lỗi màu đỏ bên dưới.
5. **Logic xử lý submit:** Tạo bản ghi với trạng thái mặc định `Open`, `creator_id` lấy từ session token (INT), `ticket_id` tự động sinh qua DB AUTO_INCREMENT (xử lý tuần tự theo thứ tự request khi có hành động tạo đồng thời). Gửi thông báo in-app `ASSIGNMENT` nếu có gán Agent xử lý.
6. **Ghi log Timeline chat:** Tự động chèn System Event Message chứa hyperlink mã Ticket dạng màu xanh (`var(--primary-color)`) trên Timeline. Click vào link gọi hàm `openDetailTicketPopup(ticketId)`.
7. **Sidebar Ticket liên quan:** Accordion hiển thị tối đa 5 Ticket gần nhất của khách hàng đang chat. Click vào dòng bất kỳ để mở popup chi tiết; click nút "Xem tất cả" để chuyển sang màn hình quản lý Ticket và tự động lọc danh sách theo khách hàng đó.

**Acceptance Criteria:**

**Happy Path (Luồng thành công):**
- [ ] AC-01: Khi Agent hoặc Admin click nút "Tạo Ticket", hệ thống hiển thị đúng form tạo Ticket với thông tin tên + SĐT khách hàng và mã hội thoại được điền sẵn.
- [ ] AC-02: Khi nhấn nút "Xác nhận" với tiêu đề hợp lệ, hệ thống lưu Ticket với status `Open`, hiển thị Toast "Tạo Ticket #[ID] thành công!" và đóng Popup.
- [ ] AC-03: Khi Ticket được tạo thành công, một tin nhắn hệ thống ghi nhận sự kiện được chèn vào Timeline chat với hyperlink `#ID` màu xanh. Click vào hyperlink này sẽ mở popup xem chi tiết Ticket.
- [ ] AC-04: Khi Ticket được tạo thành công, Sidebar phải cập nhật ngay lập tức danh sách Ticket liên quan (hiển thị tối đa 5 ticket gần nhất theo thứ tự mới nhất lên đầu).
- [ ] AC-05: Khi click nút "Xem tất cả" dưới Sidebar, hệ thống chuyển hướng sang màn hình Quản lý Ticket, tự động điền tên khách hàng vào ô tìm kiếm và render danh sách tương ứng.
- [ ] AC-06: Khi Admin thực hiện click tạo Ticket ở bất kỳ hội thoại nào, hệ thống luôn cho phép mở form và tạo thành công (không bị chặn bởi BR-CRE-01).

**Edge Cases / Luồng ngoại lệ:**
- [ ] AC-07: Khi Agent không phải người phụ trách hoặc hội thoại không ở trạng thái "In process" click tạo Ticket, hệ thống chặn không mở form và hiển thị Toast báo lỗi BR-CRE-01.
- [ ] AC-08: Khi ô Tiêu đề bị để trống hoặc vượt quá 255 ký tự, nút "Xác nhận" bị disabled (opacity 0.5, cursor not-allowed) và hiển thị thông báo lỗi màu đỏ phía dưới.
- [ ] AC-09: Khi hai người cùng tạo Ticket đồng thời, DB xử lý tuần tự (AUTO_INCREMENT) để đảm bảo không trùng ID.

**Out of Scope:**
- Tạo Ticket từ màn hình Quản lý Ticket (thuộc story khác).
- Tự động tạo Ticket theo kịch bản Chatbot (thuộc tính năng Automation).
- Chỉnh sửa thông tin Ticket trực tiếp từ Popup (thuộc US-02/US-04).

# Story: Quản lý Danh sách Ticket

---

## US-01 · Xem, lọc và tìm kiếm danh sách Ticket

**Mục tiêu:**
Để Admin/Manager/Agent nhanh chóng theo dõi và phân tích tiến độ xử lý các yêu cầu của khách hàng, hệ thống cần cung cấp màn hình quản lý tập trung với dashboard chỉ số hiệu suất và bộ lọc đa dạng — thay thế việc ghi chú thủ công dẫn đến trôi thông tin và không đo được chất lượng dịch vụ.

---

**Yêu cầu nghiệp vụ:**

**Kênh / Luồng nghiệp vụ:**
- Kênh: Nội bộ hệ thống GapOne Conversation
- Đường dẫn: `Đăng nhập > Menu chính > Ticket`
- Luồng:
  1. User truy cập màn hình Ticket → hệ thống hiển thị Dashboard + bảng danh sách mặc định lọc `Active` (tất cả trừ `Closed`)
  2. User áp dụng bộ lọc (trạng thái / độ ưu tiên / người phụ trách) hoặc nhập từ khóa tìm kiếm → bảng tự động render lại kết quả (`oninput`)
  3. Không có kết quả → bảng hiển thị thông báo *"Không tìm thấy Ticket nào phù hợp."*

**Định dạng / Tài liệu liên quan:**
- Đầu vào: Text search (LIKE theo Mã, Tiêu đề, Tên/SĐT khách hàng), Dropdown bộ lọc
- Đầu ra: Dashboard 3 thẻ thống kê + bảng dữ liệu Ticket đã lọc
- Tham chiếu: `Docs/SRS Ticket Management.md`

**Tính năng chính:**
1. **Dashboard chỉ số hiệu suất**: 3 thẻ thống kê — Tổng số Ticket; Đang xử lý (trạng thái `Open` hoặc `In_Progress`, màu vàng cam); Tỷ lệ Giải quyết RT (%) = $\frac{N_{\text{Resolved}} + N_{\text{Closed}}}{N_{\text{Total}}} \times 100\%$ (màu xanh lá)
2. **Thanh tìm kiếm**: Tìm gần đúng (LIKE) theo Mã Ticket, Tiêu đề, Tên khách hàng, Số điện thoại; trigger tự động re-render bảng khi nhập (`oninput`)
3. **Bộ lọc trạng thái**: Dropdown gồm `Active` *(mặc định)*, `All`, `Open`, `In_Progress`, `Resolved`, `Closed`
4. **Bộ lọc độ ưu tiên**: Dropdown gồm `All`, `Low`, `Medium`, `High`, `Urgent`
5. **Bộ lọc người phụ trách**: Dropdown gồm `All`, `Unassigned`, và danh sách Agent tải động
6. **Bảng dữ liệu Ticket**: Các cột — Mã Ticket (link mở popup chi tiết), Tiêu đề (rút gọn 50 ký tự + tooltip đầy đủ), Khách hàng (link chuyển sang phân hệ Hội thoại), Độ ưu tiên (badge màu), Trạng thái (badge màu), Người phụ trách, Ngày tạo (`hh:mm dd/mm/yyyy`)
7. **Phân quyền hiển thị**: Admin/Manager xem tất cả Ticket; Agent chỉ xem Ticket được phân công cho mình hoặc Team

---

**Acceptance Criteria:**

**Happy Path (Luồng thành công):**
- [ ] **AC-01**: User truy cập màn hình Ticket → Dashboard hiển thị đúng 3 thẻ thống kê; bảng mặc định lọc `Active` (ẩn các Ticket `Closed`)
- [ ] **AC-02**: User nhập từ khóa vào ô tìm kiếm → bảng tự động lọc theo Mã Ticket, Tiêu đề, Tên hoặc SĐT khách hàng mà không cần nhấn nút
- [ ] **AC-03**: User chọn bộ lọc trạng thái `Resolved` → bảng chỉ hiển thị Ticket `Resolved`; tương tự với các bộ lọc độ ưu tiên và người phụ trách
- [ ] **AC-04**: Click tên khách hàng trong bảng → hệ thống tự động chuyển sang phân hệ Hội thoại và mở đúng cuộc chat của khách hàng đó
- [ ] **AC-05**: Agent đăng nhập → chỉ thấy Ticket được phân công cho mình/Team; không thấy Ticket của Agent khác

**Edge Cases / Luồng ngoại lệ:**
- [ ] **AC-06**: Không có Ticket nào thỏa mãn điều kiện lọc → bảng hiển thị thông báo *"Không tìm thấy Ticket nào phù hợp."* căn giữa, không hiển thị bảng rỗng

**Out of Scope:**
- Phân trang (pagination) → sẽ xem xét khi số lượng Ticket lớn
- Xuất danh sách Ticket ra file (Excel/CSV) → story báo cáo riêng
- Sắp xếp cột (sort) trên bảng → xem xét ở phiên bản sau

---

## US-02 · Chỉnh sửa nhanh Ticket trực tiếp trên bảng (Inline Edit)

**Mục tiêu:**
Để Agent và Manager tiết kiệm thao tác, hệ thống cần cho phép cập nhật nhanh độ ưu tiên, trạng thái và người phụ trách của Ticket ngay trên dòng bảng mà không cần mở popup — đồng thời tự động gửi thông báo phân công và kích hoạt cảnh báo SLA khi cần thiết.

---

**Yêu cầu nghiệp vụ:**

**Kênh / Luồng nghiệp vụ:**
- Kênh: Nội bộ hệ thống GapOne Conversation
- Luồng thay đổi trạng thái sang `Resolved`:
  1. Chọn `Resolved` trong Dropdown trạng thái → hệ thống ghi nhận `resolved_date`
  2. Tính $T_{\text{xử lý}} = \frac{\text{resolved\_date} - \text{created\_date}}{3600 \times 1000}$ (giờ, làm tròn 1 chữ số thập phân)
  3. Nếu `Urgent` và $T_{\text{xử lý}} > 4\text{ giờ}$ → kích hoạt thông báo vi phạm SLA gửi Manager
  4. Toast: *"Ticket #[ID] đã giải quyết. Thời gian xử lý: [X] giờ"*
- Luồng thay đổi người phụ trách:
  1. Chọn Agent trong Dropdown → ghi nhận `assignee_id` → tự động gửi thông báo in-app đến Agent nhận việc
  2. Chọn `-- Chưa gán --` → `assignee_id = null` → Toast xác nhận gỡ phân công

**Định dạng / Tài liệu liên quan:**
- Đầu vào: Dropdown inline trên từng dòng bảng
- Đầu ra: Cập nhật DB ngay lập tức + Toast xác nhận + thông báo in-app (nếu có phân công)
- Tham chiếu: `Docs/SRS Ticket Management.md`

**Tính năng chính:**
1. **Thay đổi Độ ưu tiên**: Dropdown inline → cập nhật trường `priority` → Toast: *"Cập nhật độ ưu tiên Ticket #[ID] thành: [Mức mới]"*
2. **Thay đổi Trạng thái**: Dropdown inline → cập nhật `status`; khi chuyển sang `Resolved`: ghi nhận `resolved_date`, tính thời gian xử lý, kiểm tra vi phạm SLA; khi chuyển ngược từ `Resolved` về trạng thái trước: reset `resolved_date = NULL`
3. **Thay đổi Người phụ trách**: Dropdown inline → cập nhật `assignee_id`; tự động gửi thông báo in-app *"Bạn được phân công xử lý Ticket #[ID] - [Tiêu đề]"* đến Agent nhận việc; nếu Agent nhận là người đang đăng nhập → hiển thị Toast in-app; nếu khác → Toast chung *"Đã phân công cho [Tên Agent]"*
4. **Gỡ phân công**: Chọn `-- Chưa gán --` → `assignee_id = null` → Toast: *"Gỡ phân công Ticket #[ID]"*

---

**Acceptance Criteria:**

**Happy Path (Luồng thành công):**
- [ ] **AC-01**: Thay đổi độ ưu tiên qua Dropdown → badge màu cập nhật ngay trên dòng → Toast xác nhận hiển thị đúng mức mới
- [ ] **AC-02**: Chuyển trạng thái sang `Resolved` → `resolved_date` được ghi nhận → Toast hiển thị thời gian xử lý tính bằng giờ (làm tròn 1 chữ số thập phân)
- [ ] **AC-03**: Ticket `Urgent` chuyển sang `Resolved` sau > 4 giờ kể từ khi tạo → hệ thống kích hoạt thông báo vi phạm SLA gửi tới Manager
- [ ] **AC-04**: Gán Ticket cho Agent B → Agent B nhận thông báo in-app *"Bạn được phân công xử lý Ticket #[ID] - [Tiêu đề]"*
- [ ] **AC-05**: Chọn `-- Chưa gán --` → `assignee_id` về `null` → Toast *"Gỡ phân công Ticket #[ID]"* xuất hiện

**Edge Cases / Luồng ngoại lệ:**
- [ ] **AC-06**: Ticket đang `Resolved` được chuyển ngược về `In_Progress` → `resolved_date` reset về `NULL`, không còn tính thời gian xử lý trước đó
- [ ] **AC-07**: Agent đang đăng nhập tự gán Ticket cho chính mình → hiển thị Toast in-app cá nhân thay vì Toast chung

**Out of Scope:**
- Lịch sử thay đổi trạng thái/người phụ trách (Audit trail) → xem xét ở phiên bản sau
- Cấu hình ngưỡng SLA khác nhau theo từng loại Ticket → story cấu hình SLA riêng

---

## US-03 · Cảnh báo vi phạm SLA định kỳ cho Ticket Urgent

**Mục tiêu:**
Để Manager không bỏ sót các Ticket khẩn cấp bị trễ xử lý, hệ thống cần chủ động kiểm tra và gửi cảnh báo SLA tự động — đảm bảo mọi Ticket `Urgent` được theo dõi liên tục trong giới hạn 4 giờ.

---

**Yêu cầu nghiệp vụ:**

**Kênh / Luồng nghiệp vụ:**
- Kênh: Nội bộ hệ thống GapOne Conversation (tiến trình ngầm)
- Luồng:
  1. Hệ thống chạy `setInterval` kiểm tra mỗi **30 giây**
  2. Lọc Ticket có `priority = Urgent` và `status` **khác** `Resolved` / `Closed`
  3. Với mỗi Ticket thỏa mãn: tính $T_{\text{trôi qua}} = \frac{\text{Thời điểm hiện tại} - \text{created\_date}}{3600 \times 1000}$ (giờ)
  4. Nếu $T_{\text{trôi qua}} > 4\text{ giờ}$ và `slaAlertTriggered === false`:
     - Đánh dấu `slaAlertTriggered = true` (không gửi lặp lại)
     - Đẩy thông báo vào Bell Notification + hiển thị Toast khẩn cấp

**Định dạng / Tài liệu liên quan:**
- Đầu vào: Dữ liệu Ticket từ DB (không cần thao tác người dùng)
- Đầu ra: Thông báo in-app (Event Type: `SLA_ALERT`) với tiêu đề *"Cảnh báo SLA quá hạn"* và nội dung *"Ticket Urgent #[ID] - \"[Tiêu đề]\" quá hạn giải quyết (Thời gian: [X]h > 4h)"*; Toast khẩn cấp trên màn hình
- Tham chiếu: `Docs/SRS Ticket Management.md`

**Tính năng chính:**
1. **Tiến trình kiểm tra ngầm định kỳ**: `setInterval` chạy mỗi 30 giây; lọc đúng tập Ticket `Urgent` đang mở (`Open`, `In_Progress`)
2. **Cơ chế chống gửi lặp**: Cờ `slaAlertTriggered = true` đảm bảo mỗi Ticket chỉ gửi cảnh báo đúng 1 lần dù interval vẫn chạy
3. **Bell Notification + Toast khẩn cấp**: Thông báo đẩy vào danh sách Bell và hiển thị Toast popup trên màn hình ngay lập tức

---

**Acceptance Criteria:**

**Happy Path (Luồng thành công):**
- [ ] **AC-01**: Ticket `Urgent` ở trạng thái `Open` đã tồn tại > 4 giờ → hệ thống tự động gửi cảnh báo vào Bell Notification và hiển thị Toast khẩn cấp trong vòng tối đa 30 giây kể từ khi vượt ngưỡng
- [ ] **AC-02**: Nội dung thông báo đúng cú pháp: *"Ticket Urgent #[ID] - "[Tiêu đề]" quá hạn giải quyết (Thời gian: [X]h > 4h)"*

**Edge Cases / Luồng ngoại lệ:**
- [ ] **AC-03**: Cảnh báo chỉ được gửi **đúng 1 lần** per Ticket; các lượt kiểm tra tiếp theo của interval không gửi thêm cảnh báo cho cùng Ticket đó
- [ ] **AC-04**: Ticket `Urgent` đã chuyển sang `Resolved` hoặc `Closed` trước khi vượt 4 giờ → hệ thống không gửi cảnh báo
- [ ] **AC-05**: Ticket có `priority = High` (không phải `Urgent`) dù đã tồn tại > 4 giờ → hệ thống không gửi cảnh báo SLA

**Out of Scope:**
- Cấu hình ngưỡng thời gian SLA động theo từng mức ưu tiên → story cấu hình SLA riêng
- Gửi cảnh báo qua email/SMS ra bên ngoài → phụ thuộc module Notification

---

## US-04 · Xem chi tiết & Xóa Ticket

**Mục tiêu:**
Để Agent/Manager nắm đầy đủ thông tin một Ticket cụ thể (mô tả, nguồn hội thoại, trạng thái SLA động) và dọn dẹp các Ticket đã hoàn tất, hệ thống cần cung cấp Popup chi tiết với thông tin toàn diện và cơ chế xóa an toàn chỉ khi Ticket ở trạng thái `Closed`.

---

**Yêu cầu nghiệp vụ:**

**Kênh / Luồng nghiệp vụ:**
- Kênh: Nội bộ hệ thống GapOne Conversation
- Luồng xem chi tiết: Click liên kết `#ID` trên bảng → Popup `detail-ticket-modal` (rộng tối đa 550px) mở ra
- Luồng xóa: Ticket ở trạng thái `Closed` → nút **[Xóa Ticket]** (nền đỏ) hiển thị → click → Confirm dialog → xác nhận → xóa khỏi hệ thống

**Định dạng / Tài liệu liên quan:**
- Đầu vào: Click link `#ID` từ bảng danh sách
- Đầu ra: Modal hiển thị đầy đủ thông tin Ticket; Ticket bị xóa hoàn toàn sau xác nhận
- Tham chiếu: `Docs/SRS Ticket Management.md`

**Tính năng chính:**
1. **Popup chi tiết Ticket**: Hiển thị — Tiêu đề, Badge Độ ưu tiên + Badge Trạng thái (song song), Mô tả (giữ định dạng xuống dòng `white-space: pre-wrap`), Tên khách hàng, Mã cuộc hội thoại nguồn, Người phụ trách, Người tạo, Ngày tạo, Thời điểm giải quyết
2. **Hộp trạng thái SLA động**: Hiển thị màu thay đổi theo tình trạng:
   - Đã `Resolved`/`Closed`: nền xanh mờ — *"Đã giải quyết sau [X] giờ."*
   - `Urgent` đang xử lý, **trong** 4 giờ: nền cam mờ — *"Ưu tiên khẩn cấp (SLA 4h). Đã xử lý: [X] giờ."*
   - `Urgent` đang xử lý, **quá** 4 giờ: nền đỏ mờ — *"Quá hạn SLA 4 giờ! Đang xử lý: [X] giờ."*
   - Các mức ưu tiên khác: nền xám mờ — *"Thời gian trôi qua: [X] giờ."*
3. **Xóa Ticket (BR-DEL-01)**: Nút **[Xóa Ticket]** chỉ hiển thị khi `status = Closed`; ẩn hoàn toàn với các trạng thái khác; yêu cầu xác nhận *"Bạn có chắc muốn xóa Ticket #[ID]? Hành động này sẽ không thể hoàn tác."* trước khi xóa

---

**Acceptance Criteria:**

**Happy Path (Luồng thành công):**
- [ ] **AC-01**: Click `#ID` trên bảng → Popup mở hiển thị đầy đủ 4 phần thông tin: thông tin cơ bản, mô tả, hồ sơ nguồn, thông tin gán việc & mốc thời gian
- [ ] **AC-02**: Popup Ticket `Urgent` đang `In_Progress` chưa quá 4 giờ → hộp SLA nền cam, hiển thị đúng thời gian đã xử lý
- [ ] **AC-03**: Popup Ticket `Urgent` đang `In_Progress` đã quá 4 giờ → hộp SLA nền đỏ, nội dung *"Quá hạn SLA 4 giờ!"*
- [ ] **AC-04**: Popup Ticket `Closed` → nút **[Xóa Ticket]** hiển thị; click → Confirm dialog; xác nhận OK → Ticket bị xóa, Popup đóng, bảng không còn hiển thị Ticket đó

**Edge Cases / Luồng ngoại lệ:**
- [ ] **AC-05**: Popup Ticket có `status = Open`, `In_Progress`, hoặc `Resolved` → nút **[Xóa Ticket]** **không** xuất hiện
- [ ] **AC-06**: Confirm dialog xuất hiện → User chọn **Hủy** → Ticket không bị xóa, Popup vẫn mở

**Out of Scope:**
- Chỉnh sửa nội dung Ticket từ bên trong Popup (tiêu đề, mô tả) → V1 chỉ hỗ trợ xem
- Ghi chú nội bộ (Internal Note) trên Ticket → story riêng

# Story: Kết nối AI Chatbot với khách truy cập trên Website

---

## US-01 · Đăng ký tên miền & lấy mã nhúng SDK Chat Widget

**Mục tiêu:**
Để doanh nghiệp tiếp cận khách hàng ngay trên website của họ, Admin/Manager cần đăng ký tên miền vào hệ thống và nhận mã JavaScript SDK để nhúng vào website — từ đó kích hoạt AI Chatbot tự động chào hỏi khách truy cập và chuyển đổi lưu lượng web thành khách hàng tiềm năng.

---

**Yêu cầu nghiệp vụ:**

**Kênh / Luồng nghiệp vụ:**
- Kênh: Website (Web Livechat / Chat Widget SDK)
- Đường dẫn: `Đăng nhập > Cài đặt > Kênh (tab Kênh) > Accordion Website`
- Luồng:
  1. Admin click **[Kết nối]** → chọn icon **Website** → nhập tên miền → click **[Kết nối]**
  2. Hệ thống validate định dạng RFC 1035 & kiểm tra tính duy nhất
  3. Hợp lệ → tạo bản ghi `website_channels` + sinh `sdk_token` UUID → Accordion Website tự mở + popup mã nhúng SDK hiển thị
  4. Không hợp lệ / trùng lặp → Toast lỗi: *"Tên miền không hợp lệ hoặc đã được kết nối trước đó!"*

**Định dạng / Tài liệu liên quan:**
- Đầu vào: Text field — tên miền thuần, không giao thức, không đường dẫn con (VD: `app.gapone.vn`)
- Đầu ra: Bản ghi `website_channels` (`status = Active`, `sdk_token` UUID); đoạn mã script hiển thị trong textarea read-only
- Tham chiếu: `Docs/SRS Website Channel Connection.md`

**Tính năng chính:**
1. **Validate tên miền**: Chỉ chấp nhận domain hợp lệ theo RFC 1035; từ chối nếu có giao thức (`http://`, `https://`), đường dẫn con (`/path`), ký tự đặc biệt ngoài `-` và `.`, hoặc đã tồn tại trong hệ thống
2. **Bảng danh sách Website**: Cột STT, Website (hyperlink → mở lại popup SDK), Ngày kết nối (`dd/mm/yyyy hh:mm:ss`), nút hành động `⋮`
3. **Popup mã nhúng SDK**: Textarea read-only chứa đoạn script với `sdk_token` riêng; nút **[Sao chép mã]** → copy clipboard → Toast xanh: *"Đã sao chép mã nhúng SDK vào bộ nhớ tạm!"*
4. **Phân quyền**: Chỉ Admin/Manager thao tác được; Agent không có quyền truy cập trang cài đặt này

**Acceptance Criteria:**

**Happy Path (Luồng thành công):**
- [ ] **AC-01**: Admin nhập `myweb.com` → click [Kết nối] → hệ thống tạo bản ghi thành công, Accordion Website tự mở, bảng danh sách hiển thị domain vừa thêm, popup mã nhúng SDK tự động xuất hiện
- [ ] **AC-02**: `sdk_token` hiển thị trong đoạn script của popup phải khớp chính xác với token được sinh ra cho domain đó trong DB
- [ ] **AC-03**: Admin click tên miền trong bảng danh sách → popup mã nhúng SDK tương ứng mở lại đúng `sdk_token`
- [ ] **AC-04**: Admin click [Sao chép mã] → toàn bộ đoạn script được copy vào clipboard → Toast xanh xác nhận xuất hiện
- [ ] **AC-05**: Agent đăng nhập → không thấy màn hình Cài đặt > Kênh Website

**Edge Cases / Luồng ngoại lệ:**
- [ ] **AC-06**: Nhập `http://myweb.com` hoặc `myweb.com/index` → click [Kết nối] → Toast lỗi, không tạo bản ghi
- [ ] **AC-07**: Nhập domain đã tồn tại trong hệ thống → click [Kết nối] → Toast lỗi, không tạo bản ghi mới
- [ ] **AC-08**: Admin không thể trực tiếp chỉnh sửa nội dung trong textarea chứa mã nhúng

**Out of Scope:**
- Tái tạo (regenerate) `sdk_token` mới → xem xét trong phiên bản sau
- Cấu hình giao diện widget (màu sắc, logo) → story riêng

---

## US-02 · Ngắt kết nối Website & bảo mật CORS Whitelisting

**Mục tiêu:**
Để bảo vệ hệ thống khỏi lạm dụng và đảm bảo AI Chatbot chỉ hoạt động trên các website được ủy quyền, Admin/Manager cần có khả năng xóa tên miền không còn sử dụng — đồng thời hệ thống phải tự động chặn mọi kết nối từ domain chưa đăng ký hoặc đã bị xóa.

---

**Yêu cầu nghiệp vụ:**

**Kênh / Luồng nghiệp vụ:**
- Kênh: Website (Web Livechat / Chat Widget SDK)
- Luồng xóa: Bảng danh sách → click `⋮` → chọn **Xóa** → Modal xác nhận → Xác nhận → xóa bản ghi khỏi `website_channels` → chatbot trên domain đó ngừng hoạt động ngay
- Luồng CORS: Mỗi request đến AI Chatbot Gateway → kiểm tra `Origin` header với danh sách `website_channels` có `status = Active` → Hợp lệ: `200 OK` | Không hợp lệ: `403 Forbidden`

**Định dạng / Tài liệu liên quan:**
- Đầu vào (xóa): Thao tác click; xác nhận qua Modal — không nhập liệu
- Đầu vào (CORS): `Origin` header từ request trình duyệt khách
- Đầu ra: Bản ghi bị xóa; domain bị chặn ngay lập tức; server trả `403 Forbidden` với domain không hợp lệ
- Tham chiếu: `Docs/SRS Website Channel Connection.md`

**Tính năng chính:**
1. **Nút `⋮` (More options)**: Mỗi hàng trong bảng có nút này; click mở dropdown chỉ chứa **Xóa** (không có nút chỉnh sửa)
2. **Modal xác nhận**: Hiển thị trước khi xóa để tránh thao tác nhầm; Admin chọn Xác nhận hoặc Hủy
3. **CORS Domain Whitelist**: Gateway chỉ chấp nhận `Origin` khớp với domain `Active` trong DB; danh sách cập nhật ngay sau mỗi thao tác thêm/xóa
4. **Yêu cầu HTTPS bắt buộc**: Website tích hợp phải chạy HTTPS; request từ `http://` bị trình duyệt chặn do Mixed Content Policy

**Acceptance Criteria:**

**Happy Path (Luồng thành công):**
- [ ] **AC-01**: Admin click `⋮` → dropdown xuất hiện với duy nhất nút **Xóa** (không có nút chỉnh sửa)
- [ ] **AC-02**: Chọn Xóa → Modal xác nhận hiển thị tên domain sắp bị xóa
- [ ] **AC-03**: Xác nhận trong Modal → hàng bị xóa khỏi bảng; chatbot trên domain đó ngừng hoạt động ngay lập tức
- [ ] **AC-04**: Domain đã đăng ký và `Active` gửi request → Gateway trả `200 OK`, chat widget tải và kết nối thành công

**Edge Cases / Luồng ngoại lệ:**
- [ ] **AC-05**: Admin chọn Hủy trong Modal → Modal đóng, bảng danh sách không thay đổi
- [ ] **AC-06**: Domain chưa đăng ký (`hack.com`) gọi SDK → Gateway từ chối, trả `403 Forbidden`
- [ ] **AC-07**: Domain vừa bị xóa gửi request tiếp → Gateway từ chối ngay, trả `403 Forbidden`

**Out of Scope:**
- Vô hiệu hóa tạm thời (`Inactive`) mà không xóa hẳn → xem xét phiên bản sau
- Rate limiting / chống DDoS trên Gateway → thuộc phạm vi hạ tầng
- Lịch sử log thao tác xóa (Audit log) → story báo cáo kiểm toán riêng

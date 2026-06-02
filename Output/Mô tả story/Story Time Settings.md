# Story: Thiết lập thời gian chờ trên GapOne Conversation

---

## US-01 · Thiết lập thời gian chờ trên hệ thống GapOne Conversation

**Mục tiêu:**
Là PO, tôi muốn Admin có thể thiết lập và quản lý toàn bộ cấu hình thời gian trên hệ thống GapOne Conversation — bao gồm múi giờ, lịch làm việc, ngày nghỉ lễ và các quy tắc thời gian theo từng kênh/tài khoản — để hệ thống tự động nhận diện giờ làm việc, đóng hội thoại không hoạt động, đo SLA phản hồi và phân công lại hội thoại đúng thời điểm.

---

**Yêu cầu nghiệp vụ:**

**Kênh / Luồng nghiệp vụ:**
- Kênh: Toàn bộ kênh tích hợp trên GapOne Conversation (Zalo OA, Telegram, Facebook Messenger, Webchat, Email...)
- Luồng tổng quan:
  1. Admin đăng nhập → vào **Cài đặt** → chọn **Kênh** → chọn tab **Thời gian chờ**
  2. Trang **Thời gian chờ** có 2 sub-tab: **Cấu hình** và **Quy tắc**

**Luồng – Sub-tab Cấu hình:**
  1. Chọn **Quốc gia** → hệ thống tự động lọc danh sách **Múi giờ** tương ứng → chọn Múi giờ (VD: UTC+7)
  2. Thiết lập **Lịch làm việc tiêu chuẩn trong tuần**: bật/tắt từng ngày bằng Checkbox → nhập **Giờ mở cửa** và **Giờ đóng cửa** (HH:mm) cho từng ngày được chọn
  3. Cấu hình **Ngày nghỉ lễ**: nhấn [Thêm ngày +] → chọn ngày trên Calendar Picker → chọn kiểu lặp lại (Lặp lại hàng năm / Không lặp lại) → nhấn [Lưu] trong Date Picker
  4. Nhấn **[Lưu]** để lưu toàn bộ tab Cấu hình hoặc **[Hủy]** để quay về trạng thái trước

**Luồng – Sub-tab Quy tắc:**
  1. Nhấn **[Tạo mới +]** → một Card Quy tắc mới được khởi tạo
  2. **Cột trái – Phạm vi áp dụng**: chọn Kênh (VD: Zalo) → chọn Tài khoản thuộc kênh đó → nhấn [Kênh +] để thêm kênh khác nếu cần
  3. **Cột phải – Cấu hình thời gian**: nhập Thời gian đóng hội thoại (hh:mm:ss) + chọn Điều kiện đóng; nhập Thời gian yêu cầu phản hồi lần đầu; nhập Thời gian chờ phân công lại
  4. Nhấn **[Lưu]** để lưu quy tắc hoặc **[Hủy]** để bỏ qua thay đổi

**Định dạng / Tài liệu liên quan:**
- Đầu vào: Dropdown (Quốc gia, Múi giờ, Điều kiện đóng), Checkbox, Time Picker HH:mm (tab Cấu hình), Time Picker hh:mm:ss (tab Quy tắc), Calendar Picker, Radio button, Tag + Dropdown (Kênh, Tài khoản)
- Đầu ra: Cấu hình thời gian và quy tắc được lưu, áp dụng ngay cho hội thoại mới phát sinh
- Tham chiếu: `Docs/SRS Time Settings.docx`

**Tính năng chính:**

*Tab Cấu hình:*
1. **Chọn Quốc gia và Múi giờ**: Dropdown Múi giờ tự lọc theo Quốc gia; nếu quốc gia chỉ có một múi giờ (VD: Việt Nam → UTC+7), hệ thống tự động điền sẵn
2. **Lịch làm việc tiêu chuẩn trong tuần**: 7 hàng checkbox (Thứ 2 → Chủ nhật); khi check (màu cam) → Giờ mở cửa và Giờ đóng cửa được enable và bắt buộc nhập; khi uncheck → disabled, hiển thị `--:--`; nếu nhập giá trị vượt giới hạn (VD: 123 giây), hệ thống tự đặt về giá trị tối đa cho phép (59 giây); Giờ đóng cửa phải lớn hơn Giờ mở cửa
3. **Ngày nghỉ lễ**: Mở Calendar Picker chọn nhiều ngày; ngày đã lưu trước hiển thị màu xám nhạt (click lại để hủy chọn); chọn kiểu **Lặp lại hàng năm** (DD/MM) hoặc **Không lặp lại** (DD/MM/YYYY); bấm ra ngoài picker không lưu thay đổi; danh sách ngày hiển thị inline bên dưới nút [Thêm ngày +]
4. **Lưu / Hủy tab Cấu hình**: [Lưu] lưu toàn bộ; [Hủy] quay về rỗng (nếu chưa có data) hoặc phiên bản đã lưu trước (nếu đã có data)

*Tab Quy tắc:*
5. **Tạo nhiều quy tắc độc lập**: Mỗi nhấn [Tạo mới +] tạo một Card Quy tắc mới; nhiều card hiển thị danh sách dọc với thanh cuộn khi vượt màn hình
6. **Phạm vi áp dụng theo kênh và tài khoản**: Mỗi card chọn một hoặc nhiều cặp Kênh + Tài khoản; một tài khoản chỉ thuộc về một quy tắc — tài khoản đã được gán vào quy tắc khác hiển thị disabled trong danh sách chọn
7. **Thời gian đóng hội thoại + Điều kiện đóng**: nhập thời gian (hh:mm:ss, tối đa 99:59:59) kết hợp Dropdown điều kiện (chọn 1): *"So với thời điểm nhận tin nhắn cuối"* hoặc *"So với thời điểm gửi tin nhắn cuối"*
8. **SLA phản hồi lần đầu**: Giới hạn thời gian (hh:mm:ss) nhân viên phản hồi tin nhắn đầu tiên; nếu vượt, hệ thống ghi log phục vụ báo cáo
9. **Thời gian chờ phân công lại**: Sau thời gian này nếu nhân viên không tiếp nhận hội thoại được phân bổ, hệ thống tự động thu hồi và phân bổ cho nhân viên khác đang online
10. **Lưu / Hủy trên mỗi card**: [Lưu] màu cam – validate và lưu; [Hủy] màu xám – khôi phục trạng thái trước, không cần popup xác nhận

---

**Acceptance Criteria:**

**Happy Path (Luồng thành công):**
- [ ] **AC1 – Truy cập**: Admin đăng nhập, điều hướng `Cài đặt > Kênh > Thời gian chờ` thành công; thấy 2 sub-tab Cấu hình và Quy tắc. Agent không thể thấy hoặc truy cập trang này.
- [ ] **AC2 – Lọc Múi giờ theo Quốc gia**: Khi Admin chọn Quốc gia, Dropdown Múi giờ chỉ hiển thị múi giờ thuộc quốc gia đó; nếu duy nhất một múi giờ, hệ thống tự động điền sẵn.
- [ ] **AC3 – Lịch làm việc tuần**: Khi Admin check một ngày, Giờ mở cửa và Giờ đóng cửa được enable và bắt buộc nhập; khi uncheck, hai ô bị disabled và hiển thị `--:--`.
- [ ] **AC4 – Validation giờ làm việc**: Nếu nhập giá trị vượt giới hạn (VD: giây = 123), hệ thống tự đổi về giá trị tối đa (59); Giờ đóng cửa nhỏ hơn hoặc bằng Giờ mở cửa → báo lỗi, không cho Lưu.
- [ ] **AC5 – Lưu ngày nghỉ lễ lặp lại hàng năm**: Admin chọn ngày + "Lặp lại hàng năm" + nhấn [Lưu] trong picker → danh sách **Lặp lại:** hiển thị đúng định dạng `DD/MM`.
- [ ] **AC6 – Lưu ngày nghỉ lễ không lặp lại**: Admin chọn ngày + "Không lặp lại" + nhấn [Lưu] trong picker → danh sách **Trong năm:** hiển thị đúng định dạng `DD/MM/YYYY` hoặc khoảng `DD-DD/MM/YYYY`.
- [ ] **AC7 – Lưu tab Cấu hình thành công**: Khi Admin nhấn [Lưu], hệ thống hiển thị toast "Cập nhật thành công"; cấu hình có hiệu lực ngay với hội thoại mới (không hồi tố dữ liệu cũ).
- [ ] **AC8 – Tạo và lưu quy tắc thành công**: Admin tạo quy tắc với ít nhất một kênh/tài khoản và một trường thời gian hợp lệ → nhấn [Lưu] → toast "Lưu thành công"; quy tắc áp dụng ngay.
- [ ] **AC9 – Tự động đóng hội thoại theo quy tắc**: Sau đúng thời gian cấu hình kể từ khi điều kiện đóng được đáp ứng, hệ thống chuyển trạng thái hội thoại từ `Đang xử lý` sang `Đóng`.
- [ ] **AC10 – Nhận diện ngoài giờ làm việc**: Khi khách hàng gửi tin ngoài khung giờ hoặc vào ngày nghỉ lễ đã cấu hình, hệ thống gắn cờ "Ngoài giờ" để AI nhận diện và gọi tool phản hồi phù hợp.
- [ ] **AC11 – Phân công lại tự động**: Sau thời gian chờ phân công lại, nếu nhân viên không tiếp nhận, hệ thống thu hồi và phân bổ cho nhân viên khác đang online.

**Edge Cases / Luồng ngoại lệ:**
- [ ] **AC12 – Thoát Date Picker không lưu**: Admin mở Calendar Picker, chọn ngày rồi nhấp ra ngoài (không nhấn [Lưu] trong picker) → danh sách ngày nghỉ không thay đổi.
- [ ] **AC13 – Hủy tab Cấu hình**: Admin nhấn [Hủy] → nếu chưa có data: giao diện reset về rỗng; nếu đã có data: giao diện trở về phiên bản đã lưu trước đó.
- [ ] **AC14 – Validate lưu quy tắc thiếu kênh**: Admin nhấn [Lưu] mà chưa chọn kênh nào → báo lỗi "Vui lòng chọn ít nhất một kênh", không lưu.
- [ ] **AC15 – Validate lưu quy tắc trống thời gian**: Admin nhấn [Lưu] với tất cả trường thời gian để trống → báo lỗi "Vui lòng nhập ít nhất một giá trị thời gian", không lưu.
- [ ] **AC16 – Tài khoản đã dùng trong quy tắc khác**: Tài khoản đã gán vào quy tắc khác hiển thị disabled trong dropdown chọn tài khoản, không thể chọn lại.
- [ ] **AC17 – Hủy chỉnh sửa quy tắc**: Admin nhấn [Hủy] trên card → card khôi phục về trạng thái trước khi chỉnh sửa; không hiện popup xác nhận.
- [ ] **AC18 – Kênh không thuộc quy tắc nào**: Hội thoại từ tài khoản chưa được gán quy tắc ở chế độ mặc định, không áp dụng quy tắc thời gian.
- [ ] **AC19 – Thanh cuộn khi nhiều quy tắc**: Khi số lượng card Quy tắc vượt chiều cao màn hình, thanh cuộn dọc xuất hiện để Admin cuộn xem thêm.

**Out of Scope:**
- Cấu hình thời gian riêng cho từng nhân viên (Agent-level) → thuộc phạm vi quản lý nhân sự
- Lịch sử thay đổi cấu hình thời gian (Audit log) → sẽ xem xét trong phiên bản sau
- Đồng bộ lịch làm việc với hệ thống HRM/ERP bên ngoài
- Xóa quy tắc đã tạo → sẽ là story riêng nếu có yêu cầu
- Sắp xếp lại thứ tự ưu tiên giữa các quy tắc bằng kéo-thả

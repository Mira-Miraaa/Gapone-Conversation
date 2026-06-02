# 🔔 Danh sách User Stories — Tính năng Notification (Thông báo)

> **Nguồn tài liệu:** SRS Notification final.docx — V1.0
> **Ghi chú cập nhật:** 
> - Toast Notification đã có ticket riêng nên không gộp vào. 
> - 4 tính năng còn lại (Chuông, Email, Cài đặt, DND) được gộp thành 2 story lớn về Giao diện nhận thông báo và Cấu hình cài đặt.
> - Quyết định PO: DND = Quyền ưu tiên tuyệt đối (phục vụ nhân viên nghỉ phép), không có ngoại lệ. Có thông báo mất phân công cho Agent (EVT-02b).

---

### US-NTF-01 Hiển thị giao diện chuông thông báo và gửi Email

**Mục tiêu:**
Để không bỏ lỡ công việc, Agent/Admin cần thấy thông báo trên thanh điều hướng của app và nhận email báo cáo khi đang offline. Giúp nắm bắt và phản hồi kịp thời mọi sự kiện.

**Yêu cầu nghiệp vụ:**

**Kênh / Luồng nghiệp vụ:**
- Kênh: Web App (Thanh điều hướng) và Email.
- Luồng App: Sự kiện mới xảy ra → Hệ thống tăng số lượng trên chuông → Agent click chuông → Xem danh sách → Click vào thông báo → Điều hướng đến hội thoại và đánh dấu đã đọc.
- Luồng Email: Agent offline quá 15 phút → Có sự kiện quan trọng → Hệ thống chờ và gộp các sự kiện → Gửi 1 email tổng hợp duy nhất.

**Tính năng chính:**
1. Hiển thị số lượng thông báo chưa đọc trên biểu tượng chuông (tối đa hiển thị "99+").
2. Hiển thị danh sách tối đa 20 thông báo mới nhất khi click vào chuông, hỗ trợ tự động tải thêm (infinite scroll).
3. Chuyển trạng thái thành "đã đọc" và điều hướng khi click vào thông báo; cung cấp nút "Đánh dấu tất cả đã đọc".
4. Đồng bộ trạng thái đã đọc tức thì giữa các thiết bị đăng nhập cùng tài khoản.
5. Gửi 1 email tổng hợp các sự kiện bị lỡ khi người dùng offline (tắt app) quá 15 phút.
6. Gộp nhiều sự kiện diễn ra trong cùng 15 phút offline vào chung 1 email để tránh spam hộp thư.

**Acceptance Criteria:**

**Happy Path (Luồng thành công):**
- [ ] AC1: Khi có sự kiện mới, số trên chuông tăng 1 trong vòng 2 giây và thông báo hiển thị nền màu cam trong dropdown.
- [ ] AC2: Khi Agent click vào chuông, hệ thống hiển thị tối đa 20 thông báo mới nhất sắp xếp theo thời gian giảm dần.
- [ ] AC3: Khi Agent click vào một thông báo chưa đọc, thông báo chuyển sang nền trắng, số trên chuông giảm 1 và màn hình điều hướng đến hội thoại tương ứng.
- [ ] AC4: Khi Agent click "Đánh dấu tất cả đã đọc", số đếm trên chuông về 0 và toàn bộ thông báo chuyển nền trắng.
- [ ] AC5: Khi Agent offline quá 15 phút và có sự kiện mới, hệ thống gửi email tổng hợp thông báo trong vòng 30 giây kể từ khi đủ điều kiện.
- [ ] AC6: Khi Agent click link "Xem chi tiết" trong email, hệ thống mở màn hình hội thoại tương ứng trên Gapone Conversation.

**Edge Cases / Luồng ngoại lệ:**
- [ ] AC7: Khi số lượng thông báo chưa đọc lớn hơn 99, hệ thống hiển thị "99+" trên biểu tượng chuông.
- [ ] AC8: Khi có nhiều sự kiện (VD: 5 sự kiện) xảy ra trong cùng 15 phút offline, hệ thống gộp lại và chỉ gửi 1 email duy nhất.
- [ ] AC9: Khi hội thoại bị lấy lại từ Agent A để giao cho Agent B, Agent A nhận thông báo mất phân công (nền cam, số chuông tăng), đồng thời Agent B nhận thông báo được phân công mới.
- [ ] AC10: Khi Agent đã bật tính năng Email Digest (nhận email tổng hợp cuối ngày), hệ thống KHÔNG gửi các email thông báo tức thì nữa.
- [ ] AC11: Khi kết nối mạng (WebSocket) bị gián đoạn và khôi phục lại, hệ thống tự động tải các thông báo bị nhỡ và cập nhật số lượng trên chuông.

**Out of Scope:**
- Không hiển thị hay đếm các thông báo đã cũ hơn 30 ngày.

---

### US-NTF-02 Cài đặt thông báo cá nhân, Thời gian và chế độ Không làm phiền (DND)

**Mục tiêu:**
Để tự kiểm soát luồng thông báo, người dùng cần cấu hình chi tiết ma trận nhận thông báo, thời gian nhận và chế độ DND. Giúp cá nhân hóa trải nghiệm, không bị trôi việc và không bị quấy rầy khi nghỉ phép.

**Yêu cầu nghiệp vụ:**

**Kênh / Luồng nghiệp vụ:**
- Kênh: Web App (Profile > Cài đặt thông báo)
- Luồng: Người dùng truy cập cài đặt → Chọn thông số trong ma trận thông báo / cấu hình thời gian DND / Email Digest → Bấm Lưu → Hệ thống tự động chặn/mở/gửi thông báo theo đúng cấu hình.

**Tính năng chính:**
1. **Cài đặt ma trận nhận thông tin:** Bảng lưới cho phép bật/tắt nhận thông báo cho từng loại sự kiện (Tin nhắn, Phân công, SLA...) chéo với từng kênh (In-app App hoặc Email).
2. **Cài đặt thời gian chung:** Cho phép cài đặt mốc thời gian nhận Email tổng hợp trong ngày (Email Digest time - ví dụ: 08:00 sáng).
3. **Cài đặt DND (Giữ nguyên luật tuyệt đối):**
   - Bật nhanh chế độ DND theo số giờ nhập vào (tối đa 7 ngày).
   - Cài đặt DND lặp lại tự động theo lịch trình (chọn giờ bắt đầu/kết thúc và ngày trong tuần).
4. Nút bật/tắt nhanh toàn bộ thông báo (Global Toggle).
5. Chặn tuyệt đối mọi Toast và Email gửi đi trong thời gian DND. Chuông hiển thị biểu tượng mặt trăng khuyết.

**Acceptance Criteria:**

**Happy Path (Luồng thành công):**
- [ ] AC1: Khi truy cập Profile > Cài đặt thông báo, hệ thống hiện **bảng ma trận** chọn kênh cho từng sự kiện. Mặc định bật hết trên App, tắt hết trên Email.
- [ ] AC2: Khi người dùng thiết lập **thời gian Email Digest** (vd: 08:00), hệ thống chỉ gửi 1 email tổng hợp vào đúng giờ này thay vì gửi tức thì.
- [ ] AC3: Khi thay đổi cài đặt ma trận hoặc thời gian và click Lưu, hệ thống hiển thị "Cập nhật thành công" và áp dụng luật cấu hình ngay lập tức. Cấu hình được đồng bộ ở mọi thiết bị.
- [ ] AC4: Khi bật DND nhanh 1 giờ, hệ thống lập tức chặn Toast/Email, sau đó tự động tắt DND khi hết đúng 60 phút để thông báo hoạt động lại.
- [ ] AC5: Khi thiết lập lịch DND (VD: 22:00 đến 08:00, từ Thứ 2-Thứ 6), hệ thống tự động bật DND đúng 22:00 và tự động tắt lúc 08:00 trong các ngày đã chọn.
- [ ] AC6: Khi DND đang trong giờ hoạt động, biểu tượng chuông trên thanh điều hướng thay đổi thành hình mặt trăng khuyết và hiển thị giờ kết thúc.

**Edge Cases / Luồng ngoại lệ:**
- [ ] AC7: Khi người dùng tắt nhận In-app cho sự kiện "Tin nhắn" trong ma trận, Toast popup sẽ không hiện khi có tin nhắn mới, nhưng số lượng trên biểu tượng chuông vẫn tăng.
- [ ] AC8: Khi người dùng tắt nút Global Toggle, hệ thống chặn hoàn toàn mọi Toast và Email gửi đi (chỉ lưu thông báo vào chuông).
- [ ] AC9: Khi DND đang bật và có cảnh báo khẩn cấp (SLA Alert), hệ thống VẪN CHẶN hoàn toàn Toast/Email. (Quyền DND là tuyệt đối để phục vụ nghỉ phép).
- [ ] AC10: Khi người dùng nhập số giờ bật nhanh DND quá thời hạn 7 ngày, hệ thống báo lỗi và không cho phép lưu.

**Out of Scope:**
- Không tồn tại quyền Admin nào (Critical Override) được phép vượt qua giới hạn của DND.

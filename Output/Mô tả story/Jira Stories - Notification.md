# User Stories – Tính năng Notification (Thông báo) trên Gapone Conversation

> **Epic:** EPIC-NOTI – Notification (Thông báo)
> **Tài liệu tham chiếu:** SRS Notification final v2.0
> **Product Owner:** PO – Gapone Conversation Team
> **Ngày:** 26/05/2026

---

## 📊 Bảng tổng hợp Stories

| Story ID | Tiêu đề | Priority | Story Points | Dependencies | Status |
|:---:|---|:---:|:---:|---|:---:|
| US-NOTI-01 | Hiển thị chuông thông báo & Badge số chưa đọc | Must Have | 3 | — | New |
| US-NOTI-02 | Xem danh sách thông báo (Dropdown & Notification Center) | Must Have | 5 | US-NOTI-01 | New |
| US-NOTI-03 | Hiển thị Toast popup khi có sự kiện mới | Must Have | 5 | US-NOTI-01 | New |
| US-NOTI-04 | Gửi Email thông báo khi người dùng offline | Should Have | 5 | US-NOTI-01 | New |
| US-NOTI-05 | Cài đặt thông báo cá nhân theo loại sự kiện & kênh | Must Have | 5 | US-NOTI-01 | New |
| US-NOTI-06 | Chế độ Không làm phiền (Do Not Disturb – DND) | Should Have | 5 | US-NOTI-05 | New |
| US-NOTI-07 | Email Digest – Email tổng hợp định kỳ | Could Have | 3 | US-NOTI-04 | New |
| US-NOTI-08 | Đồng bộ trạng thái đã đọc đa thiết bị | Must Have | 3 | US-NOTI-02 | New |
| US-NOTI-09 | Cài đặt nhạc chuông thông báo | Could Have | 2 | US-NOTI-05 | New |
| TECH-NOTI-01 | Xây dựng Notification Service & WebSocket real-time | Must Have | 8 | — | New |

```
📊 Tổng quan Backlog:
├── Tổng số Epics: 1 (EPIC-NOTI)
├── Tổng số User Stories: 9
├── Tổng số Technical Stories: 1
├── Tổng Story Points: 44
├── Phân bổ Priority:
│   ├── Must Have: 5 stories (24 points)
│   ├── Should Have: 2 stories (10 points)
│   ├── Could Have: 2 stories (5 points)
│   └── Won't Have: 0 stories
└── Dependencies: Không có vòng lặp phụ thuộc
```

---

## EPIC-NOTI – Notification (Thông báo) trên Gapone Conversation

**Mô tả Epic:**
Xây dựng hệ thống thông báo toàn diện cho nền tảng Gapone Conversation, giúp Agent và Admin cập nhật tức thì các sự kiện quan trọng (tin nhắn mới, phân công hội thoại, @mention, cảnh báo SLA, thay đổi hệ thống) thông qua In-app Bell, Toast popup và Email, từ đó tối ưu hóa thời gian phản hồi và nâng cao hiệu quả vận hành CSKH.

---

## US-NOTI-01 – Hiển thị chuông thông báo & Badge số chưa đọc

**Epic:** EPIC-NOTI – Notification
**Module:** Navigation Bar
**Priority:** Must Have
**Story Points:** 3

### Mô tả

> **As a** Nhân viên CSKH (Agent) hoặc Quản lý (Admin),
> **I want** thấy biểu tượng chuông thông báo với badge đỏ hiển thị số lượng thông báo chưa đọc trên thanh điều hướng,
> **So that** tôi biết ngay khi có sự kiện mới mà không cần phải chủ động kiểm tra từng màn hình.

### Mô tả chi tiết

Biểu tượng chuông (Bell Icon) được gắn cố định trên Navigation Bar và luôn hiển thị với tất cả người dùng đã đăng nhập. Khi có thông báo chưa đọc mới, badge đỏ hiện số lượng tương ứng. Đây là entry point chính của toàn bộ tính năng Notification.

### Yêu cầu nghiệp vụ

**Kênh / Luồng nghiệp vụ:**
- Kênh: Zalo OA, Facebook Fanpage, Web Livechat, Hệ thống nội bộ
- Luồng: Sự kiện xảy ra → Notification Service xử lý → Badge trên chuông cập nhật (+1) trong vòng 2 giây

**Tính năng chính:**
1. Hiển thị icon chuông cố định trên Navigation Bar với tất cả người dùng đã đăng nhập.
2. Badge đỏ xuất hiện với số lượng thông báo chưa đọc; tự động ẩn khi không còn thông báo chưa đọc.
3. Hiển thị **"99+"** khi số lượng chưa đọc vượt quá 99.
4. Badge cập nhật real-time (không cần reload trang) qua WebSocket.

### Acceptance Criteria

**Happy Path:**
- [ ] **AC1:** Given người dùng đã đăng nhập, When truy cập bất kỳ trang nào trong ứng dụng, Then icon chuông luôn hiển thị trên Navigation Bar.
- [ ] **AC2:** Given khách hàng gửi tin nhắn mới vào hội thoại được phân công cho Agent, When sự kiện được xử lý, Then badge trên chuông của Agent tăng lên 1 đơn vị **trong vòng 2 giây**.
- [ ] **AC3:** Given Agent đọc/đánh dấu đã đọc tất cả thông báo, When badge được cập nhật, Then badge biến mất hoàn toàn (không hiển thị số 0).

**Edge Cases:**
- [ ] **AC4:** Given số thông báo chưa đọc là 100, When badge hiển thị, Then badge hiển thị **"99+"** thay vì số thực.
- [ ] **AC5:** Given kết nối WebSocket bị đứt, When kết nối được khôi phục, Then badge cập nhật đúng số lượng thông báo bị nhỡ trong thời gian mất kết nối.

**Out of Scope:**
- Tùy chỉnh màu sắc hoặc vị trí icon chuông.
- Badge hiển thị trên tab browser (favicon badge).

### Business Rules
- Badge chỉ đếm thông báo trong vòng 30 ngày gần nhất.
- Badge không bao gồm thông báo đã quá 30 ngày dù chưa đọc.

### Dependencies
- TECH-NOTI-01: Notification Service & WebSocket phải được xây dựng trước.

### Technical Notes
- WebSocket / SSE để đẩy event real-time.
- API: `GET /api/notifications/unread-count` để lấy số badge khi load trang.

### Ghi chú từ SRS
- **Tham chiếu SRS:** Mục III.1 – In-app Notification – Chuông thông báo
- **Trích dẫn:** "Badge đỏ hiển thị số lượng thông báo chưa đọc. Nếu số lượng > 99, hiển thị '99+'. Badge tự động ẩn khi không còn thông báo chưa đọc."

---

## US-NOTI-02 – Xem danh sách thông báo (Dropdown & Notification Center)

**Epic:** EPIC-NOTI – Notification
**Module:** In-app Notification Dropdown & Full-page Notification Center
**Priority:** Must Have
**Story Points:** 5

### Mô tả

> **As a** Nhân viên CSKH (Agent),
> **I want** click vào chuông để xem danh sách thông báo với đầy đủ thông tin (icon, tiêu đề, tóm tắt, thời gian, trạng thái đọc),
> **So that** tôi có thể nhanh chóng xem và điều hướng đến sự kiện cần xử lý mà không bỏ lỡ.

### Mô tả chi tiết

Khi click vào chuông, một dropdown hiển thị tối đa 20 thông báo mới nhất. Thông báo chưa đọc có nền cam nhạt để dễ phân biệt. Người dùng có thể đánh dấu tất cả đã đọc hoặc click vào từng thông báo để điều hướng. Link "Xem tất cả" dẫn đến trang Notification Center đầy đủ.

### Yêu cầu nghiệp vụ

**Kênh / Luồng nghiệp vụ:**
- Luồng: Agent click chuông → Dropdown mở → Xem danh sách → Click thông báo → Điều hướng đến hội thoại → Thông báo chuyển trạng thái Đã đọc

**Định dạng / Tài liệu liên quan:**
- Đầu ra: Danh sách thông báo với trạng thái nền cam nhạt (chưa đọc) / nền trắng (đã đọc)
- Tham chiếu: SRS Notification final – Mục III.1

**Tính năng chính:**
1. Dropdown hiển thị tối đa 20 thông báo mới nhất; cuộn xuống tự động tải thêm (Infinite Scroll) trong 30 ngày.
2. Mỗi thông báo gồm: Icon sự kiện, [Module] Tiêu đề (in đậm), Nội dung tóm tắt, Thời gian tương đối (hover → tuyệt đối), Nền cam nhạt nếu chưa đọc.
3. Nút "Đánh dấu tất cả đã đọc" ở góc trên dropdown → badge về 0, tất cả chuyển nền trắng.
4. Click vào thông báo → đóng dropdown → điều hướng đến màn hình tương ứng → đánh dấu đã đọc → badge giảm 1.
5. Link "Xem tất cả" → mở trang Notification Center đầy đủ (lọc theo loại sự kiện, khoảng thời gian).

### Acceptance Criteria

**Happy Path:**
- [ ] **AC1:** Given Agent click vào icon chuông, When dropdown mở, Then hiển thị tối đa 20 thông báo mới nhất, sắp xếp theo thời gian giảm dần (mới nhất lên trên).
- [ ] **AC2:** Given có thông báo chưa đọc, When dropdown mở, Then thông báo chưa đọc hiển thị **nền cam nhạt**; thông báo đã đọc hiển thị **nền trắng**.
- [ ] **AC3:** Given Agent click "Đánh dấu tất cả đã đọc", When thao tác hoàn tất, Then badge về 0 và toàn bộ thông báo chuyển nền trắng.
- [ ] **AC4:** Given Agent click vào 1 thông báo, When điều hướng hoàn tất, Then thông báo đó chuyển nền trắng và badge giảm 1.
- [ ] **AC5:** Given Agent cuộn xuống cuối danh sách 20 thông báo, When trigger Infinite Scroll, Then hệ thống tải thêm thông báo cũ hơn (trong 30 ngày).

**Edge Cases:**
- [ ] **AC6:** Given thông báo không còn tài nguyên liên kết (hội thoại đã bị xóa), When Agent click vào thông báo đó, Then hệ thống vẫn đánh dấu đã đọc và hiển thị thông báo "Hội thoại không còn tồn tại".
- [ ] **AC7:** Given không có thông báo nào, When Agent click chuông, Then dropdown hiển thị trạng thái rỗng với message "Bạn chưa có thông báo nào".

**Out of Scope:**
- Xóa từng thông báo riêng lẻ (sẽ xem xét trong phiên bản sau).
- Ghim (pin) thông báo quan trọng.

### Business Rules
- Danh sách luôn sắp xếp theo thời gian giảm dần; không được đẩy thông báo chưa đọc lên trên thông báo đã đọc mới hơn.
- Thời gian hiển thị tương đối: < 1 phút → "Vừa xong"; < 1 giờ → "X phút trước"; < 24 giờ → "X giờ trước"; >= 1 ngày → "dd/mm/yyyy hh:mm" khi hover.

### Dependencies
- US-NOTI-01: Icon chuông & Badge phải hoàn thành trước.
- TECH-NOTI-01: Notification Service & WebSocket.

### Technical Notes
- API: `GET /api/notifications?page=1&limit=20` (pagination)
- API: `PATCH /api/notifications/mark-all-read`
- API: `PATCH /api/notifications/{id}/read`

### Ghi chú từ SRS
- **Tham chiếu SRS:** Mục III.1 – Bảng "Các thành phần hiển thị", "Cấu trúc một mục thông báo", "Hành động khi click"

---

## US-NOTI-03 – Hiển thị Toast popup khi có sự kiện mới

**Epic:** EPIC-NOTI – Notification
**Module:** Toast Notification (Overlay toàn ứng dụng)
**Priority:** Must Have
**Story Points:** 5

### Mô tả

> **As a** Nhân viên CSKH (Agent) đang làm việc trên ứng dụng,
> **I want** thấy popup Toast xuất hiện ở góc phải dưới màn hình ngay khi có sự kiện mới,
> **So that** tôi có thể phản hồi kịp thời mà không cần phải chủ động click vào chuông để kiểm tra.

### Mô tả chi tiết

Toast là popup nhỏ, không cản trở công việc, tự động ẩn sau 5 giây. Có thể click vào Toast để điều hướng trực tiếp hoặc click X để đóng sớm. Hệ thống xếp hàng tối đa 3 Toast cùng lúc để tránh spam màn hình.

### Yêu cầu nghiệp vụ

**Kênh / Luồng nghiệp vụ:**
- Luồng: Sự kiện xảy ra → Notification Service xử lý → WebSocket đẩy xuống client → Toast hiển thị góc phải dưới → Tự ẩn sau 5s hoặc Agent click điều hướng

**Tính năng chính:**
1. Toast xuất hiện ở **góc phải dưới màn hình** với nội dung: Icon sự kiện, Tiêu đề in đậm, Tóm tắt ≤ 2 dòng, Nút (X) đóng sớm.
2. Toast tự động ẩn sau **5 giây**.
3. Click vào Toast → đóng Toast → điều hướng đến hội thoại → đánh dấu thông báo đã đọc.
4. Tối đa **3 Toast cùng lúc**; Toast thứ 4 trở đi xếp hàng chờ.
5. Không hiển thị Toast khi DND đang bật.

### Acceptance Criteria

**Happy Path:**
- [ ] **AC1:** Given Agent đang online và DND tắt, When có sự kiện mới (EVT-01), Then Toast xuất hiện ở góc phải dưới **trong vòng 2 giây** với đúng nội dung.
- [ ] **AC2:** Given Toast đang hiển thị, When đủ 5 giây, Then Toast tự động ẩn.
- [ ] **AC3:** Given Toast đang hiển thị, When Agent click nút (X), Then Toast đóng ngay lập tức.
- [ ] **AC4:** Given Agent click vào nội dung Toast, When điều hướng hoàn tất, Then thông báo được đánh dấu đã đọc và badge giảm 1.

**Edge Cases:**
- [ ] **AC5:** Given DND đang bật, When có sự kiện mới, Then Toast **không xuất hiện**; badge vẫn tăng và thông báo lưu vào In-app Bell.
- [ ] **AC6:** Given 5 sự kiện đến đồng thời, When Toast được hiển thị, Then chỉ **3 Toast** xuất hiện cùng lúc; 2 Toast còn lại xếp hàng chờ.

**Out of Scope:**
- Toast khi ứng dụng không mở (cần Push Notification – xử lý story riêng).
- Tùy chỉnh vị trí Toast.

### Business Rules
- Toast không được che khuất các control quan trọng của giao diện (ưu tiên góc phải dưới, không chồng lên chat input).
- Thứ tự Toast xếp hàng: FIFO (First In First Out).

### Dependencies
- US-NOTI-01: Notification Service & WebSocket.
- TECH-NOTI-01.

### Technical Notes
- Implement Toast queue manager trên frontend.
- API không cần thiết riêng; dùng WebSocket event `notification.created`.

### Ghi chú từ SRS
- **Tham chiếu SRS:** Mục III.2 – Toast Notification

---

## US-NOTI-04 – Gửi Email thông báo khi người dùng offline

**Epic:** EPIC-NOTI – Notification
**Module:** Email Notification Service
**Priority:** Should Have
**Story Points:** 5

### Mô tả

> **As a** Nhân viên CSKH (Agent),
> **I want** nhận email thông báo khi tôi đang offline và có sự kiện quan trọng được gán cho tôi,
> **So that** tôi không bỏ lỡ tin nhắn khách hàng hay hội thoại được phân công dù không mở ứng dụng.

### Mô tả chi tiết

Sau 15 phút người dùng offline, hệ thống kiểm tra nếu có sự kiện chưa được xử lý thì gửi 1 email tổng hợp (không gửi nhiều email riêng lẻ). Email có link "Xem chi tiết" điều hướng thẳng vào ứng dụng.

### Yêu cầu nghiệp vụ

**Kênh / Luồng nghiệp vụ:**
- Kênh: Email (SMTP/SendGrid)
- Luồng: Người dùng offline > 15 phút → Sự kiện xảy ra (EVT-01/02/03/04) → Notification Service xếp hàng email → Sau 15 phút, gộp tất cả sự kiện → Gửi 1 email tổng hợp

**Tính năng chính:**
1. Trigger gửi email khi người dùng **offline > 15 phút** và có sự kiện EVT-01/02/03/04.
2. **Gộp nhiều sự kiện** trong 15 phút offline thành 1 email duy nhất (chống spam).
3. Email bao gồm: Tiêu đề rõ ràng, Danh sách sự kiện nhỡ, Link "Xem chi tiết" điều hướng đến ứng dụng.
4. Người dùng có thể bật/tắt Email cho từng loại sự kiện riêng biệt.

### Acceptance Criteria

**Happy Path:**
- [ ] **AC1:** Given Agent offline > 15 phút và có tin nhắn mới, When hệ thống kiểm tra, Then Agent nhận được email tổng hợp **trong vòng 30 giây**.
- [ ] **AC2:** Given có 5 sự kiện trong 15 phút offline, When email được gửi, Then Agent chỉ nhận **1 email gộp** (không phải 5 email riêng).
- [ ] **AC3:** Given email được gửi, When Agent click link "Xem chi tiết", Then Agent được điều hướng đến đúng hội thoại tương ứng (sau khi đăng nhập nếu chưa có session).

**Edge Cases:**
- [ ] **AC4:** Given Agent bật DND và offline, When có sự kiện mới, Then email **không được gửi** trong thời gian DND.
- [ ] **AC5:** Given Agent tắt Email notification cho EVT-01, When có tin nhắn mới, Then Agent **không nhận** email cho sự kiện này.
- [ ] **AC6:** Given Agent bật Email Digest, When có sự kiện nhỡ, Then hệ thống **không gửi email tức thì** (chỉ gửi vào giờ Digest đã cấu hình).

**Out of Scope:**
- Email template tùy chỉnh theo thương hiệu (cần thiết kế riêng).
- Tracking email mở/click.

### Business Rules
- Tỷ lệ delivery email phải đạt >= 99.5%.
- Email gửi tối đa 1 lần mỗi 15 phút/người dùng để tránh spam.
- Cần cấu hình SPF/DKIM/DMARC để tránh bị lọc spam.

### Dependencies
- US-NOTI-05: Cài đặt thông báo (người dùng phải bật Email notification mới gửi).
- TECH-NOTI-01: Notification Service.

### Technical Notes
- Email queue: SQS hoặc tương đương.
- Email provider: SMTP/SendGrid.
- API: `GET /api/users/{id}/online-status` để xác định offline.

### Ghi chú từ SRS
- **Tham chiếu SRS:** Mục III.3 – Email Notification

---

## US-NOTI-05 – Cài đặt thông báo cá nhân theo loại sự kiện & kênh

**Epic:** EPIC-NOTI – Notification
**Module:** Profile > Notification Settings
**Priority:** Must Have
**Story Points:** 5

### Mô tả

> **As a** Nhân viên CSKH (Agent),
> **I want** tùy chỉnh cách tôi nhận thông báo theo từng loại sự kiện (tin nhắn mới, phân công, @mention, SLA) và theo từng kênh (In-app, Push, Email) một cách độc lập,
> **So that** tôi chỉ nhận những thông báo thực sự quan trọng với công việc của mình, tránh bị overload thông tin.

### Mô tả chi tiết

Người dùng truy cập Profile > Cài đặt thông báo và thao tác trên bảng ma trận Event × Kênh (In-app / Push / Email). Cài đặt được lưu per-user, áp dụng ngay lập tức và duy trì qua mọi phiên đăng nhập.

### Yêu cầu nghiệp vụ

**Kênh / Luồng nghiệp vụ:**
- Đường dẫn: Profile → Cài đặt thông báo (Notification Settings)
- Luồng: Mở trang → Xem bảng ma trận → Check/uncheck → Click "Lưu" → Hệ thống lưu per-user → Áp dụng ngay

**Tính năng chính:**
1. **Global Toggle:** Bật/tắt toàn bộ thông báo (Toast, Push, Email) bằng 1 thao tác. In-app Bell vẫn ghi nhận khi tắt.
2. **Bảng ma trận Event × Kênh:** Check/uncheck độc lập cho từng tổ hợp (5 sự kiện × 3 kênh = 15 checkbox).
3. **Giá trị mặc định:** In-app = BẬT tất cả; Email & Push = TẮT tất cả.
4. **Lưu per-user:** Cài đặt duy trì qua đăng xuất/đăng nhập lại và trên mọi thiết bị.

### Acceptance Criteria

**Happy Path:**
- [ ] **AC1:** Given Agent vào Profile > Cài đặt thông báo, When trang tải, Then hiển thị bảng ma trận với 5 loại sự kiện × 3 kênh và đúng trạng thái đang áp dụng.
- [ ] **AC2:** Given Agent uncheck Email cho "Tin nhắn mới", When Agent đăng xuất và đăng nhập lại, Then cài đặt vẫn được giữ nguyên.
- [ ] **AC3:** Given Agent tắt Global Toggle, When có bất kỳ sự kiện nào, Then không có Toast, Push hoặc Email nào được gửi; nhưng In-app Bell vẫn cập nhật badge.

**Edge Cases:**
- [ ] **AC4:** Given Agent thay đổi cài đặt nhưng không click "Lưu", When Agent rời khỏi trang, Then hệ thống hỏi xác nhận "Bạn có muốn lưu thay đổi không?".
- [ ] **AC5:** Given cài đặt mới được lưu, When có sự kiện tiếp theo, Then hệ thống áp dụng cài đặt mới **ngay lập tức** (không cần reload).

**Out of Scope:**
- Cài đặt thông báo cấp hệ thống (Admin-level policy) – xem xét phiên bản sau.
- Export/Import cài đặt thông báo.

### Business Rules
- Khi Global Toggle = OFF: không gửi Toast, Push, Email nhưng In-app Bell vẫn hoạt động.
- Khi user bật Email Digest: tắt tự động Email tức thì cho cùng loại sự kiện.
- Phải có ít nhất 1 kênh BẬT để hệ thống không cảnh báo "Bạn đang tắt tất cả thông báo".

### Dependencies
- US-NOTI-01: Notification Bell (cần có trước để cài đặt có hiệu lực).
- TECH-NOTI-01.

### Technical Notes
- API: `GET /api/users/{id}/notification-preferences`
- API: `PUT /api/users/{id}/notification-preferences`
- Schema DB: Bảng `notification_preferences` (xem Data Model trong SRS).

### Ghi chú từ SRS
- **Tham chiếu SRS:** Mục III.4 – Cài đặt thông báo; Mục VIII – Data Model Bảng 3

---

## US-NOTI-06 – Chế độ Không làm phiền (Do Not Disturb – DND)

**Epic:** EPIC-NOTI – Notification
**Module:** Profile > Notification Settings > DND
**Priority:** Should Have
**Story Points:** 5

### Mô tả

> **As a** Nhân viên CSKH (Agent),
> **I want** bật chế độ Không làm phiền (DND) để tạm thời dừng nhận Toast, Push và Email thông báo trong khoảng thời gian nhất định hoặc theo lịch trình tự động,
> **So that** tôi có thể tập trung làm việc hoặc nghỉ ngơi mà không bị gián đoạn, nhưng vẫn có thể xem lại thông báo nhỡ sau đó qua In-app Bell.

### Mô tả chi tiết

DND có 2 mode: Quick DND (bật ngay với thời hạn cố định) và Scheduled DND (tự động bật/tắt theo khung giờ và ngày trong tuần). Khi DND active, icon trăng lưỡi liềm hiển thị cạnh chuông để báo hiệu trạng thái.

### Yêu cầu nghiệp vụ

**Kênh / Luồng nghiệp vụ:**
- Đường dẫn: Profile → Cài đặt thông báo → Chế độ DND
- Luồng Quick DND: Chọn "1 giờ" → Toggle bật → Icon trăng hiển thị → Sau 1 giờ tự động tắt
- Luồng Scheduled DND: Cấu hình lịch → Đến giờ hệ thống tự bật → Hết giờ tự tắt

**Tính năng chính:**
1. **Quick DND:** Bật ngay với 3 tùy chọn: **1 giờ / 8 giờ / Cho đến khi tắt thủ công**.
2. **Scheduled DND:** Thiết lập giờ bắt đầu, giờ kết thúc (HH:mm), lặp lại theo ngày trong tuần (checkbox Thứ 2 → CN).
3. **Icon DND:** Khi DND active, hiển thị icon trăng lưỡi liềm cạnh chuông kèm thời gian kết thúc.
4. **Quy tắc DND:** Không Toast, không Push, không Email; In-app Bell vẫn lưu thông báo.

### Acceptance Criteria

**Happy Path:**
- [ ] **AC1:** Given Agent chọn Quick DND "1 giờ", When bật, Then icon trăng xuất hiện cạnh chuông kèm thời gian kết thúc; Toast và Email không được gửi trong 1 giờ.
- [ ] **AC2:** Given DND "1 giờ" đang bật, When đủ 60 phút, Then DND tự động tắt; icon trăng biến mất; Toast và Email hoạt động trở lại.
- [ ] **AC3:** Given Agent cài Scheduled DND 22:00–08:00 từ T2–T6, When đến 22:00 thứ Hai, Then hệ thống tự bật DND; icon trăng hiển thị.
- [ ] **AC4:** Given Scheduled DND đang active, When có sự kiện mới, Then thông báo được lưu vào In-app Bell; badge tăng; không có Toast/Push/Email.

**Edge Cases:**
- [ ] **AC5:** Given DND đang bật, When có hội thoại vi phạm SLA, Then **không có Toast hoặc Email** nào được gửi (DND ưu tiên tuyệt đối).
- [ ] **AC6:** Given Scheduled DND và Quick DND cùng được cấu hình, When cả 2 active, Then DND vẫn bật cho đến khi **cả 2 điều kiện đều kết thúc**.

**Out of Scope:**
- Critical Override DND do Admin thiết lập (⚠️ Cần xác nhận từ PO – xem R-03 trong SRS).
- DND theo nhóm người dùng.

### Business Rules
- Scheduled DND và Quick DND có thể hoạt động đồng thời (additive).
- DND không ngăn In-app Bell ghi nhận thông báo.

### Dependencies
- US-NOTI-05: Cài đặt thông báo phải hoàn thành trước.

### Technical Notes
- Cron job kiểm tra lịch DND mỗi phút.
- API: `PUT /api/users/{id}/notification-preferences` (cập nhật `dnd_enabled`, `dnd_until`, `dnd_schedule`).

### Ghi chú từ SRS
- **Tham chiếu SRS:** Mục III.5 – Chế độ DND; Mục IV.3 – Giao diện DND

---

## US-NOTI-07 – Email Digest – Email tổng hợp định kỳ

**Epic:** EPIC-NOTI – Notification
**Module:** Email Digest Service
**Priority:** Could Have
**Story Points:** 3

### Mô tả

> **As a** Nhân viên CSKH (Agent),
> **I want** nhận 1 email tổng hợp duy nhất mỗi ngày vào giờ tôi chọn thay vì nhiều email rải rác,
> **So that** tôi có thể review toàn bộ sự kiện nhỡ một lần mà không bị spam hộp thư.

### Yêu cầu nghiệp vụ

**Tính năng chính:**
1. Toggle bật Email Digest tại Profile > Cài đặt thông báo.
2. Chọn **giờ gửi Digest** cố định mỗi ngày (VD: 08:00 sáng).
3. Khi bật Digest: **tắt tự động Email tức thì** cho cùng loại sự kiện (mutual exclusion).
4. Email Digest bao gồm: Tổng số sự kiện nhỡ, Phân loại theo loại, Link "Xem chi tiết".

### Acceptance Criteria

**Happy Path:**
- [ ] **AC1:** Given Agent bật Email Digest với giờ gửi 08:00, When đến 08:00 hàng ngày, Then Agent nhận 1 email tổng hợp liệt kê tất cả sự kiện nhỡ trong ngày hôm trước.
- [ ] **AC2:** Given Email Digest đang bật, When có sự kiện nhỡ, Then hệ thống **không gửi email tức thì** cho Agent.

**Edge Cases:**
- [ ] **AC3:** Given Email Digest bật nhưng không có sự kiện nhỡ trong ngày, When đến giờ gửi, Then **không gửi email** (tránh email rỗng).

**Out of Scope:**
- Weekly Digest (tổng hợp theo tuần).

### Dependencies
- US-NOTI-04: Email Notification phải có trước.
- US-NOTI-05: Cài đặt thông báo.

### Ghi chú từ SRS
- **Tham chiếu SRS:** Mục III.6 – Email Digest

---

## US-NOTI-08 – Đồng bộ trạng thái đã đọc đa thiết bị

**Epic:** EPIC-NOTI – Notification
**Module:** Notification Service – Cross-device Sync
**Priority:** Must Have
**Story Points:** 3

### Mô tả

> **As a** Nhân viên CSKH (Agent) đăng nhập trên nhiều thiết bị (web và mobile),
> **I want** khi tôi đọc thông báo trên thiết bị này thì thiết bị kia cũng tự động cập nhật trạng thái đã đọc,
> **So that** tôi không phải đánh dấu đã đọc nhiều lần trên từng thiết bị và không bị nhầm lẫn bởi badge đỏ không chính xác.

### Yêu cầu nghiệp vụ

**Tính năng chính:**
1. Khi đánh dấu đọc trên thiết bị 1 (Web), badge và nền thông báo trên thiết bị 2 cập nhật **trong vòng 2 giây**.
2. Đồng bộ hoạt động qua WebSocket broadcast đến tất cả session của cùng user_id.
3. Khi click "Đánh dấu tất cả đã đọc", tất cả session đồng bộ badge về 0.

### Acceptance Criteria

**Happy Path:**
- [ ] **AC1:** Given Agent đăng nhập trên Web và Mobile, When click vào 1 thông báo trên Web, Then badge trên Mobile giảm 1 đơn vị **trong vòng 2 giây**.
- [ ] **AC2:** Given Agent click "Đánh dấu tất cả đã đọc" trên Web, When thao tác hoàn tất, Then badge trên Mobile cũng về 0 trong vòng 2 giây.

**Edge Cases:**
- [ ] **AC3:** Given Mobile đang offline khi Web đánh dấu đã đọc, When Mobile reconnect, Then badge được cập nhật đúng ngay sau khi kết nối lại.

### Dependencies
- US-NOTI-01, US-NOTI-02.
- TECH-NOTI-01: WebSocket broadcast.

### Technical Notes
- WebSocket broadcast: event `notification.read` gửi đến tất cả socket của cùng `user_id`.

### Ghi chú từ SRS
- **Tham chiếu SRS:** Mục VI – Business Rules – BR-01 Đồng bộ đa thiết bị

---

## US-NOTI-09 – Cài đặt nhạc chuông thông báo

**Epic:** EPIC-NOTI – Notification
**Module:** Profile > Notification Settings
**Priority:** Could Have
**Story Points:** 2

### Mô tả

> **As a** Nhân viên CSKH (Agent),
> **I want** chọn âm thanh thông báo từ danh sách có sẵn,
> **So that** tôi có thể phân biệt thông báo Gapone với các ứng dụng khác và cá nhân hóa trải nghiệm làm việc.

### Yêu cầu nghiệp vụ

**Tính năng chính:**
1. Dropdown chọn nhạc chuông từ danh sách âm thanh chuẩn của hệ thống (ít nhất 3 lựa chọn + "Im lặng").
2. Preview âm thanh khi hover/chọn.
3. Lưu lựa chọn per-user; áp dụng cho tất cả Toast và In-app thông báo.

### Acceptance Criteria

- [ ] **AC1:** Given Agent vào Cài đặt thông báo, When chọn nhạc chuông mới và click Lưu, Then âm thanh mới được phát khi có thông báo tiếp theo (khi DND tắt).
- [ ] **AC2:** Given Agent chọn "Im lặng", When có thông báo mới, Then Toast hiển thị nhưng không phát âm thanh.

### Dependencies
- US-NOTI-05: Cài đặt thông báo phải hoàn thành trước.

### Ghi chú từ SRS
- **Tham chiếu SRS:** Mục III.4 – Cài đặt thông báo – STT 2 "Nhạc chuông"

---

## TECH-NOTI-01 – Xây dựng Notification Service & WebSocket real-time

**Loại:** Technical Story / Enabler Story
**NFR Category:** Performance, Scalability, Reliability
**Priority:** Must Have
**Story Points:** 8

### Mô tả

Xây dựng backend Notification Service gồm: WebSocket/SSE cho real-time delivery, Message Broker (Kafka/RabbitMQ) để xử lý event không đồng bộ, schema DB cho bảng `notifications` và `notification_preferences`, và Cron Service cho Scheduled DND + Email Digest + cleanup 30 ngày.

### Acceptance Criteria

- [ ] **AC1:** WebSocket kết nối ổn định; event từ backend đến client trong vòng **2 giây** trong điều kiện tải bình thường.
- [ ] **AC2:** Notification Service chịu tải **10,000 thông báo/giây** khi benchmark (load test).
- [ ] **AC3:** Hệ thống hỗ trợ tối thiểu **10,000 WebSocket connections đồng thời** mà không degradation.
- [ ] **AC4:** Email delivery rate >= **99.5%** trong 7 ngày đầu production.
- [ ] **AC5:** Cron job cleanup chạy thành công mỗi ngày, xóa thông báo > 30 ngày.
- [ ] **AC6:** Toàn bộ request/response được log đầy đủ: User ID, Kênh, Loại sự kiện, Timestamp, Status (delivered/failed).

### Ảnh hưởng đến Stories
- US-NOTI-01, 02, 03, 04, 05, 06, 07, 08, 09 đều phụ thuộc vào Technical Story này.

### Technical Notes
- Schema DB: Bảng `notifications` + `notification_preferences` (xem Mục VIII SRS).
- Message Broker: Kafka (preferred) hoặc RabbitMQ.
- Email: SMTP/SendGrid; cần SPF/DKIM/DMARC.
- Cron: Scheduler service (Quartz/Bull/Celery tùy stack).

---

*Tài liệu được chuẩn bị theo yêu cầu của Product Owner – Gapone Conversation Team*
*Ngày: 26/05/2026 | Trạng thái: Ready for Sprint Planning*

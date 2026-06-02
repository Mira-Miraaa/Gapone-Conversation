
# SRS – CÀI ĐẶT THỜI GIAN HỆ THỐNG (TIME SETTINGS)



# BẢNG GHI NHẬN THAY ĐỔI TÀI LIỆU



| **Ngày thay đổi** | **Vị trí** | **Lý do** | **Mô tả thay đổi** | **Phiên bản cũ** | **Phiên bản mới** |
| --- | --- | --- | --- | --- | --- |
| 26/05/2026 | Tạo mới | Yêu cầu tính năng mới | Tài liệu đặc tả tính năng Cài đặt thời gian hệ thống | — | V1.0 |



# BẢNG QUẢN LÝ TIẾN ĐỘ THỰC THI



| **Giai đoạn** | **Thời gian** | **Phần mục** | **Phiên bản áp dụng** |
| --- | --- | --- | --- |
| Sprint 7 |  | Toàn bộ tài liệu | V1.0 |



# TÀI LIỆU THAM CHIẾU



| **STT** | **Tài liệu** |
| --- | --- |
| 1 |  |



## I. TỔNG QUAN & MỤC TIÊU



### 1.1. Hiện trạng


Hệ thống GapOne Conversation cần một cơ chế cấu hình thời gian tập trung để quản lý các quy tắc xử lý hội thoại tự động, thời gian làm việc của nhân viên và các SLA nội bộ. Hiện tại chưa có màn hình quản lý thống nhất cho các thiết lập này.


### 1.2. Mục tiêu tính năng


Xây dựng module **Cài đặt thời gian hệ thống** cho phép Admin thiết lập và quản lý toàn bộ các loại cấu hình thời gian trong hệ thống:

- Tự động đóng hoặc chuyển trạng thái hội thoại không có tương tác sau khoảng thời gian định sẵn.

- Định nghĩa khung giờ làm việc chính thức (Business Hours) và ngày nghỉ lễ.

- Cấu hình SLA phản hồi lần đầu, thời gian phân bổ lại và thời gian phiên làm việc.


### 1.3. Phạm vi áp dụng



| **Phạm vi** | **Chi tiết** |
| --- | --- |
| **Đường dẫn truy cập** | Đăng nhập > Cài đặt > Kênh > tab Thời gian chờ |
| **Đối tượng người dùng** | Admin / Quản lý (Manager): xem, cấu hình, chỉnh sửa và lưu |
| **Ngoài phạm vi** | Agent không có quyền xem hoặc cấu hình tính năng này trong phần Cài đặt |



## II. ĐỊNH NGHĨA ĐỐI TƯỢNG & PHÂN QUYỀN



### 2.1. Đối tượng người dùng



| **Vai trò** | **Quyền hạn** | **Ghi chú** |
| --- | --- | --- |
| **Admin / Quản lý (Manager)** | Xem, cấu hình, chỉnh sửa và lưu toàn bộ thiết lập thời gian của hệ thống | — |
| **Nhân viên (Agent)** | Không có quyền xem hoặc cấu hình | Bị ảnh hưởng trực tiếp bởi các thiết lập (thời gian làm việc, thời gian đóng hội thoại) |



### 2.2. Nhóm thiết lập thời gian



| **STT** | **Nhóm** | **Mô tả** |
| --- | --- | --- |
| 1 | **Cấu hình thời gian hệ thống** | Cấu hình múi giờ, khung giờ làm việc chính thức và ngày nghỉ lễ |
| 2 | **Quy tắc thời gian hội thoại theo kênh** | Thiết lập các quy tắc về thời gian: tự động đóng sau thời gian định sẵn, thời gian yêu cầu phản hồi lần đầu, thời gian tự động phân công lại. |



## III. PHÂN TÍCH CHI TIẾT TÍNH NĂNG



### 3.1. Thiết lập thời gian đóng cuộc hội thoại theo kênh



#### Mô tả chức năng:



| **Tên nghiệp vụ** | Thiết lập thời gian đóng cuộc hội thoại theo kênh |
| --- | --- |
| **Module** | Cài đặt > Kênh > tab Thời gian chờ |
| **Mô tả** | Hỗ trợ hệ thống tự động đóng hoặc chuyển trạng thái các cuộc hội thoại không có tương tác sau một khoảng thời gian nhất định, nhằm giải phóng hàng chờ, giữ giao diện gọn gàng và tối ưu hóa hiệu suất nhân viên. |
| **Điều kiện kích hoạt** | Toggle thiết lập được bật; hội thoại không có tương tác trong khoảng thời gian đã cấu hình |
| **Kết quả** | Hội thoại được tự động đóng hoặc gắn tag phân loại theo cấu hình |



#### Các tùy chọn cấu hình



| **STT** | **Cấu hình** | **Mô tả** | **Đơn vị** |
| --- | --- | --- | --- |
| 1 | **Phạm vi áp dụng** | Cho phép thiết lập quy tắc chung cho tất cả các kênh, hoặc tùy chỉnh riêng cho từng kênh (Zalo, Facebook, Webchat, Email...) | — |
| 2 | **Customer Inactivity Timeout** | Khoảng thời gian kể từ tin nhắn cuối cùng của nhân viên mà khách hàng không phản hồi | Phút / Giờ / Ngày |
| 3 | **Agent Inactivity Timeout** | Khoảng thời gian kể từ tin nhắn cuối cùng của khách hàng mà nhân viên chưa xử lý / phản hồi | Phút / Giờ / Ngày |



#### Hành động tự động khi hết thời gian



| **Hành động** | **Mô tả** |
| --- | --- |
| Tự động đóng hội thoại | Chuyển trạng thái hội thoại sang Closed |
| Đánh dấu / Gắn tag phân loại | Gắn tag “Hết thời gian chờ" |
| Gửi tin nhắn thông báo tự động (tùy chọn) | Auto-reply cho khách hàng trước khi đóng hội thoại |



### 3.2. Thiết lập thời gian hoạt động của nhân viên (Business Hours)



#### Mô tả chức năng



| **Tên nghiệp vụ** | Thiết lập thời gian hoạt động của nhân viên (Business Hours) |
| --- | --- |
| **Module** | Cài đặt > Kênh > tab Thời gian chờ |
| **Mô tả** | Cho phép định nghĩa khung thời gian làm việc chính thức của doanh nghiệp. Cấu hình này là cơ sở để hệ thống nhận diện khách hàng tương tác đang nằm "Trong giờ làm việc" hay "Ngoài giờ làm việc" và áp dụng luồng xử lý tương ứng. |
| **Kết quả** | Hệ thống tự động cờ hoá các hội thoại "Ngoài giờ" để kích hoạt Automation phù hợp (VD: gửi tin nhắn báo bận) |



#### Các tùy chọn cấu hình



| **STT** | **Cấu hình** | **Mô tả** |
| --- | --- | --- |
| 1 | **Múi giờ (Timezone)** | Lựa chọn múi giờ làm chuẩn áp dụng cho toàn hệ thống (VD: (GMT+07:00) Bangkok, Hanoi, Jakarta) |
| 2 | **Lịch làm việc trong tuần** | Chọn các ngày làm việc (Thứ 2 – Chủ Nhật); thiết lập khung giờ chi tiết cho từng ngày. |
| 3 | **Ngày nghỉ lễ, Tết (Holidays)** | Cấu hình danh sách ngày nghỉ đặc biệt trong năm; trong những ngày này hệ thống tự động coi là Out of office hours bất chấp lịch làm việc tiêu chuẩn |



### 3.3. Thiết lập các loại thời gian khác



#### Mô tả chức năng



| **Tên nghiệp vụ** | Thiết lập các loại thời gian SLA và phân bổ |
| --- | --- |
| **Module** | Cài đặt > Kênh > tab Thời gian chờ |
| **Mô tả** | Các thiết lập linh hoạt phục vụ nghiệp vụ SLA và phân bổ mở rộng của hệ thống. |



#### Các tùy chọn cấu hình



| **STT** | **Cấu hình** | **Mô tả** | **Ví dụ** |
| --- | --- | --- | --- |
| 1 | **First Response Time SLA** | Giới hạn thời gian tối đa để nhân viên phản hồi tin nhắn đầu tiên của khách hàng; dùng để cảnh báo quá hạn | 15 phút |
| 2 | **Re-assignment Timeout (Routing Timeout)** | Nếu sau X thời gian nhân viên không tiếp nhận hội thoại được phân bổ tự động, hệ thống thu hồi và phân bổ cho nhân viên khác đang online | — |



## IV. GIAO DIỆN NGƯỜI DÙNG (UI/UX)



### 4.1. Đường dẫn truy cập (Navigation Path)



| **Bước** | **Hành động** | **Mô tả** |
| --- | --- | --- |
| 1 | Đăng nhập hệ thống | Đăng nhập với tài khoản có vai trò Admin / Quản lý |
| 2 | Vào Cài đặt | Click vào menu **Cài đặt** trên thanh điều hướng chính |
| 3 | Chọn “Kênh” | Trong Cài đặt, chọn mục **Kênh** trên thanh tab ngang (breadcrumb: Home > Cài đặt > Kênh) |
| 4 | Chọn tab Thời gian chờ | Trên trang Kênh, chọn tab **Thời gian chờ** (tab thứ ba, sau "Kênh" và "Nhóm kênh") |



### 4.2. Cấu trúc tab trong trang "Thời gian chờ"


Trang **Thời gian chờ** có 2 sub-tab:


| **STT** | **Sub-tab** | **Nội dung chính** | **Tham chiếu mục** |
| --- | --- | --- | --- |
| 1 | **Cấu hình** (tab mặc định) | Quốc gia, Múi giờ, Lịch làm việc tiêu chuẩn trong tuần, Ngày nghỉ lễ | Mục 4.3 |
| 2 | **Quy tắc** | Tạo và quản lý các quy tắc thời gian theo từng kênh/tài khoản: thời gian đóng hội thoại, điều kiện đóng, SLA phản hồi lần đầu, thời gian chờ phân công lại | Mục 4.5 |


**Lưu ý:** Tab đang được chọn được đánh dấu màu cam (primary color) và có gạch chân. Các tab còn lại hiển thị màu xám.


### 4.3. Chi tiết giao diện tab "Cấu hình"


Tab **Cấu hình** là tab đầu tiên và mặc định khi người dùng truy cập vào trang Thời gian chờ.

Wireframe minh họa màn hình Admin lần đầu truy cập tab Cấu hình:

Wireframe minh họa Admin đang thiết lập các trường dữ liệu cấu hình thời gian:

Giao diện được chia thành 3 nhóm trường chính theo thứ tự từ trên xuống dưới:


#### 4.3.1. Nhóm trường: Múi giờ



| **STT** | **Tên trường** | **Loại UI** | **Bắt buộc** | **Placeholder / Giá trị mặc định** | **Mô tả** |
| --- | --- | --- | --- | --- | --- |
| 1 | **Quốc gia** | Dropdown | Bắt buộc | Chọn quốc gia | Chọn quốc gia để hệ thống gợi ý múi giờ phù hợp. Ví dụ: Việt Nam |
| 2 | **Múi giờ** | Dropdown | Bắt buộc | Chọn múi giờ | Chọn múi giờ làm chuẩn áp dụng cho toàn hệ thống. Ví dụ: UTC+7. Danh sách múi giờ được lọc theo Quốc gia đã chọn |


**Quy tắc:** Khi chọn Quốc gia, Dropdown Múi giờ tự động lọc và gợi ý các múi giờ tương ứng. Nếu quốc gia chỉ có một múi giờ (VD: Việt Nam → UTC+7), hệ thống có thể tự động điền sẵn.


#### 4.3.2. Nhóm trường: Lịch làm việc tiêu chuẩn trong tuần



| **STT** | **Tên trường** | **Loại UI** | **Bắt buộc** | **Giá trị mặc định** | **Mô tả** |
| --- | --- | --- | --- | --- | --- |
| 1 | **Ngày làm việc** (Checkbox) | Checkbox | Không | Unchecked | Checkbox để kích hoạt ngày làm việc. Gồm 7 hàng: Thứ 2, Thứ 3, Thứ 4, Thứ 5, Thứ 6, Thứ 7, Chủ nhật. Checkbox được check → màu cam (primary); unchecked → màu xám |
| 2 | **Giờ mở cửa** | Time Picker (HH:mm) | Bắt buộc khi ngày được check | --:-- (trống) | Giờ bắt đầu làm việc của ngày đó. Chỉ nhập được khi Checkbox ngày tương ứng được bật. Không được rỗng khi checkbox bật Trong phạm vi từ 00:00 - 23:59, không cho phép vượt ngoài phạm vi. |
| 3 | **Giờ đóng cửa** | Time Picker (HH:mm) | Bắt buộc khi ngày được check | --:-- (trống) | Giờ kết thúc làm việc của ngày đó. Phải lớn hơn Giờ mở cửa. Chỉ nhập được khi Checkbox ngày tương ứng được bật. Không được rỗng khi checkbox bật Trong phạm vi từ 00:00 - 23:59, không cho phép vượt ngoài phạm vi. |


**Lưu ý:** Thiết lập giới hạn điền ngày, tháng, năm, giờ, phút, giây. Nếu Admin điền ngày ngày, tháng, năm, giờ, phút, giây lớn hơn giới hạn quy định, lựa chọn số lớn nhất trong phạm vi cho phép.

VD:  Admin điền 123 giây, hệ thống tự đổi thành 59 giây.

**Trạng thái trường theo từng ngày:**


| **Trạng thái ngày** | **Checkbox** | **Giờ mở cửa** | **Giờ đóng cửa** |
| --- | --- | --- | --- |
| Ngày chưa được chọn (mặc định) | ☐ Unchecked | Disabled, hiển thị --:-- | Disabled, hiển thị --:-- |
| Ngày được chọn | ☑ Checked (màu cam) | Enabled, nhập được, bắt buộc nhập | Enabled, nhập được, bắt buộc nhập |
| Ngày được chọn và đã có giờ | ☑ Checked (màu cam) | Hiển thị giờ đã nhập (VD: 08:00) | Hiển thị giờ đã nhập (VD: 18:00) |



#### 4.3.3. Nhóm trường: Ngày nghỉ lễ



| **STT** | **Tên trường / Thành phần** | **Loại UI** | **Bắt buộc** | **Mô tả** |
| --- | --- | --- | --- | --- |
| 1 | **Thêm ngày** | Button + Thêm ngày | Không | Mở Date Picker để chọn ngày nghỉ lễ. Có thể thêm nhiều ngày |
| 2 | **Date Picker – Lịch tháng** | Calendar Picker | Bắt buộc khi thêm ngày | Lịch theo tháng (tháng/năm). Có nút điều hướng < / > để chuyển tháng. Ngày được chọn highlight màu cam. Ngày đã được thêm từ lần trước highlight màu xám nhạt, cho phép chọn nhiều ngày 1 lần. Khi nhấp chọn lại ngày đã chọn trước đó (màu xám nhạt), đồng nghĩa với hủy chọn ngày đó. Thêm bằng cách nhấp chọn lại, ngày được hủy xong sau đó chọn lại sẽ hiển thị màu cam. Cho phép bấm ra ngoài Date Picker để thoát mà không lưu lại những chỉnh sửa trong Date Picker. Nếu không bấm lưu, việc chọn ngày của phiên làm việc Date Picker này sẽ không được lưu lại. |
| 3 | **Options Lặp lại** | Radio button | Bắt buộc khi thêm ngày | Lựa chọn: 1. Lặp lại hàng năm (ngày nghỉ cố định mỗi năm, VD: 01/01 Tết Dương lịch) 2. Không lặp lại (chỉ nghỉ đúng năm đó) |
| 4 | **Nút [Lưu] trong Date Picker** | Button | — | Lưu ngày nghỉ vừa chọn vào danh sách, chỉ khả dụng khi chọn ít nhất 1 ngày. |
| 5 | **Danh sách ngày nghỉ đã lưu** | Text (inline) | — | Hiển thị ngay bên dưới ô "Thêm ngày" sau khi lưu, chia thành 2 dòng: **Lặp lại:** (danh sách ngày lặp, định dạng DD/MM) và **Trong năm:** (danh sách ngày không lặp, định dạng DD/MM/YYYY hoặc khoảng DD-DD/MM/YYYY) |
| 6 | **Nút [Lưu] cấu hình** | Button |  | Lưu tất cả những thiết lập cấu hình thời gian trong tab **Cấu hình **vào hệ thống |
| 7 | **Nút [Hủy] cấu hình** | Button |  | Hủy tất cả những thiết lập cấu hình thời gian, quay về giao diện Cấu hình rỗng nếu chưa từng có data cấu hình, quay về giao diện Cấu hình phiên bản trước đó nếu đã từng có data cấu hình. |


**Ví dụ hiển thị danh sách ngày nghỉ sau khi lưu:**

Ngày nghỉ lễ:  [Thêm ngày +]   Lặp lại:   01/01, 30/04, 01/05, 02/09   Trong năm: 23/04/2026, 08-11/07/2026, 19/11/2026

Wireframe minh họa giao diện hoàn tất cấu hình thời gian:


### 4.5. Chi tiết giao diện tab "Quy tắc"


Tab **Quy tắc** cho phép Admin tạo và quản lý nhiều quy tắc thời gian riêng biệt, mỗi quy tắc áp dụng cho một tập hợp kênh/tài khoản cụ thể.


#### 4.5.1. Tổng quan bố cục tab Quy tắc


Wireframe minh họa giao diện Admin truy cập tab Quy tắc lần đầu:

Wireframe minh họa giao diện Admin nhấp **Tạo mới +** để tạo mới quy tắc:

Thành phần chính của màn thiết lập quy tắc:


| **Thành phần** | **Vị trí** | **Mô tả** |
| --- | --- | --- |
| Nút **[Tạo mới +]** | Trên cùng, góc trái | Tạo thêm một quy tắc mới. Màu cam, luôn hiển thị |
| **Card Quy tắc** | Bên dưới nút Tạo mới | Mỗi quy tắc là một card riêng biệt (VD: Quy tắc 1:, Quy tắc 2:...).  Mỗi Card chia thành 2 cột: Phạm vi áp dụng (trái) và Cấu hình thời gian (phải) |
| **Thanh cuộn dọc** | Giáp bên phải phạm vi tab cấu hình Quy tắc | Cho phép Admin cuộn kéo để xem thêm những Quy Tắc được ẩn bên dưới vì giới hạn màn hình. Thể hiện vị trí xem. Chỉ xuất hiện khi có nhiều quy tắc trên hệ thống và cần cuộn xuống để xem. |



#### 4.5.2. Cột trái – Phạm vi áp dụng (Scope)


Mỗi card quy tắc có một bảng **Phạm vi áp dụng** để xác định quy tắc này áp dụng cho kênh và tài khoản nào:


| **STT** | **Tên trường** | **Loại UI** | **Bắt buộc** | **Mô tả** |
| --- | --- | --- | --- | --- |
| 1 | **Kênh** | Tag + Dropdown chọn kênh | Bắt buộc | Loại kênh áp dụng quy tắc (VD: Zalo, Telegram, Facebook...). Hiển thị dưới dạng tag màu xám nhạt có tên kênh |
| 2 | **Tài khoản** | Tag + Dropdown chọn tài khoản | Bắt buộc | Danh sách tài khoản (OA/Page) thuộc kênh đó được áp dụng quy tắc. Mỗi tài khoản là một tag riêng. VD: Zalo OA 01, Zalo OA Gapit, Zalo OA demo |
| 3 | **Nút [Kênh +]** | Button | Không | Thêm một dòng kênh + tài khoản mới vào phạm vi áp dụng của quy tắc này |


**Quy tắc hiển thị phạm vi áp dụng:**

Áp dụng như cách hiển thị thiết lập node Kênh & tài khoản ở Automation/Tự động hóa


#### 4.5.3. Cột phải – Cấu hình thời gian của quy tắc



| **STT** | **Tên trường** | **Loại UI** | **Bắt buộc** | **Placeholder** | **Mô tả** |
| --- | --- | --- | --- | --- | --- |
| 1 | **Thời gian đóng hội thoại** | Time Picker (hh:mm:ss) | Không | hh:mm:ss | Điền số thời gian kể từ khi điều kiện đóng hội thoại được áp dụng. Được điền tối đa 99:59:59. Áp dụng cho các kênh/tài khoản trong phạm vi quy tắc này. |
| 2 | **Điều kiện đóng hội thoại** | Dropdown | Không | Chọn điều kiện | Điều kiện để kích hoạt việc đóng hội thoại. So với thời điểm nhận tin nhắn cuối, So với thời điểm gửi tin nhắn cuối. Chỉ được chọn 1 điều kiện. |
| 3 | **Thời gian yêu cầu phản hồi lần đầu** | Time Picker (hh:mm:ss) | Không | hh:mm:ss | SLA phản hồi lần đầu: giới hạn thời gian tối đa để nhân viên phản hồi tin nhắn đầu tiên của khách hàng trong phạm vi quy tắc này. Nếu nhân viên phản hồi chậm hơn trong thời gian làm việc, hệ thống ghi log lại, phục vụ tính năng báo cáo trong tương lai. |
| 4 | **Thời gian chờ phân công lại** | Time Picker (hh:mm:ss) | Không | hh:mm:ss | Nếu sau khoảng thời gian này nhân viên không tiếp nhận hội thoại được phân bổ, hệ thống tự động thu hồi và phân bổ lại cho nhân viên khác đang online. |


**Lưu ý về format thời gian:** Các trường trong tab Quy tắc sử dụng định dạng hh:mm:ss (giờ:phút:giây), khác với tab Cấu hình dùng HH:mm. Điều này cho phép thiết lập thời gian chính xác đến giây.


#### 4.5.4. Ràng buộc nghiệp vụ của tab Quy tắc



| **Quy tắc** | **Mô tả** |
| --- | --- |
| Một tài khoản kênh chỉ thuộc về một quy tắc | Khi một tài khoản kênh đã được thêm vào quy tắc thời gian, nếu tạo mới một quy tắc khác, tài khoản kênh đó vẫn sẽ hiển thị trong danh sách chọn nhưng không thể được chọn (unavailable/disabled). |
| Kênh không thuộc quy tắc nào | Tất cả cuộc hội thoại của kênh đó được ở chế độ mặc định, không áp dụng bất cứ quy tắc thời gian nào |
| Quy tắc không có phạm vi áp dụng (không có bất cứ tài khoản kênh nào) | Quy tắc phải có ít nhất một kênh được chọn mới có thể lưu |



## V. ACCEPTANCE CRITERIA



### Happy Path



| **AC** | **Mô tả** | **Điều kiện pass** |
| --- | --- | --- |
| AC1 | Truy cập trang Cài đặt thời gian | Người dùng Admin đăng nhập, đi tới Cài đặt > Kênh > Thời gian chờ thành công và thấy đầy đủ giao diện các tab cấu hình, quy tắc. Người dùng Agent không thể thấy hoặc truy cập vào trang này. |
| AC2 | Validation dữ liệu nhập | Các ô nhập liệu thời gian chỉ cho phép số nguyên dương (không nhận số âm, số thập phân hoặc text). Nếu để trống trường bắt buộc khi đã bật toggle, hệ thống báo lỗi và không cho phép Lưu. |
| AC3 | Tự động đóng hội thoại | Sau đúng X phút kể từ tương tác cuối cùng hợp lệ theo cấu hình, hệ thống tự động chuyển trạng thái hội thoại từ Đang xử lý sang Đóng. |
| AC4 | Nhận diện giờ làm việc | Khi cài đặt thời gian hành chính và ngày nghỉ lễ thành công: nếu khách hàng gửi tin ngoài khung giờ hoặc vào ngày lễ, hệ thống gắn cờ Ngoài giờ để AI nhận diện và gọi tool phản hồi phù hợp. |
| AC5 | Lưu và áp dụng cấu hình | Khi ấn [Lưu thay đổi], hệ thống hiển thị toast message "Cập nhật thành công". Các quy tắc thời gian mới có hiệu lực ngay lập tức với dữ liệu/hội thoại mới phát sinh sau thời điểm lưu (không hồi tố dữ liệu cũ). |



### Edge Cases



| **AC** | **Mô tả** | **Điều kiện pass** |
| --- | --- | --- |
| AC6 | Thay đổi chưa lưu khi chuyển trang | Khi người dùng có thay đổi chưa lưu và cố chuyển sang trang khác, hệ thống hiển thị popup cảnh báo: |



## VI. OUT OF SCOPE



| **Tính năng** | **Lý do** |
| --- | --- |
| Cấu hình thời gian riêng cho từng nhân viên (Agent-level) | Thuộc phạm vi quản lý nhân sự, không xử lý tại module Time Settings |
| Lịch sử thay đổi cấu hình thời gian (Audit log) | Sẽ được xem xét trong phiên bản sau |
| Đồng bộ lịch làm việc với hệ thống HRM/ERP bên ngoài | Ngoài phạm vi tích hợp hiện tại |

**SRS TỰ ĐỘNG HÓA**

**--------------------------------------------------------**


# BẢNG GHI NHẬN THAY ĐỔI TÀI LIỆU



| **Ngày thay đổi** | **Vị trí** | **Lý do** | **Mô tả thay đổi** | **Phiên bản cũ** | **Phiên bản mới** |
| --- | --- | --- | --- | --- | --- |
| 30/09/2025 | Tạo mới |  |  |  | V1 |
| 24/10/2025 | 2. Tạo mới kịch bản tự động hóa > Flow > **Giải thích mối quan hệ và ràng buộc cơ bản** | Làm rõ các ràng buộc check trùng điều kiện giữa các kịch bản | Bổ sung thêm mô tả giải thích mối quan hệ và ràng buộc giữa việc trùng điều kiện và tài khoản kênh | V1 | V1.0.1 |
|  | 2. Tạo mới kịch bản tự động hóa > **Thêm điều kiện** | Làm rõ các ràng buộc check trùng điều kiện | Bổ sung thêm bảng **Tổng quan các loại điều kiện **và bảng **ràng buộc trùng điều kiện** |  |  |
| 07/11/2025 | 2. Tạo mới kịch bản tự động hóa > 2.4. Thử nghiệm | Thêm mô tả tên của tài khoản thử nghiệm | Bổ sung mô tả trường dữ liệu tên tài khoản thử nghiệm | V1.0.1 | V1.0.2 |
| 02/12/2025 | 2. Tạo mới kịch bản tự động hóa > 2.3 Wireframe tạo mới kịch bản tự động hóa > **Mô tả chi tiết thiết lập** | Thay đổi để phù hợp hơn với thiết kế hệ thống > tách điều kiện thời gian thành khối thiết lập khác. > Bổ sung các ràng buộc để phù hợp với các tính năng | Cải tiến, bổ sung chức năng thiết lập các khối: **Điều kiện, Thời gian, Hành động, chuyển tới nhân sự.** Cập nhật giao diện menu popup thiết lập kịch bản, tách điều kiện thời gian ra khỏi khung thiết lập điều kiện. | V1.0.2 | V1.1.1 |


--------------------------------------------------------


# BẢNG QUẢN LÝ TIẾN ĐỘ THỰC THI



| **Giai đoạn** | **Thời gian** | **Phần mục** | **Phiên bản áp dụng ** |
| --- | --- | --- | --- |
| Sprint 3 | 01/10/2025 - 25/11/2025 | - Quản lý (xem) danh sách kịch bản tự động hóa - Giao diện kéo thả để xây dựng kịch bản tự động hóa - Tạo kịch bản tự động hóa - Chỉnh sửa kịch bản tự động hóa - Tạm dừng kịch bản tự động hóa - Xóa thiết lập kịch bản tự động hóa - Test (thử nghiệm) kịch bản tự động hóa | V1.0.2 |
| Sprint 4 | Start: 01/12/2025 - ../…/2025 Bàn giao story test 01/12/2025 - ../…/2025 Review họp 01/12/2025 - ../…/2025 |  | V1.1.1 |


--------------------------------------------------------


# Bảng tài liệu bổ sung từ nền tảng khác



| **STT** | **Tài liệu** |
| --- | --- |
| 1 | - Figma |
|  |  |



# MỤC LỤC


**2**

2

4

4

5

6

6

**7**

7

8

8

9

12

12

17

17

24

28

34

34

38

38

40

**41**

41

42

42

42

**43**

43

43

43

43

43

43


## 1. Xem danh sách các kịch bản tự động hóa - (Gắn với task giao diện danh sách kịch bản tự động hóa)



### 1.1. Mô tả chức năng



| **Tên nghiệp vụ** | Xem danh sách và chi tiết kịch bản tự động |
| --- | --- |
| **Module** | Menu > Tự động hóa |
| **Mô tả** | Tính năng cho phép xem danh sách những kịch bản tự động hóa đã được tạo trong hệ thống Danh sách kịch bản tự động hóa bao gồm các cột thông tin: + ID:  thể hiện ID kịch bản + Tên kịch bản:  thể hiện tên kịch bản + Ngày tạo: thể hiện ngày tạo kịch bản + Trạng thái:  thể hiện tình trạng kích hoạt hoặc ngưng kích hoạt một kịch bản + Ngày cập nhật:  thể hiện ngày cập nhật gần nhất của kịch bản. + Cột thao tác hiển thị icon thể hiện thao tác chọn hành động chỉnh sửa hoặc xoá |
| **Điều kiện cần để thực hiện hành động** | Người dùng được phân quyền Xem của chức năng "Tự động hóa” được thiết lập tại mục Cài đặt > Thiết lập người dùng > Phân quyềnSau khi đăng nhập vào hệ thống, nhấp chọn “**Tự động hóa**” trong thanh menu Quyền chức năng thiết lập người dùng như sau: - Quyền xem: thể hiện người dùng được phép xem toàn bộ kịch bản - Quyền tạo mới: thể hiện người dùng được phép tạo/thêm mới kịch bản - Quyền chỉnh sửa: thể hiện người dùng được phép chỉnh sửa thông tin kịch bản - Quyền xoá: thể hiện người dùng được thực hiện xoá kịch bản đã được tạo |
| **Hành động** | Người dùng thực hiện theo các bước sau: **Bước 1:** Truy cập màn danh sách kịch bản tự động hóa bằng cách nhấp vào biểu tượng Tự động hóa trên menu. Giao diện Tự động hóa sẽ xuất hiện, tab "Quản lý kịch bản" mặc định hiển thị khi truy cập tính năng Tự động hóa. **Bước 2: **Xem Danh sách kịch bản tự động hóa hiển thị **Bước 3:** Xem chi tiết một kịch bản tự động hóa. Nhấp chuột hai lần vào tên của một kịch bản trong danh sách kịch bản tự động hóa để mở xem chi tiết. |
| **Kết quả** | Người dùng truy cập Xem được danh sách kịch bản tự động hóa. Người dùng truy cập xem được chi tiết một kịch bản tự động hóa. |



### 1.2 Flow


- Người dùng đăng nhập vào hệ thống => Giao diện trang chủ hiện ra

- Người dùng nhấp chọn **Tự động hóa** => Giao diện **Tự động hóa** hiện ra. Tab **Quản lý kịch bản tự động hóa** sẽ mặc định hiển thị khi truy cập tính năng **Tự động hóa**. (Tab còn lại là **Mẫu kịch bản tự động hóa** sẽ dùng để quản lý các mẫu kịch bản tự động hóa).

- Người dùng xem **Danh sách kịch bản chat tự động** trong giao diện **Tự động hóa**. Giao diện **Tự động hóa** bao gồm: Danh sách kịch bản kèm các nút tác vụ (bật tắt kịch bản, thử nghiệm, chỉnh sửa, xóa), thanh tìm kiếm, nút tạo mới.

- Trong **Danh sách kịch bản chat tự động** có các tính năng: xem chi tiết kịch bản, Bật/tắt kịch bản, chỉnh sửa kịch bản, xóa kịch bản.


### 1.3 Wireframe


*Lưu ý: Wireframe minh họa các trường dữ liệu và các ô dữ liệu, không đóng vai trò quyết định thiết kế giao diện thực sự. Thiết kế vẫn theo mẫu template hiện có trên server Product.*


### 1.4 Mô tả trường dữ liệu:



| **STT** | **Trường dữ liệu** | **Kiểu dữ liệu** | **Mô tả** | **Ràng buộc / Quy tắc** |
| --- | --- | --- | --- | --- |
| **1** | **STT** | Số nguyên (int) | Số thứ tự hiển thị kịch bản. (Có thể có hoặc không, có thể chuyển thành ID kịch bản) | Tự động tăng, duy nhất, không cho phép sửa tay |
| **2** | **Tên kịch bản** | Văn bản (string, max 255 ký tự) | Tên hiển thị cho kịch bản chatbot | Bắt buộc nhập, không trùng tên trong cùng 1 tài khoản |
| **3** | **Tài khoản** | Văn bản (string, đồng bộ từ tài khoản được chọn) | Tài khoản doanh nghiệp (VD: GAPONE, GAPIT MEDIA) | Bắt buộc, lấy từ danh sách tài khoản đã liên kết, lấy từ danh sách tài khoản được chọn trong phần thiết lập |
| **4** | **Kênh** | Enum (Zalo, Messenger, WhatsApp, …) | Kênh triển khai chatbot | Bắt buộc, chọn từ danh sách kênh được hỗ trợ |
| **5** | **Ngày tạo** | Date (dd/MM/yyyy) | Ngày hệ thống ghi nhận kịch bản được tạo | Tự động sinh khi tạo, không cho phép chỉnh sửa |
| **6** | **Ngày cập nhật** | Date (dd/MM/yyyy) | Ngày chỉnh sửa gần nhất | Tự động cập nhật khi có chỉnh sửa |
| **7** | **Trạng thái** | Boolean (On/Off) | Bật = kịch bản đang chạy; Tắt = kịch bản ngưng hoạt động | Giá trị mặc định = On khi tạo mới; có thể bật/tắt |
| **8** | **Chức năng** | Action (Sửa, Xóa) | Menu thao tác cho từng kịch bản | - Sửa: chỉ cho phép khi user có quyền - Xóa: yêu cầu xác nhận, không được xóa nếu đang được kích hoạt trong flow khác. |



### 1.5 Ràng buộc hệ thống:


- **Tên kịch bản** không được để trống và phải duy nhất trong phạm vi **một tài khoản**.

- **Ngày tạo** được hệ thống sinh tự động, người dùng không sửa được.

- **Ngày cập nhật** cập nhật tự động mỗi lần người dùng chỉnh sửa kịch bản.

- **Trạng thái**:

- Nếu chuyển từ *On → Off* thì flow chatbot sẽ ngừng phản hồi khách hàng.

- Nếu chuyển từ *Off → On* thì flow chatbot hoạt động lại.

- **Xóa kịch bản**:

- Nếu kịch bản đang chạy (On) → hiển thị cảnh báo và yêu cầu tắt trước khi xóa.

- Nếu kịch bản đang được dùng trong **flow tích hợp khác** → không cho phép xóa.

- **Tìm kiếm (Search bar)**: cho phép tìm kiếm theo **Tên kịch bản** (chứa từ khóa, không phân biệt hoa thường).


### 1.6 Use case



| **#** | **Tên Use Case** | **Tác nhân chính** | **Mô tả** | **Kết quả mong muốn** |
| --- | --- | --- | --- | --- |
| UC1.01 | Nhân viên không có quyền xem kịch bản | User, Hệ thống Gapone tính năng **phân quyền**, tính năng **tự động hóa** | Khi nhân viên chưa được phân quyền để xem được kịch bản **Tự động hóa** muốn truy cập vào. | Toàn bộ giao diện** danh sách kịch bản tự động hóa**  được ẩn. Hiện text: “Hiện bạn chưa có quyền xem “Danh sách kịch bản tự động”, vui lòng liên hệ quản trị viên để được phân quyền. |



## 2. Tạo mới kịch bản tự động từ đầu



### 2.1 Mô tả chức năng



| **Tên nghiệp vụ** | Tạo mới kịch bản tự động |
| --- | --- |
| **Module** | Menu > Cài đặt > Tự động hóa |
| **Mô tả** | Tính năng cho phép tạo mới kịch bản tự động hóa, hỗ trợ người dùng tiết kiệm thời gian và nhân lực trong khâu chăm sóc và phản hồi khách hàng. Trigger: Nút “Tạo mới” trong giao diện **Quản lý kịch bản tự động hóa**. Cài đặt tạo mới kịch bản tự động hóa bao gồm các thiết lập: - Thiết lập phân quyền: Kênh và tài khoản - Phân quyền sử dụng kịch bản này cho kênh nào và tài khoản kênh nào. Là bước bắt buộc, là khung thiết lập đầu tiên. - Thiết lập hành động: Thiết lập các bước hành động trong kịch bản. Thiết lập hành động hiện tại bao gồm: - Thêm điều kiện: Xác định điều kiện nảy sinh ra sự kiện cần hành động xử lý - Thêm hành động: Xác định hành động cần làm khi sự kiện phát sinh - Chuyển đến nhân sự: Xác định sự kiện cần chuyển giao cuộc hội thoại tới nhân sự đồng thời chỉ định nhân sự xử lý. - Thiết lập AI: - Trợ lý AI: Tương tự như một “hành động”, khi một sự kiện nào đó sảy ra và chọn nút này sẽ tương ứng với việc chuyển cuộc hội thoại này cho AI xử lý. - Liên kết n8n: Tạm ngưng |
| **Điều kiện cần để thực hiện hành động** | Người dùng được phân quyền **Tạo mới** của chức năng "**Kịch bản tự động hóa**". Truy cập phân quyền người dùng tại mục Cài đặt > Thiết lập người dùng > Phân quyền. Truy cập **Kịch bản tự động hóa** tại Trang chủ > **Tự động hóa.** Quyền chức năng thiết lập người dùng như sau: - Quyền tạo mới: thể hiện người dùng được phép tạo/thêm mới kịch bản trong hệ thống |
| **Hành động** | Người dùng thực hiện theo các bước sau: **Bước 1:** Truy cập màn danh sách kịch bản tự động hóa bằng cách nhấp vào biểu tượng **Tự động hóa** trên menu. Giao diện **Tự động hóa** sẽ xuất hiện, tab **Quản lý kịch bản tự động hóa** mặc định hiển thị khi truy cập tính năng **Tự động hóa.** **Bước 2:** - Nhấp chọn “**Tạo mới**” để được chuyển tới giao diện **Thiết lập kịch bản tự động hóa.** **Bước 3:** - Chọn và hoàn thành các thiết lập về: - Thiết lập phân quyền cho kênh và tài khoản kênh - Thiết lập điều kiện - Thiết lập hành động - Thiết lập chỉ định người dùng - Thiết lập trợ lý AI **Bước 4:** - Sau khi hoàn thành đầy đủ các thiết lập, các thiết lập hợp lệ, nhấn nút “**Hoàn thành**” để lưu kịch bản tự động. Sau đó người dùng sẽ được chuyển đến giao diện **Thử nghiệm** kịch bản vừa tạo. Các thông tin thiết lập sẽ được lưu về giao diện “**Quản lý kịch bản tự động hóa.** |
| **Kết quả** | Người dùng truy cập tạo thành công một kịch bản tự động hóa. |



### 2.2 Flow


**Giải thích các khối chức năng cơ bản:**


| **Thành phần** | **Mô tả ngắn gọn** | **Mối quan hệ** |
| --- | --- | --- |
| **User** | Người dùng hệ thống (nhân viên, quản trị viên, v.v.) | Khởi tạo tương tác bằng hành động đăng nhập |
| **Gapone Conversation** | Trang tổng quan của hệ thống, nơi người dùng truy cập các tính năng | Chứa các module con như *Hội thoại*, *Cài đặt*, *Tự động hóa* |
| **Tự động hóa** | Nơi tạo và quản lý kịch bản tự động phản hồi | Dẫn đến bước *Thiết lập kịch bản* |
| **Thiết lập kịch bản** | Trung tâm điều khiển, nơi gán kênh, điều kiện, hành động, AI | Liên kết với các module cấu hình chi tiết |
| **Kênh & Tài khoản** | Xác định nơi chatbot hoạt động (tài khoản thuộc các kênh Zalo, Messenger, Webchat...) | Cấu hình cho kịch bản |
| **Điều kiện** | Các quy tắc kích hoạt: sự kiện kích hoạt (còn được gọi là “**điều kiện sự kiện**’’) và thời gian kích hoạt ( còn được gọi là “**điều kiện thời gian**” | Gắn vào hành động cụ thể |
| **Hành động** | Hành vi hệ thống khi điều kiện được thỏa mãn (gửi tin, gửi đến Gapone, chuỗi câu hỏi...) | Liên kết trực tiếp với *Điều kiện* |
| **Chuyển đến nhân sự** | Khi Flow tự động hoặc AI không xử lý được, chuyển cuộc trò chuyện sang nhân viên thật | Phụ thuộc vào điều kiện kích hoạt |
| **Trợ lý AI** | Nơi thiết lập chọn mô hình AI và cấu hình prompt bổ sung sau khi điều kiện được kích hoạt | Tích hợp vào các hành động hoặc chuỗi hội thoại |


**Giải thích mối quan hệ và ràng buộc cơ bản (bản cũ-lỗi thời):**


| **STT** | **Thực thể chính (Use Case)** | **Thực thể liên quan** | **Mối quan hệ** | **Ràng buộc / Ghi chú** |
| --- | --- | --- | --- | --- |
| 1 | **User** | **Gapone Conversation** | Association (Login) | User phải đăng nhập để truy cập vào hệ thống Gapone Conversation. |
| 2 | **Gapone Conversation** | **Automotive Flow (Tự động hóa)** | Association | Người dùng chọn chức năng “Tự động hóa” trong hệ thống để thao tác với các kịch bản. |
| 3 | **Automotive Flow** | **Thiết lập kịch bản** | <include> | Quá trình tạo hoặc chỉnh sửa kịch bản **luôn bao gồm** bước thiết lập kịch bản. |
| 4 | **Thiết lập kịch bản** | **Kênh & Tài khoản** | <include> | Bước thiết lập **bắt buộc** phải chọn Kênh và Tài khoản sử dụng cho kịch bản. |
| 5 | **Thiết lập kịch bản** | **Điều kiện** | <include> | Kịch bản luôn có ít nhất một điều kiện kích hoạt (sự kiện hoặc thời gian). Mỗi kịch bản được chọn nhiều điều kiện, nhưng 1 điều kiện chỉ nên áp dụng cho 1 kịch bản. Hệ thống check trùng và gửi popup cảnh báo khi người dùng chọn trùng điều kiện áp dụng cho cùng một tài khoản kênh. Trường hợp khách hàng bấm chọn trùng điều kiện, hiện popup thông báo: “**Điều kiện đã bị trùng trong một kịch bản khác có áp dụng cho tài khoản kênh bạn đang chọn. Bạn chắc chắn muốn tiếp tục tạo kịch bản trùng điều kiện? Điều này sẽ tăng rủi ro khách hàng của bạn nhận tin nhắn bị trùng lặp**.” nhấn “**Xác nhận**” để lựa chọn tiếp tục chọn khung thiết lập điều kiện có trùng điều kiện. Bấm “**Quay lại**” để hủy bỏ và chọn lại điều kiện khác. => Check trùng điều kiện giữa các kịch bản áo dụng cho cùng một kênh. Trong cùng một kịch bản, không cho chọn trùng điều kiện. Đồng nghĩa với trong cùng một kịch bản, tại khung thiết lập điều kiện thứ 2, không được chọn lại điều kiện cũ trùng với điều kiện trước đó. Có thể ẩn các điều kiện đơn lẻ (bắt đầu, kết thúc cuộc trò chuyện) nếu đã có trong bất cứ khung thiết lập điều kiện nào trước đó. |
| 6 | **Thiết lập kịch bản** | **Hành động** | <extend> | Có thể thêm hành động tùy chọn (gửi tin nhắn, gửi đến gapone, chuỗi câu hỏi, v.v.) sau khi điều kiện được thiết lập. Hoặc có thể chọn “trợ lý AI” và thay hành động. |
| 7 | **Thiết lập kịch bản** | **Chuyển đến nhân sự** | <extend> | Một số kịch bản có thể được mở rộng để **chuyển tiếp hội thoại** cho nhân viên CS. |
| 8 | **Thiết lập kịch bản** | **Trợ lý AI** | <extend> | Kịch bản có thể mở rộng bằng cách thêm **AI Assistant** để phản hồi tự động. |
| 9 | **Điều kiện** | **Điều kiện sự kiện / Điều kiện thời gian** | Composition | Điều kiện trong kịch bản có thể được định nghĩa bằng sự kiện (event) và thời gian (schedule). Điều kiện = 1 sự kiện phát sinh. Những sự kiện phát sinh không nên trùng nhau. |
| 10 | **Hành động** | **Gửi tin nhắn / Gửi đến Gapone / Chuỗi câu hỏi** | Composition | Hành động bao gồm các loại thực thi khác nhau, tùy nhu cầu cấu hình của người dùng. |
| 11 | **Chuyển đến nhân sự** | **Điều kiện kích hoạt / Chỉ định nhân sự** | Composition | Khi kịch bản mở rộng đến nhân sự, hệ thống cần xác định **điều kiện** và **người phụ trách**. |
| 12 | **Trợ lý AI** | **Chọn AI / Prompt bổ sung** | Composition | Người dùng có thể chọn AI và cung cấp thêm prompt tùy chỉnh để mở rộng phản hồi. |


Ràng buộc chi tiết trong **thiết lập kịch bản**:


| **STT** | **Thực thể chính** | **Thực thể liên quan** | **Mối quan hệ** | **Ràng buộc / Ghi chú** |
| --- | --- | --- | --- | --- |
| 1 | **Kênh & Tài khoản** | Điều kiện | 1 - n | Bắt buộc có khung thiết lập kênh và tài khoản đầu tiên. Chỉ có khung thiết lập điều kiện được phép gắn tới khung thiết lập Kênh & tài khoản. Một khung thiết lập kênh và tài khoản có thể gắn tới nhiều khung thiết lập điều kiện. Khung điều kiện và các khung thiết lập khác sẽ được kích hoạt theo thứ tự, Khung nào xếp đầu sẽ được kích hoạt đầu tiên kèm các chuỗi hành động đi theo. |
|  | **Điều kiện** | Thời gian | 1 - 1..n | Một khung điều kiện có thể nối tới nhiều khung thời gian Bắt buộc phải có 1 khung điều kiện và 1 khung thời gian |
| 2 | **Thời gian** | Hành động | 1 - 0..1 | 1 khung thiết lập thời gian có thể gắn tới không hoặc tối đa một khung hành động. 1 khung thiết lập thời gian có thể gắn tới không hoặc tối đa một khung trợ lý AI. 1 khung thiết lập thời gian có thể gắn tới không hoặc tối đa một khung chuyển tới nhân sự. Nhưng tối thiểu phải nối tới 1 trong 3 khung trên, nếu không sẽ bất khả thi khi User bấm “**Hoàn thành**” |
| 3 | **Thời gian** | Trợ lý AI | 1 - 0..1 |  |
|  | **Thời gian** | Chuyển tới nhân sự | 1 - 0..1 |  |
| 3 | **Trợ lý AI** | Chuyển tới nhân sự | 1 - 0..1 | Một khung thiết lập trợ lý Ai có thể gắn tới khung chuyển tới nhân sự hoặc không. Nếu không gắn tới chuyển tới nhân sự, cuộc hội thoại này sẽ luôn luôn tự động được AI xử lý và can thiệp trong bất cứ tình huống nào cho đến khi người dùng hệ thống chủ động can thiệp vào cuộc hội thoại thì AI sẽ dừng. |
| Các khung thiết lập không được mô tả trong bảng này, mặc định tại giai đoạn hiện tại (15/10/2025) là không được phép kết nối với nhau. Kênh  x   Hành động Kênh  x   Trợ lý AI Hành động  x  Chuyển tới nhân sự Hành động  x  Trợ lý AI Điều kiện x các khung khác |  |  |  |  |


Flow tổng quan cơ bản:


### 2.3 Wireframe tạo mới kịch bản tự động hóa


*Lưu ý: Wireframe minh họa các trường dữ liệu và các ô dữ liệu, không đóng vai trò quyết định thiết kế giao diện thực sự. Thiết kế vẫn theo mẫu template hiện có trên server Product.*


#### 2.3.1 Wireframe chính


Mô tả trường dữ liệu:


| **Trường dữ liệu / Thành phần** | **Kiểu dữ liệu** | **Ràng buộc hệ thống** | **Ghi chú** |
| --- | --- | --- | --- |
| **Tên kịch bản** | Text | - Bắt buộc, không quá 255 ký tự. Tự sinh theo giờ:phút ngày/tháng/năm. Cho phép người dùng chỉnh sửa | Cho phép chỉnh sửa |
| Nút **Thử nghiệm** | Button | - Chỉ khả dụng khi có dữ liệu hợp lệ trong các trường thiết lập được thêm vào. (trường hợp chưa có dữ liệu thì disabled). - Khi click → hệ thống lưu lại các thiết lập và chạy kiểm tra dữ liệu/thiết lập AI. - Nếu lỗi, hiển thị thông báo cho người dùng. | Trạng thái **Enable/Disable** |
| Nút **Hoàn thành** | Button | - Luôn hiển thị góc trên phải. - Chỉ khả dụng khi có dữ liệu hợp lệ trong các trường thiết lập được thêm vào. - Khi click → lưu thông tin và kết thúc tiến trình. - Nếu chưa đủ dữ liệu → hiển thị cảnh báo viền đỏ tại khung thiết lập kèm thông báo “Vui lòng nhập đầy đủ thông tin”. | Trạng thái **Enable/Disable** |
| Khu vực nội dung chính (khung trắng giữa màn hình) | Panel | - Ban đầu để trống. - Sau khi người dùng click chọn những nút thiết lập ở menu, giữa màn hình sẽ hiện những khung thiết lập tương ứng vs nút được chọn. - Thanh cuộn dọc và ngang hỗ trợ cho những kịch bản quá lớn - Cho phép room in - room out khi người dùng thực hiện các phím tắt phóng to, thu nhỏ hoặc khi kéo cuộn chuột hoặc kéo cuộn tab chuột. | Có thể mở rộng |
| Khung thiết lập Kênh & Tài khoản | Node | - Luôn xuất hiện sẵn khi bấm tạo mới kịch bản tự động. - Được phép di chuyển, kéo thả | Trống dữ liệu |



#### 2.3.2. Wireframe hiển thị menu thiết lập hành động


Trigger: Nút dấu (+)

Người dùng nhấn vào (+) để mở Popup menu lựa chọn thiết lập kịch bản.

Ngoài nút: “**Thêm điều kiện**” khả dụng, các nút khác không khả dụng do ràng buộc kết nối giữa các khung thiết lập

**Khung menu thiết lập:**


| **STT** | **Tên thiết lập** | **Mô tả** |
| --- | --- | --- |
| 1 | Thiết lập phân quyền | Phân quyền sử dụng kịch bản này cho kênh nào và tài khoản kênh nào Đã có sẵn trong canvas thiết kế |
| 2 | Thêm điều kiện | Xác định điều kiện nảy sinh ra sự kiện cần hành động xử lý |
| 3 | Thêm hành động | Xác định hành động cần làm khi sự kiện phát sinh |
| 4 | Chuyển đến nhân sự | Xác định sự kiện cần chuyển giao cuộc hội thoại tới nhân sự đồng thời chỉ định nhân sự xử lý. |
| 5 | Trợ lý AI | Tương tự như một “hành động”, khi một sự kiện nào đó sảy ra và chọn nút này sẽ tương ứng với việc chuyển cuộc hội thoại này cho AI xử lý. |
| 6 | Liên kết n8n | Tạm ngưng |
| 7 | Button (x) | Đóng popup. |



##### Mô tả chi tiết thiết kế từng thiết lập:


*Bảng yêu cầu thiết kế:*


| STT | Mô tả yêu cầu | Minh họa |
| --- | --- | --- |
| 1 | Lớp layer cuối cùng: Canvas thiết kế kịch bản. Đây là vùng thiết kế. Là một màn trống cho phép thao tác thêm mới, di chuyển các node. Nếu kịch bản quá dài, có thêm thanh cuộn dọc và thanh cuộn ngang để tùy chỉnh vị trí xem Cho phép phóng to thu nhỏ khi cuộn chuột hoặc sử dụng phím tắt để zoom in-out |  |
| 2 | Layer giữa: Các node (Khung thiết lập) Các khung thiết lập xuất hiện khi được nhấp chọn tại menu chọn button kích hoạt tương ứng (trừ node:khung thiết lập kênh & tài khoản luôn xuất hiện đầu tiên) Có thể di chuyển Không thể phóng to thu nhỏ từng node, nếu phóng to thu nhỏ là do ràng buộc tỉ lệ thuận giữa kích thước của canvas và node. |  |
| 3 | Popup: Menu chọn button thiết lập kịch bản Xuất hiện khi người dùng nhấp chọn vào mỗi dấu (+) ở các khung thiết lập Không thể di chuyển Mỗi loại khung thiết lập có thể mở quyền các nút khác nhau. |  |
| 4 | Layer đầu: Heading line Luôn luôn xuất hiện Chứa tên kịch bản và 2 button “”Thử nghiệm”” “”Hoàn thành”” |  |
| 5 | Node: Khung thiết lập Có thể di chuyển được Có thể liên kết với các node khác theo ràng buộc mối quan hệ |  |
| 6 | Option: Các lựa chọn Bấm vào bất cứ chỗ nào trong khung lựa chọn sẽ tự động hiện thị dấu tích ở ô checkbox ở lựa chọn đó, bấm thêm 1 lần nữa sẽ tự động hủy chọn. Không nhất định phải di chuột nhấp vào chính xác ô checkbox. |  |
| 6 | Đường truyền: Dây kết nối Tự động xuất hiện Gắn liền 2 node khung thiết kế với nhau. Nếu gắn đúng theo mối quan hệ và ràng buộc thì sẽ hiện màu xám đậm hoặc đen Nếu gắn sai mối quan hệ và ràng buộc thì sẽ hiện màu đỏ hoặc xám nhạt kèm dấu (\) và không thể hoạt động thành công. Xử lý logic kết nối giống n8n hoặc để tự động kết nối giữa 2 node gần nhất. Nếu có chuỗi node được nối và khối ở giữa bị xóa, tự động nối tới khối tiếp theo) |  |


*Bảng hỗ trợ phân biệt một số ký hiệu dễ nhầm lẫn:*


| ***STT*** | ***Ký hiệu*** | ***Ý nghĩa*** |
| --- | --- | --- |
| *1* |  | ***Hình tròn trong droplist*** *Droplist chỉ cho phép chọn duy nhất 1 lựa chọn* |
| *2* |  | ***Hình vuông trong droplist*** *Droplist cho phép chọn nhiều lựa chọn cùng lúc* |


**Phân loại và tác các block hỗn hợp thành từng node chức năng:**


| **Phân loại** | **Node chức năng** |
| --- | --- |
| Điều kiện/ Trigger | Bắt đầu cuộc trò chuyện |
|  | Kết thúc cuộc trò chuyện |
|  | Phản hồi tin nhắn chiến dịch |
|  | Bấm nút CTA trong tin nhắn chiến dịch |
| Thời gian/ Time | Ngay lập tức |
|  | Khung giờ nhất định |
|  | Ngày giờ cụ thể |
|  | Chờ sau khoảng thời gian |
| Hành động/Action | Gửi tin nhắn |
|  | Chiến dịch gửi tin |
|  | Trợ lý AI |
|  | Chuyển đến nhân sự |


**Yêu cầu cải tiến giao diện (Dự kiến thực hiện sau 19/12):**

Từ giao diện thiết lập trực tiếp trong node, chuyển đổi thành tất cả các thiết lập được thực hiện trong khung bên trái.

Cập nhật thay đổi các node:

Vì tách các block có chung thiết lập thành các node chức năng đơn lẻ, phân theo properties nên các node không còn khung chọn options, không còn nút chức năng sửa/xóa thông tin thiết lập bên trong node (vẫn giữ nguyên nút xóa node), không còn khung thiết lập thông tin. Tất cả khung chọn options, khung chứa dữ liệu thông tin thiết lập và các button sửa/xóa đều không còn tồn tại trong node mà được chuyển đến khu vực thiết lập chung (establelish table).


##### Thiết lập phân quyền



###### Kênh & tài khoản


Thiết lập phân quyền kênh và tài khoản giúp người dùng chỉ định được kênh nào và tài khoản nào được phép áp dụng kịch bản tự động hóa này.


| **STT** | **Mô tả** | **Wireframe chi tiết từng mô tả** |
| --- | --- | --- |
| 1 | **Hiển thị khung** **thiết lập phân quyền kênh và tài khoản** —------ Mô tả: Sau khi truy cập vào giao diện tạo mới kịch bản tự động hóa thành công, ở bảng giao diện thiết kế sẽ xuất hiện **khung thiết lập phân quyền** |  |
| 2 | **Chọn kênh** —-------- Mô tả: Để thiết lập **kênh & tài khoản**, người dùng có thể nhấp trực tiếp vào khung thiết lập kênh và tài khoản mặc định hiển thị trên màn hình Khi nhấp “**Kênh +**”, hiện droplist (gồm tên các kênh) để chọn kênh cần áp dụng kịch bản tự động hóa. Từ droplist, mỗi lần chọn chỉ được một kênh Danh sách droplist các kênh được đồng bộ từ tính năng tích hợp kênh. Trong hệ thống có bao nhiêu loại kênh sẽ hiển thị bấy nhiêu kênh trên danh sách droplist |  |
| 3 | **Chọn tài khoản kênh** —------- Mô tả: Sau khi hoàn tất chọn kênh, danh sách droplist các **tài khoản kênh** thuộc kênh đó sẽ được hiển thị ở bên cạnh. Mặc định tất cả option tài khoản thuộc kênh đó đã được chọn. Người dùng muốn hủy chọn tài khoản kênh nào có thể nhấp lại vào tài khoản đó để hình tròn trong droplist không còn hiện dấu tích chọn. Nếu không chọn bỏ, mặc định chọn tất cả các tài khoản thuộc kênh đó Các thông tin thiết lập sẽ được lưu tạm ngay lập tức với bất cứ thay đổi gì. ** ** |  |
| 4 | **Hoàn thành thiết lập kênh và tài khoản thuộc kênh đó:** —---- Mô tả: Sau khi hoàn thành chọn kênh và tài khoản, khung thiết lập sẽ trở về trạng thái tạm hoàn thành. Tất cả thiết lập đều được tạm lưu lại trên hệ thống |  |
| 5 | **Thêm kênh mới trong khung thiết lập.** —---- Mô tả: Một khung thiết lập kênh có thể có nhiều kênh cùng lúc. Bấm “Kênh +” dưới khung để thêm kênh mới. Sau đó lặp lại các hiển thị để thiết lập như bước 3,4,5 Tất cả thiết lập đều được tạm lưu lại trên hệ thống |  |
| 6 | **Thêm tài khoản mới trong kênh chọn sẵn** —---- Mô tả: Nhấn chọn biểu tượng **thêm mới** ở nút chứa tên kênh, danh sách droplist tài khoản chứa kênh đó sẽ hiện ra theo đúng những thiết lập gần nhất do người dùng chọn. Sau đó người dùng có thể tích chọn thêm tài khoản kênh mới hoặc loại bỏ tài khoản kênh cũ. Tất cả thiết lập đều được tạm lưu lại trên hệ thống |  |
| 7 | **Xóa tài khoản ra khỏi kênh đã chọn** —---- Mô tả: Có 2 cách: Cách 1: Di chuyển chuột vào tài khoản kênh muốn xóa, biểu tượng **Xóa **(thùng rác) sẽ hiện ra. Nhấp chọn biểu tượng **Xóa**. Tài khoản sẽ được xóa ngay lập tức khỏi khung thiết lập, không cần hiện cảnh báo. Cách 2: Giống bước 7. Nhấn chọn biểu tượng **thêm mới** ở nút chứa tên kênh, danh sách droplist tài khoản chứa kênh đó sẽ hiện ra theo đúng những thiết lập gần nhất do người dùng chọn. Sau đó người dùng có thể tích chọn thêm tài khoản kênh mới hoặc loại bỏ tài khoản kênh cũ. Tất cả thiết lập đều được tạm lưu lại trên hệ thống |  |
| 8 | **Xóa kênh khỏi khung thiết lập:** —---- Mô tả: Nhấn chọn biểu tượng **Xóa** ở nút chứa tên kênh. Kênh sẽ lập tức bị xóa khỏi khung thiết lập. Không cần hiện cảnh báo. Người dùng có thể thiết lập lại nếu lỡ xóa. Mọi tài khoản theo kênh cũng bị xóa. Tất cả được tạm lưu lại trên hệ thống |  |


Usecase:


| **#** | **Tên Use Case** | **Tác nhân chính** | **Mô tả** | **Kết quả mong muốn** |
| --- | --- | --- | --- | --- |
| UC2.3.2.1.1 | Bỏ trống chọn kênh | Người dùng, Khung thiết lập Kênh & Tài Khoản tại tính năng thiết lập kịch bản tự động hóa | Người dùng bỏ trống không chọn kênh, sau đó sau đó thực hiện các thiết lập khác và bấm “Hoàn thành”. | Hệ thống hiện thị khung đỏ và popup cảnh báo dưới khung thiết lậpi: “**Chưa hoàn tất thiết lập kênh & tài khoản**” |
| UC2.3.2.1.2 | Bỏ trống chọn tài khoản | Người dùng, Khung thiết lập Kênh & Tài Khoản tại tính năng thiết lập kịch bản tự động hóa | Người dùng chọn kênh nhưng bỏ trống không chọn tài khoản, sau đó thực hiện các thiết lập khác và bấm “Hoàn thành” | Hệ thống hiện thị khung đỏ và popup cảnh báo dưới khung thiết lập: “**Chưa hoàn tất thiết lập kênh & tài khoản**” |
| Minh họa: |  |  |  |  |



##### Thiết lập kịch bản



###### Thêm điều kiện


Thiết lập điều kiện giúp người dùng xác định được thời điểm diễn ra sự kiện cần có sự xử lý và can thiệp của các hành động tương ứng.

Lưu ý: Mỗi khung thiết lập đều có ID riêng để kiểm soát và quản lý. ID khung thiết lập là trường dữ liệu ẩn và không hiển thị.


| **STT** | **Mô tả** | **Wireframe chi tiết từng mô tả** |
| --- | --- | --- |
| 1 | **Chọn thêm khung thiết lập điều kiện** —------- Mô tả: Nhấp chọn nút “**Thêm điều kiện**” trong menu popup **Thiết lập kịch bản** |  |
| 2 | **Hiển thị khung** **thiết lập “Thêm điều kiện”** —------ Mô tả: Sau khi nhấp chọn nút “**Thêm điều kiện**”, ở bảng giao diện thiết kế sẽ xuất hiện **khung thiết lập điều kiện** |  |
| 3 | **Sửa tên điều kiện** —------ Mô tả: Người dùng được phép thay đổi tên điều kiện, bằng cách nhấp chuột vào chữ “**Điều kiện 1**” ở tiêu đề đầu khung thiết lập. Giới hạn 50 ký tự. Nếu dài quá khung thì tên sẽ hiển thị xuống dòng. Khi đã có sẵn một khung thiết lập điều kiện trong giao diện bảng thiết kế, người dùng nhấp “**Thêm điều kiện**” để tạo thêm một khung thiết lập điều kiện nữa, khung mới sẽ hiển thị tên = “**Điều kiện 2**” => Tự tăng khi phát sinh thêm |  |
| 4 | **Chọn điều kiện** —------ Mô tả: Người dùng nhấp chuột vào ô **chọn điều kiện**, droplist chọn điều kiện sẽ được hiển thị, có thanh cuộn dọc khi danh sách quá dài (Hiển thị tối đa 4 option chọn điều kiện trong droplist, sau đó sử dụng thanh cuộn để xem các option bên dưới nếu có) Người dùng tích chọn điều kiện cần chọn, chỉ được chọn 1 điều kiện. Hiện tại tạm thời chỉ có 4 điều kiện: - Bắt đầu cuộc trò chuyện - Kết thúc cuộc trò chuyện - Phản hồi tin nhắn chiến dịch - Bấm nút CTA tin nhắn chiến dịch |  |
| 4.1 | **Chọn điều kiện đơn:** —------ Mô tả: Điều kiện đơn là điều kiện gắn liền với sự kiện phát sinh, không cần phải thiết lập thêm. Điều kiện đơn bao gồm: - Bắt đầu cuộc trò chuyện: Gắn với event khi hệ thống nhận diện được tin nhắn đầu tiên do khách hàng gửi tới. - Kết thúc cuộc trò chuyện: Gắn với event khi người dùng hệ thống nhấp chọn “Đóng hội thoại” khi hoàn thành xử lý một cuộc hội thoại. |  |
| 4.2 | **Chọn “Phản hồi tin nhắn chiến dịch”:** —------ Mô tả: Khi chọn điều kiện này, cần chọn thêm mẫu template (lấy template ID và tên template từ Gapone). Sảy ra khi khách hàng phản hồi lại tin nhắn chiến dịch gửi tin do hệ thống Gapone gửi đi. Chỉ áp dụng cho tài khoản kênh có template, những tài khoản không có template coi như được bỏ qua. |  |
| 4.3 | **Chọn “Bấm nút CTA trong tin nhắn chiến dịch”:** —------ Mô tả: Khi chọn điều kiện này, cần chọn thêm mẫu template (lấy template ID và tên template từ Gapone). Sau khi hoàn tất chọn template, đồng thời đồng bộ được thông tin của các nút có thiết lập trong mẫu. Button có trong mẫu sẽ hiện ra dưới dạng droplist Người dùng tích chọn button có trong droplist. Chỉ áp dụng cho tài khoản kênh có template, những tài khoản không có template coi như được bỏ qua. |  |
| 5 | **Đổi điều kiện:** —------ Mô tả: Khi người dùng có nhu cầu đổi điều kiện kích hoạt, có 2 cách: 1. Nhấp trực tiếp vào thanh hiện điều kiện, 2. nhấp chọn biểu tượng chỉnh sửa (biểu tượng cây bút), droplist điều kiện sẽ được hiển thị theo lần cập nhật gần nhất. Người dùng chọn lại điều kiện khác phù hợp với nhu cầu. Trường hợp các điều kiện cần thiết lập phụ (thiết lập các trường thông tin phụ thuộc kèm theo) lỡ bị loại khỏi danh sách (hủy chọn), được tính là một lần loại bỏ và phải thiết lập lại từ đầu. |  |
| 6 | **Xóa điều kiện:** —------ Mô tả: Khi người dùng muốn xóa điều kiện, nhấp chọn biểu tượng xóa ở góc trên bên phải khung thiết lập điều kiện. Khung thiết lập sẽ bị xóa ngay lập tức. |  |


**Tổng quan các loại điều kiện:**


| **STT** | **Tên điều kiện** | **Mô tả chi tiết** | **Trường dữ liệu phụ thuộc** |
| --- | --- | --- | --- |
| 1 | **Bắt đầu cuộc trò chuyện** | Kích hoạt khi khách hàng gửi **tin nhắn đầu tiên** đến kênh (Zalo, Messenger, v.v.) hoặc khi hệ thống khởi tạo một cuộc hội thoại mới. | Không có |
| 2 | **Kết thúc cuộc trò chuyện** | Kích hoạt khi cuộc trò chuyện được đánh dấu là **đã kết thúc** (ví dụ: agent đóng ticket, khách hàng không phản hồi sau X phút). | Không có |
| 3 | **Phản hồi tin nhắn chiến dịch** | Kích hoạt khi người dùng **trả lời** một tin nhắn được gửi từ **chiến dịch marketing**. | Template (chọn mẫu tin nhắn chiến dịch) |
| 4 | **Bấm nút CTA trong tin nhắn chiến dịch** | Kích hoạt khi người dùng **nhấn nút CTA (Call To Action)** trong một tin nhắn chiến dịch cụ thể. | Template (chọn mẫu tin nhắn chiến dịch) Button (chọn nút CTA cụ thể) |
| 5 | **Thời gian kích hoạt** *(bổ sung điều kiện thời gian)* | Cho phép giới hạn khung thời gian mà điều kiện được kích hoạt (ví dụ: chỉ hoạt động trong giờ hành chính hoặc theo lịch định sẵn). | HH:MM (giờ kích hoạt), Điều kiện thời gian (trước/sau, trong khoảng, hàng ngày, hàng tuần, v.v.) |


**Ràng buộc trùng điều kiện:**


| **STT** | **Loại ràng buộc** | **Mô tả chi tiết** |
| --- | --- | --- |
| 1 | **Không trùng điều kiện trong cùng một kịch bản** | Mỗi điều kiện trong kịch bản (Automation Flow) chỉ được phép chọn **duy nhất một lần**. Ví dụ, không thể lặp lại điều kiện “Bắt đầu cuộc trò chuyện” 2 lần. Phương án giải quyết: Nếu người dùng đã chọn điều kiện “bắt đầu cuộc trò chuyện”, ở khung thiết lập điều kiện tiếp theo, điều kiện “bắt đầu cuộc trò chuyện” sẽ bị ẩn |
| 2 | **Không trùng điều kiện giữa các kịch bản cùng kênh** | Nếu hai kịch bản cùng áp dụng cho **một kênh (ví dụ: Zalo Official Account)**, thì điều kiện kích hoạt của chúng không được **trùng nhau**. ➡️ Điều này đảm bảo khi khách hàng gửi tin nhắn, hệ thống chỉ kích hoạt **một** kịch bản duy nhất. Phương án giải quyết: Hệ thống gửi popup cảnh báo nhưng vẫn cho tạo trùng nếu người dùng chấp nhận rủi ro |
| 3 | **Ràng buộc giữa Template và Button** | Khi điều kiện có **Trường dữ liệu phụ thuộc** (vd: chọn **Template** hoặc **Button)**, giá trị này phải khớp với nội dung tồn tại trong hệ thống tin nhắn chiến dịch. Không cho phép chọn cùng một Template/Button đã được sử dụng cho một kịch bản khác cùng kênh.Một điều kiện có trường dữ liệu phụ thuộc sẽ check trùng dựa trên [điều kiện + trường dữ liệu phụ thuộc], không check đơn lẻ. Case: template A1 có 2 button là “Truy cập web” và “đặt bàn”, khi người dùng chọn điều kiện “**Bấm nút CTA trong tin nhắn chiến dịch**”, chọn template A1, chọn buttton “truy cập web”. [**Bấm nút CTA trong tin nhắn chiến dịch** - template A1 - truy cập web] được tính là một điều kiện. “**Bấm nút CTA trong tin nhắn chiến dịch**” không được tính là một điều kiện. |
| 4 | **Ràng buộc thời gian** | Nếu có điều kiện thời gian, chỉ kích hoạt khi thỏa mãn khung giờ định sẵn. Hệ thống sẽ bỏ qua trigger nếu ngoài khung thời gian. |



###### Thêm thời gian


Thiết lập thời gian là một trong những điều kiện về thời gian, giúp người dùng xác định được thời điểm nào sẽ kích hoạt hành động tiếp theo sau khi sự kiện phát sinh.

Lưu ý: Mỗi khung thiết lập đều có ID riêng để kiểm soát và quản lý. ID khung thiết lập là trường dữ liệu ẩn và không hiển thị.


| **STT** | **Mô tả** | **Wireframe chi tiết từng mô tả** |
| --- | --- | --- |
| 1 | **Chọn điều kiện thời gian kích hoạt:** —------ Mô tả: Sau khi chọn điều kiện event, người dùng có thể thiết lập điều kiện về thời gian so với event đó, bằng cách click chọn thêm khung thiết lập thời gian trong menu popup bên trái. Hiện tại, có 4 điều kiện thời gian kích hoạt: - Ngay lập tức - Khung giờ nhất định - Ngày giờ cụ thể - Chờ sau khoảng thời gian |  |
| 1.1 | **Chọn “Ngay lập tức”:** —------ Mô tả: Chọn điều kiện thời gian này, khi phát sinh event thì sẽ kích hoạt hành động ngay lập tức. Case minh họa: Chọn event “**bắt đầu cuộc trò chuyện**”, chọn thời gian kích hoạt “**Ngay lập tức**”, chọn hành động “**Gửi tin nhắn**” với nội dung “Chào anh chị! Anh chị cần hỗ trợ gì?”. => Khi khách hàng nhắn tin và hệ thống ghi nhận trạng thái cuộc hội thoại là open, hệ thống sẽ tự động gửi tin nhắn đã cài đặt ngay lập tức cho khách hàng. |  |
| 1.2 | **Chọn “Khung giờ nhất định”** —------ Mô tả: Chọn điều kiện thời gian này, khi phát sinh event thì sẽ đợi đến đúng khung giờ đó trong ngày (hoặc khung giờ tiếp theo gần nhất nếu lỡ qua khung giờ đó) sẽ kích hoạt hành động Sau đó chọn giờ cần cố định. Case minh họa: Chọn event “kết thúc cuộc hội thoại”, chọn “Khung giờ nhất định” lúc 21:00:00. Cài đặt hành động gửi tin nhắn với nội dung: Chúc quý khách buổi tối ấm áp! Nếu quý khách cần <Tên tài khoản> tư vấn hay hỗ trợ thêm gì thì có thể liên hệ với <Tên tài khoản> nhé! => Đúng 21h ngày phát sinh event kết thúc hội thoại, tin nhắn được gửi tới khách hàng |  |
| 1.3 | **Chọn “Ngày giờ cụ thể”****:** —------ Mô tả: Chọn điều kiện thời gian này, đến đúng ngày và giờ được thiết lập so với event được chọn sẽ kích hoạt hành động. Có tính nhắc lại theo năm Sử dụng cho những event kỷ niệm, ngày lễ, v..v.. Cần thiết lập thêm ngày và giờ tương ứng. Nếu không hoàn tất thiết lập, vẫn có thể thiết lập các khung tiếp theo nhưng không thể bấm “**Thử nghiệm**” hay “**Hoàn thành**”. Định dạng DD:MM:YYYY HH:MM:SS |  |
| 1.4 | **Chọn “Chờ sau khoảng thời gian”** —------ Mô tả: Chọn điều kiện thời gian này, hành động sẽ được kích hoạt sau khi nhận được các tiêu chí. Số ngày chờ (ngày delay gửi tin nhắn) không quá 30 ngày. Có 4 loại tiêu chí event: - So với thời điểm nhận tin nhắn đầu - So với thời điểm gửi tin nhắn đầu - So với thời điểm nhận tin nhắn cuối - So với thời điểm gửi tin nhắn cuối *Lưu ý: Trong lịch sử hội thoại với khách hàng có nhiều ****Cuộc hội thoại****. Một ****Cuộc hội thoại**** được tính từ lúc trạng thái cuộc hội thoại là Open (new) đến lúc đóng cuộc hội thoại -Closed. Tin nhắn đầu là tin nhắn đầu tiên hệ thống nhận được khi tình trạng Open (new) được mở. Tin nhắn cuối là tin nhắn cuối cùng trước khi cuộc hội thoại vào trạng thái Closed.* Case: Tin nhắn cuối: Dạ sản phẩm này có giá là 12.599.000 ạ. Đóng cuộc hội thoại do khách hàng không còn phản hồi. User cài đặt kịch bản tự động hóa gửi tin bám đuôi tư vấn “Dạ chị còn thắc mắc gì thêm về sản phẩm không ạ? Hiện bên em đang có chương trình bốc thăm khi khách hàng…” vào sau 0 ngày 12 tiếng kể từ tin nhắn cuối. Hệ thống gửi tin nhắn khi bắt được event đóng cuộc hội thoại và sau 12 tiếng *—--------* *Xóa điều kiện delay dựa theo ngày vì đã mở quyền multiple khung thiết lập thời gian chờ cho 1 kịch bản. * |  |
| 6 | **Đổi điều kiện thời gian:** —------ Mô tả: Khi người dùng có nhu cầu đổi điều kiện kích hoạt, có 2 cách: 1. Nhấp trực tiếp vào thanh hiện điều kiện, 2. nhấp chọn biểu tượng chỉnh sửa (biểu tượng cây bút), droplist điều kiện sẽ được hiển thị theo lần cập nhật gần nhất. Trường hợp các điều kiện cần thiết lập phụ lỡ bị loại khỏi danh sách (hủy chọn), được tính là một lần loại bỏ và phải thiết lập lại từ đầu. |  |
| 7 | **Xóa điều kiện:** —------ Mô tả: Khi người dùng muốn xóa điều kiện, nhấp chọn biểu tượng xóa ở góc trên bên phải khung thiết lập điều kiện. Khung thiết lập sẽ bị xóa ngay lập tức. |  |



###### Thêm hành động


Thiết lập hành động giúp người dùng xác định được hành động cần làm khi sự kiện phát sinh.

Lưu ý: Mỗi khung thiết lập đều có ID riêng để kiểm soát và quản lý. ID khung thiết lập là trường dữ liệu ẩn và không hiển thị.


| **STT** | **Mô tả** | **Wireframe chi tiết từng mô tả** |
| --- | --- | --- |
| 1 | **Chọn thêm khung thiết lập Hành động** —------- Mô tả: Nhấp chọn nút “**Thêm hành động**” trong menu **Thiết lập kịch bản** |  |
| 2 | **Hiển thị khung** **thiết lập “Thêm hành động”** —------ Mô tả: Sau khi nhấp chọn nút “**Thêm hành động**”, ở bảng giao diện thiết kế sẽ xuất hiện **khung thiết lập hành động** Một “**Điều kiện”** có thể nối tới nhiều khung thiết lập hành động cùng lúc. Hiện tại, nối tới tối đa 2 khung thiết lập hành động và 1 khung thiết lập trợ lý AI. |  |
| 3 | **Sửa tên Hành động** —------ Mô tả: Người dùng được phép thay đổi tên Hành động, bằng cách nhấp chuột vào chữ “**Hành động 1**” ở tiêu đề đầu khung thiết lập. Giới hạn 50 ký tự. Nếu dài quá khung thì tên sẽ hiển thị xuống dòng. Khi đã có sẵn một khung thiết lập hành động trong giao diện bảng thiết kế, người dùng nhấp “**Thêm hành động**” để tạo thêm một khung thiết lập hành động nữa, khung mới sẽ hiển thị tên = “**Hành động 2**” => Tự tăng khi phát sinh thêm |  |
| 4 | **Chọn hành động** —------ Mô tả: Người dùng nhấp chuột vào ô “**chọn hành động”**, droplist chọn hành động sẽ được hiển thị, có thanh cuộn dọc khi danh sách quá dài (Hiển thị tối đa 8 option chọn hành động trong droplist, sau đó sử dụng thanh cuộn để xem các option bên dưới nếu có) Người dùng tích chọn hành động cần chọn, chỉ được chọn 1 option trong 1 khung thiết lập Hiện tại tạm thời chỉ có 4 hành động: - Gửi tin nhắn - Gửi đến Gapone (pending) - Chuỗi câu hỏi - Chiến dịch gửi tin |  |
| 4.1 | **Chọn hành động “Gửi tin nhắn”** —------ Mô tả: Khi người dùng chọn hành động này, hệ thống sẽ tự động gửi đi tin nhắn khi điều kiện (event và thời gian) được kích hoạt. Người dùng nhập nội dung tin nhắn vào ô **Nội dung tin nhắn**. Nội dung tin nhắn cho phép định dạng **B**, *i*, U. Tối đa 2000 ký tự. Để sau: Cho phép cá nhân hóa trong tin nhắn các trường thông tin cá nhân trong contact khách hàng và tên tài khoản kênh. Cho phép thêm nút vào tin nhắn. Người dùng nhập tên nút tối đa 20 ký tự. Người dùng nhập link (cấm link độc) Tối đa 5 nút trong một hành động. Quá 5 nút dấu + sẽ biến mất. Xóa nút bằng cách đưa chuột vào nút để hiện biểu tượng thùng rác |  |
| 4.2 | **Pending: ****Chọn hành động “Gửi đến Gapone”** —------ Mô tả: Trong trường hợp người dùng chọn hành động này và lưu kịch bản thành công, khi đáp ứng điều kiện kích hoạt tạo ra một event khác, gửi đến hệ thống Gapone. Hệ thống Gapone sẽ nhận event và lên campaign gửi tin nhắn. |  |
| 4.3 | **Chọn hành động “Chuỗi câu hỏi”** —------ Mô tả: Khi người dùng chọn hành động này, hệ thống sẽ tự động gửi đi tin nhắn chủ đề kèm các button chứa các câu hỏi đơn khi điều kiện (event và thời gian) được kích hoạt. Khách hàng nhấp chọn button câu hỏi sẽ kích hoạt câu trả lời tự động tương ứng với button đó. Để sau: Cho phép cá nhân hóa trong tin nhắn các trường thông tin cá nhân trong contact khách hàng và tên tài khoản kênh. Có bảng mô tả các bước cùng trường dữ liệu và ràng buộc tại: |  |
|  | **Chọn hành động “Chiến dịch gửi tin”** —------ Mô tả: Hành động này cho phép người dùng trực tiếp sử dụng các template gửi tin nhắn có sẵn trong hệ thống Gapone để gửi tin tới khách hàng. (Đóng vai trò bổ trợ thậm chí là thay thế cho chiến dịch tự động hiện tại của hệ thống Gapone) **Bước 1**: Chọn hành động “Chiến dịch gửi tin”. **Bước 2**: Chọn kênh và tài khoản áp dụng. Ràng buộc: Chỉ được chọn một kênh và một tài khoản **Bước 3**: Chọn mẫu gửi tin tương ứng với kênh và tài khoản kênh được chọn. Ràng buộc: mẫu gửi tin phải thuộc tài khoản kênh được chọn. Không thể chọn mẫu gửi tin của tài khoản kênh khác hoặc kênh khác |  |
| 5 | **Thay đổi hành động** —------ Mô tả: Có 2 cách để thay đổi hành động. C1: nhấp trực tiếp vô ô chứa dữ liệu “Chọn hành động”, droplist sẽ hiện ra cùng với kết quả tương tự lần cập nhật gần nhất. Tích chọn vào điều kiện cần chọn lại. C2: nhấp vào biểu tượng chỉnh sửa hình cây bút. droplist sẽ hiện ra cùng với kết quả tương tự lần cập nhật gần nhất. Tích chọn vào điều kiện cần chọn lại. Trường hợp người dùng lỡ tay hủy chọn hành động cần có thiết lập phụ, đồng nghĩa với hủy tất cả thiết lập phụ, tất cả thiết lập phụ đều bị xóa. Người dùng cần tự nhập lại nếu cần. |  |
| 6 | **Xóa hành động** —------ Mô tả: Khi người dùng muốn xóa hành động, nhấp chọn biểu tượng xóa ở góc trên bên phải khung thiết lập điều kiện. Khung thiết lập sẽ bị xóa ngay lập tức. |  |



###### Mô tả trường dữ liệu và ràng buộc bổ sung cho Khung thiết lập hành động: **Chuỗi câu hỏi**



| **Trường dữ liệu / Thành phần** | **Mô tả chức năng** | **Ràng buộc hệ thống** |  |
| --- | --- | --- | --- |
| 1. Khung thiết lập hành động | 1.1. Tên khối | Tự sinh khi tăng thêm, có thể thay đổi. Không quá 50 ký tự | - Tự sinh khi tăng thêm |
|  | 1.2. ID khối hành động (Trường dữ liệu ẩn) | Dùng để quản lý và kiểm soát các block | - Tự sinh khi tăng thêm - Không trùng với bất cứ ID nào |
|  | 1.3. Chọn Hành động (dropdown) = Chuỗi câu hỏi | Chọn loại hành động: "**Chuỗi câu hỏi**" | - Người dùng lựa chọn option **Chuỗi câu hỏi** để mở ra các thiết lập về chuỗi câu hỏi tiếp theo |
|  | 1.2. Tin nhắn chủ đề (Câu hỏi chủ đề) | Nội dung tin nhắn mở đầu chuỗi câu hỏi (mô tả, hướng dẫn). | - Cho phép định dạng Bold, Italic, Underline. - Tối đa 500 ký tự. - Có thể để trống nếu bên dưới có nội dung khác (bao gồm nội dung câu hỏi đơn, v.v…) - Đóng vai trò là layer câu hỏi đầu tiên |
|  | 1.3. Ký hiệu đính kèm ảnh, link, tệp | Cho phép tải ảnh lên, cho phép gửi file, cho phép đính kèm link vào tin nhắn | - Ảnh có dung lượng tối đa 50MB, kích thước không bắt buộc, nếu quá kích thước tiêu chuẩn của nền tảng sẽ hiển thị dạng tệp. - File có dung lượng tối đa 50MB, chỉ cho phép định dạng PDF và word. - Cần check link an toàn, nếu check ra rủi ro, hệ thống hiển thị cảnh báo: “URL không hợp lệ. Cảnh báo rủi ro an toàn.” |
|  | 1.4. Nút "Chuỗi câu hỏi +” | Thêm chuỗi | - Tạo thêm một khối phụ trong khung thiết lập hành động. Khối này đóng vai trò là layer câu hỏi thứ 2. Bao gồm các trường dữ liệu theo mô tả của phần 2: Thiết lập một chuỗi câu hỏi - Tối đa 10 chuỗi |
| 2. Thiết lập một chuỗi câu hỏi | 2.1. Tên chuỗi (Chuỗi 1) | Chuỗi câu hỏi chính (chain root). | - ID chuỗi tự sinh. - Tên chuỗi tự sinh, không thể sửa |
|  | 2.1 Id chuỗi (trường dữ liệu ẩn) | Dùng để quản lý và kiểm soát các chuỗi | - Tự sinh khi tăng thêm - Không trùng với bất cứ ID nào |
|  | 2.2. Chọn loại hình (dropdown) | Chọn type câu hỏi trong chuỗi. | 2 tùy chọn: - Câu hỏi đơn - Kết thúc chuỗi câu hỏi *Trong tương lai có thể phát triển thêm tùy chọn khác* |
|  | 2.3. Thêm <Câu hỏi đơn> (Button) | Thêm một câu hỏi vào chuỗi. | - Không tạo mới nếu câu hỏi cuối cùng đang để trống. |
|  | 2.4 Danh sách câu hỏi đơn (1,2,3...) (Block text) | Các câu hỏi trong chuỗi chính. | - Vị trí nằm trước nút “+ thêm <câu hỏi đơn>”, nhưng nếu chưa có câu hỏi nào sẽ không được hiển thị - Mỗi câu hỏi bắt buộc có nội dung. - Mỗi câu hỏi có ID ẩn kèm theo để liên kết tới các khối mở rộng. - Chỉ xuất hiện thêm khung điền câu hỏi khi bấm chọn “+ thêm <câu hỏi đơn>” - Số câu hỏi tối đa: 10 |
|  | 2.5 Icon mũi tên mở rộng (→) (Button) | Mở thiết lập nhân nhánh mở rộng (popup) | - Chỉ hoạt động nếu nội dung câu hỏi không trống. |
| 3. Sub Node/Block phụ Có thiết kế gần tương đồng như một khối phụ chuỗi câu hỏi. Đóng vai trò mở rộng thiết lập câu hỏi | 3.1 Tên phân nhánh (Câu hỏi 1 / 1.1 / 1.2...) | Tự động đánh số theo mức phân nhánh | - Không cho phép trùng số thứ tự. - Số thứ tự theo chuẩn cây: • Chuỗi chính: 1,2,3 • Nhánh con: 1.1, 1.2… Sử dụng quy tắc viết tắt đánh số khi số quá dài. VD: 1.1.1.1.1.1.1.1.1.2 => 1.1(8).2 VD: 1.1.1.1.2.2.2.2.3.4 => 1.1(3).2(4).3.4 |
|  | 3.2 ID khối phụ | Dùng để quản lý và kiểm soát các khối. Liên kết tới các câu hỏi | - Tự sinh khi tăng thêm - Không trùng với bất cứ ID nào |
|  | **Chọn loại hình** | Chọn loại câu hỏi trong phân nhánh mở rộng. | - Chỉ chọn **Câu hỏi đơn** hoặc **Kết thúc**. - Không cho phép chọn loại hình chưa hỗ trợ. |
|  | **Các câu hỏi trong phân nhánh (1.1.1, 1.1.2...)** | Câu hỏi nằm trong nhánh con. | - Không được để trống. - Không vượt quá giới hạn thiết kế (ví dụ max 10 câu). |
|  | **Thêm "Câu hỏi đơn"** | Thêm câu hỏi trong nhánh. | - Không thêm nếu câu hỏi cuối đang trống. |
|  | **Không cho phép tạo nhánh vô hạn** | Giới hạn mức mở rộng phân nhánh | - Ví dụ: tối đa 3 cấp (1 ➝ 1.1 ➝ 1.1.1). |



###### Chuyển đến nhân sự:


Thiết lập chuyển đến nhân sự giúp người dùng xác định sự kiện cần chuyển giao cuộc hội thoại tới nhân sự đồng thời chỉ định nhân sự xử lý.

Lưu ý: Mỗi khung thiết lập đều có ID riêng để kiểm soát và quản lý. ID khung thiết lập là trường dữ liệu ẩn và không hiển thị.


| **STT** | **Mô tả** | **Wireframe chi tiết từng mô tả** |
| --- | --- | --- |
| 1 | **Chọn thêm khung thiết lập “Chuyển đến nhân sự”** —------- Mô tả: Nhấp chọn nút “**Chuyển đến nhân sự**” trong menu **Thiết lập kịch bản** |  |
| 2 | Hiển thị khung thiết lập “Chuyển đến nhân sự” —------ Mô tả: Sau khi nhấp chọn nút “Chuyển đến nhân sự”, ở bảng giao diện thiết kế sẽ xuất hiện khung thiết lập Chuyển tới nhân sự Một khung thiết lập “Hành động” có thể nối tới một khung thiết lập “Chuyển đến nhân sự”. Một khung thiết lập “Trợ lý AI” có thể nối tới một khung thiết lập “Chuyển đến nhân sự”. Trường hợp đặc biệt: Phục vụ cho case phân công nhân sự tự động. Trường hợp đặc biệt này không xử lý bất cứ nội dung cuộc hội thoại nào, chỉ xử lý việc phân công chỉ định nhân viên tự động vào các cuộc hội thoại. Đối với trường hợp phân công nhân sự tự động, một khung thiết lập nhân sự có thể gắn với một khung thời gian. Ràng buộc: Chỉ nối tới điều kiện “Bắt đầu cuộc trò chuyện”, chỉ nối tới điều kiện thời gian “Ngay lập tức”. => Nếu chọn chuyển đến nhân sự ngay sau khung thiết lập thời gian, khóa hết các lựa chọn thiết lập khác tại khung điều kiện và khung thời gian. |  |
| 3 | Sửa tên thiết lập “Chuyển tới nhân sự” —------ Mô tả: Người dùng được phép thay đổi tên thiết lập “Chuyển tới nhân sự”, bằng cách nhấp chuột vào chữ “Chuyển tới nhân sự 1” ở tiêu đề đầu khung thiết lập. Giới hạn tối đa 50 ký tự. Nếu dài quá khung thì tên sẽ hiển thị xuống dòng. Khi đã có sẵn một khung thiết lập Chuyển tới nhân sự trong giao diện bảng thiết kế, người dùng nhấp “Chuyển tới nhân sự” để tạo thêm một khung thiết lập Chuyển tới nhân sự nữa, khung mới sẽ hiển thị tên = “Chuyển tới nhân sự 2” => Tự tăng khi phát sinh thêm |  |
| 4.1 | Xử lý ẩn, để sau: Chọn điều kiện “Nội dung chứa những ký tự” —------ Mô tả: Nếu người dùng chọn điều kiện này, khi trong tin nhắn từ phía khách hàng xuất hiện những ký tự, từ ngữ trong danh sách sẽ tự động kích hoạt việc chuyển tới nhân sự. Có 2 cách xác định các ký tự: Tải lên danh sách chứa ký tự: File hợp lệ: word, excel, pdf không độc hại, tối đa 20Mb Nhập URL danh sách chứa ký tự, URL phải an toàn (hệ thống cảnh báo nếu nghi ngờ tính an toàn: “Đường dẫn bị nghi ngờ, vui lòng nhập lại đường dẫn khác”. Sau đó bấm ký tự chuyển đổi để chính thức nhập danh sách chứa ký tự. | Minh họa cũ: Sau khi xử lý ẩn điều kiện, giao diện chính thức như sau: |
| 4.2 | Xử lý ẩn. Chọn điều kiện “Button yêu cầu nhân viên” —------ Mô tả: Button sẽ luôn xuất hiện tại tin nhắn đầu tiên của mỗi kịch bản tự động khi được kích hoạt. Khi khách hàng nhấn vào nút yêu cầu nhân viên, cuộc hội thoại sẽ được chuyển tới ngườ dùng được phân công hoặc chuyển tới cho hệ thống phân công tự động theo round-robin ngay lập tức | Minh họa cũ: Sau khi xử lý ẩn điều kiện, giao diện chính thức như sau: Minh họa: Hình ảnh tin nhắn tự động của shopee kèm button yêu cầu nhân viên trong giao diện cuộc hội thoại |
| 4.3 | Xử lý ẩn. Chọn điều kiện “AI từ chối trả lời” —------ Mô tả: Cuộc hội thoại sẽ được chuyển tới người dùng khi AI từ chối trả lời. Chỉ áp dụng khi thiết lập AI trong phần Cài đặt có cài đặt trường hợp AI từ chối trả lời. Chỉ được chọn khi trước đó là hành động chọn thiết lập “Trợ lý AI” | Minh họa cũ: Sau khi xử lý ẩn điều kiện, giao diện chính thức như sau: |
| 7 | Chỉ định nhân sự: —------ Mô tả: Sau khi người dùng hoàn thành chọn điều kiện, người dùng có thể tiếp tục chọn nhân viên hoặc nhóm nhân viên cần chỉ định. Trước khi chỉ định nhân sự, người dùng cần xác nhận việc chỉ định này áp dụng cho tất cả các cuộc hội thoại hay chỉ áp dụng cho cuộc hội thoại chưa có nhân viên phụ trách. - Áp dụng cho tất cả các cuộc hội thoại: Chỉ định nhân sự ở module kịch bản tự động hóa sẽ đè lên các cuộc hội thoại đã được chỉ định nhân viên trước đó trong Module Hội Thoại - Chỉ áp dụng cho cuộc hội thoại chưa chỉ định nhân viên: Chỉ định nhân sự ở module kịch bản tự động hóa sẽ tìm các cuộc hội thoại tại module Hội thoại chưa được chỉ định nhân sự và phân công nhân viên vào những cuộc hội thoại đó. Ràng buộc hệ thống: Đối với phân quyền theo nhóm nhân sự: - Nếu cuộc hội thoại đang thuộc một nhóm kênh, thì chỉ cho phép hiển thị danh sách nhân sự được cấp quyền phụ trách nhóm kênh đó. - Logic phân công theo lần lượt. Logic phân công tương tự logic phân công theo nhóm trong module Hội thoại -  Chỉ định theo nhóm có thể chọn multiple nhiều options, các options không nhất định phải liên quan tới nhau. |  |
| 8 | Thay đổi “Chỉ định người dùng” —------ Mô tả: Người dùng có nhu cầu muốn thay đổi người dùng được chỉ định cuộc hội thoại, nhấp trực tiếp vô ô chứa dữ liệu “Chỉ định người dùng”, droplist sẽ hiện ra cùng với kết quả tương tự lần cập nhật gần nhất. Tích chọn lại vào người hoặc nhóm người dùng. |  |
| 9 | Xóa thiết lập “Chuyển đến nhân sự”: —------ Mô tả: Khi người dùng muốn xóa thiết lập, nhấp chọn biểu tượng xóa ở góc trên bên phải khung thiết lập Chuyển đến nhân sự. Khung thiết lập sẽ bị xóa ngay lập tức. |  |



#### Thiết lập AI



###### Trợ lý AI


Thiết lập này cho phép AI bắt đầu tham gia vào cuộc hội thoại khi nhận được tín hiệu điều kiện kích hoạt sự kiện được gán.

Thiết lập này tương tự như một “Hành động” nhưng khác tính chất. Thiết lập “Hành động” trong hệ thống là cố định theo kịch bản, còn thiết lập “Trợ lý AI” sẽ linh hoạt phát sinh thêm nhiều tin nhắn không cài đặt sẵn trong hệ thống.

Lưu ý: Mỗi khung thiết lập đều có ID riêng để kiểm soát và quản lý. ID khung thiết lập là trường dữ liệu ẩn và không hiển thị.


| STT | Mô tả | Wireframe chi tiết từng mô tả |
| --- | --- | --- |
| 1 | Chọn thêm khung thiết lập “Trợ lý AI” —------- Mô tả: Nhấp chọn nút “Trợ lý AI” trong menu Thiết lập kịch bản |  |
| 2 | Hiển thị khung thiết lập “Trợ ký Ai” —------ Mô tả: Sau khi nhấp chọn nút “Trợ lý AI”, ở bảng giao diện thiết kế sẽ xuất hiện khung thiết lập Trợ lý AI Một khung thiết lập “điều kiện” có thể nối tới một khung thiết lập “Trợ lý AI”. Một khung thiết lập “Trợ lý AI” có thể nối tới một khung thiết lập “Chuyển đến nhân sự”. |  |
| 3 | Sửa tên thiết lập “Trợ lý AI” —------ Mô tả: Người dùng được phép thay đổi tên thiết lập “Trợ lý AI 1”, bằng cách nhấp chuột vào chữ “Trợ lý AI 1” ở tiêu đề đầu khung thiết lập. Giới hạn 50 ký tự. Nếu dài quá khung thì tên sẽ hiển thị xuống dòng. Khi đã có sẵn một khung thiết lập Trợ lý AI trong giao diện bảng thiết kế, người dùng nhấp “Trợ lý AI” để tạo thêm một khung thiết lập Trợ lý AI  nữa, khung mới sẽ hiển thị tên = “Trợ lý AI 2” => Tự tăng khi phát sinh thêm |  |
| 4 | Chọn Trợ lý AI —------ Mô tả: Người dùng nhấp chuột vào ô “Chọn AI”, danh sách droplist AI sẽ được hiển thị. Danh sách này được đồng bộ từ các AI có trong bảng Danh sách AI tại giao diện Quản lý AI trong tính năng Cài đặt> Thiết lập AI. Tên AI trong danh sách được hiển thị theo cú pháp: Tên AI_Model AI Chỉ được chọn duy nhất 1 AI. |  |
| 5 | Điền “Prompt bổ sung” —------ Mô tả: Khi người dùng có nhu cầu bổ sung prompt cho AI xử lý, có thể bổ sung mô tả ngắn gọn cho AI trong vòng 500 ký tự, không chứa mã độc, script. Prompt bổ sung chỉ mang tính chất bổ sung về giọng điệu, cách thể hiện, AI tuân theo đa số chỉ thị của prompt gốc đồng thời kết hợp prompt bổ sung. Nếu không điền prompt bổ sung, AI sẽ hoạt động theo prompt gốc trong cài đặt > thiết lập AI |  |
| 6 | Thay đổi “Chọn AI” —------ Mô tả: Người dùng có nhu cầu muốn thay đổi AI được chỉ định cuộc hội thoại, nhấp trực tiếp vô ô chứa dữ liệu “Chọn AI”, droplist sẽ hiện ra cùng với kết quả tương tự lần cập nhật gần nhất. Tích chọn lại vào AI cần thay đổi. |  |
| 7 | Thay đổi “Prompt bổ sung” —------ Mô tả: Người dùng có nhu cầu muốn thay đổi Prompt bổ sung, nhấp trực tiếp vô ô text chứa dữ liệu “Prompt bổ sung”. Hiển thị cho phép chỉnh sửa nội dung như khung text thông thường |  |
| 8 | Xóa thiết lập “Trợ lý AI”: —------ Mô tả: Khi người dùng muốn xóa thiết lập, nhấp chọn biểu tượng xóa ở góc trên bên phải khung thiết lập Trợ lý AI Khung thiết lập sẽ bị xóa ngay lập tức. |  |



#### Thiết lập khác


Thay đổi tên kịch bản: Người dùng có thể thay đổi tên kịch bản. Tên kịch bản sau klhi thay đổi sẽ được hiển thị ở danh sách kịch bản tự động hóa tại tab giao diện Quản lý kịch bản tự động hóa


| STT | Mô tả | Wireframe chi tiết từng mô tả |
| --- | --- | --- |
| 1 | Lưu kịch bản (Nhấn “Hoàn thành”) —------- Mô tả: Người dùng có thể lựu kịch bản bằng 2 cách: Nhấn “Hoàn thành” để lưu kịch bản và quay về giao diện Quản lý kịch bản tự động hóa Nhấn “Thử nghiệm” để lưu kịch bản và chuyển tới giao diện thử nghiệm phản hồi chat của hệ thống theo kịch bản. |  |
| 1 | Thay đổi tên kịch bản —------- Mô tả: Người dùng có thể thay đổi tên kịch bản bằng cách nhấp vào tên kịch bản. Tên kịch bản sẽ tự sinh theo cú pháp: Kịch bản tự động hóa HH:MM  DD:MM:YYYY Không cho phép để trống, nếu để trống hiện báo lỗi: “Không được để trống tên kịch bản” |  |



### 2.4 Thử nghiệm kịch bản tự động hóa


Wireframe

Bước 1: Sau khi nhấp chọn thử nghiệm, màn hình hiển thị popup chọn cuộc trò chuyện để thử nghiệm.

Bước 2: Thử nghiệm

Mô tả trường dữ liệu:


| Trường dữ liệu | Mô tả | Ràng buộc/Quy tắc |
| --- | --- | --- |
| Khung hội thoại | Hiển thị luồng hội thoại giữa người dùng và hệ thống | - Nội dung được sinh tự động từ kịch bản và người dùng nhập. - Thử nghiệm không trực tiếp gửi tới nền tảng và khách hàng -> không phân kênh và tài khoản kênh (không dựa trên khung thiết lập kênh và tài khoản) - Không cho phép chỉnh sửa trực tiếp nội dung đã gửi - Tin nhắn hiển thị theo thời gian thực |
| Tên Tài khoản | Hiển thị tên của tài khoản kênh của doanh nghiệp | - Lấy từ tên tài khoản kênh của doanh nghiệp. - Nếu kịch bản được áp dụng cho nhiều tài khoản thì minh họa bằng tên tài khoản kênh đầu tiên được chọn trong danh sách. |
| Ô nhập nội dung trò chuyện | Người dùng nhập câu hỏi hoặc tin nhắn để gửi cho hệ thống và chờ hệ thống phản hồi | - Không được để trống khi bấm gửi - Không cho phép gửi tin chứa mã độc, script HTML/JS - Tối đa 2000 ký tự |
| Nút gửi tin nhắn (mũi tên cam) | Gửi nội dung trong ô nhập cho hệ thống | - Chỉ khả dụng khi ô nhập có dữ liệu hợp lệ - Gửi thành công thì xóa nội dung trong ô nhập |
| Nút làm mới (↻) | Làm mới hoặc reset cuộc hội thoại | - Sau khi làm mới, toàn bộ nội dung chat cũ sẽ bị xóa khỏi khung hội thoại |
| Nút "Quay lại chỉnh sửa" | Quay về màn hình thiết lập kịch bản tự động để sửa cấu hình | - Luôn khả dụng - Không ảnh hưởng đến dữ liệu hội thoại đang thử nghiệm |
| Nút "Hoàn thành" | Xác nhận kết thúc thử nghiệm | - Luôn khả dụng ngay cả khi người dùng không thử nghiệm cuộc hội thoại nào |


Ràng buộc hệ thống:

- Người dùng không thể chỉnh sửa tin nhắn đã gửi.

- Hệ thống sẽ trả lời theo đúng thiết lập. Với trường hợp ủy quyền cho trợ lý AI, AI chỉ trả lời dựa trên prompt và kho dữ liệu đã thiết lập trước đó.

- Nếu AI không tìm thấy dữ liệu → trả lời theo fallback mặc định hoặc từ chối trả lời nếu đã cài đặt từ chối trả lời.

- Cuộc hội thoại với AI là cuộc hội thoại giả lập, không trực tiếp lưu hay ảnh hưởng tới tính năng Conversation hay màn hội thoại thực tế trên nền tảng (Zalo, telegram, v…)

- Trạng thái cuộc hội thoại giả lập thử nghiệm kịch bản tự động hóa:


| STT | Từ trạng thái | Sang trạng thái | Điều kiện kích hoạt/Hành vi |
| --- | --- | --- | --- |
| 1 | - | Mới | User gửi tin nhắn câu hỏi |
| 2 | Mới | Đang xử lý | Hệ thống đang phản hồi. User đang tiếp tục gửi tin nhắn thử nghiệm kịch bản tự động và sự phản hồi từ hệ thống |
| 3 | Đang xử lý | Đóng | User nhấn “Hoàn thành” hoặc thoát khỏi giao diện Thử nghiệm kịch bản tự động hóa |



### 2.5 Ràng buộc hệ thống



## 3. Chỉnh sửa kịch bản tự động



### 3.1 Mô tả chức năng



| Tên nghiệp vụ | Chỉnh sửa kịch bản tự động |
| --- | --- |
| Module | Menu > Tự động hóa |
| Mô tả | Tính năng cho phép chỉnh sửa kịch bản tự động hóa đã có trong hệ thống. Trigger: Nút “Chỉnh sửa” trong menu ẩn tại giao diện Quản lý kịch bản tự động hóa. Chỉnh sửa kịch bản tự động hóa có thể bao gồm các thiết lập chỉnh sửa sau đây tùy vào nhu cầu của người dùng: - Thiết lập phân quyền: Kênh và tài khoản - Chỉnh sửa phân quyền sử dụng kịch bản này cho kênh nào và tài khoản kênh nào. - Thiết lập hành động: Chỉnh sửa thiết lập các bước hành động trong kịch bản. Chỉnh sửa thiết lập hành động hiện tại bao gồm: - Thêm/chỉnh sửa/xóa điều kiện: Thêm/chỉnh sửa/xóa điều kiện nảy sinh ra sự kiện cần hành động xử lý - Thêm/chỉnh sửa/xóa hành động: Thêm/chỉnh sửa/xóa hành động cần làm khi sự kiện phát sinh - Thêm/chỉnh sửa/xóa chuyển đến nhân sự. - Thêm/chỉnh sửa/xóa Trợ lý AI: Tương tự như một “hành động”, khi một sự kiện nào đó sảy ra và chọn nút này sẽ tương ứng với việc chuyển cuộc hội thoại này cho AI xử lý. - Thêm/chỉnh sửa/xóa Liên kết n8n: Tạm ngưng |
| Điều kiện cần để thực hiện hành động | Người dùng được phân quyền Chỉnh sửa của chức năng "Kịch bản tự động hóa". Truy cập phân quyền người dùng tại mục Cài đặt > Thiết lập người dùng > Phân quyền. Truy cập Kịch bản tự động hóa tại Trang chủ > Tự động hóa. Quyền chức năng thiết lập người dùng như sau: - Quyền chỉnh sửa: thể hiện người dùng được phép chỉnh sửa kịch bản có sẵn trong hệ thống. - Có 2 cấp phân quyền chỉnh sửa: Chỉnh sửa kịch bản tự động hóa do bản thân tự tạo và chỉnh sửa kịch bản tự động do người dùng khác tạo. |
| Hành động | Người dùng thực hiện theo các bước sau: Bước 1: Truy cập màn danh sách kịch bản tự động hóa bằng cách nhấp vào biểu tượng Tự động hóa trên menu. Giao diện Tự động hóa sẽ xuất hiện, tab Quản lý kịch bản tự động hóa mặc định hiển thị khi truy cập tính năng Tự động hóa. Bước 2: - Xác định kịch bản cần chỉnh sửa, nhấp chọn vào biểu tượng menu ẩn “...” và chọn biểu tượng “Chỉnh sửa” để được chuyển tới giao diện Thiết lập kịch bản tự động hóa. Bước 3: - Xác định thiết lập cần chính sửa và hoàn thành các thiết lập về: - Thiết lập phân quyền cho kênh và tài khoản kênh - Thiết lập điều kiện - Thiết lập hành động - Thiết lập chỉ định người dùng - Thiết lập trợ lý AI Bước 4: - Sau khi hoàn thành đầy đủ các thiết lập, các thiết lập hợp lệ, nhấn nút “Hoàn thành” để lưu kịch bản tự động. Sau đó người dùng sẽ được chuyển đến giao diện Thử nghiệm kịch bản vừa tạo. Các thông tin thiết lập sẽ được lưu về giao diện “Quản lý kịch bản tự động hóa. - Bấm “Thử nghiệm” |
| Kết quả | Người dùng chỉnh sửa thành công một kịch bản tự động hóa. |



### 3.2 Flow



### (Đang bổ sung)



### 3.6 Use case



| # | Tên Use Case | Tác nhân chính | Mô tả | Kết quả mong muốn |
| --- | --- | --- | --- | --- |
| UC1.01 | Nhân viên không có quyền xem kịch bản | User, Hệ thống Gapone tính năng phân quyền, tính năng tự động hóa | Khi nhân viên chưa được phân quyền để xem được kịch bản Tự động hóa muốn truy cập vào. | Toàn bộ giao diện danh sách kịch bản tự động hóa  được ẩn. Hiện text: “Hiện bạn chưa có quyền xem “Danh sách kịch bản tự động”, vui lòng liên hệ quản trị viên để được phân quyền. |



## 4. Xóa kịch bản tự động



### 4.1 Mô tả chức năng



| Tên nghiệp vụ | Xóa kịch bản tự động đã có trong hệ thống |
| --- | --- |
| Module | Menu > Tự động hóa |
| Mô tả | Tính năng cho phép xóa kịch bản đã có trong hệ thống Gapone Conversation. Trigger: Nút “xóa” Người dùng hoàn thành việc xóa kịch bản thành công. Kịch bản bị xóa thành công khỏi hệ thống, đồng thời thông tin kịch bản trong bảng danh sách kịch bản tại giao diện Quản lý kịch bản tự động hóa cũng bị xóa bỏ. |
| Điều kiện cần để thực hiện hành động | Người dùng được phân quyền Xóa của tính năng "Tự động hóa". Truy cập phân quyền người dùng tại mục Cài đặt > Thiết lập người dùng > Phân quyền. Truy cập kịch bản tự động hóa tại Cài đặt > Tự động hóa Quyền chức năng thiết lập người dùng như sau: - Quyền xóa: thể hiện người dùng được phép xóa kịch bản trong hệ thống Có kịch bản hợp lệ đã tạo trong hệ thống. |
| Hành động | Người dùng thực hiện theo các bước sau: Bước 1: - Truy cập màn danh sách kịch bản tự động hóa bằng cách nhấp vào biểu tượng Tự động hóa trên menu. Giao diện Tự động hóa sẽ xuất hiện, tab Quản lý kịch bản tự động hóa mặc định hiển thị khi truy cập tính năng Tự động hóa. Bước 2: - Xác định kịch bản cần xóa, nhấp chọn vào biểu tượng menu ẩn “...” và chọn biểu tượng “Xóa”. Bước 3: - Ấn chọn "Xác nhận” để xác nhận và hoàn thành thao tác xoá/loại bỏ kịch bản ra khỏi hệ thống. Ấn chọn "Quay lại" để huỷ thao tác xoá đang thực hiện. |
| Kết quả | Người dùng xóa một kịch bản đã có trong hệ thống thành công khi thỏa mãn các điều kiện |



### 4.2 Wireframe


4.2.1 Wireframe Quản lý kịch bản tự động hóa > Chọn xóa

4.2.2 Wireframe Quản lý kịch bản tự động hóa > Chọn xóa > Popup thông báo xác nhận


### 4.4 Mô tả trường dữ liệu



| # | Thành phần | Kiểu dữ liệu | Ràng buộc hệ thống | Ghi chú |
| --- | --- | --- | --- | --- |
| 1. Menu ẩn chứa các nút hành động (Số nút hành động có thể tăng thêm khi hệ thống có cập nhật hạ tầng tính năng này) |  |  |  |  |
| 1.1 | Nút Thử nghiệm | Button | Khi click → mở giao diện thử nghiệm kịch bản đã chọn | Luôn khả dụng |
| 1.2 | Nút Chỉnh sửa | Button | Khi click → mở giao diện chỉnh sửa thiết lập kịch bản tự động hóa | Chỉ khả dụng với user có quyền chỉnh sửa |
| 1.3 | Nút Xóa | Button | Khi click → hiển thị popup xác nhận xoá kịch bản tự động hóa | Là điều kiện kích hoạt modal |
| 2. Popup thông báo |  |  |  |  |
| 2.1 | Popup Thông báo | Modal | Chỉ hiển thị khi người dùng click “Xóa” | Nội dung: “Bạn chắc chắn muốn xoá?” |
| 2.2 | Nút Quay lại (trong popup) | Button | Đóng popup, không xoá dữ liệu | Không thay đổi dữ liệu |
| 2.3 | Nút Xác nhận (trong popup) | Button | Thực hiện xoá bản ghi kịch bản khỏi hệ thống | Nếu xoá thành công → hiển thị thông báo, refresh danh sách kịch bản tự động hóa |



### 4.5 Ràng buộc hệ thống



| Trường hợp ràng buộc | Mô tả chức năng | Ràng buộc hệ thống | Thông báo hiển thị | Hành động của hệ thống |
| --- | --- | --- | --- | --- |
| 1. Người dùng nhấn nút “Xóa” | Cho phép người dùng chọn thao tác xóa trong danh sách kịch bản. | Bắt buộc hiển thị popup xác nhận trước khi thực hiện. | - | Hiển thị popup “Bạn có chắc chắn muốn xóa kịch bản này?” gồm hai nút Quay lại và Xác nhận. |
| 2. Người dùng chọn “Quay lại” trên popup | Người dùng thay đổi ý định, không muốn xóa. | — | — | Đóng popup, không thay đổi dữ liệu. |
| 3. Người dùng chọn “Xác nhận” | Người dùng xác nhận thực hiện xóa kịch bản. | - Hệ thống kiểm tra lại toàn bộ ràng buộc trên (quyền, trạng thái, liên kết). - Nếu hợp lệ thì xóa. | — | Gọi API DELETE /automation/{id} để xóa kịch bản, cập nhật danh sách. |
| 4. Người dùng không có quyền xóa | Hệ thống kiểm tra quyền thao tác của người dùng trước khi cho phép xóa. | Chỉ người dùng thuộc nhóm Quản trị hệ thống hoặc Quản lý vùng mới có quyền xóa kịch bản. | “Bạn không có quyền thực hiện thao tác này.” | Ngừng thao tác xóa, không hiển thị popup xác nhận. |
| 5. Kịch bản đang ở trạng thái hoạt động (Active) | Kịch bản đang bật, có thể đang chạy tự động hoặc nhận dữ liệu từ AI. | Không cho phép xóa nếu trạng thái = Đang hoạt động. | “Không thể xóa vì kịch bản đang được kích hoạt. Vui lòng tạm dừng trước khi xóa.” | Dừng xử lý, hiển thị cảnh báo và giữ nguyên danh sách. |
| 6. Kịch bản đang liên kết với AI hoặc nhóm khách hàng | Kịch bản có liên kết tới AI hoặc nhóm khách hàng cụ thể trong hệ thống. | Khi người dùng xác nhận xóa, hệ thống tự động gỡ kết nối với AI và nhóm khách hàng | - | Hệ thống thực hiện thao tác gỡ kết nối tới Ai và nhóm người dùng, sau đó thực hiện thao tác xóa. |
| 7. Xóa thành công | Hệ thống đã xóa kịch bản khỏi cơ sở dữ liệu. | — | “Xóa kịch bản thành công.” | - Cập nhật lại danh sách kịch bản. - Ghi log thao tác |
| 8. Ghi log thông tin | Ghi lại các thông tin về người xóa, thời gian xóa của kịch bản được chọn xóa trong hệ thống | Ghi lại các thông tin người xóa, thời gian xóa của kịch bản được chọn xóa. => Gửi thông báo notification “[Tên User] đã xóa thành công [Tên kịch bản]” kèm giờ và ngày. (Phát triển sau, không phải sprint này) | “[Tên User] đã xóa thành công [Tên kịch bản]” HH:MM DD:MM:YYYY | Xóa kịch bản, ghi log, gửi thông báo |



## 5. Bật/Tắt kịch bản tự động hóa



| Tên nghiệp vụ | Bật/tắt kịch bản tự động đã có trong hệ thống |
| --- | --- |
| Module | Menu > Tự động hóa |
| Mô tả | Tính năng cho phép xóa kịch bản đã có trong hệ thống Gapone Conversation. Trigger: On-Off button Người dùng hoàn thành việc bật hoặc tắt kịch bản thành công. Kịch bản được bật sẽ active real-time. Kịch bản được tắt sẽ paused real-time |
| Điều kiện cần để thực hiện hành động | Người dùng được phân quyền Chỉnh sửa của tính năng "Tự động hóa". Truy cập phân quyền người dùng tại mục Cài đặt > Thiết lập người dùng > Phân quyền. Truy cập kịch bản tự động hóa tại Cài đặt > Tự động hóa Quyền chức năng thiết lập người dùng như sau: - Quyền chỉnh sửa: thể hiện người dùng được phép chỉnh sửa kịch bản trong hệ thống. Đồng thời được quyền điều chỉnh trạng thái (bật - tắt) của kịch bản Có kịch bản hợp lệ đã tạo trong hệ thống. |
| Hành động | Người dùng thực hiện theo các bước sau: Bước 1: - Truy cập màn danh sách kịch bản tự động hóa bằng cách nhấp vào biểu tượng Tự động hóa trên menu. Giao diện Tự động hóa sẽ xuất hiện, tab Quản lý kịch bản tự động hóa mặc định hiển thị khi truy cập tính năng Tự động hóa. Bước 2: - Xác định kịch bản cần bật/tắt, nhấp chọn vào biểu tượng menu bật tắt, sau đó điều chỉnh theo nhu cầu |
| Kết quả | Người dùng bật- tắt một kịch bản đã có trong hệ thống thành công khi thỏa mãn các điều kiện. Kịch bản tự động active và paused realtime theo điều chỉnh của người dùng. |



### 5.2 Wireframe


Bảng mô tả trạng thái và ràng buộc:


| STT | Tên thành phần | Trạng thái | Mô tả chi tiết | Ràng buộc hệ thống |
| --- | --- | --- | --- | --- |
| 1 | Công tắc Trạng thái (bật/tắt) | ✅ Bật (ON) – màu xanh | Kịch bản đang hoạt động, hệ thống cho phép tự động gửi tin nhắn, xử lý hành động theo luồng đã cấu hình. | - Khi bật, hệ thống kích hoạt cron job hoặc trigger automation. - Không cho phép bật nếu kịch bản bị lỗi cấu hình hoặc thiếu dữ liệu. - Kịch bản đạt tiêu chuẩn mặc định luôn ở tình trạng được kích hoạt - Tình trạng kích hoạt không ảnh hưởng đến việc thử nghiệm kịch bản, chỉ ảnh hưởng tới cuộc hội thoại thực tế. |
| 2 | Công tắc Trạng thái (bật/tắt) | ⛔ Tắt (OFF) – màu xám | Kịch bản đang ngừng hoạt động, hệ thống không thực hiện bất kỳ tự động hoá nào liên quan đến kịch bản này. | - Khi tắt, hệ thống hủy kích hoạt các trigger và event đang chạy. - Không ảnh hưởng đến dữ liệu lịch sử. |


Use case:


| STT | Tên Use Case | Mô tả ngắn gọn | Tác nhân (Actor) | Tiền điều kiện | Luồng thực hiện chính | Ràng buộc hệ thống | Kết quả mong đợi |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Bật trạng thái kịch bản | Cho phép người dùng kích hoạt kịch bản tự động hoá để hệ thống bắt đầu thực thi. | Người dùng có quyền quản lý kịch bản (Quản trị viên/Người dùng được phân quyền) | - Kịch bản đang ở trạng thái Tắt. - Kịch bản đã cấu hình đầy đủ các điều kiện và hành động. | 1. Người dùng bật công tắc trạng thái. 2. Hệ thống kiểm tra điều kiện hợp lệ. 3. Nếu hợp lệ → Hệ thống chuyển trạng thái sang “Hoạt động”. 4. Gửi thông báo “Kích hoạt thành công”. | - Không cho phép bật nếu kịch bản bị lỗi cấu hình hoặc thiếu dữ liệu. - Phải kiểm tra kết nối API (Zalo, Telegram...) trước khi kích hoạt. | Kịch bản chuyển sang trạng thái “Bật”, hệ thống bắt đầu chạy automation tương ứng. |
| 2 | Tắt trạng thái kịch bản | Cho phép người dùng tạm dừng hoạt động tự động hoá của kịch bản. | Người dùng có quyền quản lý kịch bản | - Kịch bản đang ở trạng thái Bật. | 1. Người dùng tắt công tắc trạng thái. 2. Hệ thống hiển thị thông báo xác nhận. 3. Khi người dùng đồng ý → hệ thống chuyển trạng thái sang “Tắt”. | - Hệ thống hủy kích hoạt các cron job và event liên quan. - Không ảnh hưởng đến lịch sử tin nhắn đã gửi. | Kịch bản ngừng hoạt động, trạng thái hiển thị là “Tắt”. |
| 3 | Kiểm tra trạng thái hiện tại của kịch bản | Hiển thị trạng thái hiện tại (Bật/Tắt) của từng kịch bản trong danh sách. | Người dùng có quyền xem | - | 1. Người dùng mở danh sách kịch bản. 2. Hệ thống hiển thị trạng thái thực tế của từng kịch bản. | - Dữ liệu trạng thái được đồng bộ theo thời gian thực từ backend. | Người dùng nhìn thấy trạng thái chính xác của mỗi kịch bản. |
| 4 | Thông báo lỗi khi bật thất bại | Hệ thống hiển thị cảnh báo khi kịch bản không thể bật. | Người dùng | - Kịch bản chưa hoàn tất cấu hình hoặc kênh bị ngắt kết nối. | 1. Người dùng bật công tắc. 2. Hệ thống kiểm tra lỗi. 3. Nếu phát hiện lỗi → hiện thông báo “Không thể kích hoạt do thiếu dữ liệu hoặc kênh chưa kết nối”. | - Bắt buộc xử lý lỗi phía backend (API connection, missing field...) nếu do hệ thống - Bắt buộc xử lý thiết lập kịch bản (thiếu dữ liệu) nếu do người dùng để trống các trường bắt buộc. | Người dùng biết lý do thất bại và có thể chỉnh sửa cấu hình. |



## 6. Flow đặc biệt


- Kết thúc một flow

- Người dùng can thiệp vào flow

- Người dùng can thiệp vào flow có AI

- Người dùng tạo nhiều kịch bản khác nhau bị trùng điều kiện

- Người dùng tạo một kịch bản bị trùng điều kiện

------------------------------------------------------------------------------------------------------------
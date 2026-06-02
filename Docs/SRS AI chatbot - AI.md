**SRS TÍCH HỢP AI**

**--------------------------------------------------------**


# BẢNG GHI NHẬN THAY ĐỔI TÀI LIỆU



| **Ngày thay đổi** | **Vị trí** | **Lý do** | **Mô tả thay đổi** | **Phiên bản cũ** | **Phiên bản mới** |
| --- | --- | --- | --- | --- | --- |
| 30/09/2025 | Tạo mới |  | V1 |  |  |
| 16/10/2025 | 2. Thêm mới AI vào hệ thống | Tích hợp để loại bỏ bớt màn giao diện | Tích hợp giao diện **Thông tin chung** vào giao diện **Thiết lập AI.** Bỏ bớt **Thử nghiệm AI** ra khỏi flow thiết lập AI. | V1 | V1.0.1 |
|  | 3. Chỉnh sửa thiết lập AI | Tích hợp để loại bỏ bớt màn giao diện | Tích hợp giao diện **Thông tin chung** vào giao diện **Thiết lập AI.** Bỏ bớt **Thử nghiệm AI** ra khỏi flow chỉnh sửa thiết lập AI. |  |  |
|  | 5. Thử nghiệm AI | Tách chức năng thử nghiệm để tối giản hóa quy trình thiết lập | Thử nghiệm AI ở mục **2.Th****êm mới AI** được tách và tạo mới tại phần **5.Th****ử nghiệm AI** |  |  |
| 21/10/2025 | 2. Thêm mới AI vào hệ thống > 2.3 wireframe | Bổ sung ràng buộc chọn cài đặt mở rộng của phần thiết lập AI | Bổ sung phần “Cài đặt khác” (trường hợp AI từ chối trả lời). | V1.0.1 | V1.0.2 |
|  | 4. Xóa AI > Mô tả trường dữ liệu | Bổ sung ràng buộc hệ thống | Bổ sung ràng buộc hệ thống cho những trường hợp xóa AI còn được gán cho kịch bản |  |  |
| 24/10/2025 | 3. Chỉnh sửa AI > Wireframe | Bổ sung 1 bước xác nhận trước khi chỉnh sửa | Người dùng nhấp chọn chỉnh sửa thiết lập AI, hệ thống hiện pop up cảnh báo, người dùng cần nhấn xác nhận để truy cập chức năng chỉnh sửa thiết lập AI | V1.0.2 | V1.0.3 |
| 27/10/2025 | 2. Thêm mới AI vào hệ thống > Wireframe > Model AI | Chỉnh sửa lại việc chọn model AI trong khâu thiết lập AI. | Người dùng nhấp chọn nhà cung cấp AI trong droplist, sau đó nhấp chọn model AI khả dụng do nhà cung cấp đã chọn cung cấp trong droplist tiếp theo | V1.0.3 | V1.0.4 |
| 07/11/2025 | 5. Thử nghiệm AI > 5.3 mô tả trường dữ liệu | Thêm mô tả tên của AI thử nghiệm | Bổ sung mô tả trường dữ liệu tên AIthử nghiệm | V1.0.4 | V1.0.5 |


--------------------------------------------------------


# BẢNG QUẢN LÝ TIẾN ĐỘ THỰC THI



| **Giai đoạn** | **Ngày bắt đầu** | **Phần mục** | **Phiên bản áp dụng ** |
| --- | --- | --- | --- |
| Quý 4/2025 |  |  | V1.03 |


--------------------------------------------------------


# Bảng tài liệu bổ sung từ nền tảng khác



| **STT** | **Tài liệu** |
| --- | --- |
| 1 | - Figma |
| 2 |  |



# MỤC LỤC



## 1. Xem danh sách AI được tích hợp vào hệ thống



### 1.1. Mô tả chức năng



| **Tên nghiệp vụ** | Xem danh sách các AI được tích hợp vào hệ thống |
| --- | --- |
| **Module** | Menu > Cài đặt > Thiết lập AI |
| **Mô tả** | Tính năng cho phép xem danh sách những AI đã được tích hợp vào hệ thống Danh sách quản lý kết nối AI, tên chính thức: “**Quản lý AI**”, dựa theo thông tin cột bao gồm: + Tên AI - agent: thể hiện AI được kết nối vào hệ thống + Model: Thể hiện phiên bản AI được kết nối vào hệ thống + Ngày tạo: thể hiện ngày kết nối AI này lần đầu + Ngày cập nhật: thể hiện ngày chỉnh sửa gần nhất thông tin AI này + Cột thao tác hiển thị icon thể hiện thao tác chọn hành động chỉnh sửa hoặc xoá |
| **Điều kiện cần để thực hiện hành động** | Người dùng được phân quyền Xem của chức năng "Thiết lập AI". Truy cập phân quyền người dùng tại mục Cài đặt > Thiết lập người dùng > Phân quyền. Truy cập thiết lập AI tại Cài đặt > Thiết lập AI Quyền chức năng thiết lập người dùng như sau: - Quyền xem: thể hiện người dùng được phép xem toàn bộ danh sách AI kết nối - *Quyền tạo mới: thể hiện người dùng được phép tạo/thêm mới AI vào hệ thống* - *Quyền chỉnh sửa: thể hiện người dùng được phép chỉnh sửa thông tin AI đã kết nối* - *Quyền xoá: thể hiện người dùng được thực hiện xoá AI đã được kết nối* |
| **Hành động** | Người dùng thực hiện theo các bước sau: **Bước 1:** Truy cập màn danh sách quản lý thiết lập AI tại mục Cài đặt > Thiết lập AI Giao diện **Quản lý A**I sẽ hiển thị. Giao diện sẽ bao gồm thanh tìm kiếm, nút “+ Thêm AI”, bảng danh sách các AI đã kết nối (bao gồm cả menu thao tác ẩn) |
| **Kết quả** | Người dùng truy cập Xem được danh sách quản lý thiết lập AI, tạo tiền đề cho việc thực hiện thao tác Tạo mới, Chỉnh sửa, Xoá theo đúng với quyền người dùng đã được thiết lập. |



### 1.2 Wireframe


*Lưu ý: Wireframe minh họa các trường dữ liệu và các ô dữ liệu, không đóng vai trò quyết định thiết kế giao diện thực sự. Thiết kế vẫn theo mẫu template hiện có trên server Product.*

- Wireframe Quản lý AI tổng quan

- Wireframe Quản lý AI > menu ẩn


### 1.3 Mô tả trường dữ liệu



| **STT** | **Tên Trường** | **Kiểu Dữ Liệu** | **Mô tả** | **Ràng Buộc/Quy Tắc** |
| --- | --- | --- | --- | --- |
| 1 | ID AI (Ẩn) | INT (PK, Auto) | Mã định danh duy nhất của AI trong hệ thống. | Khóa chính, tự động tăng, không trùng lặp |
| 2 | Tên AI | VARCHAR(255) | Tên hiển thị của trợ lý AI (ví dụ: GapOne Chatbot). | Bắt buộc, không được trùng trong cùng ORG |
| 3 | Phân loại | VARCHAR(50) | Loại mô hình AI được tích hợp (GPT-4.1-mini, GPT o3, Grok 5, …) hay Agent | Bắt buộc. Đối với AI Model, hiển thị tên của model. Đối với AI Agent, hiển thị “**AI Agent”** |
| 4 | Số kịch bản | NUMBER | Số kịch bản tự động một AI được gán vào | Bắt buộc. Nếu không có kịch bản được gán vào, hiện 0. Nếu có kịch bản được gán vào, count số kịch bản, hiện tổng số kịch bản AI được gán, đồng thời hiện tên của những kịch bản được gán khi di chuột vào số đó. |
| 5 | Ngày tạo | DATETIME | Thời điểm hệ thống ghi nhận tạo mới AI. | Tự động sinh khi thêm mới, không cho phép chỉnh sửa |
| 6 | Ngày cập nhật | DATETIME | Thời điểm cập nhật gần nhất. | Tự động cập nhật khi chỉnh sửa thông tin AI |
| 7 | Người quản lý | VARCHAR(100) | Người dùng quản lý AI (ví dụ: Trần Tuấn Nam – Quản lý vùng). | Liên kết với tài khoản người dùng hệ thống (FK → User.ID) |
| 8 | Thao tác (Hiển thị dưới dạng menu ẩn) | ENUM | Các chức năng có thể thực hiện trên mỗi AI. | Giá trị hợp lệ: {Thử nghiệm, Chỉnh sửa, Xóa} |



#### Ràng buộc hệ thống:


- Tìm kiếm: Ô tìm kiếm theo tên AI, theo model AI. Cho phép tìm kiếm không dấu ra kết quả tương ứng

- Nút “ **+ Thêm AI**”: Trigger cho tính năng tạo mới, thêm mới AI vào hệ thống.


### 1.4 Use case



| **Usecase ID** | **Tên Use Case** | **Tác nhân chính** | **Mô tả** | **Điều kiện đầu vào** | **Kết quả mong muốn** |
| --- | --- | --- | --- | --- | --- |
| UC1.01 | Xem danh sách AI | Người dùng | Người dùng truy cập **Cài dặt >** **Thiết lập AI** để mở giao diện **Quản lý AI **xem toàn bộ danh sách AI đã tạo. | Người dùng đã đăng nhập, có quyền truy cập vào mục **Cài đặt > Thiết lập AI**. | Hệ thống hiển thị danh sách AI (STT, Tên AI, Model, Ngày tạo, Ngày cập nhật). |
| UC1.01.1 | User xem danh sách AI không có quyền | Người dùng | Người dùng truy cập **Cài dặt >** **Thiết lập AI** để mở giao diện **Quản lý AI **xem toàn bộ danh sách AI đã tạo nhưng chưa được phân quyền | Người dùng đã đăng nhập, chưa được hoặc không được quản trị viên phân quyền xem danh sách và các thiết lập AI | Toàn bộ giao diện** danh sách AI **và nút Thêm AI  được ẩn. Hiện text: “Hiện bạn chưa có quyền xem “Danh sách Ai”, vui lòng liên hệ quản trị viên để được phân quyền. |
| UC1.02 | Tìm kiếm AI => Có kết quả | Người dùng | Người dùng nhập tên AI vào ô tìm kiếm để lọc danh sách. Hệ thống tìm thấy | Có ít nhất một AI đã được tạo trong hệ thống. | Hệ thống trả về danh sách AI khớp với từ khóa tìm kiếm. |
| UC1.02.1 | Tìm kiếm AI => Không có kết quả | Người dùng | Người dùng nhập tên AI vào ô tìm kiếm để lọc danh sách. Hệ thống không tìm thấy | Có ít nhất một AI đã được tạo trong hệ thống. | Hệ thống trả về danh sách trống kèm mô tả “Không tìm thấy kết quả tương ứng. Vui lòng thử lại từ khóa khác” |
| UC1.03 | Thêm mới AI (Có quyền) | Người dùng | Người dùng nhấn nút **+ Thêm AI** để tạo mới một AI. | Người dùng có quyền tạo mới AI. | Hệ thống mở form nhập thông tin AI, lưu AI mới và hiển thị trong danh sách. (Tính năng thêm mới AI vào hệ thống) |
| UC1.03.1 | Thêm mới AI (Không có quyền) | Người dùng | Người dùng nhấn nút **+ Thêm AI** để tạo mới một AI. | Người dùng không có quyền tạo mới AI. | Nút **+ Thêm AI** màu xám, khi người dùng click vô thì hiện thông báo màu cam ở góc trên bên phải màn hình: *“Nhắc nhở: Bạn chưa được cấp quyền thêm mới AI vào hệ thống. Vui lòng liên hệ Quản trị viên của doanh nghiệp để được cấp quyền.”* |
| UC1.04 | Thử nghiệm AI | Người dùng | Người dùng chọn menu **Thử nghiệm** từ dấu ba chấm (…) trên 1 AI. | AI đã tồn tại trong hệ thống. | Hệ thống mở giao diện cho phép người dùng test thử phản hồi AI. |
| UC1.05 | Chỉnh sửa AI(có quyền) | Người dùng | Người dùng chọn **Chỉnh sửa** trong menu để cập nhật thông tin AI. | AI đã tồn tại; Người dùng có quyền chỉnh sửa. | Hệ thống mở form chỉnh sửa, lưu thay đổi và cập nhật cột **Ngày cập nhật**. |
| UC1.05.1 | Chỉnh sửa AI (không có quyền) | Người dùng | Người dùng muốn chọn **Chỉnh sửa** trong menu để cập nhật thông tin AI. | AI đã tồn tại; Người dùng không có quyền chỉnh sửa. | Hệ thống không hiện “**chỉnh sửa**” để người dùng không click chọn được. Chỉ hiển thị **Xem**, **Thử nghiệm**. |
| UC1.06 | Xóa AI (Có quyền) | Người dùng | Người dùng chọn **Xóa** tỏng menu để loại bỏ AI khỏi danh sách. | AI tồn tại; Không nằm trong trạng thái bị ràng buộc hoặc sử dụng. Người dùng có quyền xóa | Hệ thống yêu cầu xác nhận Xác nhận → Hiện thống báo: Xóa AI thành công khỏi hệ thống. |
| UC1.06.1 | Xóa AI (không có quyền) | Người dùng | Người dùng muốn chọn **Xóa** trong menu để loại bỏ AI khỏi danh sách. | AI tồn tại; Không nằm trong trạng thái bị ràng buộc hoặc sử dụng. Người dùng không có quyền xóa | Hệ thống không hiện “**xóa**” để người dùng không click chọn được. Chỉ hiển thị **Xem**, **Thử nghiệm**. |



## **2. Thêm mới AI vào hệ thống**



### 2.1 Mô tả chức năng



| **Tên nghiệp vụ** | Thêm mới AI vào hệ thống Gapone Conversation |
| --- | --- |
| **Module** | Menu > Cài đặt > Thiết lập AI |
| **Mô tả** | Tính năng cho phép tích hợp mới (Tạo mới AI) vào hệ thống Gapone Conversation. Trigger: Nút “+ Thêm AI” - Thiết lập bao gồm: Đặt tên, mô tả AI, chọn model, nhập Mã kết nối, cài đặt Prompt, cài đặt Kho kiến thức, cài đặt mức độ mở rộng và cài đặt khác của AI Người dùng hoàn thành việc điền các trường dữ liệu thiết lập,sau đó bấm **Lưu** để hoàn tất thiết lập thêm mới một AI vào hệ thống. AI được thêm thành công sẽ hiển thị ở bảng danh sách AI tại giao diện **Quản lý AI. ** |
| **Điều kiện cần để thực hiện hành động** | Người dùng được phân quyền **Tạo mới** của chức năng "Thiết lập AI". Truy cập phân quyền người dùng tại mục Cài đặt > Thiết lập người dùng > Phân quyền. Truy cập thiết lập AI tại Cài đặt > Thiết lập AI Quyền chức năng thiết lập người dùng như sau: - Quyền tạo mới: thể hiện người dùng được phép tạo/thêm mới AI vào hệ thống Người dùng có AI hợp lệ và an toàn để tích hợp vào hệ thống. |
| **Hành động** | Người dùng thực hiện theo các bước sau: - Bước 1: Sau khi đăng nhập vào hệ thống, nhấp chọn “**Cài đặt**” trong thanh menu, sau đó click chọn “**Thiết lập AI**” trong sub menu của **Cài đặt**, giao diện **Quản lý AI **sẽ xuất hiện. - Bước 2: Để thực hiện thêm mới AI vào hệ thống, nhấp chọn nút “**+ Thêm AI**” trong màn giao diện **Quản lý AI**. Giao diện **Chi tiết thiết lập AI** sẽ hiển thị với các trường dữ liệu trống (Khác với **Chỉnh sửa AI**, giao diện **Chi tiết thiết lập AI** sẽ hiển thị với các trường dữ liệu đã có thông tin từ lần lưu cuối cùng). - Bước 3: Hoàn thành các trường dữ liệu Nhập tên AI: Người dùng tự đặt tên cho AI trong hệ thống Mô tả AI: Mô tả mục tiêu, mục đích hoặc ghi chú AI Ảnh đại diện: Tải ảnh hoặc kéo thả vào khung. (nếu không có ảnh Model: Chọn model AI Mã kết nối: Nhập Mã kết nối AI Prompt: Điền prompt vận hành AI Kho kiến thức: Tải lên hoặc nhập URL các tài liệu kiến thức Mức độ mở rộng: chọn mức độ AI trả lời các câu hỏi trực tiếp hay cung cấp thêm các thông tin bên lề. Cài đặt khác: Trường hợp từ chối trả lời: Chọn trường hợp AI từ chối trả lời. Khi các trường hợp này được kích hoạt, sẽ sinh event và tự động chuyển cuộc hội thoại đến người dùng để xử lý. Lưu tất cả các thiết lập ở bước này để hệ thống nhận diện AI và đưa AI vào sử dụng - Bước 5: Thử nghiệm Khung hội thoại cho phép chat thử nghiệm với AI sau khi AI lưu vào hệ thống. Nếu phát sinh những phản hồi không mong đợi, người dùng có thể nhấn nút **Quay lại chỉnh sửa** để chỉnh sửa các thiết lập AI. |
| **Kết quả** | Người dùng thêm mới một AI vào hệ thống thành công khi thỏa mãn các điều kiện |



### 2.2 Flow


**Các bước của người dùng:**

Bước 1: Đăng nhập vào hệ thống, truy cập **Cài đặt** sau đó nhấp chọn **Thiết lập AI** để mở giao diện ** Quản lý AI**

Bước 2:  Để thực hiện thêm mới AI vào hệ thống, nhấp chọn nút “**+ Thêm AI**” trong màn giao diện **Quản lý AI**.

Bước 3: Hoàn thành **Thiết lập**

- Nhập tên AI: Người dùng tự đặt tên cho AI trong hệ thống

- Mô tả AI: Mô tả mục tiêu, mục đích hoặc ghi chú AI

- Model: Chọn model AI

- Mã kết nối: Nhập Mã kết nối AI

- Prompt: Điền prompt vận hành AI

- Kho kiến thức: Tải lên hoặc nhập URL các tài liệu kiến thức

- Mức độ mở rộng: chọn mức độ AI trả lời các câu hỏi trực tiếp hay cung cấp thêm các thông tin bên lề.

- Cài đặt khác: Trường hợp từ chối trả lời: Chọn trường hợp AI từ chối trả lời. Khi các trường hợp này được kích hoạt, sẽ sinh event và tự động chuyển cuộc hội thoại đến người dùng để xử lý.

Lưu tất cả các thiết lập ở bước này để hệ thống nhận diện AI và đưa AI vào sử dụng

Đồng thời thông tin về AI sẽ xuất hiện ở **Bảng danh sách AI** trong giao diện **Quản lý AI**

**Các bước của hệ thống:**

- Bước 1: Mở các giao diện và cho phép thiết lập thêm mới AI

- Bước 2: Lưu các thiết lập

- Bước 3: Call API kết nối đến AI

- Thành công: Lưu vào hệ thống và hiển thị AI vừa được thiết lập mới ở **Bảng danh sách AI** trong giao diện **Quản lý AI**

- Thất bại: Hiển thị thông báo lỗi, đồng thời quay lại giao diện **Thiết lập** để người dùng kiểm tra lại các thông tin thiết lập.

*Thông báo lỗi sẽ được mô tả ở phần các trường thông tin và ràng buộc.*


### 2.3 Wireframe


*Lưu ý: Wireframe minh họa các trường dữ liệu và các ô dữ liệu, không đóng vai trò quyết định thiết kế giao diện thực sự. Thiết kế vẫn theo mẫu template hiện có trên server Product.*

Wireframe Thiết lập AI > Chọn model AI

Wireframe Thiết lập AI > chọn kiến thức


#### Mô tả trường dữ liệu Thiết lập AI:



| **STT** | **Tên Trường** | **Kiểu Dữ Liệu** | **Mô tả** | **Ràng buộc / Quy tắc** |
| --- | --- | --- | --- | --- |
| 1 | Tên AI | VARCHAR(255) | Đặt tên cho AI | - Không để trống - Độ dài tối thiểu: 1 ký tự - Độ dài tối đa: 255 ký tự - Không chứa ký tự đặc biệt không hợp lệ ( . , ; : “ ‘ { [ ] } = - ) ( * ! @ # $ % ^ & ~ `) |
| 2 | Mô tả AI | TEXT | Nhập mô tả mục đích, mục tiêu, hoặc ghi chú về AI | - Có thể để trống - Độ dài tối đa 2000 ký tự |
| 2. Model Trường bắt buộc, không được để trống. Bao gồm 2 trường dữ liệu phụ thuộc đều không thể bỏ trống. |  |  |  |  |
| 2.1 | Chọn nhà cung cấp AI | DROPDOWN LIST | Danh sách các nhà cung cấp AI khả dụng có thể tích hợp vào hệ thống | - Chỉ được chọn 1 nhà cung cấp - Bắt buộc không được trống. - Nếu để trống, khi lưu, hệ thống hiện thông báo dưới trường dữ liệu “Bạn chưa chọn nhà cung cấp AIl” - Có scroll nếu danh sách dài |
| 2.1 | Chọn Model AI | DROPDOWN LIST | Danh sách các model AI khả dụng có thể tích hợp vào hệ thống do nhà cung cấp đã chọn cung cấp. | - Chỉ khả dụng sau khi đã hoàn thành trường “Chọn nhà cung cấp AI” - Chỉ được chọn 1 model AI - Bắt buộc không được trống. - Nếu để trống, khi lưu, hệ thống hiện thông báo dưới trường dữ liệu “Bạn chưa chọn Model AI” - Có scroll nếu danh sách dài. |
| 3 | Mã kết nối AI | TEXT | Mã mã kết nối để xác thực kết nối AI. Giai đoạn 1: là mã kết nối với AI Giai đoạn 2 có thể cải tiến kết nối bằng giao thức **OAuth2** hoặc **SSO** | - Bắt buộc nhập, không để trống. - Nhập hợp lệ API key - mã kết nối do nhà cung cấp cung cấp. Nếu sai, hệ thống từ chối lưu và hiện cảnh báo dưới trường “**Mã kết nối**”: Mã kết nối không hợp lệ - Không được nhập trùng nếu chọn cùng model AI. Nếu trùng, hệ thống từ chối lưu và hiện cảnh báo dưới trường “**Mã kết nối**”: Mã kết nối đến model bạn chọn đã tồn tại |
| 4 | Prompt | TEXT | Nội dung hướng dẫn chi tiết hành vi AI | **Bắt buộc nhập**, độ dài khuyến nghị ≤ 2000 ký tự. Không chứa Script hoặc mã độc |
| 5 | Kho kiến thức | Dropdown List | Tập tài liệu, dữ liệu huấn luyện bổ sung cho AI. | **Tùy chọn**, người dùng có thể chọn tài liệu hoặc nhóm tài liệu từ tính năng **Kho kiến thức**. Khi hoàn tất lựa chọn tài liệu cần đưa cho AI, tài liệu đó sẽ được đẩy vào **Danh sách tài liệu của AI đó**. |
| 6. Danh sách tài liệu bao gồm: Ràng buộc giới hạn tài liệu: Thử 2 options: - 1. Số tài liệu trong kho kiến thức không vượt quá 10 tài liệu, mỗi tài liệu không quá 20MB - 2. Số tài liệu trong kho kiến thức không vượt quá 50 tài liệu, mỗi tài liệu không quá 20MB |  |  |  |  |
| 6.1 | Tên tài liệu | VARCHAR(255) | Tên hiển thị của tài liệu trong danh sách | **Bắt buộc**, không được trùng trong cùng 1 AI |
| 6.2 | Loại tài liệu | ENUM (Word, Excel, PDF, Link) | Định dạng loại file/nguồn tài liệu Nếu là file, không quá 20Mb | **Bắt buộc**, chọn từ danh sách có sẵn |
| 6.3 | Ngày tạo tài liệu | DATE (dd/MM/yyyy) | Ngày hệ thống ghi nhận file/link được thêm | **Tự động sinh**, không cho chỉnh sửa |
| 6.4 | Tên tài liệu dạng up URL | VARCHAR(255) | Tên tài liệu (nếu loại là link và có tên). Khi nhấp chuột vào có thể mở link dẫn tới tài liệu đó. Nếu loại là link và không có tên thì hiện URL ở phần **Tên tài liệu** | **Bắt buộc nếu loại tài liệu = Link**, phải đúng định dạng URL |
| 5 | Mức độ mở rộng | INT (0–100) | Tỷ lệ % mức mở rộng khả năng trả lời của AI | **Mặc định = 20%**, giá trị trong khoảng từ **0 → 100** Chọn theo các mốc được chia sẵn. |
| 6 | Cài đặt khác | BOOLEAN[] (multi-select) | Các tùy chọn bổ sung để AI xử lý tình huống | Option tiên quyết: “Kích hoạt trường hợp AI từ chối trả lời” Options con: - Không tìm thấy thông tin chính xác - Phát hiện nội dung rủi ro/dữ liệu sai - Phát hiện khách hàng yêu cầu tư vấn sâu Nếu chọn option tiên quyết, mặc định hiển thị chọn hết tất cả options con. Người dùng nhấp chọn vào ô checkbox để loại các options họ thấy không cần thiết. Nếu loại bỏ hết tất cả ô checkbox, tự động chuyển trạng thái ô checkbox của option tiên quyết về trống. |
| 7 | Nút “Hủy” | Action | Hủy bỏ thao tác thiết lập và quay lại màn hình trước | Không lưu dữ liệu đã nhập. Hiện Popup cảnh báo: “Bạn chắc chắn muốn hủy? Mọi thiết lập cũ sẽ không được lưu”, nhấp chọn “**Xác nhận**” để xác nhận hủy, nhấp chọn “**Quay lại”** để hủy bỏ thao tác **Hủy** |
| 8 | Nút “Lưu” | Action | Lưu cấu hình thiết lập AI | **Bắt buộc kiểm tra hợp lệ dữ liệu** trước khi lưu. |


**Ràng buộc hệ thống:**


| **Nhóm ràng buộc hệ thống** | **Mô tả chi tiết** |
| --- | --- |
| **Xác thực & bảo mật** | - Trường **Mã kết nối AI** bắt buộc hợp lệ để hệ thống có thể kết nối.- Không cho phép lưu nếu thiếu Mã kết nối hoặc Model. - Mã kết nối phải được mã hóa khi lưu trữ. |
| **Toàn vẹn dữ liệu** | - Không cho phép trùng lặp tên tài liệu trong danh sách. - Chỉ chấp nhận file đúng định dạng (Word, Excel, PDF) hoặc URL hợp lệ. - Nếu file tải lên hỏng hoặc URL không truy cập được → báo lỗi. |
| **Quy tắc nhập liệu** | - Trường **Prompt** phải nằm trong giới hạn ký tự, không được chứa mã HTML/script. - Các trường text (Model, Mã kết nối AI) không được nhập ký tự đặc biệt trái phép. |
| **Điều kiện lưu tất cả thiết lập** | - Phải có ít nhất 1 giá trị hợp lệ trong các trường bắt buộc (**Model**, **Mã kết nối AI**, **Prompt**). - Nếu người dùng không chọn kho kiến thức, hệ thống vẫn cho lưu nhưng AI sẽ hoạt động với Prompt mặc định. |
| **Mức độ mở rộng (slider)** | - Giới hạn từ 0% → 100% theo 5 mốc. Ghi nhận mốc gần nhất người dùng click chọn. |
| **Xử lý lỗi & thông báo** | - Nếu thiếu thông tin bắt buộc → hiện thông báo lỗi ngay tại trường nhập.- Khi upload tài liệu lỗi hoặc không đúng định dạng → cảnh báo và không thêm vào danh sách. |
| **Tương tác người dùng** | - Nút **Lưu** chỉ được bật khi toàn bộ trường bắt buộc hợp lệ.- Nút **Hủy** thoát form mà không lưu dữ liệu |
| **Lưu lỗi do vấn đề bên ngoài hệ thống** | - Những trường hợp nhập sai Mã kết nối AI nên kết nối thất bại, sẽ hiện cửa sổ thông báo, đồng thời quay trở lại giao diện thiết lập để người dùng cập nhật lại Mã kết nối AI. |
| **Ngăn chặn trùng AI** | - Check trùng dựa theo quy tắc: (model AI + API key) không được trùng nhau. Model AI có thể trùng khi và chỉ khi API key không trùng, API key có thể trùng khi và chỉ khi Model AI không trùng, nếu cả 2 đều trùng => Hệ thống từ chối kết nối. |



#### Mô tả trường dữ liệu và ràng buộc bổ sung cho Kho kiến thức:



| **STT** | **Tên trường** | **Kiểu dữ liệu** | **Mô tả chức năng** | **Ràng buộc / Ghi chú** |
| --- | --- | --- | --- | --- |
| 1 | **Chọn tài liệu & nhóm tài liệu** | Button | Nhấp vào để hiện màn phụ và dropdown list chọn tài liệu và nhóm tài liệu |  |
| 2 | **Tìm kiếm tài liệu & nhóm tài liệu** | Textbox (input) | Cho phép người dùng nhập từ khóa để tìm kiếm tài liệu hoặc nhóm tài liệu trong danh sách | Không bắt buộc nhập; lọc danh sách động theo từ khóa |
| 3 | **Chọn tất cả** | Checkbox | Cho phép người dùng tick để chọn toàn bộ tài liệu trong danh sách | Pending. Hiện tại chưa cho phép chọn tất cả vì chờ xác nhận lại giới hạn số lượng tài liệu. |
| 4 | **Danh sách tài liệu** | List / Table | Hiển thị danh sách tài liệu hoặc nhóm tài liệu trong kho để lựa chọn | Dữ liệu được lấy từ “Kho kiến thức” đã upload sẵn trong hệ thống. Upload theo thứ tự nhóm kiến thức lên đầu (sắp xếp theo bảng chữ cái), sau đó tới tất cả các tài liệu. (sắp xếp theo bảng chữ cái) Nếu tài liệu có trong nhóm kiến thức đã được chọn, auto bị ẩn khỏi danh sách chọn. |
| 5 | **Tài liệu (từng dòng)** | Checkbox + Label | Mỗi dòng thể hiện 1 tài liệu cụ thể (VD: “Mô tả chức năng GapOne”, “Tổng quan về GapOne”, “Hướng dẫn sử dụng kênh”…). Người dùng có thể tick để chọn tài liệu đó. | Có thể chọn nhiều tài liệu cùng lúc. |
| 6 | **Biểu tượng thu gọn / mở rộng danh sách (▲)** | Icon / Button | Cho phép thu gọn hoặc mở rộng phần danh sách tài liệu để tối ưu không gian hiển thị | Không có ràng buộc; chỉ ảnh hưởng giao diện người dùng |


Ràng buộc bổ sung:


| **STT** | **Ràng buộc** | **Mô tả chi tiết** |
| --- | --- | --- |
| 1 | Tài liệu hiển thị theo nhóm đã tồn tại | Danh sách chỉ hiển thị tài liệu thuộc nhóm được định nghĩa trước trong “Kho kiến thức”. |
| 2 | Chức năng “Chọn tất cả” có tác dụng toàn phần | Pending. Khi tick “Chọn tất cả” → tất cả checkbox trong danh sách được chọn; khi bỏ tick → toàn bộ bỏ chọn. |
| 3 | Tìm kiếm theo từ khóa | Khi người dùng nhập từ khóa, danh sách lọc theo tên tài liệu hoặc nhóm tài liệu có chứa chuỗi ký tự đó. |
| 4 | Dữ liệu đồng bộ với hệ thống “Kho kiến thức” | Khi tài liệu bị xóa khỏi “Kho kiến thức”, danh sách ở đây tự động cập nhật (ẩn hoặc loại bỏ tài liệu đó). |
| 5 | Lược bỏ tài liệu trùng lặp | Trong nhóm kiến thức được chọn có thể bị lặp tài liệu, loại bỏ các tài liệu trùng lặp đó. Op2: Thay đổi ràng buộc từ tính năng **Kho kiến thức**, chỉ cho mỗi tài liệu thuộc 1 nhóm kiến thức. |



#### Mô tả bổ sung cho Cài đặt mức độ mở rộng:



| **Mức độ** | **Mô tả** | **Mô tả ví dụ** |
| --- | --- | --- |
| 0% | Mức độ mở rộng thấp nhất Ai không trả lời lan man, vào thẳng trực tiếp vấn đề | Hỏi: “Gapit cung cấp dịch vụ gì?” Trả lời: “Gapit cung cấp dịch vụ: - Mobile Marketing / Messaging Platform - MarTech / Giải pháp Công nghệ Marketing - CPaaS (Communication Platform as a Service)” Anh/chị còn cần [AccountName] hỗ trợ tư vấn thêm gì không ạ? |
| 20% | Mức độ mở rộng rất ít AI trả lời trực tiếp vấn đề, có cung cấp thêm ít thông tin quan trọng | Hỏi: “Gapit cung cấp dịch vụ gì?” Trả lời: “Dịch vụ của công ty cổ phần Gapit bao gồm: - **Mobile Marketing / Messaging Platform**SMS Brandname, MMS, A2P SMS, Viber Business Messaging, … Kèm thêm hỗ trợ lên chiến dịch gửi tin nhắn tự động qua nền tảng Gapone - **MarTech / Giải pháp Công nghệ Marketing** CRM & Marketing Automation, HubSpot để triển khai cho doanh nghiệp Việt Nam. - **CPaaS (Communication Platform as a Service)** Nền tảng giao tiếp (messaging, gửi thông báo, chăm sóc khách hàng…) dưới dạng dịch vụ. Anh/chị còn cần [AccountName] hỗ trợ tư vấn thêm gì không ạ? |
| 40% | Mức độ mở rộng ít AI trả lời trực tiếp vấn đề, cung cấp thêm thông tin quan trọng | Hỏi: “Gapit cung cấp dịch vụ gì?” Trả lời: “Dịch vụ của công ty cổ phần Gapit bao gồm: - **Mobile Marketing / Messaging Platform**SMS Brandname, MMS, A2P SMS, Viber Business Messaging, Zalo ZNS, WhatsApp Business API, RCS. Kèm thêm hỗ trợ lên chiến dịch gửi tin nhắn tự động qua nền tảng Gapone - **MarTech / Giải pháp Công nghệ Marketing** CRM & Marketing Automation như HubSpot để triển khai cho doanh nghiệp Việt Nam: tư vấn, onboarding, đào tạo, tích hợp hệ thống - **CPaaS (Communication Platform as a Service)** Nền tảng giao tiếp (messaging, gửi thông báo, chăm sóc khách hàng…) dưới dạng dịch vụ. Anh/chị còn cần [AccountName] hỗ trợ tư vấn thêm gì không ạ? |
| 60% | Mức độ mở rộng nhiều hơn Ai cung cấp thêm nhiều thông tin khác để gợi ý khai thác thêm nhu cầu của khách. Có thể thu thập thông tin từ bên ngoài kho kiến thức được thiết lập để trả lời câu hỏi của khách nhưng không nhiều | Hỏi: “Gapit cung cấp dịch vụ gì?” Trả lời: “Dịch vụ của công ty cổ phần Gapit bao gồm: - **Mobile Marketing / Messaging Platform**GAPIT cung cấp hệ sinh thái gửi tin nhắn qua nhiều kênh như: SMS Brandname, MMS, A2P SMS, Viber Business Messaging, Zalo ZNS, WhatsApp Business API, RCS. Hỗ trợ doanh nghiệp lập kịch bản tự động, tích hợp với hệ thống Marketing Automation. - **MarTech / Giải pháp Công nghệ Marketing** GAPIT cung cấp giải pháp toàn diện MarTech, giúp doanh nghiệp tối ưu hóa các hoạt động marketing đa kênh Hợp tác với nền tảng CRM & Marketing Automation như HubSpot để triển khai cho doanh nghiệp Việt Nam: tư vấn, onboarding, đào tạo, tích hợp hệ thống. - **CPaaS (Communication Platform as a Service)** Nền tảng giao tiếp (messaging, gửi thông báo, chăm sóc khách hàng…) dưới dạng dịch vụ. GAPIT là một trong những nhà cung cấp CPaaS uy tín nhất tại Việt Nam. Anh/chị còn cần [AccountName] hỗ trợ tư vấn thêm gì không ạ? |
| 80% | Mức độ mở rộng nhiều AI cung cấp nhiều thông tin hơn, bao gồm cả thông tin để trả lời câu hỏi và thông tin gợi ý khai thác nhu cầu. Mức độ thu thập thông tin từ bên ngoài kho kiến thức được thiết lập để trả lời câu hỏi của khách nhiều hơn | Hỏi: “Gapit cung cấp dịch vụ gì?” Trả lời: “Dịch vụ của công ty cổ phần Gapit bao gồm: - **Mobile Marketing / Messaging Platform**GAPIT cung cấp hệ sinh thái gửi tin nhắn qua nhiều kênh như: SMS Brandname, MMS, A2P SMS, Viber Business Messaging, Zalo ZNS, WhatsApp Business API, RCS. Hỗ trợ doanh nghiệp lập kịch bản tự động, tích hợp với hệ thống Marketing Automation. - **MarTech / Giải pháp Công nghệ Marketing** GAPIT cung cấp giải pháp toàn diện MarTech, giúp doanh nghiệp tối ưu hóa các hoạt động marketing đa kênh Hợp tác với nền tảng CRM & Marketing Automation như HubSpot để triển khai cho doanh nghiệp Việt Nam: tư vấn, onboarding, đào tạo, tích hợp hệ thống. - **CPaaS (Communication Platform as a Service)** Nền tảng giao tiếp (messaging, gửi thông báo, chăm sóc khách hàng…) dưới dạng dịch vụ. GAPIT là một trong những nhà cung cấp CPaaS uy tín nhất tại Việt Nam Gapit là đối tác “Platinum” duy nhất của HubSpot tại Việt Nam – đặc biệt trong việc triển khai CRM + Marketing Automation. Cùng với hệ thống kết nối với các mạng viễn thông lớn tại Việt Nam để hỗ trợ dịch vụ SMS/MMS: Viettel, Mobifone, Vinaphone, Vietnamobile, Gmobile. Gapit tin rằng mình có thể đồng hành hỗ trợ và giúp đỡ cho các doanh nghiệp trong việc thực thi CRM và tìm ra các giải pháp martech hiệu quả. Anh/chị còn cần [AccountName] hỗ trợ tư vấn thêm gì không ạ? |
| 100% | Mức độ mở rộng lớn nhất. AI cung cấp nhiều thông tin hơn, bao gồm cả thông tin để trả lời câu hỏi và thông tin gợi ý khai thác nhu cầu. Mức độ thu thập thông tin từ bên ngoài kho kiến thức được thiết lập để trả lời câu hỏi của khách lớn nhất. | Hỏi: “Gapit cung cấp dịch vụ gì?” Trả lời: “Dịch vụ của công ty cổ phần Gapit bao gồm: **Mobile Marketing / Messaging Platform**GAPIT cung cấp hệ sinh thái gửi tin nhắn qua nhiều kênh như: SMS Brandname, MMS, A2P SMS, Viber Business Messaging, Zalo ZNS, WhatsApp Business API, RCS. Hỗ trợ doanh nghiệp lập kịch bản tự động, tích hợp với hệ thống Marketing Automation. **MarTech / Giải pháp Công nghệ Marketing** GAPIT cung cấp giải pháp toàn diện MarTech, giúp doanh nghiệp tối ưu hóa các hoạt động marketing đa kênh Hợp tác với nền tảng CRM & Marketing Automation như HubSpot để triển khai cho doanh nghiệp Việt Nam: tư vấn, onboarding, đào tạo, tích hợp hệ thống. **CPaaS (Communication Platform as a Service)** Nền tảng giao tiếp (messaging, gửi thông báo, chăm sóc khách hàng…) dưới dạng dịch vụ. GAPIT là một trong những nhà cung cấp CPaaS uy tín nhất tại Việt Nam GAPIT đã phục vụ **10 000+ khách hàng đối tác** và có hơn **30 000 dự án hoàn thành**. Gapit là đối tác “Platinum” (Bạch kim) duy nhất của HubSpot tại Việt Nam – đặc biệt trong việc triển khai CRM + Marketing Automation. Cùng với hệ thống kết nối với các mạng viễn thông lớn tại Việt Nam để hỗ trợ dịch vụ SMS/MMS: Viettel, Mobifone, Vinaphone, Vietnamobile, Gmobile. Gapit tin rằng mình có thể đồng hành hỗ trợ và giúp đỡ cho các doanh nghiệp trong việc thực thi CRM và tìm ra các giải pháp martech hiệu quả. Anh/chị còn cần [AccountName] hỗ trợ tư vấn thêm gì không ạ? |
| Lưu ý: Mức độ mở rộng càng cao, AI tiêu tốn token càng nhiều |  |  |



### 2.4 Use Case chi tiết:



| **Usecase ID** | **Tên use case** | **Tác nhân chính** | **Mô tả** | **Điều kiện đầu vào** | **Kết quả mong muốn** |
| --- | --- | --- | --- | --- | --- |
| UC2.1.01 Luồng chính | Người dùng Nhập tên AI | Người dùng | Người dùng nhập tên AI vào trường bắt buộc. | Form thiết lập AI đang mở; vị trí: **Thông tin chung**. Người dùng có quyền thêm mới AI vào hệ thống | Tên AI được lưu tạm thời trong hệ thống, không để trống khi chuyển bước. |
| UC2.1.01a Thay thế | Người dùng để trống tên AI | Người dùng | Người dùng để trống trường dữ liệu tên AI | Form thiết lập AI đang mở; vị trí: **Thông tin chung**. Người dùng có quyền thêm mới AI vào hệ thống | Khi bấm "**Hoàn thành**", hệ thống hiển thị cảnh báo tại trường dữ liệu tên AI "Tên AI là thông tin bắt buộc". => Người dùng hoàn thành bước điền tên AI. |
| UC2.1.01b Thay thế | Người dùng nhập tên AI chứa ký tự không hợp lệ | Người dùng | Người dùng nhập ký tự không hợp lệ vào tên AI | Form thiết lập AI đang mở; vị trí: **Thông tin chung**. Người dùng có quyền thêm mới AI vào hệ thống | Hệ thống chặn nhập hoặc thông báo lỗi: “Tên AI không được chứa các ký tự đặc biệt” khi bấm "**Tiếp theo**" => Người dùng hoàn thành bước điền tên AI. |
| UC2.1.2 Luồng chính | Người dùng nhập mô tả AI | Người dùng | Người dùng nhập mô tả mục tiêu, ghi chú hoặc phạm vi AI. | Form thiết lập AI đang mở; vị trí: **Thông tin chung**. | Mô tả được lưu tạm thời, có thể để trống nhưng nếu nhập thì phải đúng định dạng text. |
| UC2.1.2a Thay thế | Người dùng nhập mô tả AI quá giới hạn ký tự | Người dùng | Người dùng nhập mô tả mục tiêu, ghi chú hoặc phạm vi AI quá 2000 ký tự | Form thiết lập AI đang mở; vị trí: **Thông tin chung**. | Hệ thống hiển thị cảnh báo giới hạn: “Giới hạn mô tả trong 2000 ký tự”=> Người dùng hoàn thành điền mô tả trong giới hạn và đúng định dạng. Mô tả được lưu tạm thời. |
| UC2.1.4 | Người dùng **Hủy **thao tác thiết lập | Người dùng | Người dùng bấm nút **Hủy**. | Giao diện **Thông tin chung** đang mở. | Hệ thống hiện Popup cảnh báo: “Bạn chắc chắn muốn hủy? Mọi thiết lập cũ sẽ không được lưu”, nhấp chọn “**Xác nhận**” để xác nhận hủy, nhấp chọn “**Quay lại**” để hủy bỏ thao tác **Hủy** |
| UC2.2.1 Luồng chính | Model AI: Chọn Nhà cung cấp AI | Người dùng | Người dùng chọn nhà cung cấp AI từ dropdown list do hệ thống cung cấp | Người dùng có quyền thêm mới AI. Đang ở giao diện **Thiết lập** *(Sau đây, tất cả UC có mã UC2.2. đều có điều kiện đầu tiên tương tự)* | Nhà cung cấp AI được chọn thành công |
|  | Model AI: Chọn model AI | Người dùng | Người dùng chọn model AI tương ứng với nhà cung cấp từ dropdown list do hệ thống cung cấp |  | Model được chọn thành công và tương ứng |
| UC2.2…. | Để trống Nhà cung cấp AI | Người dùng | Người dùng không chọn nhà cung cấp AI | Trường dữ liệu **Nhà cung cấp** bị để trống. Người dùng bấm “**Lưu**” | Hệ thống hiện cảnh báo lỗi: “Nhà cung cấp AI không được để trống”. Đồng thời trường dữ liệu liên kết **Model AI** không khả dụng, không cho phép chọn => Người dùng nhập model AI và hệ thống lưu thành công |
| UC2.2.1a Luồng thay thế | Để trống Model AI | Người dùng | Người dùng không chọn model AI | Trường dữ liệu **Model** bị để trống. Người dùng bấm “**Lưu**” | Hệ thống hiện cảnh báo lỗi: “Model không được để trống” => Người dùng nhập model AI và hệ thống lưu thành công |
| UC2.2.2 Luồng chính | Nhập Mã kết nối AI | Người dùng | Người dùng nhập mã kết nối AI hợp lệ để hệ thống xác thực | Mã kết nối hợp lệ từ nhà cung cấp AI | Mã kết nối AI được xác nhận và lưu |
| UC2.2.2a Luồng thay thế | Không nhập mã kết nối AI | Người dùng | Người dùng không nhập mã kết nối AI | Mã kết nối AI bị bỏ trống Người dùng bấm “**Lưu**” | Hệ thống không cho lưu đồng thời hiện cảnh báo: “Mã kết nối không được để trống và phải hợp lệ” |
| UC2.2.2b Luồng thay thế | Nhập sai mã kết nối AI | Người dùng | Người dùng nhập mã kết nối AI không hợp lệ để hệ thống xác thực | Mã kết nối AI không hợp lệ - sai mã kết nối AI | Hệ thống không cho lưu đồng thời hiện cảnh báo: “Mã kết nối không được để trống và phải hợp lệ” |
| UC2.2.2c Luồng thay thế | Nhập mã kết nối AI đã tồn tại trong hệ thống | Người dùng | Người dùng nhập mã kết nối AI không hợp lệ | Mã kết nối bị trùng | Hệ thống không cho lưu đồng thời hiện cảnh báo: “Mã kết nối không được để trống và phải hợp lệ”. Hiện popup thông báo: “Mã kết nối hết hạn. Vui lòng kiểm tra lại mã kết nối của bạn” |
| UC2.2.2d Luồng thay thế | Nhập mã kết nối AI hết hạn | Người dùng | Người dùng nhập mã kết nối AI hết hạn để hệ thống xác thực | Mã kết nối hết hạn | Hệ thống không cho lưu đồng thời hiện cảnh báo: “Mã kết nối không được để trống và phải hợp lệ”. Hiện popup thông báo: “Mã kết nối hết hạn. Vui lòng kiểm tra lại mã kết nối của bạn” |
| UC2.2.3 Luồng chính | Nhập Prompt | Người dùng | Nhập đoạn prompt mô tả cách AI cần phản hồi trong các tình huống | Người dùng có prompt khoa học. | Hệ thống lưu Prompt và chuyển tới AI để trainning |
| UC2.2.3a Luồng thay thế | Để trống Prompt | Người dùng | Người dùng để trống prompt | Trường Prompt bị bỏ trống | Hệ thống cho lưu nhưng AI sẽ vận hành theo chế độ mặc định của nhà cung cấp AI |
| UC2.2.3b Luồng thay thế | Nhập prompt quá giới hạn | Người dùng | Người dùng nhập prompt quá 2000 ký tự | Ghi nhận tình trạng nhập quá 2000 ký tự | Hệ thống ngay lập tức cảnh báo hoặc không cảnh báo nhưng không cho nhập thêm. |
| UC2.2.4 Luồng chính | Tải file kiến thức | Người dùng | Upload tài liệu nội bộ để AI tham chiếu khi trả lời | File hợp lệ (Word, Excel, PDF, Link) không lớn hơn 20mb | File được tải lên và hiển thị trong danh sách tài liệu |
| UC2.2.4.a Luồng thay thế | Tải file kiến thức quá dung lượng hoặc sai định dạng | Người dùng | Upload tài liệu nội bộ để AI tham chiếu sai định dạng hoặc quá dung lượng | File ko hợp lệ ( không phải Word, Excel, PDF, Link) không lớn hơn 20mb | Hệ thống hiện cảnh báo. “Hỗ trợ file word, excel, PDF không quá 20Mb” |
| UC2.2.5. Luồng chính | Thêm URL kiến thức | Người dùng | Nhập link tài liệu/URL để AI sử dụng làm nguồn tham chiếu | URL hợp lệ | Link được thêm vào danh sách tài liệu |
| UC2.2.5.a Luồng thay thế | Thêm URL link không an toàn | Người dùng | Nhập link tài liệu/URL không an toàn | URL không hợp lệ | Hệ thống hiện cảnh báo “Phát hiện đường dẫn không an toàn. Vui lòng nhập đường dẫn khác” |
| UC2.2.5.b Luồng thay thế | Không truy cập được URL người dùng tải lên | Người dùng | Nhập link tài liệu/URL sai hoặc giới hạn quyền | URL không đọc được | Hệ thống hiện cảnh báo “Không thể xác thực nội dung URL” |
| UC2.2.6 Luồng chính | Thay đổi quản lý danh sách tài liệu | Người dùng | Thêm, hoặc xóa tài liệu tham chiếu cho AI | Có ít nhất một tài liệu đã upload hoặc nhập link | Danh sách tài liệu hiển thị và được cập nhật |
| UC2.2.6.a Luồng thay thế | Xóa tài liệu trong danh sách | Người dùng | Người dùng nhấp biểu tượng xóa trong bảng danh sách | Có ít nhất một tài liệu đã upload hoặc nhập link | Hệ thống hiện thông báo (popup): “Bạn chắc chắn muốn xóa?” kèm nút “Quay lại”, “Đồng ý” |
| UC2.2.6.b Luồng thay thế | Chỉnh sửa không hợp lệ | Người dùng | Thêm tài liệu không hợp lệ | Chỉnh sửa không hợp lệ (tên trùng, định dạng sai) → báo lỗi. | Hệ thống hiển thị thông báo: “Tài liệu đã tồn tại trong hệ thống” nếu trùng. Hiện: “Hỗ trợ file word, excel, PDF không quá 20Mb” nếu không trùng nhưng sai định dạng |
| UC2.2.7 | Cấu hình mức độ mở rộng | Người dùng | Thay đổi lựa chọn mức độ để thay đổi phạm vi trả lời của AI (từ hẹp đến mở rộng) | Người dùng có quyền điều chỉnh | AI thay đổi cách phản hồi theo mức độ mở rộng đã chọn khi người dùng nhấn lưu. |
| UC2.2.8 | Kích hoạt tùy chọn nâng cao | Người dùng | Tích chọn các tùy chọn: từ chối trả lời và chọn điều kiện: không tìm thấy thông tin, phát hiện ngữ cảnh tiêu cực, phát hiện nhu cầu tư vấn chuyên sâu | Màn hình hiển thị các checkbox tùy chọn | Các tùy chọn được lưu và áp dụng cho AI. Sinh ra event “AI từ chối trả lời” khi trùng khớp với điều kiện được tích chọn. Nếu không chọn coi như người dùng không kích hoạt, AI sẽ chạy tự nhiên và không sinh ra event “AI từ chối trả lời”. |
| UC2.2.8 | Người dùng **Hủy **thao tác thiết lập | Người dùng | Người dùng bấm nút **Hủy**. | Giao diện **Thiết lập** đang mở. | Hệ thống hiện Popup cảnh báo: “Bạn chắc chắn muốn hủy? Mọi thiết lập cũ sẽ không được lưu” nhấp chọn “**Xác nhận**” để xác nhận hủy, nhấp chọn “**Quay lại**” để hủy bỏ thao tác **Hủy** |
| UC2.2.9 | Người dùng lưu thiết lập AI | Người dùng | Người dùng bấm **“Lưu”** | - Trường **Model, mã kết nối, mức độ mở rộng, **không rỗng | Hệ thống lưu thông tin và cập nhật thông tin mới vào danh sách AI tại giao diện **Quản lý AI** |



### 2.5 Usecase ngoại lệ:



| **Usecase ID** | **Tên Use Case** | **Tác nhân chính** | **Mô tả** | **Điều kiện đầu vào** | **Kết quả mong muốn** |
| --- | --- | --- | --- | --- | --- |
| UC2.01 | Người dùng muốn ngừng AI | Người dùng | Người dùng muốn tạm ngừng AI trong hệ thống Gapone Conversation | Người dùng có quyền thao tác chỉnh sửa, xóa, tạo mới, quản lý AI Có ít nhất 1 AI đã được thêm mới vào hệ thống thành công | Nghiên cứu thêm. Vì một AI sẽ được gán vào ít nhất 1 kịch bản tự động hóa. Nếu người dùng muốn tạm ngưng AI có thể chỉnh sửa ở các kịch bản chứa AI đó hoặc ngưng kịch bản tự động đó. Hiện tại AI chỉ có thiết lập chỉnh sửa hoặc xóa để giảm tải cho các thiết lập kịch bản tự động (case kịch bản tự động bị lỗi khi AI bị tạm ngưng hoặc xóa khỏi hệ thống) |



## **3. Chỉnh sửa thiết lập AI**



### 3.1 Mô tả chức năng



| **Tên nghiệp vụ** | Chỉnh sửa AI được tích hợp vào hệ thống |
| --- | --- |
| **Module** | Menu > Cài đặt > Thiết lập AI |
| **Mô tả** | Tính năng cho phép chỉnh sửa AI đã được thiết lập trên hệ thống Gapone Conversation. Trigger: Nút “chỉnh sửa” Chỉnh sửa AI trong hệ thống bao gồm 3 phần chính: Thông tin thiết lập: bao gồm thông tin cơ bản về AI trong hệ thống, cài đặt Prompt, cài đặt Kho kiến thức, cài đặt mức độ mở rộng và cài đặt khác của AI (Không cho phép thay đổi model và mã kết nối AI) |
| **Điều kiện cần để thực hiện hành động** | Người dùng được phân quyền **chỉnh sửa** của chức năng "Thiết lập AI". Truy cập phân quyền người dùng tại mục Cài đặt > Thiết lập người dùng > Phân quyền. Truy cập thiết lập AI tại Cài đặt > Thiết lập AI Quyền chức năng thiết lập người dùng như sau: - Quyền chỉnh sửa: thể hiện người dùng được phép chỉnh sửa AI trong hệ thống Có AI hợp lệ và an toàn đã tích hợp vào hệ thống. |
| **Hành động** | Người dùng thực hiện theo các bước sau: - **Bước 1: **Sau khi đăng nhập vào hệ thống, nhấp chọn “Cài đặt” trong thanh menu, sau đó click chọn “Thiết lập AI” trong sub menu của Cài đặt, giao diện Quản lý AI sẽ xuất hiện. - **Bước 2:** Để thực hiện chỉnh sửa AI trên hệ thống, nhấp chọn biểu tượng “chỉnh sửa” trong thanh menu ẩn tại màn giao diện Quản lý AI. Giao diện Chi tiết thiết lập AI sẽ hiển thị các thông tin thiết lập, các trường dữ liệu đã có thông tin từ lần lưu cuối cùng cũng được hiển thị. Thông tin chỉnh sửa bao gồm: - Nhập tên AI: Người dùng có thể thay đổi tên cho AI trong hệ thống - Mô tả AI: Người dùng có thể thay đỏi mô tả mục tiêu, mục đích hoặc ghi chú AI - Model: Không cho phép thay đổi model AI - Mã kết nối: Không cho phép thay đổi Mã kết nối AI - Prompt: Có thể thay đổi prompt vận hành AI - Kho kiến thức: Có thể thay đổi Tải lên hoặc nhập URL các tài liệu kiến thức, chỉnh sửa, xóa bớt file kiến thức cũ trước đó, - Mức độ mở rộng: Có thể thay đổi mức độ AI trả lời các câu hỏi trực tiếp hay cung cấp thêm các thông tin bên lề. - Cài đặt khác: Trường hợp từ chối trả lời: Có thể thay đổi trường hợp AI từ chối trả lời. Khi các trường hợp này được kích hoạt, sẽ sinh event và tự động chuyển cuộc hội thoại đến người dùng để xử lý. - **Bước 3: **Ấn chọn "Lưu" tất cả các thiết lập ở bước này để hệ thống nhận diện AI và đưa AI vào sử dụng. - **Bước 4: **Thử nghiệm Khung hội thoại cho phép chat thử nghiệm với AI sau khi AI lưu vào hệ thống. Nếu phát sinh những phản hồi không mong đợi, người dùng có thể nhấn nút Quay lại chỉnh sửa để chỉnh sửa các thiết lập AI. |
| **Kết quả** | Người dùng cập nhật chỉnh sửa một AI vào hệ thống thành công khi thỏa mãn các điều kiện |



### 3.2 Flow



### 3.3 Wireframe


3.3.1 Wireframe Quản lý AI > Chọn chỉnh sửa

3.3.2 Wireframe Quản lý AI > Chọn chỉnh sửa > Hiện popup cảnh báo


#### Mô tả trường dữ liệu:



| **#** | **Thành phần** | **Kiểu dữ liệu** | **Ràng buộc hệ thống** | **Ghi chú** |
| --- | --- | --- | --- | --- |
| **1. Menu ẩn chứa các nút hành động** (Số nút hành động có thể tăng thêm khi hệ thống có cập nhật hạ tầng tính năng này) |  |  |  |  |
| **1.1** | **Nút Thử nghiệm** | Button | Khi click → mở giao diện thử nghiệm AI đã chọn | Luôn khả dụng |
| **1.2** | **Nút Chỉnh sửa** | Button | Khi click → mở giao diện chỉnh sửa cấu hình AI | Chỉ khả dụng với user có quyền chỉnh sửa |
| **1.3** | **Nút Xóa** | Button | Khi click → hiển thị popup xác nhận xoá AI | Là điều kiện kích hoạt modal |
| **2. Popup thông báo** |  |  |  |  |
| **2.1** | **Popup Thông báo** | Modal | Chỉ hiển thị khi người dùng click “Chỉnh sửa” | Nội dung: “Bạn chắc chắn muốn chỉnh sửa?” Kèm thông tin:“Chỉnh sửa thiết lập AI có thể ảnh hưởng tới cách AI trả lời trong những kịch bản tự động hóa” |
| **2.2** | **Nút Quay lại (trong popup)** | Button | Đóng popup, không chỉnh sửa thiết lập | Không thay đổi thiết lập |
| **2.3** | **Nút Xác nhận (trong popup)** | Button | Thực hiện chuyển người dùng tới giao diện chỉnh sửa thiết lập AI | Nếu chỉnh sửa thành công → cập nhật các thiết lập và cập nhật lại thông tin trong danh sách AI. |


**Mô tả trường dữ liệu:**


| **STT** | **Tên Trường** | **Kiểu Dữ Liệu** | **Mô tả** | **Ràng buộc / Quy tắc** |
| --- | --- | --- | --- | --- |
| 1 | Tên AI | VARCHAR(255) | Đặt tên cho AI | - Không để trống - Độ dài tối thiểu: 1 ký tự - Độ dài tối đa: 255 ký tự - Không chứa ký tự đặc biệt không hợp lệ ( . , ; : “ ‘ { [ ] } = - ) ( * ! @ # $ % ^ & ~ `) |
| 2 | Mô tả AI | TEXT | Nhập mô tả mục đích, mục tiêu, hoặc ghi chú về AI | - Có thể để trống - Độ dài tối đa 2000 ký tự |
| 3 | Model | VARCHAR(255) | Tên hoặc mã model AI được sử dụng | **Không cho phép chỉnh sửa** |
|  |  |  |  |  |
| 4 | Mã kết nối AI | TEXT | Mã mã kết nối để xác thực kết nối AI | **Không cho phép chỉnh sửa** |
| 5 | Prompt | TEXT | Nội dung hướng dẫn chi tiết hành vi AI | **Bắt buộc nhập ** nếu có thay đổi, độ dài khuyến nghị ≤ 2000 ký tự. Không chứa Script hoặc mã độc |
| 6 | Kho kiến thức | Dropdown list | Tập tài liệu, dữ liệu huấn luyện bổ sung cho AI. | **Tùy chọn**, người dùng có thể chọn file thêm file mới từ từ hệ thống hoặc upload thêm file mới. Mỗi khi up lên hệ thống một tài liệu thành công, tài liệu đó sẽ được đẩy vào **Danh sách tài liệu** Người dùng cũng có thể lựa chọn xóa bớt tài liệu cũ |
| 7. Danh sách tài liệu bao gồm: |  |  |  |  |
| 7.1 | Tên tài liệu | VARCHAR(255) | Tên hiển thị của tài liệu trong danh sách | **Bắt buộc**, không được trùng trong cùng 1 AI |
| 7.2 | Loại tài liệu | ENUM (Word, Excel, PDF, Link) | Định dạng loại file/nguồn tài liệu Nếu là file, không quá 20Mb | **Bắt buộc**, chọn từ danh sách có sẵn |
| 7.3 | Ngày tạo tài liệu | DATE (dd/MM/yyyy) | Ngày hệ thống ghi nhận file/link được thêm | **Tự động sinh**, không cho chỉnh sửa |
| 7.4 | Tên tài liệu dạng up URL | VARCHAR(255) | Tên tài liệu (nếu loại là link và có tên). Khi nhấp chuột vào có thể mở link dẫn tới tài liệu đó. Nếu loại là link và không có tên thì hiện URL ở phần **Tên tài liệu** | **Bắt buộc nếu loại tài liệu = Link**, phải đúng định dạng URL |
| 7 | Mức độ mở rộng | INT (0–100) | Tỷ lệ % mức mở rộng khả năng trả lời của AI | **Mặc định = 20%**, giá trị trong khoảng từ **0 → 100** Chọn theo các mốc được chia sẵn. |
| 8 | Cài đặt khác | BOOLEAN[] (multi-select) | Các tùy chọn bổ sung để AI xử lý tình huống | Có thể chọn nhiều giá trị. Danh sách gồm: - Không tìm thấy thông tin chính xác - Phát hiện nội dung rủi ro/dữ liệu sai - Phát hiện khách hàng yêu cầu tư vấn sâu |
| 9 | Nút “Hủy” | Action | Hủy bỏ thao tác thiết lập và quay lại màn hình trước | Không lưu dữ liệu đã nhập. Hiện Popup cảnh báo: “Bạn chắc chắn muốn hủy? Mọi thiết lập cũ sẽ không được lưu”, nhấp chọn “**Xác nhận**” để xác nhận hủy, nhấp chọn “**Quay lại”** để hủy bỏ thao tác **Hủy** |
| 10 | Nút “Lưu” | Action | Lưu cấu hình thiết lập AI | **Bắt buộc kiểm tra hợp lệ dữ liệu** trước khi lưu. |


**Ràng buộc hệ thống:**


| **Nhóm ràng buộc hệ thống** | **Mô tả chi tiết** |
| --- | --- |
| **Toàn vẹn dữ liệu** | - Không cho phép trùng lặp tên tài liệu trong danh sách. - Chỉ chấp nhận file đúng định dạng (Word, Excel, PDF, CSV) hoặc URL hợp lệ. - Nếu file tải lên hỏng hoặc URL không truy cập được → báo lỗi. |
| **Xác  nhận chỉnh sửa** | - Hệ thống yêu cầu xác nhận đồng ý chỉnh sửa. Nhấp chọn “Xác nhận” để bắt đầu chỉnh sửa thiết lập AI, nhấp chọn “Quay lại” để hủy thao tác truy cập giao diện chỉnh sửa. |
| **Quy tắc nhập liệu** | - Trường **Prompt** phải nằm trong giới hạn ký tự, không được chứa mã HTML/script. - Các trường text (Model, Mã kết nối AI) không được nhập ký tự đặc biệt trái phép. |
| **Điều kiện lưu tất cả thiết lập** | - Phải có ít nhất 1 giá trị hợp lệ trong các trường bắt buộc (**Model**, **Mã kết nối AI**, **Prompt**). - Nếu người dùng thay đổi kho kiến thức bằng cách xóa hết, hệ thống vẫn cho lưu nhưng AI sẽ hoạt động với Prompt mặc định. |
| **Mức độ mở rộng (slider)** | - Giới hạn từ 0% → 100% theo 5 mốc. Ghi nhận mốc gần nhất người dùng click chọn. |
| **Xử lý lỗi & thông báo** | - Nếu thiếu thông tin bắt buộc → hiện thông báo lỗi ngay tại trường nhập.- Khi upload tài liệu lỗi hoặc không đúng định dạng → cảnh báo và không thêm vào danh sách. |
| **Tương tác người dùng** | - Nút **Lưu** chỉ được phép nhấn khi toàn bộ trường bắt buộc hợp lệ. Hoàn thành check URL hợp lệ và an toàn mới được phép lưu. Nếu là link không hợp lệ, hệ thống hiện thông báo “URL không hợp lệ. Cảnh báo rủi ro an toàn.” - Nút **Hủy** thoát form mà không lưu dữ liệu. |
| **Lưu lỗi do vấn đề bên ngoài hệ thống** | - Những trường hợp nhập sai Mã kết nối AI nên kết nối thất bại, sẽ hiện cửa sổ thông báo, đồng thời quay trở lại giao diện thiết lập để người dùng cập nhật lại Mã kết nối AI. |



##### Case đặc biệt của luồng chỉnh sửa thiết lập AI:


Thử nghiệm AI > dẫn đến giao diện chỉnh sửa

Mô tả sơ bộ:

Có 2 cách để truy cập “**Chỉnh sửa thiết lập AI**”

- Nhấp chọn “Chỉnh sửa” trong thanh menu ẩn => Mở trực tiếp giao diện **Thông tin chung + Thiết lập AI** trong màn Thiết lập AI và thực hiện các bước như mô tả ở phần 3.3.1 và 3.3.2.

=> Sau khi lưu thiết lập được chỉnh sửa, chuyển tới giao diện **Thử nghiệm** để thử nghiệm AI một lần nữa.

- Nhấp chọn “Thử nghiệm” trong thanh menu ẩn => Mở trực tiếp giao diện **Thử nghiệm**. Sau khi người dùng thử nghiệm AI và đưa ra quyết định cần chỉnh sửa AI, người dùng nhấp chọn nút “**Quay lại chỉnh sửa” **tại giao diện **Thử nghiệm. **=> Mở giao diện **Thông tin chung + Thiết lập AI** trong màn Thiết lập AI và thực hiện các bước như mô tả ở phần 3.3.1 và 3.3.2.

=> Sau khi lưu thiết lập được chỉnh sửa, chuyển tới giao diện **Thử nghiệm** để thử nghiệm AI một lần nữa.


### 3.4 Use case tổng quan



| **Usecase ID** | **Tên Use Case** | **Tác nhân chính** | **Mô tả** | **Điều kiện đầu vào** | **Kết quả mong muốn** |
| --- | --- | --- | --- | --- | --- |
| UC3.1.01 Luồng chính | Người dùng thay đổi tên AI | Người dùng | Người dùng nhập tên AI vào trường bắt buộc. | Form thiết lập AI đang mở; vị trí: **Thông tin chung**. Người dùng có quyền thêm mới AI vào hệ thống | Tên AI được lưu tạm thời trong hệ thống, không để trống khi chuyển bước. |
| UC3.1.01a Thay thế | Người dùng xóa và để trống tên AI | Người dùng | Người dùng để trống trường dữ liệu tên AI | Form thiết lập AI đang mở; vị trí: **Thông tin chung**. Người dùng có quyền thêm mới AI vào hệ thống | Khi bấm "**Tiếp theo**", hệ thống hiển thị cảnh báo tại trường dữ liệu tên AI "Tên AI là thông tin bắt buộc". => Người dùng hoàn thành bước điền tên AI. Tên AI được lưu tạm thời trong hệ thống, không để trống khi chuyển bước. |
| UC3.1.01b Thay thế | Người dùng thay đổi tên AI chứa ký tự không hợp lệ | Người dùng | Người dùng nhập ký tự không hợp lệ vào tên AI | Form thiết lập AI đang mở; vị trí: **Thông tin chung**. Người dùng có quyền thêm mới AI vào hệ thống | Hệ thống chặn nhập hoặc thông báo lỗi: “Tên AI không được chứa các ký tự đặc biệt” khi bấm "**Tiếp theo**" => Người dùng hoàn thành bước điền tên AI. Tên AI được lưu tạm thời trong hệ thống, không để trống khi chuyển bước. |
| UC3.1.2 Luồng chính | Người dùng thay đổi mô tả AI | Người dùng | Người dùng nhập mô tả mục tiêu, ghi chú hoặc phạm vi AI. | Form thiết lập AI đang mở; vị trí: **Thông tin chung**. | Mô tả được lưu tạm thời, có thể để trống nhưng nếu nhập thì phải đúng định dạng text. |
| UC3.1.2a Thay thế | Người dùng thay đổi mô tả AI quá giới hạn ký tự | Người dùng | Người dùng thay đổi mô tả mục tiêu, ghi chú hoặc phạm vi AI quá 2000 ký tự | Form thiết lập AI đang mở; vị trí: **Thông tin chung**. | Hệ thống hiển thị cảnh báo giới hạn: “Giới hạn mô tả trong 2000 ký tự”=> Người dùng hoàn thành điền mô tả trong giới hạn và đúng định dạng. Mô tả được lưu tạm thời. |
| UC3.1.3 | Người dùng **Hủy **thao tác chỉnh sửa | Người dùng | Người dùng bấm nút **Hủy**. | Giao diện **Thông tin chung** đang mở. | Hệ thống hiện Popup cảnh báo: “Bạn chắc chắn muốn hủy? Mọi thiết lập cũ sẽ không được lưu”, nhấp chọn “**Xác nhận**” để xác nhận hủy, nhấp chọn “**Quay lại**” để hủy bỏ thao tác **Hủy** |
| UC4.01 Luồng tổng quan | Người dùng thay đổi thiết lập AI khi kịch bản tự động hóa đang chạy | Người dùng | Người dùng đã thay đổi thiết lập AI trong khi AI đó đang được phân công xử lý tại một kịch bản tự động hóa | Người dùng có quyền chỉnh sửa Có AI hợp lệ đã tồn tại trong hệ thống AI đang được gán vào một kịch bản tự động đang hoạt động Chỉnh sửa hợp lễ đã được lưu. | Kịch bản đó vẫn vận hành bình thường, AI sẽ tự động trả lời theo thiết lập mới nhất. |
| UC4.01.1 Luồng chính (chi tiết) | Thay đổi trong **tên AI **trong **Thông tin chung** | Người dùng | Người dùng đã thay đổi thông tin **Tên AI** trong khi AI đó đang được phân công xử lý tại một kịch bản tự động hóa | AI đã được gán vào một kịch bản tự động hóa đang hoạt động | Kịch bản vẫn hoạt động bình thường. Danh sách droplist chứa tên AI được cập nhật Tên AI được gán được cập nhật trong kịch bản tự động hóa |
| UC4.01.2 Luồng chính (chi tiết) | Thay đổi **mô tả, hình ảnh đại diện của AI **trong** Thông tin chung** | Người dùng | Người dùng đã thay đổi thông tin **mô tả, hình ảnh đại diện của AI ** trong khi AI đó đang được phân công xử lý tại một kịch bản tự động hóa | AI đã được gán vào một kịch bản tự động hóa đang hoạt động | Kịch bản hoạt động bình thường |
| UC4.01.3 Luồng chính (chi tiết) | Thay đổi **Prompt** trong **Thiết lập AI** | Người dùng | Người dùng đã thay đổi thông tin **Prompt **trong khi AI đó đang được phân công xử lý tại một kịch bản tự động hóa | AI đã được gán vào một kịch bản tự động hóa đang hoạt động | Kịch bản hoạt động bình thường, có một số thay đổi trong việc AI trả lời khách hàng. Thứ tự ưu tiên nhận prompt. - Prompt bổ sung - Prompt trong thiết lập. Nếu không có cả 2 prompt thì AI sẽ tự phản hồi theo cài đặt mặc định từ nhà cung cấp Khi thay đổi prompt trong thiết lập, mọi thay đổi phản hồi của AI sẽ diễn ra ngay lập tức mà không cần chỉnh sửa lại kịch bản |
| UC4.01.3a Luồng thay thế | Thay đổi bằng cách xóa **Prompt **trong thiết lập AI | Người dùng | Người dùng đã thay đổi thông tin **Prompt** bằng cách **Xóa prompt **trong khi AI đó đang được phân công xử lý tại một kịch bản tự động hóa |  | Kịch bản hoạt động bình thường, có một số thay đổi trong việc AI trả lời khách hàng. Nếu có Prompt bổ sung trong Kịch bản thì theo prompt bổ sung. Nếu không có cả 2 prompt thì AI sẽ tự phản hồi theo cài đặt mặc định từ nhà cung cấp Khi xóa prompt trong thiết lập, mọi thay đổi phản hồi của AI sẽ diễn ra ngay lập tức mà không cần chỉnh sửa lại kịch bản |
| UC4.01.4 Luồng chính (chi tiết) | Thay đổi **Kho kiến thức **trong **Thiết lập AI** | Người dùng | Người dùng đã thay đổi **Danh sách tài liệu** trong khi AI đó đang được phân công xử lý tại một kịch bản tự động hóa (thêm mới, xóa cũ) | AI đã được gán vào một kịch bản tự động hóa đang hoạt động | Kịch bản hoạt động bình thường, có một số thay đổi trong việc AI trả lời khách hàng. AI trả lời theo kho kiến thức mới Khi thay đổi **Kho kiến thức **trong thiết lập, mọi thay đổi phản hồi của AI sẽ diễn ra ngay lập tức mà không cần chỉnh sửa lại kịch bản |
| UC4.01.4a Luồng thay thế | Thay đổi **Kho kiến thức **trong **Thiết lập AI** bằng cách xóa hết | Người dùng | Người dùng đã xóa hết **Danh sách tài liệu** trong khi AI đó đang được phân công xử lý tại một kịch bản tự động hóa |  | Kịch bản hoạt động bình thường, có một số thay đổi trong việc AI trả lời khách hàng. AI trả lời theo thông tin Ai tự tìm thấy và không dựa vào bất cứ tài liệu nào. Khi xóa **Kho kiến thức **trong thiết lập, mọi thay đổi phản hồi của AI sẽ diễn ra ngay lập tức mà không cần chỉnh sửa lại kịch bản. Không cho phép chọn option “Không tìm thấy thông tin chính xác” trong phần cài đặt kích hoạt các trường hợp AI từ chối trả lời |
| UC4.01.5 Luồng chính (chi tiết) | Thay đổi **Mức độ mở rộng **và** Cài đặt khác **trong **Thiết lập AI** | Người dùng | Người dùng đã thay đổi thông tin **Tên AI** trong khi AI đó đang được phân công xử lý tại một kịch bản tự động hóa | AI đã được gán vào một kịch bản tự động hóa đang hoạt động | Kịch bản hoạt động bình thường, có một số thay đổi trong việc AI trả lời khách hàng. AI trả lời theo thiết lập mới Khi thay đổi **Kho kiến thức **trong thiết lập, mọi thay đổi phản hồi của AI sẽ diễn ra ngay lập tức mà không cần chỉnh sửa lại kịch bản |



## **4. Xóa AI**



### 4.1 Mô tả chức năng



| **Tên nghiệp vụ** | Xóa AI được tích hợp vào hệ thống |
| --- | --- |
| **Module** | Menu > Cài đặt > Thiết lập AI |
| **Mô tả** | Tính năng cho phép xóa AI đã được tích hợp vào hệ thống Gapone Conversation. Trigger: Nút “xóa” Người dùng hoàn thành việc xóa AI thành công. AI bị xóa thành công khỏi hệ thống, đồng thời thông tin AI trong bảng danh sách AI tại giao diện **Quản lý AI** cũng bị xóa bỏ. |
| **Điều kiện cần để thực hiện hành động** | Người dùng được phân quyền **Xóa** của chức năng "Thiết lập AI". Truy cập phân quyền người dùng tại mục Cài đặt > Thiết lập người dùng > Phân quyền. Truy cập thiết lập AI tại Cài đặt > Thiết lập AI Quyền chức năng thiết lập người dùng như sau: - Quyền xóa: thể hiện người dùng được phép xóa AI trong hệ thống Có AI hợp lệ và an toàn đã tích hợp vào hệ thống. |
| **Hành động** | Người dùng thực hiện theo các bước sau: - Bước 1: Sau khi đăng nhập vào hệ thống, nhấp chọn “**Cài đặt**” trong thanh menu, sau đó click chọn “**Thiết lập Ai**” trong sub menu của **Cài đặt**, giao diện **Quản lý AI **sẽ xuất hiện. - Bước 2: Để thực hiện xóa AI ra khỏi hệ thống, nhấp chọn biểu tượng “**Xóa**” trong thanh menu ẩn tại màn giao diện **Quản lý AI**. - Bước 3: Ấn chọn "Xác nhận” để xác nhận và hoàn thành thao tác xoá/loại bỏ AI ra khỏi hệ thống. Ấn chọn "Quay lại" để huỷ thao tác xoá đang thực hiện. |
| **Kết quả** | Người dùng xóa một AI đã có trong hệ thống thành công khi thỏa mãn các điều kiện |



### 4.3 Wireframe


4.3.1. Wireframe Quản lý AI > Chọn xóa

4.3.2. Wireframe Quản lý AI > Chọn xóa > Popup thông báo xác nhận


### 4.4 Mô tả trường dữ liệu:



| **#** | **Thành phần** | **Kiểu dữ liệu** | **Ràng buộc hệ thống** | **Ghi chú** |
| --- | --- | --- | --- | --- |
| **1. Menu ẩn chứa các nút hành động** (Số nút hành động có thể tăng thêm khi hệ thống có cập nhật hạ tầng tính năng này) |  |  |  |  |
| **1.1** | **Nút Thử nghiệm** | Button | Khi click → mở giao diện thử nghiệm AI đã chọn | Luôn khả dụng |
| **1.2** | **Nút Chỉnh sửa** | Button | Khi click → mở giao diện chỉnh sửa cấu hình AI | Chỉ khả dụng với user có quyền chỉnh sửa |
| **1.3** | **Nút Xóa** | Button | Khi click → hiển thị popup xác nhận xoá AI | Là điều kiện kích hoạt modal |
| **2. Popup thông báo** |  |  |  |  |
| **2.1** | **Popup Thông báo** | Modal | Chỉ hiển thị khi người dùng click “Xóa” | Nội dung: “Bạn chắc chắn muốn xoá?” |
| **2.2** | **Nút Quay lại (trong popup)** | Button | Đóng popup, không xoá dữ liệu | Không thay đổi dữ liệu |
| **2.3** | **Nút Xác nhận (trong popup)** | Button | Thực hiện xoá bản ghi AI khỏi hệ thống | Nếu xoá thành công → hiển thị thông báo, refresh danh sách AI |



### 4.5 Ràng buộc hệ thống:



| **STT** | **Ràng buộc** | **Mô tả chức năng** | **Ràng buộc liên kết trong hệ thống** | **Thông báo hiển thị** | **Hành động của hệ thống** |
| --- | --- | --- | --- | --- | --- |
| 2 | **Trạng thái gán kịch bản tự động hóa** | Kiểm tra AI này có đang được gán cho bất kỳ **kịch bản tự động hóa** nào không. | ❗ **Không được phép xóa nếu AI còn đang được sử dụng trong bất kỳ kịch bản nào.** → Bắt buộc kiểm tra liên kết AI_ID trong bảng Automation_Scripts. | “Không thể xóa AI này vì AI đang được sử dụng cho kịch bản tự động hóa: [Tên kịch bản 1], [Tên kịch bản 2],[Tên kịch bản 3] .” | Hệ thống **chặn thao tác xóa**, yêu cầu người dùng gỡ AI khỏi kịch bản trước. |
| 3 | **Ràng buộc lịch sử hội thoại / nhật ký hoạt động** | Nếu AI có log hội thoại hoặc lịch sử sử dụng, chỉ cho phép xóa khi người dùng xác nhận. | Hệ thống hiển thị cảnh báo: “AI có dữ liệu lịch sử. Bạn có chắc muốn xóa toàn bộ dữ liệu liên quan không?” | “Xóa thành công.” hoặc “Hủy thao tác.” | Nếu người dùng xác nhận → Xóa AI + log liên quan. Nếu không → Dừng thao tác. |
| 4 | **Xác nhận hành động** | Yêu cầu xác nhận người dùng để tránh thao tác nhầm. | Bắt buộc hiển thị popup xác nhận: “Bạn có chắc chắn muốn xóa AI này không?” | “Hủy” hoặc “Xóa” | Nếu chọn “Xóa” → Hệ thống tiến hành kiểm tra ràng buộc. |
| 5 | **Phân quyền người dùng** | Xác định người dùng hiện tại có quyền xóa AI hay không. | - Chỉ người dùng có quyền “Quản trị viên” hoặc “Quản lý vùng” được phép xóa. | “Bạn không có quyền xóa AI.” | Hệ thống dừng thao tác và ghi log từ chối. |
| 6 | **Ghi log thông tin** | Ghi lại các thông tin về người xóa, thời gian xóa của AI được chọn xóa trong hệ thống | Ghi lại các thông tin người xóa, thời gian xóa của AI được chọn xóa. => Gửi thông báo notification “[Tên User] đã xóa thành công [Tên AI]” kèm giờ và ngày. (Phát triển sau, không phải sprint này) | “[Tên User] đã xóa thành công [Tên AI]” HH:MM DD:MM:YYYY | Xóa AI, ghi log, gửi thông báo |



### 4.6 Use case



| **Usecase ID** | **Tên Use Case** | **Tác nhân chính** | **Mô tả** | **Điều kiện đầu vào** | **Kết quả mong muốn** | **Luồng chính** |
| --- | --- | --- | --- | --- | --- | --- |
| UC-01 | Ngăn chặn xóa AI đang gán cho kịch bản | Người dùng | Người dùng muốn xóa một AI nhưng AI này đang được gán cho ít nhất một kịch bản tự động hóa | - AI đã được tích hợp vào hệ thống- AI đang được gán cho một hoặc nhiều kịch bản | AI **không bị xóa**, hệ thống thông báo cho người dùng biết lý do và yêu cầu gỡ liên kết trước khi xóa | 1. Người dùng nhấn **Xóa AI** 2. Hệ thống kiểm tra liên kết AI trong kịch bản 3. Hệ thống phát hiện AI đang được gán 4. Hệ thống hiển thị thông báo: “AI đang được sử dụng trong kịch bản [Tên kịch bản]. Vui lòng gỡ AI trước khi xóa.” 5. Người dùng chọn **Quay lại** |
| UC-02 | Người dùng kiên trì muốn xóa một AI ra khỏi hệ thống | Người dùng | Người dùng kiên trì muốn xóa một AI nhưng AI này đang được gán cho ít nhất một kịch bản tự động hóa | - AI đang gán cho một hoặc nhiều kịch bản- Người dùng đồng ý hủy liên kết khi xóa | Hệ thống chỉ cho phép: 1. Thay thế 1 AI mới vào vị trí của AI cũ trong hệ thống 2. Xóa bước thiết lập trợ lý AI ra khỏi kịch bản, đồng thời xóa những liên kết liên quan tới AI tại các khung thiết lập khác nếu không có AI mới thay thế. Ai mới được thêm vào và được gán thay thế AI cũ trong kịch bản. AI cũ bị gỡ ra khỏi các kịch bản, AI bị xóa khỏi hệ thống, | 1. Người dùng nhấn **Xóa AI** 2. Hệ thống kiểm tra liên kết AI trong kịch bản 3. Hệ thống phát hiện AI đang được gán 4. Hệ thống hiển thị thông báo: “AI đang được sử dụng trong kịch bản [Tên kịch bản]. Vui lòng gỡ AI trước khi xóa.” 5.1 Người dùng thay thế AI mới bằng cách chọn AI khác. Nếu không có AI khác để thay thế, người dùng cần thêm vào. Hoặc xóa luôn khung thiết lập AI và chỉnh sửa lại kịch bản như bước dự phòng 5.2 bên dưới 5.2 Người dùng chọn **Xóa **AI ra khỏi kịch bản. (Nếu có liên kết các khung thiết lập khác, cần xóa hoặc thay đổi những thiết lập liên quan tới AI mới cho phép bấm lưu). Sau khi hoàn thành việc xóa khung thiết lập AI và các yếu tố liên kết có liên quan, bấm lưu kịch bản. 6. Hệ thống check AI cần xóa không còn liên kết với kịch bản nào. 7. Hệ thống xóa AI thành công |



## 5. Thử nghiệm AI



### 5.1 Mô tả chức năng



| **Tên nghiệp vụ** | Thử nghiệm AI được tích hợp vào hệ thống |
| --- | --- |
| **Module** | Menu > Cài đặt > Thiết lập AI |
| **Mô tả** | Tính năng cho phép thử nghiệm AI đã được tích hợp vào hệ thống Người dùng được chuyển tới màn giao diện cuộc hội thoại giả lập với AI. Người dùng đóng vai trò là khách hàng và đưa ra những câu hỏi kỳ vọng AI phản hồi theo đúng prompt, kiến thức, phạm vi mở rộng, từ chối trả lời khi vượt ngoài phạm vi kiến thức và không tìm thấy nguồn uy tín |
| **Điều kiện cần để thực hiện hành động** | Người dùng được phân quyền Xem của chức năng "Thiết lập AI". Truy cập phân quyền người dùng tại mục Cài đặt > Thiết lập người dùng > Phân quyền. Truy cập thiết lập AI tại Cài đặt > Thiết lập AI Quyền chức năng thiết lập người dùng như sau: - Quyền xem: thể hiện người dùng được phép xem toàn bộ danh sách AI kết nối và thử nghiệm những AI xem được. |
| **Hành động** | Người dùng thực hiện theo các bước sau: **Bước 1:** Truy cập màn danh sách quản lý thiết lập AI tại mục Cài đặt > Thiết lập AI Giao diện **Quản lý A**I sẽ hiển thị. Giao diện sẽ bao gồm thanh tìm kiếm, nút “+ Thêm AI”, bảng danh sách các AI đã kết nối (bao gồm cả menu thao tác ẩn) Bước 2: Nhập tin nhắn câu hỏi cần thử nghiệm Bước 3: Nhấn nút gửi đi Bước 4: Nhấn “**Hoàn thành**” khi đã xong nhu cầu thử nghiệm để được trở về giao diện **Quản lý A**I. Nhấn “**Quay lại chỉnh sửa**” để được chuyển đến giao diện **Thiết lập AI** để chỉnh sửa lại thiết lập AI |
| **Kết quả** | Người dùng được chuyển tới màn giao diện **Thử nghiệm**, thử nghiệm khả năng phản hồi của AI theo thiết lập thành công. |



### 5.2 Wireframe



### 5.3 Mô tả trường dữ liệu:



| **Trường dữ liệu** | **Mô tả** | **Ràng buộc/Quy tắc** |
| --- | --- | --- |
| **Khung hội thoại ** | Hiển thị luồng hội thoại giữa người dùng và chatbot | - Nội dung được sinh tự động từ AI hoặc người dùng nhập - Không cho phép chỉnh sửa trực tiếp nội dung đã gửi - Tin nhắn hiển thị theo thời gian thực |
| **Tên AI** | Hiển thị tên AI được chọn để test | - Hiển thị tên được người dùng đặt trong phần thiết lập |
| **Ô nhập nội dung trò chuyện** | Người dùng nhập câu hỏi hoặc tin nhắn để gửi cho AI | - Không được để trống khi bấm gửi - Không cho phép gửi tin chứa mã độc, script HTML/JS - Tối đa 2000 ký tự |
| **Nút gửi tin nhắn (mũi tên cam)** | Gửi nội dung trong ô nhập cho chatbot | - Chỉ khả dụng khi ô nhập có dữ liệu hợp lệ - Gửi thành công thì xóa nội dung trong ô nhập |
| **Nút làm mới (↻)** | Làm mới hoặc reset cuộc hội thoại | - Sau khi làm mới, toàn bộ nội dung chat cũ sẽ bị xóa khỏi khung hội thoại |
| **Nút "Quay lại chỉnh sửa"** | Quay về màn hình thiết lập AI để sửa cấu hình | - Luôn khả dụng - Không ảnh hưởng đến dữ liệu hội thoại đang thử nghiệm |
| **Nút "Hoàn thành"** | Xác nhận kết thúc thử nghiệm. Quay về giao diện Quản lý AI | - Luôn khả dụng ngay cả khi người dùng không thử nghiệm cuộc hội thoại nào |


**Ràng buộc hệ thống:**

- Người dùng không thể chỉnh sửa tin nhắn đã gửi.

- AI chỉ trả lời dựa trên prompt và kho dữ liệu đã thiết lập trước đó.

- Nếu AI không tìm thấy dữ liệu → trả lời theo fallback mặc định hoặc từ chối trả lời nếu đã cài đặt từ chối trả lời.

- Cuộc hội thoại với AI là cuộc hội thoại giả lập, không trực tiếp lưu hay ảnh hưởng tới tính năng Conversation hay màn hội thoại thực tế trên nền tảng (Zalo, telegram, v…)

- Trạng thái cuộc hội thoại giả lập thử nghiệm AI:


| **STT** | **Từ trạng thái** | **Sang trạng thái** | **Điều kiện kích hoạt/Hành vi** |
| --- | --- | --- | --- |
| 1 | - | Mới | User gửi tin nhắn câu hỏi |
| 2 | Mới | Đang xử lý | AI đang phản hồi. User đang tiếp tục gửi tin nhắn thử nghiệm AI |
| 3 | Đang xử lý | Đóng | User nhấn “Hoàn thành” hoặc thoát khỏi giao diện **Thử nghiệm AI** |



## 6. Yêu cầu setting đặc biệt của AI



| **STT** | **Yêu cầu** | **Mô tả** | **Ghi chú** |
| --- | --- | --- | --- |
| 1 | Memory of AI | Trí nhớ của AI trong cuộc hội thoại. AI đọc lịch sử cuộc hội thoại giữa AI với khách hàng để lấy thêm dữ liệu và hiểu hành vi người dùng. | Chỉ cho phép AI đọc lịch sử tại cuộc hội thoại với chính khách hàng đó, lấy conversation history như memory để trao đổi với khách hàng. Không cho phép lấy conversation history của cuộc hội thoại khác. |
| 2 | Model | Model được phép tích hợp vào hệ thống phải là model AI của những nhà cung cấp AI uy tín. Chặn hết việc kết nối với những model AI do những bên cung cấp AI không uy tín, AI độc, AI chuyên đi thu lượm thông tin mật. | Giai đoạn đầu có thể chỉ cho phép kết nối tới 10 công ty: - OpenAI - Google (DeepMind / Google AI / Google Cloud AI) - Microsoft (Azure AI, Microsoft Research) - Amazon Web Services (AWS AI / Amazon SageMaker) - IBM (Watson, IBM Research) - NVIDIA - Anthropic - Databricks - Palantir Đối với các model của các nhà cung cấp, chỉ cho kết nối tới model còn khả dụng do nhà cung cấp cung cấp. (VD: modek cũ đã bị loại bỏ không thể kết nối vào) |
| 3 | AI Agent | AI Agent được doanh nghiệp khách hàng build up lên hoặc mua từ bên ngoài. Mong đợi: Khi tích hợp vào hệ thống có thể đánh giá được độ an toàn của AI hoặc ngăn không cho AI lấy những thông tin mật. => Tăng yếu tố bảo mật cho hệ thống | Giai đoạn đầu có thể chưa cần phát triển AI Agent |
| 4 | Knowledge | Kiến thức của AI. Cho phép AI tìm kiếm nguồn kiến thức từ bên ngoài, nhưng chỉ được phép dựa theo các nguồn tin tức chính quy, không cho phép nhai lại kiến thức tự dựng hoặc sử dụng các thông tin không được xác thực | Khi AI không tìm thấy thông tin hay kiến thức phù hợp có thể từ chối hoặc thú nhận với khách hàng rằng chưa đủ thông tin để phản hồi. |



## 7. Flow ngoại lệ -



### 7.1 Người dùng đột ngột xuất hiện trong khi kịch bản tự động hóa đang được vận hành


Mô tả luồng xử lý ngoại lệ trong trường hợp **AI chủ động từ chối trả lời** theo các điều kiện đã được cấu hình trước, **đồng thời người dùng (CS / Agent) can thiệp trực tiếp vào cuộc hội thoại** khi kịch bản tự động hóa đang vận hành.

Luồng này nhằm đảm bảo:

- Tránh xung đột giữa AI và người dùng

- Đảm bảo trải nghiệm hội thoại liền mạch cho khách hàng

- Đảm bảo quyền ưu tiên của con người cao hơn AI

- Đảm bảo khả năng audit, tracking và khôi phục trạng thái kịch bản


### 7.2 Phạm vi áp dụng


Luồng ngoại lệ này áp dụng cho:

- Gapone Conversation

- Các cuộc hội thoại đang được xử lý bởi:- AI Agent

- AI Model được gán trong kịch bản tự động hóa

- Các AI **đã kích hoạt “Cài đặt khác → Trường hợp AI từ chối trả lời”**

Không áp dụng cho:

- Hội thoại hoàn toàn thủ công (không có AI)

- AI không bật cơ chế từ chối trả lời


### 7.3 Điều kiện kích hoạt


Luồng ngoại lệ được kích hoạt khi **đồng thời thỏa mãn các điều kiện sau**:


| **STT** | **Điều kiện** |
| --- | --- |
| 1 | Hội thoại đang được xử lý bởi kịch bản tự động hóa có gán AI |
| 2 | AI phát hiện ít nhất **01 điều kiện từ chối trả lời** đã được cấu hình |
| 3 | AI sinh event AI_REFUSE_TO_ANSWER |
| 4 | Người dùng (CS / Agent) gửi tin nhắn thủ công vào cùng hội thoại |



### 7.4 Mô tả tổng quan luồng



#### Nguyên tắc ưu tiên


**Người dùng (Human) luôn có quyền ưu tiên cao hơn AI**

Khi người dùng can thiệp:

- AI **ngừng phản hồi ngay lập tức**

- Kịch bản tự động hóa **tạm dừng tại node hiện tại**

- Quyền điều khiển hội thoại được chuyển cho người dùng


### 7.5 Flow chi tiết



#### 7.5.1 Luồng chính


**Bước 1:** AI đang xử lý hội thoại trong kịch bản tự động hóa.

**Bước 2:** AI phát hiện điều kiện từ chối trả lời (ví dụ):

- Không tìm thấy thông tin chính xác

- Phát hiện nội dung rủi ro

- Phát hiện yêu cầu tư vấn chuyên sâu

**Bước 3:** AI:

- Không trả lời khách hàng

- Sinh event: AI_REFUSE_TO_ANSWER

- Gắn trạng thái hội thoại: WAITING_FOR_HUMAN

**Bước 4:** Hệ thống:

- Gửi thông báo đến Gapone Conversation (inbox người dùng)

- Đánh dấu hội thoại cần xử lý thủ công

**Bước 5:** Người dùng (CS / Agent) gửi tin nhắn vào hội thoại.

**Bước 6:** Hệ thống thực hiện:

- Ngắt quyền phản hồi của AI

- Tạm dừng kịch bản tự động hóa

- Gán trạng thái hội thoại: HUMAN_TAKE_OVER

**Bước 7:** Người dùng tiếp tục xử lý hội thoại thủ công.


#### 7.5.2 Luồng thay thế – Người dùng chen vào trước khi AI sinh event


**Trường hợp đặc biệt:** Người dùng gửi tin nhắn **trong khi AI đang xử lý nhưng chưa kịp từ chối**

Hệ thống sẽ:

- Hủy toàn bộ phản hồi AI đang pending

- Không sinh event AI_REFUSE_TO_ANSWER

- Chuyển ngay trạng thái hội thoại sang HUMAN_TAKE_OVER

- Log lại lý do: INTERRUPTED_BY_HUMAN


### 7.6 Trạng thái hội thoại



| **Trạng thái** | **Mô tả** |
| --- | --- |
| AI_PROCESSING | AI đang xử lý nội dung |
| AI_REFUSED | AI từ chối trả lời |
| WAITING_FOR_HUMAN | Chờ người dùng xử lý |
| HUMAN_TAKE_OVER | Người dùng đã tiếp quản |
| AUTOMATION_PAUSED | Kịch bản bị tạm dừng |
| CLOSED | Hội thoại kết thúc |



### 7.7 Ràng buộc hệ thống



| **Nhóm ràng buộc** | **Mô tả** |
| --- | --- |
| Ưu tiên xử lý | Tin nhắn người dùng luôn override AI |
| Đồng bộ trạng thái | Trạng thái hội thoại phải đồng bộ real-time |
| Không xung đột | AI không được phản hồi song song với người dùng |
| Audit log | Ghi nhận đầy đủ thời điểm AI từ chối & người dùng can thiệp |
| Khôi phục | Có thể resume automation nếu được phép |



### 7.8 Khả năng khôi phục kịch bản (Optional / Phase sau)


Sau khi người dùng xử lý xong, hệ thống **có thể hỗ trợ**:

- Resume lại kịch bản tại node kế tiếp

- Hoặc kết thúc vĩnh viễn automation cho hội thoại đó

⚠️ Việc khôi phục **chỉ thực hiện khi có flag cho phép** từ cấu hình kịch bản.


### 7.9 Bảng định nghĩa thuật ngữ



| **STT** | **Thuật ngữ** | **Định nghĩa** |
| --- | --- | --- |
| 1 | AI Refuse To Answer | Hành vi AI chủ động không phản hồi do vi phạm điều kiện cấu hình |
| 2 | Human Take Over | Trạng thái người dùng tiếp quản hội thoại |
| 3 | Automation Pause | Kịch bản tự động hóa bị tạm dừng |
| 4 | Event | Sự kiện hệ thống sinh ra để trigger xử lý |
| 5 | AI Processing | AI đang trong quá trình suy luận |
| 6 | Pending Message | Tin nhắn AI chưa gửi ra ngoài |
| 7 | Override | Ghi đè quyền xử lý |
| 8 | Audit Log | Nhật ký ghi nhận sự kiện |
| 9 | Resume Automation | Tiếp tục kịch bản tự động |
| 10 | Interrupt | Hành động ngắt luồng đang chạy |



## 8. GAPIT PROVIDER (chapter bổ sung)



### 8.1. Mục tiêu và tổng quan thiết kế


Tích hợp **GAPIT** như một **Nhà cung cấp AI (AI Provider)** trong hệ thống Gapone. GAPIT đóng vai trò là lớp trung gian (AI Gateway) kết nối Gapone với các nhà cung cấp AI gốc (OpenAI, Anthropic, Google, Grok, v.v.), đồng thời thực hiện quản lý quota, billing, phân phối model và theo dõi token usage.


#### 8.1.1. Mục tiêu của việc tích hợp GAPIT:


- Chuẩn hóa việc kết nối AI, tránh phụ thuộc trực tiếp vào từng AI Provider

- Cho phép Gapone kiểm soát quota, chi phí và chất lượng AI theo license

- Tối ưu trải nghiệm người dùng bằng việc tự động phân phối model AI

- Hỗ trợ mở rộng, thay đổi AI Provider mà không ảnh hưởng đến Gapone

**Phạm vi áp dụng:**

Đối với tất cả trường hợp có sử dụng token từ nhà cung cấp AI là Gapit:

- Áp dụng cho tất cả các tính năng sử dụng AI trong Gapone Conversation

- Áp dụng khi người dùng chọn **Nhà cung cấp AI = GAPIT** trong phần Thiết lập AI

- Không áp dụng cho các trường hợp người dùng kết nối trực tiếp với AI Provider bên thứ ba (OpenAI, Gemini, v.v.)

Bổ sung:

- Gapone không lưu trữ API key của AI Provider gốc

- Mọi thay đổi về model AI được thực hiện tại GAPIT

- Gapone phụ thuộc vào tính sẵn sàng của GAPIT khi sử dụng chế độ này


#### 8.1.2 Tổng quan thiết kế:


Link ảnh:

Bảng mô tả chi tiết:

*Lưu ý: Vì hình ảnh không đủ khả năng ghi hết mọi bước chi tiết nên chỉ đánh số luồng chính, các yêu cầu phụ và luồng phụ đi kèm luồng chính được mô tả chi tiết ở bảng dưới đây dưới dạng phân tách ý *

*VD: bước 2 có 2a,2b,2c… 2a,2b,2c là các bước phụ mà hệ thống cần thực hiện để phục vụ cho các luồng chính hoạt động ổn định. 2a,2b,2c có thể là bổ sung cho 2.1, 2.2 trong ảnh hoặc không. *


| **STT** | **Mô tả chi tiết** | **Đối tượng / Hệ thống** | **Ràng buộc** |
| --- | --- | --- | --- |
| 1 | Tài khoản GAPIT kết nối tới các AI Provider (OpenAI, Claude, Gemini, …) để thiết lập AI Gateway | GAPIT Admin / GAPIT System | API key phải được lưu trữ **bảo mật**, không chia sẻ cho hệ thống khác |
| 2 | GAPIT AI Gateway đồng bộ danh sách AI Provider và các Model khả dụng | GAPIT AI Gateway | Model chỉ được expose dưới dạng **logical model** |
| 2a | GAPIT AI Gateway cấu hình mapping Provider ↔ Model ↔ Token rule | GAPIT AI Gateway | Mỗi model phải có rule token riêng |
| 2b | GAPIT AI Gateway thiết lập quota và giới hạn token (GO-Token) theo License | GAPIT AI Gateway | Quota phải gắn với license, không gắn trực tiếp user |
| 2c | GAPIT AI Gateway cấp thông tin Gateway (endpoint, provider logic) cho hệ thống Gapone | GAPIT AI Gateway | Gapone **không nhận API key AI Provider** |
| 2d | GAPIT AI Gateway được thiết lập chế độ phân công model tự động theo quy tắc round-robin | GAPIT AI Gateway | Round-robin được kích hoạt khi user chọn trợ lý AI trong kịch bản tự động hóa. Model AI sẽ được phân công theo round-robin vào các session hội thoại. |
| 2e | Gapone Conversation cấu hình sử dụng AI thông qua GAPIT AI Gateway | Gapone Conversation | Chỉ được chọn **GAPIT** như AI Provider |
| 3 | Người dùng chọn nhà cung cấp là GAPITt trong Gapone Conversation. API sẽ tự động được call để kết nối tới GAPIT AI Gateway dựa theo license | End User / Gapone Conversation | Chỉ cho phép chọn nhà cung cấp GAPIT. Không được chọn model và nhập mã kết nối |
| 3a | Người dùng gửi nội dung hội thoại (prompt, context) | End User | Không can thiệp trực tiếp vào token |
| 3b | Gapone Conversation gửi AI request (model, license, prompt, context) tới GAPIT AI Gateway | Gapone Conversation | Chỉ gọi **1 gateway endpoint duy nhất** |
| 4 | GAPIT AI Gateway phản hồi | GAPIT AI Gateway | Yêu cầu phản hồi realtime hoặc càng nhanh càng tốt |
| 4a | GAPIT AI Gateway xác thực license, PO và trạng thái sử dụng | GAPIT AI Gateway | License hết hạn phải bị từ chối |
| 4b | GAPIT AI Gateway kiểm tra PO và giới hạn GO-Token (tương ứng bước 4.1) | GAPIT AI Gateway | Không cho phép vượt PO khả dụng (nếu vượt qua PO gần hết giới hạn mà người dùng đã mua thêm PO mới thì sẽ chạy tiếp, chưa mua sẽ ngưng chạy) |
| 4c | GAPIT AI Gateway từ chối request nếu PO không hợp lệ | GAPIT AI Gateway | Phải trả mã lỗi chuẩn hoá |
| 4d | GAPIT AI Gateway định tuyến request đến AI Provider tương ứng (tương ứng bước 4.2) | GAPIT AI Gateway | Routing do GAPIT AI Gateway kiểm soát hoàn toàn |
| 4e | AI Provider xử lý request và sinh phản hồi | AI Provider | Không nhận biết user hoặc license cuối |
| 4f | AI Provider trả về nội dung + token usage tương ứng với PO | AI Provider | Token usage phải đầy đủ cho billing |
| 5 | GAPIT ghi nhận token tiêu thụ theo request | GAPIT AI Gateway | Token phải được log chính xác |
| 5a | GAPIT AI Gateway trừ PO tương ứng với token đã dùng | GAPIT AI Gateway | Trừ quota phải đảm bảo atomic |
| 5b | Gapone xử lý các trường hợp lỗi (quota, token, provider down) | Gapone Conversation | Không retry trực tiếp AI Provider |
| 6 | GAPIT AI Gateway báo cáo | GAPIT AI Gateway | Kết quả báo cáo được hiển thị cho người dùng tại Gapone Conversation |
| 6a | GAPIT AI Gateway lưu log phục vụ billing & audit | GAPIT AI Gateway | Log không được chỉnh sửa thủ công |
| 6b | GAPIT AI Gateway ghi nhận tiêu thụ token đối soát với AI Provider để tiến hành thanh toán | GAPIT AI Gateway | Báo cáo lưu lại trong database. Có total sum rõ ràng từng mục và total sum tổng |
| 7 | AI provider đếm token đã tiêu thụ, tiến hành charge phí | AI Provider |  |
| 7a | GAPIT company tiến hành thanh toán. | GAPIT | Dựa trên tài khoản đã mở |



### 8.2. Định nghĩa & vai trò của GAPIT AI Gateway


**Định nghĩa**

**GAPIT** là hệ thống AI Gateway có thể nằm ẩn trong GAPONE CONVERSATION hoặc được xây dựng bên ngoài (Technical lead và team dev đánh giá độ khả thi của 2 phương án), hoạt động như một dịch vụ bên ngoài (external service), cung cấp API public và cơ chế xác thực riêng.

**Vai trò**

GAPIT đảm nhiệm các vai trò sau:

- **AI Gateway**: Trung gian xử lý toàn bộ request AI từ Gapone

- **Model Aggregator**: Tích hợp và quản lý nhiều model AI từ nhiều nhà cung cấp khác nhau

- **Auto Round-robin Assignment:** Tự động phân công các model AI vào những session cần xử lý

- **Quota Manager**: Phân bổ, giới hạn và giám sát quota sử dụng AI theo license/user

- **Billing & Token Tracking**: Ghi nhận token usage, phục vụ báo cáo và tính phí

- **PO**: Quản lý và chuyển đổi Token/quota sang Oder Purchase - Một dạng quản lý tài nguyên của Gapone,

Gapone không kết nối trực tiếp với AI Provider gốc khi sử dụng GAPIT.


### 8.3. Cấu hình AI khi sử dụng GAPIT



#### 8.3.1. Mô tả trường dữ liệu (bổ sung) khi user chọn nhà cung cấp GAPIT


Khi người dùng chọn **Nhà cung cấp AI = GAPIT**, hệ thống yêu cầu các thông tin sau:


| **Trường** | **Mô tả** |
| --- | --- |
| AI Provider | GAPIT (cố định) |
| GAPIT API Key | API key do GAPIT cấp cho license/user/org |
| Model AI | Hiển thị xám (không khả dụng), không cho phép người dùng lựa chọn |
| API key/mã kết nối | Hiển thị xám (không khả dụng), không cho phép người dùng lựa chọn |



#### **8.3.2. Giao diện minh họa:**



#### 8.4.3. GAPIT API Key


- GAPIT API Key được cấp bởi hệ thống GAPIT

- API key có thể được gắn với:

- License Gapone

- User

- Organization

- AI Instance

- Một license có thể có một hoặc nhiều GAPIT API key

- API key được sử dụng để:

- Xác thực request từ Gapone đến GAPIT

- Ghi nhận token usage

- Áp dụng quota và billing


### 8.4. Quản lý & phân phối Model AI



#### 8.4.1. Ràng buộc chung



| **Đối tượng/Hạng mục** | **Mô tả** | **Ghi chú bổ sung** |
| --- | --- | --- |
| Người dùng | Người dùng không có quyền lựa chọn model AI khi lựa chọn nhà cung cấp |  |
| Danh sách Model AI | - Được đánh giá bởi Business Analyst - Lựa chọn và cấu hình bởi đội Technical - Quản lý tập trung tại GAPIT AI Gateway |  |
| Quy tắc phân phối | Theo cơ chế Round-robin: - Mỗi request AI được gán cho một model trong danh sách model hợp lệ - Việc phân phối đảm bảo cân bằng tải, tối ưu chi phí, giảm phụ thuộc vào một model duy nhất | Linh hoạt trong một số trường hợp quá tải request tới AI, sắp hết token hoặc tối ưu khi test bằng limit free của các provider AI |
| Session hội thoại | - Mỗi session tại một thời điểm chỉ sử dụng một model AI - Một Model có thể cùng lúc xử lý nhiều session hội thoại - Xử lý liên tục trong một session hội thoại cho tới khi cuộc hội thoại** được đóng** (tự động bởi hệ thống khi khách không rep), khi **kích hoạt trường hợp AI từ chối trả lời **(3 điều kiện) và khi **người dùng thực can thiệp vào session hội thoại** đó. |  |



### 8.5. Quản lý PO & cảnh báo



#### 8.5.1. PO usage


- PO được tính và tổng hợp tại GAPIT AI Gateway

- PO được phân chia để cung cấp cho các doanh nghiệp khách hàng tại AdminJS và nối với GAPIT AI Gateway

- Gapone Conversation chỉ nhận trạng thái PO và usage metadata của PO đps


#### 8.5.2. Cảnh báo PO


- Khi PO sử dụng đạt **95%**, hệ thống hiển thị bảng cảnh báo

- Nội dung cảnh báo bao gồm:

- Mức PO đã sử dụng: Bạn đã sử dụng xx,xx% PO (Thường từ 95% trở lên)

- Thông báo sắp hết PO: Bạn sắp hết PO, vui lòng liên hệ bộ phận hỗ trợ khách hàng của GAPIT hoặc **Mua thêm PO**

- Nút **Mua thêm PO** (Cân nhắc phương thức mua, có thể tương lai mới triển khai)

- Nút **Liên hệ**


#### 8.5.3. Nút Liên hệ


- Hiển thị khi PO gần hết hoặc đã hết

- Nút Human Takeover/Liên hệ dẫn người dùng đến:

- Bộ phận Customer Service của GAPIT


### 8.6. Tracking & báo cáo



#### 8.6.1. Dữ liệu tracking


GAPIT cung cấp metadata cho mỗi request AI:

- Provider AI gốc

- Model AI

- Token input

- Token output

- Tổng token

- Thời gian xử lý

- Conversation ID


#### 8.6.2. Báo cáo trong Gapone


Gapone sử dụng dữ liệu từ GAPIT AI Gateway để xây dựng tính năng **Quản lý Token/Quản lý PO** (tách biệt khỏi Thiết lập AI):

- Báo cáo token theo:

- AI Provider (Gapit)

- Conversation

- User

- License

- PO còn laị

- Trạng thái PO

- Ngày mua PO

- Ngày hết hạn

- Báo cáo lịch sử sử dụng


### 8.7. Xử lý lỗi & mã lỗi



#### 8.7.1. Nguyên tắc thiết kế mã lỗi


- GAPIT trả về **mã lỗi chuẩn hóa** thông qua API public

- Gapone **không hiển thị trực tiếp lỗi từ AI Provider gốc** (OpenAI, Gemini, v.v.)

- Mọi lỗi từ GAPIT phải được mapping sang **mã lỗi nội bộ của Gapone**

- Thông báo cho người dùng phải:

- Rõ ràng

- Không lộ thông tin kỹ thuật nhạy cảm

- Một lỗi kỹ thuật có thể tương ứng với nhiều hành vi UI khác nhau (cảnh báo, block, fallback)


#### 8.7.2. Phân loại nhóm lỗi



| **Nhóm** | **Mô tả** |
| --- | --- |
| AUTH | Xác thực & phân quyền API key |
| QUOTA | Quota, token usage, billing |
| MODEL | Model AI, phân phối model |
| PROVIDER | Lỗi từ AI Provider gốc |
| NETWORK | Kết nối, timeout |
| SYSTEM | Lỗi nội bộ GAPIT |
| RATE_LIMIT | Giới hạn tần suất |
| DATA | Lỗi dữ liệu & request |



#### 8.7.3. Bảng mã lỗi chi tiết



| **Nhóm lỗi** | **Mã lỗi GAPIT AI Gateway** | **Mã lỗi Gapone** | **HTTP Code** | **Mô tả lỗi** | **Nguyên nhân phổ biến** | **Hành vi hệ thống Gapone** | **Hiển thị cho người dùng** | **Hành động đề xuất** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AUTH | GAPIT_AUTH_001 | AI_AUTH_INVALID_KEY | 401 | API Key không hợp lệ | Key sai, typo | Dừng xử lý request | API Key không hợp lệ | Nhập lại API Key |
| AUTH | GAPIT_AUTH_002 | AI_AUTH_KEY_EXPIRED | 401 | API Key hết hạn | Key bị thu hồi | Block AI | API Key đã hết hạn | Liên hệ CS GAPIT |
| AUTH | GAPIT_AUTH_003 | AI_AUTH_KEY_DISABLED | 403 | API Key bị vô hiệu hóa | Vi phạm điều khoản | Block AI | API Key bị khóa | Liên hệ CS GAPIT |
| AUTH | GAPIT_AUTHZ_001 | AI_AUTHZ_FORBIDDEN | 403 | Không đủ quyền truy cập | Key không có quyền | Block AI | Không có quyền sử dụng AI | Kiểm tra phân quyền |
| QUOTA | GAPIT_QUOTA_001 | AI_QUOTA_WARNING_80 | 200 | Quota đạt 80% | Token usage cao | Hiển thị cảnh báo nhẹ | Quota sắp hết | Theo dõi usage |
| QUOTA | GAPIT_QUOTA_002 | AI_QUOTA_WARNING_95 | 200 | Quota đạt 95% | Gần hết quota | Hiển thị cảnh báo mạnh | Quota sắp hết | Mua thêm quota |
| QUOTA | GAPIT_QUOTA_003 | AI_QUOTA_EXCEEDED | 402 | Hết quota | Vượt giới hạn token | Không gửi AI | Đã hết quota | Human Takeover |
| RATE_LIMIT | GAPIT_RATE_001 | AI_RATE_LIMITED | 429 | Quá nhiều request | Gửi request liên tục | Retry có kiểm soát | Hệ thống đang bận | Thử lại sau |
| MODEL | GAPIT_MODEL_001 | AI_MODEL_UNAVAILABLE | 503 | Model không khả dụng | Model downtime | Skip model | Đang xử lý | Tự động đổi model |
| MODEL | GAPIT_MODEL_002 | AI_MODEL_NOT_FOUND | 404 | Model không tồn tại | Model bị loại bỏ | Fallback model | Đang xử lý | Cập nhật cấu hình |
| MODEL | GAPIT_MODEL_003 | AI_MODEL_DEPRECATED | 410 | Model ngừng hỗ trợ | Model end-of-life | Fallback model | Đang xử lý | Thay thế model |
| PROVIDER | GAPIT_PROVIDER_001 | AI_PROVIDER_TIMEOUT | 504 | Provider timeout | Provider phản hồi chậm | Retry / fallback | Hệ thống đang bận | Thử lại |
| PROVIDER | GAPIT_PROVIDER_002 | AI_PROVIDER_ERROR | 502 | Lỗi từ provider | Lỗi nội bộ provider | Retry có kiểm soát | Hệ thống đang bận | Thử lại |
| NETWORK | GAPIT_NET_001 | AI_NETWORK_ERROR | 503 | Lỗi mạng | Mất kết nối | Retry theo policy | Mất kết nối | Kiểm tra mạng |
| DATA | GAPIT_DATA_001 | AI_INVALID_REQUEST | 400 | Request không hợp lệ | Payload sai | Dừng xử lý | Dữ liệu không hợp lệ | Kiểm tra input |
| DATA | GAPIT_DATA_002 | AI_CONTEXT_TOO_LARGE | 413 | Context quá lớn | Quá nhiều token input | Block request | Nội dung quá dài | Rút gọn nội dung |
| SYSTEM | GAPIT_SYS_001 | AI_SYSTEM_ERROR | 500 | Lỗi hệ thống GAPIT | Lỗi nội bộ | Dừng xử lý | Hệ thống gặp sự cố | Liên hệ CS GAPIT |
| SYSTEM | GAPIT_SYS_002 | AI_MAINTENANCE | 503 | Đang bảo trì | Maintenance | Block tạm thời | Đang bảo trì | Thử lại sau |



#### 8.7.4. Ghi chú triển khai


- Frontend chỉ nên hiển thị **cột “Hiển thị cho người dùng”**

- Backend sử dụng **Mã lỗi GAPIT + HTTP Code** để quyết định retry / fallback

- Log nội bộ phải lưu đầy đủ:

- GAPIT Error Code

- Provider gốc (nếu có)

- Model AI được gán

**Khả năng mở rộng**

- Bảng mã lỗi cho phép mở rộng thêm AI Provider mới mà không cần thay đổi Gapone

- Có thể tích hợp thêm SLA / Severity cho từng mã lỗi trong tương lai


### 8.8. Usecase



| **Use Case ID** | **Tên Use Case** | **Tác nhân chính** | **Mô tả** | **Điều kiện đầu vào** | **Kết quả mong muốn** | **Flow** |
| --- | --- | --- | --- | --- | --- | --- |
| UC-08-01 | Cấu hình AI với GAPIT | Admin / User có quyền cấu hình | Cho phép người dùng cấu hình AI Provider là GAPIT và nhập GAPIT API Key để sử dụng AI thông qua GAPIT | - Người dùng đã đăng nhập- Có quyền truy cập Thiết lập AI | - Cấu hình AI thành công với Provider = GAPIT- API Key hợp lệ được lưu | Người dùng chọn GAPIT → nhập API key → Gapone xác thực với GAPIT → lưu cấu hình |
| UC-08-02 | Gửi message AI thông qua GAPIT | Người dùng cuối | Xử lý message AI của người dùng thông qua GAPIT và nhận phản hồi từ AI | - AI đã cấu hình GAPIT- API key còn hiệu lực- Quota còn | - Phản hồi AI hiển thị cho người dùng- Token usage được ghi nhận | User gửi message → Gapone gửi GAPIT → GAPIT chọn model (round-robin) → gọi AI gốc → trả response |
| UC-08-03 | Phân phối model AI tự động (Round-robin) | Hệ thống (GAPIT) | Tự động phân công model AI cho từng request/hội thoại | - GAPIT có danh sách model hợp lệ | - Model được phân công cân bằng- Không phụ thuộc 1 model | GAPIT nhận request → chọn model theo round-robin → gán model cho conversation |
| UC-08-04 | Ghi nhận token usage & tracking | Hệ thống (GAPIT) | Ghi nhận và trả metadata token usage cho Gapone phục vụ báo cáo | - Request AI được xử lý thành công | - Token input/output được lưu- Dữ liệu sẵn sàng cho báo cáo | Sau khi có response AI → GAPIT ghi token → trả metadata cho Gapone |
| UC-08-05 | Cảnh báo quota 95% | Admin / User | Cảnh báo người dùng khi quota sử dụng AI đạt ngưỡng 95% | - Quota đạt ≥ 95% | - Hiển thị cảnh báo quota- Hiển thị CTA mua thêm & Human Takeover | GAPIT phát hiện ngưỡng → gửi trạng thái → Gapone hiển thị cảnh báo |
| UC-08-06 | Đề xuất mua thêm quota | Admin / User | Định hướng người dùng mua thêm quota khi sắp hết | - Đang ở trạng thái cảnh báo quota | - Người dùng được dẫn tới luồng mua thêm quota | User nhấn “Mua thêm quota” → điều hướng theo cấu hình |
| UC-08-07 | Human Takeover khi quota gần hết/hết | Admin / User | Chuyển người dùng sang CS GAPIT để hỗ trợ khi quota không đủ | - Quota gần hết hoặc đã hết | - Người dùng được kết nối CS GAPIT | User nhấn Human Takeover → chuyển sang CS GAPIT |
| UC-08-08 | Xử lý lỗi xác thực GAPIT | Hệ thống | Xử lý trường hợp GAPIT API Key không hợp lệ hoặc hết hạn | - API key sai / hết hạn | - Hiển thị lỗi rõ ràng- Không gửi request AI | Gapone gửi request → GAPIT trả lỗi → Gapone hiển thị lỗi |
| UC-08-09 | Xử lý model AI không khả dụng | Hệ thống (GAPIT) | Bỏ qua model lỗi và chuyển sang model khác | - Một model AI không phản hồi | - Request vẫn được xử lý nếu còn model khác | GAPIT detect lỗi → skip model → chọn model tiếp theo |


—--------------------------------------------------------------------------------------------------------------
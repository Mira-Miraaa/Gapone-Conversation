**SRS KHO KIẾN THỨC**

**--------------------------------------------------------**


# BẢNG GHI NHẬN THAY ĐỔI TÀI LIỆU



| **Ngày thay đổi** | **Vị trí** | **Lý do** | **Mô tả thay đổi** | **Phiên bản cũ** | **Phiên bản mới** |
| --- | --- | --- | --- | --- | --- |
| 30/09/2025 | Tạo mới |  |  |  | V1 |


--------------------------------------------------------


# BẢNG QUẢN LÝ TIẾN ĐỘ THỰC THI



| **Giai đoạn** | **Ngày bắt đầu** | **Phần mục** **Ghi chú** | **Phiên bản áp dụng ** |
| --- | --- | --- | --- |
|  |  |  | V0.1 |


--------------------------------------------------------


# MỤC LỤC



## 1. Xem danh sách kho kiến thức



### 1.1 Mô tả chức năng



| **Tên nghiệp vụ** | Xem danh sách các tài liệu kiến thức được thêm vào **Kho kiến thức** trong hệ thống |
| --- | --- |
| **Module** | Menu > Cài đặt > **Kho kiến thức** |
| **Mô tả** | Tính năng cho phép xem danh sách những tài liệu được tích hợp vào hệ thống. Có thể xem danh sách chi tiết các tài liệu hoặc xem theo nhóm. Danh sách tài liệu được tích hợp vào hệ thống, tên chính thức: “**Kiến thức**”, dựa theo thông tin cột bao gồm: + Tên tài liệu: Thể hiện tên tài liệu được tích hợp vào hệ thống + Định dạng: Thể hiện phân loại định dạng của tài liệu + Ngày tạo: thể hiện ngày tích hợp tài liệu này vào hệ thống + Người tạo: Thể hiện người dùng tích hợp tài liệu này vào hệ thống + Cột thao tác hiển thị icon thể hiện thao tác chọn hành động xoá |
| **Điều kiện cần để thực hiện hành động** | Người dùng được phân quyền Xem của chức năng "Kho kiến thức". Truy cập phân quyền người dùng tại mục Cài đặt > Thiết lập người dùng > Phân quyền. Truy cập **Kho kiến thức** tại Cài đặt > Kho kiến thức Quyền chức năng thiết lập người dùng như sau: - Quyền xem: thể hiện người dùng được phép xem toàn bộ danh sách tài liệu kết nối. |
| **Hành động** | Người dùng thực hiện theo các bước sau: **Bước 1:** Truy cập màn danh sách quản lý **Kho kiến thức** tại mục Cài đặt > Kho kiến thức Giao diện **Kho kiến thức** sẽ hiển thị. Giao diện sẽ bao gồm 2 tab là **Kiến thức** và **Nhóm kiến thức**. Mặc định hiển thị tab **Kiến thức** trước tiên. |
| **Kết quả** | Người dùng truy cập Xem được danh sách tài liệu có trong **Kho kiến thức **tạo tiền đề cho việc thực hiện thao tác Tạo mới, Xoá tài liệu theo đúng với quyền người dùng đã được thiết lập. |



### 1.2 Flow



### 1.3 Wireframe


1.3.1 Kiến thức (Danh sách tài liệu)

**Mô tả trường dữ liệu:**


| **STT** | **Tên trường dữ liệu** | **Kiểu dữ liệu** | **Mô tả** | **Ràng buộc / Ghi chú** |
| --- | --- | --- | --- | --- |
| 1 | **STT** | Integer | Số thứ tự hiển thị của từng tài liệu trong danh sách | - Tự động tăng theo thứ tự sắp xếp - Không cho phép chỉnh sửa thủ công |
| 2 | **Tên tài liệu** | String (255 ký tự) | Tên của tài liệu được tải lên kho kiến thức | - Bắt buộc không trống khi tải lên. Tự động điền theo tên tài liệu nếu có và nếu user không đặt tên tài liệu. (Trong trường hợp user nhập link và không hiện tên link, tự động điền link vào phần tên) - Không trùng lặp trong cùng nhóm kiến thức, nếu trùng, tự sinh số thứ tự tiếp theo (như cách lưu file trùng tên của MCS, GG doc, v..v..) |
| 3 | **Nhóm** | String (100 ký tự) | Tên nhóm mà tài liệu thuộc về (ví dụ: GapOne, Gapit…) | - Là trường bắt buộc - Liên kết với danh mục “Nhóm kiến thức” - Chỉ hiển thị các nhóm đang hoạt động |
| 4 | **Định dạng** | Enum (PDF, PowerPoint, Word, Excel, v.v.) Link | Loại định dạng file tài liệu | - Lấy từ phần mở rộng file khi tải lên - Không cho phép chỉnh sửa thủ công - Nếu file tải lên là link url, hiện “Link” |
| 5 | **Ngày tạo** | Date | Ngày tài liệu được tải lên hệ thống | - Tự động sinh theo ngày upload - Định dạng: DD/MM/YYYY |
| 6 | **Người tạo** | String (tên đăng nhập hoặc tên người dùng) | Tài khoản người dùng đã tải tài liệu lên | - Tự động ghi nhận từ tài khoản đăng nhập hiện tại - Liên kết đến bảng người dùng (User) |
| 7 | **Tìm kiếm tài liệu** | String (input) | Ô tìm kiếm tài liệu theo tên | - Cho phép tìm kiếm gần đúng (LIKE) - Không phân biệt hoa thường |
| 8 | **Tải lên** | Button | Nút chức năng để tải tài liệu mới lên kho kiến thức | - Khi nhấn → mở popup chọn file tải lên - Chỉ người có quyền “Quản lý kiến thức” được phép sử dụng |
| 9 | **Tác vụ (⋮)** | Action Menu | Menu tác vụ cho từng tài liệu (hiện tại gồm “Xóa”) | - Khi nhấn → mở danh sách hành động - Chỉ hiển thị “Xóa” cho người có quyền |
| 10 | **Xóa tài liệu** | Action | Chức năng xóa tài liệu khỏi kho kiến thức | - Hiển thị popup xác nhận trước khi xóa - Chỉ người có quyền “Quản trị viên”, “Người tạo” hoặc người dùng được cấp full quyền mới được phép xóa |



## 2. Tạo mới tài liệu kiến thức



### 2.1 Mô tả chức năng



| **Tên nghiệp vụ** | Tạo mới (thêm mới) tài liệu kiến thức vào **Kho kiến thức** trong hệ thống |
| --- | --- |
| **Module** | Menu > Cài đặt > **Kho kiến thức** |
| **Mô tả** | Tính năng cho phép tạo mới tài liệu vào **Kho kiến thức** trong hệ thống. Trigger: Nút “Tạo mới” trong tab giao diện **Kiến thức** Tạo mới tài liệu kiến thức bao gồm 2 bước thiết lập - Chọn nhóm kiến thức hoặc tạo mới nhóm kiến thức: Lựa chọn để gán tài liệu này vào một nhóm kiến thức để quản lý hoặc bỏ qua - Tải lên tài liệu kiến thức: Có 2 cách - Tải lên từ thiết bị - Nhập URL |
| **Điều kiện cần để thực hiện hành động** | Người dùng được phân quyền Tạo mới của chức năng "**Kho kiến thức**". Truy cập phân quyền người dùng tại mục Cài đặt > Thiết lập người dùng > Phân quyền. Truy cập **Kho kiến thức** tại Cài đặt > Kho kiến thức Quyền chức năng thiết lập người dùng như sau: - Quyền tạo mới: thể hiện người dùng được phép tạo mới tài liệu kiến thức. |
| **Hành động** | Người dùng thực hiện theo các bước sau: **Bước 1:** Truy cập màn danh sách quản lý **Kho kiến thức **tại mục Cài đặt > Kho kiến thức Giao diện **Kho kiến thức** sẽ hiển thị. Giao diện sẽ bao gồm 2 tab là **Kiến thức** và **Nhóm kiến thức**. Mặc định hiển thị tab **Kiến thức** trước tiên. Bước 2: Nhấp chọn “Tạo mới” tại tab giao diện **Kiến thức, **giao diện “**Tải lên tài liệu kiến thức**” sẽ được hiển thị Bước 3: Chọn Nhóm kiến thức chứa tài liệu này. Có thể tạo mới nhóm kiến thức hoặc bỏ qua bước này Bước 4: Tải lên tài liệu kiến thức bằng cách chọn từ thiết bị hoặc nhập URL Bước 5: Bấm “Lưu” để hoàn thành việc tải lên tài liệu kiến thức |
| **Kết quả** | Người dùng truy cập và tạo mới được thành công tài liệu vào **Kho kiến thức **tạo tiền đề cho việc thực hiện thao tác Xoá tài liệu theo đúng với quyền người dùng đã được thiết lập. |



### 2.2 Flow



### 2.3 Wireframe



### 2.4 Mô tả trường dữ liệu:



| **STT** | **Tên trường dữ liệu** | **Kiểu dữ liệu** | **Mô tả** | **Ràng buộc / Ghi chú** |
| --- | --- | --- | --- | --- |
| 1 | **Tên tài liệu** | Varchar(255) | Tên của tài liệu kiến thức Dùng để phân biệt với các tài liệu khác | - Bắt buộc không trống khi tải lên. - Không khả thi khi user chưa tải lên tài liệu. - Tự động điền theo tên tài liệu nếu có và nếu user không đặt tên tài liệu. (Trong trường hợp user nhập link và không hiện tên link, tự động điền link vào phần tên) - Cho phép chỉnh sửa lại. - Không trùng lặp trong cùng nhóm kiến thức, nếu trùng, tự sinh số thứ tự tiếp theo (như cách lưu file trùng tên của MCS, GG doc, v..v..) |
| 2 | **Nhóm kiến thức** | Dropdown List | Danh sách nhóm kiến thức hiện có trong hệ thống (ví dụ: GapOne, Gapit, Sản phẩm, Hướng dẫn, …) | - Là **trường không bắt buộc** - Dữ liệu lấy từ bảng “Nhóm kiến thức” - Nếu chưa có nhóm phù hợp, người dùng có thể tạo mới |
| 3 | **Tạo mới nhóm kiến thức** | Text Field | Cho phép người dùng tạo mới nhóm kiến thức khi chưa tồn tại trong danh sách | - Tùy chọn, không bắt buộc - Nếu người dùng nhập giá trị mới → hệ thống tạo bản ghi mới trong bảng “Nhóm kiến thức”. - Không được tạo trùng tên nhóm kiến thức. |
| 4 | **Chọn từ thiết bị** | File Upload | Chọn file tài liệu để tải lên từ thiết bị cá nhân | - Định dạng cho phép: PDF, DOCX, XLSX, PPTX - Dung lượng tối đa: 20 MB - Là **trường bắt buộc** nếu không nhập URL |
| 5 | **Nhập URL** | Text (URL format) | Cho phép nhập đường dẫn URL chứa tài liệu kiến thức online | - Là **trường bắt buộc** nếu không tải file từ thiết bị - URL phải hợp lệ (https:// hoặc http://) - Chỉ đọc trên trang được truy cập, không đọc thư mục con nếu là web. - Nếu URL là link web, chỉ đọc nội dung văn bản hiển thị trên trang web được nhập. Không hỗ trợ bài viết có tính phí, phải yêu cầu quyền truy cập - URL dẫn tới các trang tài liệu của các nền tảng khác (GG, notedoc, git, …) tạm thời pending chưa xử lý. |
| 6 | **Chuyển đổi** | Button | Nút dùng để chuyển đổi nội dung từ file hoặc URL | - Check URL hợp lệ mới cho phép lưu. - URL không hợp lệ hoặc không an toàn, hệ thống không cho lưu và hiện cảnh báo: “URL không hợp lệ. Cảnh báo rủi ro an toàn.” Người dùng phải nhập lại URL khác hợp lệ hoặc tải file. |
| 7 | **Hủy** | Button | Hủy thao tác tải lên, đóng popup | - Không lưu bất kỳ thay đổi nào |
| 8 | **Lưu** | Button | Lưu thông tin tài liệu kiến thức mới vào hệ thống | - Chỉ kích hoạt khi các trường bắt buộc đã hợp lệ - Ghi nhận người tạo và thời gian tải lên |



### 2.5 Ràng buộc hệ thống:


**Mối quan hệ:**


| **STT** | **Tên đối tượng (Entity)** | **Mối quan hệ với đối tượng khác** | **Loại quan hệ** | **Mô tả chi tiết mối quan hệ / Ràng buộc** |
| --- | --- | --- | --- | --- |
| 1 | **Tài liệu kiến thức (KnowledgeFile)** | ↔ **Nhóm kiến thức (KnowledgeGroup)** **Giới hạn 10 tài liệu** **Op2: 50 tài liệu** | N–1 (Nhiều tài liệu thuộc 1 nhóm) | Mỗi tài liệu kiến thức phải thuộc một nhóm kiến thức cụ thể. Khi nhóm bị xóa, có thể: - Cấm xóa nếu còn tài liệu. - Hoặc xóa kèm tất cả tài liệu trong nhóm (theo chính sách hệ thống). |
| 2 | **Tài liệu kiến thức (KnowledgeFile)** | ↔ **Người dùng (User)** | N–1 | Một người dùng có thể tạo nhiều tài liệu |
| 3 | **Tài liệu kiến thức (KnowledgeFile)** | ↔ **Tệp tin (File)** | 1–1 | Một bản ghi tài liệu kiến thức tương ứng với một file được tải lên hoặc một URL duy nhất. |
| 4 | **Tài liệu kiến thức (KnowledgeFile)** | ↔ **Trợ lý AI (AI Agent)** | N–M | Một tài liệu có thể được **nhiều trợ lý AI** sử dụng làm nguồn kiến thức, và ngược lại, một AI có thể dùng **nhiều tài liệu**. |
| 5 | **Nhóm kiến thức (KnowledgeGroup)** | ↔ **Người dùng (User)** | N–1 | Người dùng có thể tạo một hoặc nhiều nhóm kiến thức. Mỗi nhóm lưu thông tin người tạo. |
| 6 | **Tài liệu kiến thức (KnowledgeFile)** | ↔ **Lịch sử cập nhật (KnowledgeHistory)** | 1–N | Một tài liệu có thể được chỉnh sửa nhiều lần. Mỗi lần chỉnh sửa được ghi lại trong bảng lịch sử để theo dõi thay đổi nội dung, người chỉnh sửa, thời gian. |
| 7 | **Trợ lý AI (AI Agent)** | ↔ **Kho kiến thức (KnowledgeBase)** | 1–1 hoặc 1–0 | Trong hệ thống, mỗi AI Agent có thể được gán tới kho kiến thức hoặc không. (AI được gán tới toàn bộ tài liệu hoặc chọn lọc tài liệu trong kho kiến thức do người dùng tự thiết lập trong phần thiết lập AI) |
| 8 | **Tệp tin (File)** | ↔ **Bộ nhớ lưu trữ (Storage)** | N–1 | Nhiều file có thể được lưu trữ trên cùng một kho (server hoặc cloud). Khi file bị xóa khỏi Storage, bản ghi liên kết trong hệ thống cũng bị hủy hoặc đánh dấu “Không khả dụng”. |


**Ràng buộc hệ thống:**


| **STT** | **Loại ràng buộc** | **Mô tả** |
| --- | --- | --- |
| 1 | Giới hạn số tài liệu | Mỗi lần chỉ tải lên một tài liệu bằng URL hoặc tải file từ thiết bị |
| 2 | Giới hạn dung lượng tài liệu | 20Mb/1 tài liệu |
| 3 | Trường dữ liệu bắt buộc nhập | “Tải lên tài liệu kiến thức” là trường dữ liệu user bắt buộc nhập mới cho phép bấm lưu. “Tên tài liệu” là trường không được để trống nhưng không bắt buộc user nhập. Hệ thống cần tự đọc tên của file tài liệu hoặc URL (trong trường hợp không đọc được tên URL thì hiển thị link vào phần **Tên tài liệu** nếu người dùng để trống. Trong trường hợp |
| 4 | Quyền xem và khả năng truy cập | Khi người dùng nhấp chọn “Cài đặt>Kho kiến thức” nhưng chưa được quản trị viên phân quyền xem. => Toàn bộ giao diện** danh sách tài liệu kiến thức** và nút **Thêm tài liệu **được ẩn. Hiện text: “Hiện bạn chưa có quyền xem “Danh sách kịch bản tự động”, vui lòng liên hệ quản trị viên để được phân quyền. |



## 3. Xóa tài liệu kiến thức



### 3.1 Mô tả chức năng



| **Tên nghiệp vụ** | Xóa tài liệu đã tồn tại trong **Kho kiến thức** trên hệ thống |
| --- | --- |
| **Module** | Menu > Cài đặt > Kho kiến thức |
| **Mô tả** | Tính năng cho phép xóa AI đã được tích hợp vào hệ thống Gapone Conversation. Trigger: Nút “xóa” trong menu ẩn tại tab giao diện **Kiến thức** Người dùng hoàn thành việc xóa tài liệu thành công. Tài liệu bị xóa thành công khỏi hệ thống, đồng thời thông tin tài liệu trong bảng danh sách tài liệu tại **Kho kiến thức** cũng bị xóa bỏ. |
| **Điều kiện cần để thực hiện hành động** | Người dùng được phân quyền **Xóa** của chức năng "**Kho kiến thức**". Truy cập phân quyền người dùng tại mục Cài đặt > Thiết lập người dùng > Phân quyền. Truy cập thiết lập Kho kiến thức tại Cài đặt > Kho kiến thức Quyền chức năng thiết lập người dùng như sau: - Quyền xóa: thể hiện người dùng được phép xóa tài liệu trong hệ thống Có tài liệu hợp lệ đã tích hợp vào hệ thống. |
| **Hành động** | Người dùng thực hiện theo các bước sau: - Bước 1: Sau khi đăng nhập vào hệ thống, nhấp chọn “**Cài đặt**” trong thanh menu, sau đó click chọn “**Thiết lập Ai**” trong sub menu của **Cài đặt**, giao diện **Quản lý AI **sẽ xuất hiện. - Bước 2: Để thực hiện xóa AI ra khỏi hệ thống, nhấp chọn biểu tượng “**Xóa**” trong thanh menu ẩn tại màn giao diện **Quản lý AI**. - Bước 3: Ấn chọn "Xác nhận” để xác nhận và hoàn thành thao tác xoá/loại tài liệu kiến thức ra khỏi hệ thống. Ấn chọn "Quay lại" để huỷ thao tác xoá đang thực hiện. |
| **Kết quả** | Người dùng xóa một AI đã có trong hệ thống thành công khi thỏa mãn các điều kiện |



### 3.3 Wireframe



### 3.4 Mô tả trường dữ liệu



| **#** | **Thành phần** | **Kiểu dữ liệu** | **Ràng buộc hệ thống** | **Ghi chú** |
| --- | --- | --- | --- | --- |
| **1. Menu ẩn chứa các nút hành động** (Số nút hành động có thể tăng thêm khi hệ thống có cập nhật hạ tầng tính năng này) |  |  |  |  |
| **1.1** | **Nút Xóa** | Button | Khi click → hiển thị popup xác nhận xoá tài liệu | Là điều kiện kích hoạt modal |
| **2. Popup thông báo** |  |  |  |  |
| **2.1** | **Popup Thông báo** | Modal | Chỉ hiển thị khi người dùng click “Xóa” | Nội dung: “Bạn chắc chắn muốn xoá?” “Xóa tài liệu kiến thức có thể ảnh hưởng tới cách AI trả lời” |
| **2.2** | **Nút Quay lại (trong popup)** | Button | Đóng popup, không xoá dữ liệu | Không thay đổi dữ liệu |
| **2.3** | **Nút Xác nhận (trong popup)** | Button | Thực hiện xoá bản ghi tài liệu ra khỏi hệ thống | Nếu xoá thành công → hiển thị thông báo, refresh danh sách tài liệu trong tab giao diện **Kiến thức**, đồng thời xóa tài liệu ra khỏi nhóm kiến thức đã được gán vào |



### 3.5 Ràng buộc hệ thống



| **Trường hợp ràng buộc** | **Mô tả chức năng** | **Ràng buộc hệ thống** | **Thông báo hiển thị** | **Hành động của hệ thống** |
| --- | --- | --- | --- | --- |
| **1. Người dùng nhấn “Xóa”** | Khi người dùng chọn thao tác xóa từ danh sách tài liệu. | Bắt buộc hiển thị popup xác nhận trước khi thực hiện xóa. | — | Hiển thị popup: “Bạn chắc chắn muốn xóa?” “Xóa tài liệu kiến thức có thể ảnh hưởng tới cách AI trả lời” gồm 2 nút Quay lại và Xác nhận. |
| **2. Người dùng chọn “Xác nhận”** | Người dùng xác nhận thực hiện thao tác xóa. | - Hệ thống kiểm tra lại các ràng buộc quyền, liên kết nhóm và AI. - Nếu hợp lệ thì tiến hành xóa. | — | Gọi API DELETE /knowledge/{id} để xóa tài liệu khỏi hệ thống. |
| **3. Người dùng chọn “Quay lại”** | Người dùng hủy thao tác xóa. | — | — | Đóng popup, không thay đổi dữ liệu. |
| **4. Người dùng không có quyền xóa** | Kiểm tra quyền hạn người dùng khi thao tác xóa tài liệu trong kho kiến thức. | Chỉ người có vai trò Quản trị hệ thống hoặc Người tạo tài liệu mới có quyền xóa. | “Bạn không có quyền xóa tài liệu này.” | Dừng thao tác, không hiển thị popup xác nhận. |
| **5. Tài liệu đang được sử dụng trong nhóm kiến thức** | Tài liệu nằm trong 1 hoặc nhiều nhóm kiến thức khác. | Cho phép xóa | - | Hệ thống tự động gỡ liên kết tài liệu ra khỏi nhóm kiến thức |
| **6. Tài liệu đang được gán cho AI hoặc kịch bản tự động** | Tài liệu được AI hoặc kịch bản sử dụng làm dữ liệu huấn luyện / tham chiếu. | Cho phép xóa |  | Hệ thống tự động gỡ liên kết tài liệu ra khỏi AI. Cập nhật lại danh sách tài liệu trong thiết lập AI |
| **7. Xóa thành công** | Tài liệu được xóa hoàn tất khỏi kho kiến thức. | — | “Xóa tài liệu thành công.” | - Cập nhật lại danh sách tài liệu. - Ghi log thao tác xóa (thời gian, người thực hiện, ID tài liệu). |
| **8. Xóa thất bại do lỗi hệ thống hoặc kết nối mạng** | Khi hệ thống không thể xử lý yêu cầu xóa. | — | “Không thể xóa tài liệu. Vui lòng thử lại sau.” | Hiển thị thông báo lỗi, không thay đổi dữ liệu. |
| **8. Ghi log thông tin** | Ghi lại các thông tin về người xóa, thời gian xóa của tài liệu kiến thức được chọn xóa trong hệ thống | Ghi lại các thông tin người xóa, thời gian xóa của kịch bản được chọn xóa. => Gửi thông báo notification “[Tên User] đã xóa thành công [Tên kịch bản]” kèm giờ và ngày. (Phát triển sau, không phải sprint này) | “[Tên User] đã xóa thành công [Tên tài liệu]” HH:MM DD:MM:YYYY | Xóa tài liệu, ghi log, gửi thông báo |



## PENDING



## 4. Xem nhóm kiến thức



### 4.1 Mô tả chức năng



| **Tên nghiệp vụ** | Xem danh sách các nhóm tài liệu kiến thức được tạo mới trong **Kho kiến thức**. |
| --- | --- |
| **Module** | Menu > Cài đặt > **Kho kiến thức **> tab **Nhóm kiến thức** |
| **Mô tả** | Tính năng cho phép xem danh sách những **nhóm kiến thức (nhóm tài liệu)** được tạo mới trong hệ thống. Nhóm này bao gồm các tài liệu đã được tích hợp vào nhóm trước đó. Danh sách nhóm tài liệu được tích hợp vào hệ thống, tên chính thức: “**Nhóm kiến thức**”, dựa theo thông tin cột bao gồm: + Tên nhóm: Thể hiện tên nhóm kiến thức do người dùng đặt + Số lượng: Thể hiện số tài liệu có trong nhóm kiến thức này + Ngày tạo: thể hiện ngày tạo nhóm tài liệu này lần đầu + Ngày cập nhật:  thể hiện ngày gần nhất cập nhật/chỉnh sửa nhóm kiến thức này + Người tạo: Thể hiện người dùng tạo ra nhóm tài liệu này + Cột thao tác hiển thị icon thể hiện thao tác chọn hành động chỉnh sửa, xoá |
| **Điều kiện cần để thực hiện hành động** | Người dùng được phân quyền Xem của chức năng "Kho kiến thức". Truy cập phân quyền người dùng tại mục Cài đặt > Thiết lập người dùng > Phân quyền. Truy cập **Kho kiến thức** tại Cài đặt > Kho kiến thức Quyền chức năng thiết lập người dùng như sau: - Quyền xem: thể hiện người dùng được phép xem toàn bộ danh sách tài liệu kết nối và nhóm tài liệu |
| **Hành động** | Người dùng thực hiện theo các bước sau: **Bước 1:** Truy cập màn danh sách quản lý **Kho kiến thức** tại mục Cài đặt > Kho kiến thức Giao diện **Kho kiến thức** sẽ hiển thị. Giao diện sẽ bao gồm 2 tab là **Kiến thức** và **Nhóm kiến thức**. Mặc định hiển thị tab **Kiến thức** trước tiên. Nhấp chọn tab **Nhóm kiến thức. ** |
| **Kết quả** | Người dùng truy cập Xem được danh sách **Nhóm kiến thức **có trong **Kho kiến thức **tạo tiền đề cho việc thực hiện thao tác Tạo mới, Chỉnh sửa, Xoá nhóm kiến thức theo đúng với quyền người dùng đã được thiết lập. |



### 4.3 Wireframe



### 4.4 Mô tả trường dữ liệu



| **STT** | **Tên trường** | **Kiểu dữ liệu** | **Mô tả chức năng** | **Ràng buộc / Ghi chú** |
| --- | --- | --- | --- | --- |
| 1 | **Tab “NHÓM KIẾN THỨC”** | Tab button (active) | Hiển thị danh sách nhóm kiến thức đang được quản lý | Là tab giao diện quản lý **Nhóm kiến thức** |
| 2 | **Tìm kiếm nhóm kiến thức** | Textbox (input) | Cho phép nhập từ khóa để tìm nhanh nhóm kiến thức theo tên | Không bắt buộc nhập; lọc động danh sách theo ký tự gõ vào |
| 3 | **Cột STT** | Number | Hiển thị số thứ tự của từng nhóm kiến thức trong danh sách | Tự động tăng, không chỉnh sửa |
| 4 | **Cột Tên nhóm** | Text | Tên của nhóm kiến thức (VD: GapOne, Gapit, v.v.) | Không trùng lặp giữa các nhóm |
| 5 | **Cột Số lượng** | Number | Số lượng tài liệu nằm trong nhóm kiến thức đó | Tự động đếm theo số tài liệu được gán vào nhóm |
| 6 | **Cột Ngày tạo** | Date | Ngày nhóm kiến thức được tạo | Định dạng: DD/MM/YYYY – không cho phép sửa thủ công |
| 7 | **Cột Ngày cập nhật** | Date | Ngày gần nhất nhóm kiến thức có thay đổi (thêm/xóa tài liệu, đổi tên, …) | Tự động cập nhật khi nhóm có thay đổi |
| 8 | **Cột Người tạo** | Text | Tên tài khoản tạo nhóm kiến thức | Lấy từ thông tin người dùng đang đăng nhập |
| 9 | **Nút “Tạo mới”** | Button | Mở form để thêm nhóm kiến thức mới | Khi nhấn mở pop-up hoặc màn “Tạo nhóm kiến thức” |
| 10 | **Biểu tượng “Ba chấm dọc” (⋮)** | Icon button | Hiển thị menu thao tác của từng nhóm | Gồm 2 hành động: “Chỉnh sửa” và “Xóa” |
| 11 | **Tùy chọn “Chỉnh sửa”** | Action | Cho phép người dùng sửa tên nhóm hoặc cập nhật thông tin nhóm | Chỉ hiển thị với người có quyền quản lý nhóm kiến thức |
| 12 | **Tùy chọn “Xóa”** | Action | Cho phép xóa nhóm kiến thức khỏi hệ thống | Có cảnh báo xác nhận trước khi xóa (vì có thể ảnh hưởng đến AI đang sử dụng nhóm đó) |



### 4.5 Ràng buộc hệ thống



| **STT** | **Ràng buộc** | **Mô tả chi tiết** |
| --- | --- | --- |
| 1 | Tự động cập nhật số lượng tài liệu | Trường “Số lượng” thay đổi tự động khi tài liệu được thêm hoặc xóa khỏi nhóm. |
| 2 | Chỉ người có quyền quản trị hoặc tạo nhóm mới được chỉnh sửa/xóa | Kiểm tra quyền truy cập theo vai trò (Role-based Access Control). |
| 3 | Ngày cập nhật thay đổi tự động | Mỗi khi chỉnh sửa tên hoặc thêm/xóa tài liệu, ngày cập nhật sẽ tự động ghi lại thời gian hiện tại. |



### 4.6 Use case



## 5. Tạo mới nhóm kiến thức



## 5.1 Mô tả chức năng



### 5.3 Wireframe



### 5.4 Mô tả trường dữ liệu



| **STT** | **Tên trường** | **Kiểu dữ liệu** | **Mô tả** | **Ràng buộc** |
| --- | --- | --- | --- | --- |
| 1 | **Tên nhóm** | String (text) | Tên của nhóm kiến thức được tạo mới, giúp phân loại tài liệu. | - Bắt buộc nhập (Required) - Không trùng với tên nhóm đã tồn tại - Giới hạn độ dài: 1–100 ký tự |
| 2 | **Kiến thức - Ô tìm kiếm** | String (text) | Cho phép người dùng nhập tên tài liệu kiến thức cần tìm để thêm vào nhóm. | - Không bắt buộc - Tự động gợi ý (Autocomplete) theo danh sách tài liệu có sẵn |
| 3 | **Kiến thức - Danh sách chọn** | Dropdown (list) | Danh sách các tài liệu kiến thức có thể thêm vào nhóm. | - Không bắt buộc - Dữ liệu lấy từ kho tài liệu hiện có |
| 4 | **Nút Hủy** | Button | Hủy thao tác tạo nhóm và đóng cửa sổ. | - Không lưu dữ liệu khi nhấn - Trả về màn hình trước đó |
| 5 | **Nút Lưu** | Button | Lưu thông tin nhóm kiến thức mới. | - Chỉ hoạt động khi trường “Tên nhóm” hợp lệ - Thực hiện ghi dữ liệu vào hệ thống và làm mới danh sách nhóm |



### 5.5 Ràng buộc hệ thống



### 5.6 Use case



## 6. Cập nhật / chỉnh sửa nhóm kiến thức



## 6.1 Mô tả chức năng



### 6.2 Flow



### 6.3 Wireframe



### 6.4 Mô tả trường dữ liệu



### 6.5 Ràng buộc hệ thống



### 6.6 Use case



## 7. Xóa nhóm kiến thức



## 7.1 Mô tả chức năng



### 7.2 Flow



### 7.3 Wireframe



### 7.4 Mô tả trường dữ liệu



### 7.5 Ràng buộc hệ thống



### 7.6 Use case

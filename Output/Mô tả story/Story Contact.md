# EPIC & USER STORIES – MODULE LIÊN HỆ (CONTACT)

**Tài liệu tham chiếu SRS:** SRS Contact.md
**Người tạo:** AI Agent (create-story skill)
**Ngày tạo:** 02/07/2026
**Phiên bản:** 1.0

---

## 📊 Tổng quan Backlog

```
📊 Tổng quan Backlog:
├── Tổng số Epics: 7
├── Tổng số User Stories: 9
├── Tổng Story Points: 35
├── Phân bổ Priority:
│   ├── Must Have: 6 stories (23 points)
│   ├── Should Have: 3 stories (12 points)
│   ├── Could Have: 0 stories
│   └── Won't Have: Import Contact (phát triển sau)
└── Dependencies Map: Không có vòng lặp
```

---

## EPIC-CON-01 – Danh sách Liên hệ (Contact List)

**Mô tả:** Tính năng xem và tương tác với toàn bộ danh sách liên hệ khách hàng từ menu trái của hệ thống.

---

### US-CON-01 – Xem danh sách Liên hệ tổng quan

**Epic:** EPIC-CON-01
**Module:** Liên hệ (Contact List)
**Priority:** Must Have
**Story Points:** 3

#### Mô tả (User Story Format)
> **As a** người dùng hệ thống (Agent/Admin),
> **I want** xem danh sách tất cả Liên hệ với đầy đủ thông tin (STT, ID, Họ tên, Email, SĐT, Ngày sinh, Địa chỉ, Ngày tạo, Hành động),
> **So that** tôi có thể tra cứu và quản lý thông tin khách hàng nhanh chóng.

#### Mô tả chi tiết
Khi người dùng chọn "Liên hệ" từ Left Menu, hệ thống hiển thị bảng danh sách phân trang 25/50/100 bản ghi/trang. Mặc định sắp xếp theo thời gian tạo (mới nhất lên đầu). Header cố định, scroll bar dọc bên trong bảng. Dữ liệu đồng bộ hai chiều giữa GapOne và GapOne Conversation.

#### Acceptance Criteria
- [ ] **AC1:** Given người dùng có quyền xem Liên hệ, When click "Liên hệ" từ Left Menu, Then bảng danh sách hiển thị với đủ cột: STT, ID, Họ và tên, Email, SĐT, Ngày sinh, Địa chỉ, Ngày tạo, Hành động.
- [ ] **AC2:** Given bảng đang hiển thị, When scroll, Then header vẫn cố định, scroll bar dọc hiện bên phải bảng.
- [ ] **AC3:** Given không có dữ liệu, Then hiển thị "No data available".
- [ ] **AC4:** Given mặc định, Then dữ liệu sắp xếp mới nhất lên đầu; 25 bản ghi/trang với option 25/50/100.
- [ ] **AC5:** Given nội dung cột quá dài, Then hiển thị "…" + tooltip khi hover (áp dụng cho: Họ và tên, Email, SĐT, Địa chỉ, Ngày tạo).
- [ ] **AC6:** Given click tiêu đề cột Họ tên/Email/SĐT/Ngày tạo, Then hệ thống sort (đơn, mặc định A-Z).

#### Business Rules
- Dữ liệu đồng bộ hai chiều qua Shared Contact DB.
- STT bắt đầu từ 1, tăng dần qua các trang.
- ID theo quy tắc sinh ID của GapOne, luôn hiển thị 1 dòng.
- Phân trang tương tự trang Automation.

#### Dependencies
- Không có

#### Technical Notes
- API: `GET /api/contacts?page=&limit=&sort=`
- Responsive theo kích thước màn hình.

#### Ghi chú từ SRS
- **Tham chiếu SRS:** Mục I. Contact list – 2.3. Chi tiết (No 7–15)

---

### US-CON-02 – Tìm kiếm Liên hệ theo tên, email, số điện thoại

**Epic:** EPIC-CON-01
**Module:** Liên hệ (Contact List)
**Priority:** Must Have
**Story Points:** 2

#### Mô tả (User Story Format)
> **As a** người dùng hệ thống,
> **I want** tìm kiếm liên hệ real-time theo tên, email hoặc SĐT bằng thanh tìm kiếm,
> **So that** tôi nhanh chóng tìm đúng khách hàng cần thao tác.

#### Mô tả chi tiết
Thanh tìm kiếm hỗ trợ tìm tương đối (LIKE), không phân biệt hoa thường, dùng OR giữa 3 trường. Trim đầu cuối trước khi tìm; nếu rỗng sau trim thì không tìm. Click vào ô thì con trỏ trỏ về cuối chuỗi.

#### Acceptance Criteria
- [ ] **AC1:** Given nhập từ khóa vào ô tìm kiếm (real-time), Then hiển thị các Liên hệ có tên, email hoặc SĐT chứa từ khóa.
- [ ] **AC2:** Given từ khóa có khoảng trắng đầu/cuối, Then trim trước khi tìm; nếu sau trim rỗng thì không tìm.
- [ ] **AC3:** Given không có kết quả phù hợp, Then hiển thị "No data available".
- [ ] **AC4:** Given chuỗi tìm kiếm dài hơn ô, Then truncate + tooltip khi hover.

#### Business Rules
- Tìm theo OR: tên khách hàng | email | SĐT.
- Không phân biệt chữ hoa/thường.

#### Dependencies
- US-CON-01

#### Technical Notes
- API: `GET /api/contacts?q=`

#### Ghi chú từ SRS
- **Tham chiếu SRS:** Mục I. Contact list – 2.3. Chi tiết (No 3)

---

## EPIC-CON-02 – Lọc Nâng Cao (Advanced Filter)

**Mô tả:** Cho phép lọc liên hệ theo nhiều tiêu chí kết hợp với toán tử điều kiện linh hoạt.

---

### US-CON-03 – Mở và đóng bộ lọc nâng cao

**Epic:** EPIC-CON-02
**Module:** Liên hệ – Advanced Filter
**Priority:** Should Have
**Story Points:** 2

#### Mô tả (User Story Format)
> **As a** người dùng hệ thống,
> **I want** mở/đóng menu lọc nâng cao,
> **So that** tôi chọn tiêu chí lọc linh hoạt mà không làm rối giao diện chính.

#### Acceptance Criteria
- [ ] **AC1:** Given click nút "Lọc nâng cao", Then menu dropdown hiển thị; icon mũi tên xoay ngược 180 độ.
- [ ] **AC2:** Given menu đang mở, When click ra ngoài hoặc click lại nút, Then menu đóng; icon trở về mặc định.
- [ ] **AC3:** Given menu đang mở và người dùng scroll danh sách tiêu chí, Then ô tìm kiếm tiêu chí vẫn sticky (cố định) ở đầu.

#### Business Rules
- Nút "Lọc nâng cao" luôn enabled.
- Phân quyền dữ liệu: User chỉ xem dữ liệu mình tạo/phụ trách; Admin xem tất cả.

#### Dependencies
- US-CON-01

#### Technical Notes
- Field list lấy từ toàn bộ trường bảng Contact, hiển thị theo alphabet A-Z.

#### Ghi chú từ SRS
- **Tham chiếu SRS:** Mục II. Advanced filter – 2. Chi tiết (No 1, 3)

---

### US-CON-04 – Thiết lập điều kiện lọc với toán tử linh hoạt

**Epic:** EPIC-CON-02
**Module:** Liên hệ – Advanced Filter
**Priority:** Should Have
**Story Points:** 5

#### Mô tả (User Story Format)
> **As a** người dùng hệ thống,
> **I want** chọn tiêu chí lọc, toán tử điều kiện và nhập giá trị tương ứng,
> **So that** tôi lọc liên hệ theo đúng điều kiện nghiệp vụ cần thiết.

#### Mô tả chi tiết
Chọn field → tạo Filter Tag "Chưa lọc". Click vào phần trạng thái của tag → mở Popup cấu hình chi tiết. Popup có dropdown toán tử (phụ thuộc kiểu dữ liệu) và ô nhập giá trị. Click "Chọn" → cập nhật nhãn tag. Gửi server khi nhấn "Tìm kiếm" hoặc Enter.

#### Acceptance Criteria
- [ ] **AC1:** Given chọn field từ dropdown, Then Filter Tag hiển thị "[Tên Field]: Chưa lọc".
- [ ] **AC2:** Given click vào phần trạng thái của tag, Then popup cấu hình chi tiết xuất hiện.
- [ ] **AC3:** Given field kiểu text, Then toán tử: Có dữ liệu, Không có dữ liệu, Bằng, Chứa giá trị, Không chứa, Bắt đầu bằng, Kết thúc bằng.
- [ ] **AC4:** Given field kiểu number, Then toán tử: Có dữ liệu, Không có dữ liệu, Bằng, Không bằng, Lớn hơn, Nhỏ hơn, Lớn hơn hoặc bằng, Nhỏ hơn hoặc bằng, Trong khoảng, Ngoài khoảng.
- [ ] **AC5:** Given field kiểu date/datetime, Then toán tử: Có dữ liệu, Không có dữ liệu, Trong khoảng, Trước, Sau, Trước thời điểm, Sau thời điểm.
- [ ] **AC6:** Given chọn toán tử "Có dữ liệu" hoặc "Không có dữ liệu", Then ô nhập giá trị bị disable (nền xám).
- [ ] **AC7:** Given click "Chọn" mà ô điều kiện để trống (khi bắt buộc nhập), Then inline message: "Chưa chọn giá trị".
- [ ] **AC8:** Given click "Chọn" hợp lệ, Then tag cập nhật nhãn (VD: "Email: Bằng 'abc@gmail.com'"); popup đóng.
- [ ] **AC9:** Given click icon X trên tag, Then tag bị xóa ngay lập tức.
- [ ] **AC10:** Given không có tag nào, Then nút "Xóa bộ lọc" ẩn; khi có >=1 tag thì nút hiển thị cuối hàng.

#### Business Rules
- Tất cả Filter Tag kết hợp bằng **OR**.
- Dữ liệu gửi server khi nhấn "Tìm kiếm" hoặc Enter.
- Ô nhập giá trị max 255 ký tự; trim đầu cuối.
- Số: chỉ 0-9; auto format (VD: 678678 → 678.678).
- Date picker: format dd/MM/yyyy.

#### Dependencies
- US-CON-03

#### Technical Notes
- Filter Tag wrap xuống dòng khi vượt độ rộng màn hình.

#### Ghi chú từ SRS
- **Tham chiếu SRS:** Mục II. Advanced filter – 2. Chi tiết (No 4–9)

---

## EPIC-CON-03 – Tạo Mới Liên Hệ

**Mô tả:** Cho phép tạo mới một liên hệ vào hệ thống.

---

### US-CON-05 – Tạo mới Liên hệ

**Epic:** EPIC-CON-03
**Module:** Liên hệ – Form tạo mới
**Priority:** Must Have
**Story Points:** 5

#### Mô tả (User Story Format)
> **As a** người dùng hệ thống,
> **I want** tạo mới liên hệ bằng form với các thông tin: tên, SĐT, email, ngày sinh, giới tính, địa chỉ, ảnh đại diện, công ty, vị trí, sale phụ trách,
> **So that** thông tin khách hàng mới được lưu vào hệ thống để phục vụ CSKH.

#### Acceptance Criteria
- [ ] **AC1:** Given click "Tạo Liên hệ", Then form hiển thị tiêu đề "Liên hệ mới".
- [ ] **AC2:** Given để trống "Tên" và click "Lưu", Then inline message: "Tên là bắt buộc".
- [ ] **AC3:** Given để trống "Số điện thoại" và click "Lưu", Then inline message: "Số điện thoại là bắt buộc".
- [ ] **AC4:** Given nhập SĐT đã tồn tại và click "Lưu", Then inline message: "Số điện thoại đã tồn tại".
- [ ] **AC5:** Given trường SĐT, When nhập ký tự không phải 0-9, Then hệ thống chặn (max 15 ký tự).
- [ ] **AC6:** Given để trống Email và click "Lưu", Then inline message: "Email là bắt buộc".
- [ ] **AC7:** Given email sai format, When click "Lưu", Then inline message: "Email chưa đúng định dạng".
- [ ] **AC8:** Given email đã tồn tại, When click "Lưu", Then inline message: "Email đã tồn tại".
- [ ] **AC9:** Given điền đầy đủ hợp lệ, When click "Lưu", Then lưu thành công; toast "Tạo liên hệ thành công" (4 giây, góc phải trên); quay về danh sách.
- [ ] **AC10:** Given lưu thất bại, Then toast "Tạo liên hệ không thành công. Vui lòng thử lại sau."; giữ nguyên form.
- [ ] **AC11:** Given timeout, Then toast "Lỗi hệ thống. Vui lòng thử lại sau."
- [ ] **AC12:** Given upload ảnh đại diện > 5MB hoặc có định dạng khác .jpg, .png, .jpeg, When upload, Then hệ thống từ chối và hiển thị inline message: "Chỉ cho phép các định dạng sau: .jpg, .png, .jpeg".

#### Business Rules
- Bắt buộc (*): Tên (max 50), SĐT (max 15, chỉ 0-9), Email (max 255, format: a-z/0-9/./−/@).
- Không bắt buộc: Họ tên đệm (max 50), Ngày sinh (dd/MM/yyyy), Giới tính (default Nam), Địa chỉ, Địa chỉ tạm trú (max 100), Ảnh (max 5MB, định dạng: .jpg, .png, .jpeg. Helper/Placeholder text: "Chỉ cho phép các định dạng sau: .jpg, .png, .jpeg"), Công ty, Vị trí (max 50).
- Sale phụ trách: default account login; không được bỏ trống; chọn 1.
- Trim đầu cuối trước khi lưu; nếu sau trim rỗng thì không lưu (trừ bắt buộc sẽ báo lỗi).
- Check trùng SĐT và Email toàn hệ thống.

#### Dependencies
- US-CON-01

#### Technical Notes
- API: `POST /api/contacts`

#### Ghi chú từ SRS
- **Tham chiếu SRS:** Mục III. Creating the contact – 2.3. Chi tiết (No 1–15). Định dạng ảnh đại diện đã được làm rõ là .jpg, .png, .jpeg.

---

## EPIC-CON-04 – Cập Nhật Liên Hệ

**Mô tả:** Cho phép chỉnh sửa thông tin liên hệ đã có trong hệ thống.

---

### US-CON-06 – Chỉnh sửa thông tin Liên hệ

**Epic:** EPIC-CON-04
**Module:** Liên hệ – Form chỉnh sửa
**Priority:** Must Have
**Story Points:** 3

#### Mô tả (User Story Format)
> **As a** người dùng hệ thống,
> **I want** chỉnh sửa thông tin liên hệ hiện có bằng click icon Edit trong danh sách,
> **So that** thông tin khách hàng luôn được cập nhật chính xác.

#### Acceptance Criteria
- [ ] **AC1:** Given click icon Edit trên bản ghi, Then form hiển thị tiêu đề "Chỉnh sửa liên hệ" với dữ liệu hiện tại điền sẵn.
- [ ] **AC2:** Given form chỉnh sửa, Then validate áp dụng đầy đủ như US-CON-05 (bắt buộc, trùng, format, trim...).
- [ ] **AC3:** Given lưu thành công, Then toast "Chỉnh sửa liên hệ thành công" và quay về danh sách.
- [ ] **AC4:** Given click "Hủy", Then quay về danh sách không lưu thay đổi; không hiện popup confirm.

#### Business Rules
- Check trùng SĐT/Email ngoại trừ với chính bản ghi đang sửa.
- Toast: 4 giây, góc phải trên.

#### Dependencies
- US-CON-01, US-CON-05

#### Technical Notes
- API: `PUT /api/contacts/{id}`

#### Ghi chú từ SRS
- **Tham chiếu SRS:** Mục IV. Updating the contact – 2.3. Chi tiết (No 1–15)

---

## EPIC-CON-05 – Xem Chi Tiết qua SSO

**Mô tả:** Điều hướng người dùng từ GapOne Conversation sang trang Profile của GapOne bằng SSO.

---

### US-CON-07 – Xem Profile khách hàng qua SSO

**Epic:** EPIC-CON-05
**Module:** Liên hệ – SSO Profile
**Priority:** Must Have
**Story Points:** 8

#### Mô tả (User Story Format)
> **As a** người dùng GapOne Conversation,
> **I want** click ID hoặc Họ và tên của liên hệ để mở Profile trên GapOne ở tab mới mà không cần đăng nhập lại,
> **So that** tôi xem đầy đủ thông tin khách hàng nhanh chóng và bảo mật.

#### Acceptance Criteria
- [ ] **AC1:** Given người dùng có quyền xem Liên hệ, When vào menu Liên hệ, Then trường ID và Họ và tên hiển thị dạng hyperlink.
- [ ] **AC2:** Given click vào ID hoặc Họ và tên, Then mở Profile đúng liên hệ trên tab mới; không phải đăng nhập lại.
- [ ] **AC3:** Given phiên đăng nhập còn hiệu lực, Then không yêu cầu đăng nhập lại khi mở Profile.
- [ ] **AC4:** Given có quyền, Then hiển thị Profile; Given không có quyền, Then hiển thị "Bạn không có quyền truy cập chức năng này."
- [ ] **AC5:** Given Contact không tồn tại trên GapOne, Then hiển thị "Không tìm thấy hồ sơ khách hàng."
- [ ] **AC6:** Given SSO Token hết hạn/không hợp lệ, Then xử lý theo cơ chế SSO đã cấu hình.
- [ ] **AC7:** Given GapOne Conversation không tạo được xác thực SSO, Then không mở Profile; hiển thị "Lỗi hệ thống. Vui lòng thử lại sau."
- [ ] **AC8:** Given GapOne timeout/không phản hồi, Then hiển thị "Lỗi hệ thống. Vui lòng thử lại sau."
- [ ] **AC9:** Given mở Profile, Then Profile hiển thị đúng Contact ID đã chọn.
- [ ] **AC10:** Given click hyperlink, Then Profile mở tab mới; tab GapOne Conversation hiện tại không reload.
- [ ] **AC11:** Given click nhiều lần liên tiếp vào cùng 1 liên hệ, Then chỉ xử lý 1 yêu cầu; tránh mở nhiều tab.
- [ ] **AC12:** Given trình duyệt chặn mở tab mới, Then người dùng vẫn ở màn hình hiện tại; hành vi thông báo theo trình duyệt/quy định hệ thống.

#### Business Rules
- Sử dụng short-lived token xác thực chéo.
- Phân quyền theo quy tắc GapOne.
- Chỉ xử lý 1 yêu cầu khi click nhiều lần.

#### Dependencies
- US-CON-01
- Hệ thống GapOne (SSO phải được cấu hình)

#### Technical Notes
- Mở tab mới: `window.open(url, '_blank')`.
- Cần debounce/flag để tránh click nhiều lần.

#### Ghi chú từ SRS
- **Tham chiếu SRS:** Mục V. Viewing the contact – 3. Tiêu chí chấp nhận (AC-01 đến AC-13)

---

## EPIC-CON-06 – Xóa Liên Hệ

**Mô tả:** Cho phép xóa liên hệ khỏi hệ thống sau xác nhận.

---

### US-CON-08 – Xóa Liên hệ

**Epic:** EPIC-CON-06
**Module:** Liên hệ – Xóa
**Priority:** Must Have
**Story Points:** 2

#### Mô tả (User Story Format)
> **As a** người dùng hệ thống,
> **I want** xóa liên hệ qua popup xác nhận,
> **So that** danh sách liên hệ luôn được giữ sạch và chính xác.

#### Acceptance Criteria
- [ ] **AC1:** Given click icon Delete, Then popup xác nhận hiển thị: tiêu đề "Xóa liên hệ", nội dung "Bạn có chắc muốn xóa?", nút "Hủy" và "Đồng ý".
- [ ] **AC2:** Given click "Hủy"/icon X/click ngoài popup, Then popup đóng; không xóa; không hiện confirm thêm.
- [ ] **AC3:** Given click "Đồng ý" thành công, Then toast "Xóa liên hệ thành công" (4 giây, góc phải trên); quay về danh sách.
- [ ] **AC4:** Given click "Đồng ý" thất bại (lỗi server), Then toast "Xóa liên hệ không thành công. Vui lòng thử lại sau."; quay về danh sách.
- [ ] **AC5:** Given liên hệ đã có đơn hàng liên quan, When click "Đồng ý", Then không xóa; hiển thị "Khách hàng đã có đơn hàng, bạn không thể xóa."

#### Business Rules
- Không confirm khi click "Hủy" hay click ngoài popup.
- Toast: 4 giây, góc phải trên.
- Dù thành công hay thất bại đều quay về danh sách.

#### Dependencies
- US-CON-01

#### Technical Notes
- API: `DELETE /api/contacts/{id}`
- Cần kiểm tra ràng buộc dữ liệu (đơn hàng) trước khi xóa.

#### Ghi chú từ SRS
- **Tham chiếu SRS:** Mục VI. Deleting the contact – 2.3. Chi tiết (No 1–5)

---

## EPIC-CON-07 – Xuất Dữ Liệu Liên Hệ (Export)

**Mô tả:** Cho phép xuất danh sách liên hệ ra file Excel với các tùy chọn phạm vi dữ liệu.

---

### US-CON-09 – Xuất file Excel danh sách Liên hệ

**Epic:** EPIC-CON-07
**Module:** Liên hệ – Export
**Priority:** Should Have
**Story Points:** 5

#### Mô tả (User Story Format)
> **As a** người dùng hệ thống,
> **I want** xuất danh sách liên hệ ra file Excel với 3 tùy chọn: theo bộ lọc hiện tại, theo trang hiện tại, hoặc toàn bộ,
> **So that** tôi phân tích dữ liệu khách hàng offline hoặc chia sẻ với các bộ phận liên quan.

#### Acceptance Criteria
- [ ] **AC1:** Given click nút "Export", Then popup "Xuất file Excel danh sách khách hàng" hiển thị với 3 radio button và nút Cancel/Export Excel.
- [ ] **AC2:** Given chọn "Theo kết quả bộ lọc hiện tại" (mặc định), When click "Export Excel", Then xuất toàn bộ dữ liệu thỏa điều kiện filter (tất cả trang).
- [ ] **AC3:** Given không áp dụng bộ lọc, When chọn "Theo kết quả bộ lọc" và export, Then file rỗng không có dữ liệu.
- [ ] **AC4:** Given chọn "Theo trang hiện tại", When click "Export Excel", Then chỉ xuất dữ liệu trang đang hiển thị.
- [ ] **AC5:** Given click chọn "Theo toàn bộ danh sách", Then hiển thị description cảnh báo tốn thời gian (chiều cao popup không thay đổi).
- [ ] **AC6:** Given click "Export Excel", When đang xử lý, Then toast: "File Excel dữ liệu đang được xử lý! Bạn có thể tải file tại Cài đặt -> Quản lý xuất dữ liệu".
- [ ] **AC7:** Given file xử lý thành công, Then toast "Ai đó đã tải thành công file."
- [ ] **AC8:** Given xuất file thất bại, Then toast "Xuất file thất bại. Vui lòng thử lại sau."
- [ ] **AC9:** Given click "Cancel"/icon X/click ngoài popup, Then popup đóng; không xuất dữ liệu.

#### Business Rules
- Xử lý file ở background; người dùng không chờ trên popup.
- Thứ tự cột theo "Cài đặt → Thuộc tính".
- Module "Quản lý xuất dữ liệu" phát triển sau.

⚠️ **Cần làm rõ:**
- Sau click "Export Excel" popup có tự đóng không?
- Phân quyền export: User thường có quyền không hay chỉ Admin?

#### Dependencies
- US-CON-01, US-CON-04 (nếu export theo bộ lọc)

#### Technical Notes
- API: `POST /api/contacts/export` (background job)
- Cần module "Quản lý xuất dữ liệu" trong Cài đặt để tải file (phát triển sau).

#### Ghi chú từ SRS
- **Tham chiếu SRS:** Mục VIII. Export the contact – 2.3. Chi tiết (No 1–9)

---

## ⚠️ Gap Analysis – Các điểm cần làm rõ

1. **Import Contact (Mục VII):** Chưa phát triển; không tạo User Story. → **Won't Have trong sprint này.**
2. **Ảnh đại diện:** Định dạng file được phép upload ghi "Bổ sung sau" → cần BA xác nhận trước khi dev.
3. **Phân quyền Export:** Chưa rõ user thường có quyền export không hay chỉ Admin.
4. **Phân quyền toàn module:** SRS ghi "tuân thủ theo quy tắc phân quyền cũ của GapOne" → cần link/tài liệu phân quyền cụ thể.
5. **Trường Địa chỉ:** Không có max length → cần BA xác nhận.

---

## 📊 Bảng Tổng Hợp User Stories

| Story ID | Epic | Tiêu đề | Priority | Story Points | Dependencies | Status |
|:---:|:---:|---|:---:|:---:|---|:---:|
| US-CON-01 | EPIC-CON-01 | Xem danh sách Liên hệ tổng quan | Must Have | 3 | – | New |
| US-CON-02 | EPIC-CON-01 | Tìm kiếm Liên hệ theo tên/email/SĐT | Must Have | 2 | US-CON-01 | New |
| US-CON-03 | EPIC-CON-02 | Mở và đóng bộ lọc nâng cao | Should Have | 2 | US-CON-01 | New |
| US-CON-04 | EPIC-CON-02 | Thiết lập điều kiện lọc với toán tử linh hoạt | Should Have | 5 | US-CON-03 | New |
| US-CON-05 | EPIC-CON-03 | Tạo mới Liên hệ | Must Have | 5 | US-CON-01 | New |
| US-CON-06 | EPIC-CON-04 | Chỉnh sửa thông tin Liên hệ | Must Have | 3 | US-CON-01, US-CON-05 | New |
| US-CON-07 | EPIC-CON-05 | Xem Profile khách hàng qua SSO | Must Have | 8 | US-CON-01, GapOne SSO | New |
| US-CON-08 | EPIC-CON-06 | Xóa Liên hệ | Must Have | 2 | US-CON-01 | New |
| US-CON-09 | EPIC-CON-07 | Xuất file Excel danh sách Liên hệ | Should Have | 5 | US-CON-01, US-CON-04 | New |

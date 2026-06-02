# Story GMF Group

**Hiện trạng & mục tiêu:**
Trước đây, GapOne Conversation chỉ hỗ trợ lấy các cuộc hội thoại 1-1. Để quản lý toàn diện tương tác, hệ thống cần được nâng cấp để lấy toàn bộ danh sách hội thoại nhóm (Zalo Group) do kênh Zalo OA tạo về hệ thống, hỗ trợ user không bỏ sót tin nhắn, quản lý nhóm tập trung. 
 
**Bổ sung định nghĩa:**

* **Cuộc hội thoại đơn/Chat 1-1:** Cuộc hội thoại 1-1 giữa tài khoản kênh và khách hàng
* **Cuộc hội thoại nhóm/Chat nhóm:** Cuộc hội thoại 1-n giữa tài khoản kênh và các khách hàng. 
* **Gợi ý:** Các loại cuộc hội thoại có thể được phân biệt bởi type hoặc tag. Mỗi loại cuộc hội thoại sẽ có cách hiển thị thông tin, thiết lập và áp dụng tự động hóa khác nhau.
 
**Yêu cầu nghiệp vụ:**

* **Kênh:** Zalo OA (Zalo Group / GMF)
* **Luồng:** GapOne kết nối Zalo OA → Quét và đồng bộ toàn bộ danh sách Zalo Group đang có → Khởi tạo luồng chat nhóm trên giao diện → Xử lý định danh thông tin khách hàng trong nhóm → User xem tin nhắn, phân công, chat hoặc chạy luồng Automation cho cuộc hội thoại nhóm.
 
**Tính năng chính:**

* **Đồng bộ các cuộc hội thoại nhóm:** Tự động quét API/Webhook của Zalo để lấy về tất cả các Zalo Group mà OA tạo ra và hiển thị lên danh sách hội thoại của màn giao diện module Hội thoại. Chỉ đồng bộ các cuộc hội thoại nhóm có phát sinh hoạt động kể từ thời điểm kết nối tài khoản kênh thành công, lịch sử cuộc hội thoại nhóm cũng được đồng bộ từ tin nhắn đầu tiên sau khi cuộc hội thoại nhóm được đồng bộ về hệ thống.
* **Phân biệt giao diện Nhóm vs 1-1:** Cập nhật UI/UX ở cột danh sách hội thoại, thêm icon nhóm trước tên nhóm (tương tự zalo) để User dễ dàng phân biệt đâu là chat 1-1, đâu là chat Nhóm. Cuộc hội thoại nhóm zalo vẫn có symbol logo Zalo dưới avt như cuộc hội thoại đơn. Đối với những nhóm không có avt nhóm, avt sẽ là avt mặc định của hệ thống dành cho nhóm (có chứa biểu tượng nhiều người)
* **Đồng bộ thông tin thành viên (Member-Customer Info):** Giống như hội thoại đơn, hệ thống cần bóc tách dữ liệu người gửi trong nhóm để tạo/cập nhật hồ sơ khách hàng (Tên, Zalo ID, Avatar...) trên GapOne Conversation và đồng bộ về Gapone Omni.
* **Tương tác trong nhóm:** Hiển thị rõ tên/avatar của người gửi với từng tin nhắn trong nhóm. Cho phép User chat trực tiếp vào nhóm từ GapOne Conversation.
* **Kích hoạt Tự động hóa (Automation):** Cho phép các trigger (VD: gửi tin chào mừng người mới join nhóm) hoạt động dựa trên các event của Zalo Group.
* **Hiệu chỉnh hiển thị và cài đặt trạng thái cuộc hội thoại:** Phần thông tin chi tiết sẽ không hiển thị; trạng thái cuộc hội thoại đơn cũng không được áp dụng đối với cuộc hội thoại nhóm; trạng thái cuộc hội thoại đổi thành "hoạt động": khi nhóm vẫn tồn tại, "ngừng hoạt động" khi nhóm bị xóa, khóa; phân công nhân viên vẫn áp dụng với cuộc hội thoại nhóm.
 
**Acceptance Criteria:**

**Happy Path (Luồng thành công):**
* **AC1:** Hệ thống GapOne Conversation tự động lấy và hiển thị thành công danh sách các nhóm Zalo (Zalo Group) mà OA tạo ra lên cột danh sách cuộc hội thoại.
* **AC2:** Tại cột hội thoại, các cuộc hội thoại nhóm phải có icon (VD: icon nhiều người) để dễ nhận diện, tách biệt với cuộc hội thoại đơn.
* **AC3:** Khi xem chi tiết một hội thoại nhóm, khung chat hiển thị đầy đủ: Tên nhóm, danh sách thành viên hiện tại, và lịch sử tin nhắn kể từ thời điểm đồng bộ.
* **AC4:** Đối với các tin nhắn thành viên nhắn vào nhóm, hệ thống bóc tách metadata, tạo mới (hoặc map) thông tin khách hàng và hiển thị Avatar + Tên ngay cạnh tin nhắn họ gửi vào, đồng thời lấy về và đồng bộ thông tin khách hàng vào hệ thống.
* **AC5:** Khi có event tự động hóa, hệ thống Automation trigger thành công và trả đúng kịch bản tin nhắn vào trong Zalo Group đó. AC5 chỉ pass khi và chỉ khi Tự động hóa cập nhật thêm trigger cho nhóm.
 
**Edge Cases / Luồng ngoại lệ & Xử lý lỗi:**
* **AC6:** Khi API quét danh sách nhóm thất bại (do Access Token Zalo OA hết hạn hoặc lỗi mạng), hệ thống hiển thị cảnh báo "Lỗi đồng bộ Zalo Group" và ghi log lỗi 5xx/401 thay vì làm treo giao diện.
* **AC7:** Khi Zalo không trả về định danh của một user trong nhóm (do tính riêng tư, người dùng đó từ chối chia sẻ thông tin với zalo OA), hệ thống hiển thị người này là "Thành viên [Zalo_ID]" và tin nhắn vẫn hiển thị bình thường trên GapOne.
* **AC8:** Nếu Zalo OA bị xóa một nhóm, hệ thống lập tức khóa ô nhập liệu của nhóm đó, hổi trạng thái nhóm thành "ngừng hoạt động" và ngừng toàn bộ flow Automation nhắm vào nhóm này.
* **AC9:** Khi tính năng Automation cố gắng đẩy tin nhắn vào nhóm nhưng chạm Rate Limit của Zalo, hệ thống tự động đưa lệnh gửi vào hàng đợi, retry tối đa 3 lần. Nếu vẫn thất bại, đánh dấu log "Failed" và cảnh báo trên Dashboard.
 
**Out of Scope:**
* Không hỗ trợ xóa/thêm thành viên nhóm trực tiếp từ GapOne (phải thao tác trên app Zalo)

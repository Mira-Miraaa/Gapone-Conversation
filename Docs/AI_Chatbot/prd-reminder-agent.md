# **Reminder Agent**

## **1.1 Vấn đề**

Hiện tại, GAPCon AI Chatbot hoạt động theo mô hình session-based: khi khách hàng gửi tin, bot trả lời và orchestrate các tools. Hết session, bot tự refresh. Tuy nhiên không có cơ chế nào để:

* **Nhắc nhở khách quay lại:** Khi khách đang giữa chừng mua hàng (có SP trong giỏ, đang checkout) nhưng không phản hồi, session chỉ im lặng chờ. Khách có thể quên hoàn toàn.

* **Tự động đóng session:** Sessions không bao giờ được đóng tự động. Dẫn đến sessions zombie tiêu tốn tài nguyên và làm sai lệch metrics.

* **Phục hồi doanh thu:** Giỏ hàng bị bỏ rơi (abandoned cart) là nguồn mất doanh thu lớn nhất trong conversational commerce.

## **1.2 Giải pháp: Reminder Agent**

Xây dựng một worker độc lập chạy song song với chatbot chính, chịu trách nhiệm nhắc nhở và tự động đóng sessions:

| Giai đoạn | Trigger | Hành động |
| :---- | :---- | :---- |
|  | KH gửi tin cuối cùng | Bot trả lời bình thường. Timer bắt đầu. |
|  | 48h không có reply từ KH | Gửi reminder context-aware (4 loại template). Set status \= REMINDED. |
|  | 48h sau reminder, KH vẫn không reply | Gửi goodbye message. Auto-close session. Giữ lại giỏ hàng. |
|  | KH reply (dù đang REMINDED) | Reset về ACTIVE. Timer 48h bắt đầu lại. Tiếp tục bình thường. |

## **1.3 Mục tiêu**

| Mục tiêu | Chi tiết |
| :---- | :---- |
| **Phục hồi abandoned cart** | Tăng % khách quay lại hoàn tất mua hàng sau reminder. Mục tiêu: \>8% cart recovery. |
| **Giảm sessions zombie** | 100% sessions được đóng tự động sau 96h. Metrics chính xác hơn. |
| **Cải thiện trải nghiệm** | KH cảm nhận được quan tâm. Checkout gián đoạn được nhắc đúng chỗ. |
| **Không làm phiền** | Tối đa 1 reminder/session.  |

# **2\. Session Lifecycle**

**ACTIVE**  ── \[48h idle\] ──\>  **REMINDED**  ── \[48h idle\] ──\>  **CLOSED**

*KH reply bất cứ lúc nào trong REMINDED → quay về ACTIVE, timer reset.*

# **3\. Nội dung Reminder theo Context**

Tin nhắn reminder PHỤ THUỘC vào trạng thái session. Reminder Agent capture context và chọn template:

## **3.1 Context A: Abandoned cart**

**Trigger:** Session có DRAFT order với 1 hoặc nhiều order\_item.

Chào bạn\! Mình thấy bạn còn **{N} sản phẩm** trong giỏ hàng (tổng **{total}**). Bạn muốn tiếp tục đặt hàng không? Mình vẫn giữ giỏ cho bạn nhé\!

## **3.2 Context B: Checkout bị gián đoạn**

**Trigger:** order\_step khác null và khác DONE (VD: NEED\_PHONE, NEED\_ADDRESS, CONFIRMING).

Chào bạn\! Đơn hàng của bạn chỉ còn thiếu **{missing\_field}**. Bạn gửi thông tin để mình hoàn tất nhé\!

## **3.3 Context C: Browsing (xem SP, giỏ trống)**

**Trigger:** last\_products không trống nhưng giỏ hàng trống.

Chào bạn\! Lần trước bạn đang xem **{product\_name}**. Bạn có muốn mình tìm thêm hoặc thêm vào giỏ không?

## **3.4 Context D: General**

**Trigger:** Giỏ hàng trống, không có last\_products.

Chào bạn\! Bạn có cần mình hỗ trợ thêm gì không? Mình luôn sẵn sàng tư vấn nhé\!

## **3.5 Goodbye message (T+96h)**

**Có giỏ hàng**

Mình tạm đóng cuộc trò chuyện nhé. Giỏ hàng của bạn (**{N} SP, {total}**) sẽ được giữ lại. Bất cứ lúc nào bạn muốn tiếp tục, cứ nhắn tin cho mình nhé\!

**Không có giỏ hàng**

Mình tạm đóng cuộc trò chuyện nhé. Bất cứ lúc nào bạn cần, cứ nhắn tin cho mình. Hẹn gặp lại\!

## **3.6 Giỏ hàng khi đóng session**

**Quyết định:** GIỮ lại DRAFT order. Khi KH quay lại (session mới), bot thông báo: “Bạn còn giỏ hàng từ lần trước. Tiếp tục đặt hay chọn lại?” — Tăng khả năng phục hồi doanh thu.

# **4\. Kiến trúc**

## **4.1 Tổng quan**

Reminder Agent và Chatbot Agent là 2 processes độc lập, giao tiếp qua Database:

| Chatbot Agent (hiện tại) | Reminder Agent (mới) |
| :---- | :---- |
| Xử lý tin nhắn đến từ khách (event-driven) | Gửi tin proactive, không có trigger từ khách |
| Orchestrate 12 tools, LLM reasoning | Chỉ gửi message \+ cập nhật session state. Không dùng LLM. |
| Khi KH reply sau reminder: reset status về ACTIVE | Khi auto-close: set CLOSED, gửi goodbye |

# **5\. Ví dụ luồng hoàn chỉnh**

## **5.1 KH quay lại sau reminder → mua hàng**

*\[Ngày 1, 14:00\] KH thêm 2 SP vào giỏ (850,000đ)*

**Bot: Đã thêm\! Tổng: 850,000đ. Bạn muốn đặt hàng luôn?**

*\[KH không reply. 48 giờ trôi qua...\]*

*\[Ngày 3, 14:00 — Reminder Agent quét\]*

*\[Detect: ACTIVE, 48h idle, DRAFT có 2 items, total=850k\]*

*\[Context: abandoned\_cart → gửi template A\]*

**Bot: Chào bạn\! Bạn còn 2 SP trong giỏ (850,000đ). Tiếp tục đặt hàng không?**

*\[Set reminder\_sent=true, session\_status=REMINDED\]*

*\[Ngày 3, 20:00 — KH reply\]*

**KH: Ơ đúng rồi, đặt hàng luôn nhé**

*\[Chatbot: reset reminder\_sent=false, session\_status=ACTIVE\]*

*\[Chatbot: start\_order\_flow() → checkout bình thường\]*

**Bot: Tên người nhận là gì ạ?**

## **5.2 KH không quay lại → auto-close**

*\[Ngày 1, 10:00\] KH hỏi shipping*

**Bot: Miễn phí đơn từ 500k. Giao 2–3 ngày nội thành.**

*\[48h không reply...\]*

*\[Ngày 3, 10:00 — Reminder Agent\]*

*\[Detect: ACTIVE, 48h idle, giỏ trống, không có SP context\]*

*\[Context: general → gửi template D\]*

**Bot: Bạn có cần mình hỗ trợ thêm không?**

*\[Set reminder\_sent=true, session\_status=REMINDED\]*

*\[48h nữa không reply...\]*

*\[Ngày 5, 10:00 — Reminder Agent\]*

*\[Detect: REMINDED, 48h sau reminder, KH vẫn không reply\]*

*\[Auto-close\]*

**Bot: Mình tạm đóng nhé. Hẹn gặp lại\!**

*\[Set session\_status=CLOSED, closed\_reason=auto\_timeout\]*

## **5.3 Checkout gián đoạn → nhắc nhở → tiếp tục**

*\[14:00\] KH đang checkout: đã có tên \+ SĐT*

**Bot: Địa chỉ giao hàng đầy đủ là gì ạ?**

*\[KH không reply. 48h...\]*

*\[Reminder Agent: detect order\_step=NEED\_ADDRESS\]*

*\[Context: checkout\_interrupted → missing\_field=địa chỉ giao hàng\]*

**Bot: Đơn của bạn chỉ còn thiếu địa chỉ giao hàng. Gửi địa chỉ nhé\!**

*\[12h sau — KH reply\]*

**KH: 123 Lê Lợi, Q1, HCM**

*\[Reset reminder, tiếp tục state machine NEED\_ADDRESS → CONFIRMING\]*

**Bot: Xác nhận: Quần Jean x1, 450k | A | 0901234567 | 123 Lê Lợi. Đặt không?**


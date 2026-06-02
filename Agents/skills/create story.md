---
name: create-story
description: Writes Jira story descriptions based on provided documents with 4 main sections: Objective, Business Requirements (Channels, Format, Features), Acceptance Criteria (Happy Path, Edge Cases, Out of Scope), and Anti-Hallucination Rules. This skill should be used when the user asks to write a Jira story from a document, or asks to create a story from a document.
---

# Skill: Phân Rã & Mô Tả User Stories từ SRS

## Mục đích
Skill này hướng dẫn quy trình phân tích tài liệu SRS (Software Requirements Specification) để phân rã thành các User Stories theo chuẩn Agile/Scrum, phục vụ cho việc lập kế hoạch Sprint và quản lý backlog.

---

## Quy trình thực hiện

### Bước 1: Đọc & Phân tích SRS
- Đọc toàn bộ tài liệu SRS được cung cấp
- Xác định các **module/chức năng chính** (Epics)
- Xác định các **actors/personas** (ai sử dụng hệ thống)
- Liệt kê các **business rules** và **constraints**
- Ghi nhận các **non-functional requirements** (hiệu năng, bảo mật, khả năng mở rộng)

### Bước 2: Xác định Epics
- Nhóm các yêu cầu liên quan thành **Epics** (nhóm chức năng lớn)
- Mỗi Epic phải có:
  - **Epic ID**: Mã định danh (VD: `EPIC-001`)
  - **Epic Name**: Tên mô tả ngắn gọn
  - **Epic Description**: Mô tả tổng quan mục tiêu của Epic
  - **Module/Component**: Module liên quan trong hệ thống

### Bước 3: Phân rã thành User Stories
Với mỗi Epic, phân rã thành các User Stories theo template chuẩn (xem bên dưới).

---

## Template User Story

```
### [Story ID] - [Tiêu đề ngắn gọn]

**Epic:** [Epic ID - Epic Name]
**Module:** [Tên module/component]
**Priority:** [Must Have | Should Have | Could Have | Won't Have]
**Story Points:** [1 | 2 | 3 | 5 | 8 | 13]

#### Mô tả (User Story Format)
> **As a** [vai trò/persona],
> **I want** [hành động/chức năng mong muốn],
> **So that** [giá trị/lợi ích đạt được].

#### Mô tả chi tiết
[Mô tả bổ sung về bối cảnh, logic nghiệp vụ, và các lưu ý quan trọng]

#### Acceptance Criteria (Tiêu chí chấp nhận)
- [ ] **AC1:** [Given... When... Then...]
- [ ] **AC2:** [Given... When... Then...]
- [ ] **AC3:** [Given... When... Then...]

#### Business Rules
- [Rule 1]
- [Rule 2]

#### UI/UX Notes (nếu có)
- [Ghi chú về giao diện, flow]

#### Dependencies (Phụ thuộc)
- [Story ID khác hoặc hệ thống bên ngoài]

#### Technical Notes (Ghi chú kỹ thuật)
- [API endpoints, data model, integration points...]

#### Ghi chú từ SRS
- **Tham chiếu SRS:** [Section/mục trong SRS gốc]
- **Trích dẫn:** [Nội dung gốc từ SRS nếu cần]
```

---

## Bước 4: Đánh giá Story Points

Sử dụng thang Fibonacci để ước lượng độ phức tạp:

| Story Points | Độ phức tạp | Mô tả | Ví dụ |
|:---:|:---:|---|---|
| **1** | Rất đơn giản | Thay đổi nhỏ, rõ ràng, không rủi ro | Đổi label, thêm field tĩnh |
| **2** | Đơn giản | Logic đơn giản, ít tương tác | CRUD cơ bản 1 entity |
| **3** | Trung bình | Logic vừa phải, có validation | Form với validation, filter/search |
| **5** | Phức tạp | Nhiều logic, tích hợp, edge cases | Tích hợp API bên thứ 3, workflow phức tạp |
| **8** | Rất phức tạp | Nhiều phụ thuộc, rủi ro cao | Module AI/ML, realtime processing |
| **13** | Cực kỳ phức tạp | Nên xem xét tách nhỏ hơn | Hệ thống phân tán, kiến trúc mới |

### Tiêu chí đánh giá Story Points:
- **Độ phức tạp kỹ thuật**: Mức độ khó về mặt code/architecture
- **Khối lượng công việc**: Số lượng tasks cần làm
- **Rủi ro/Uncertainty**: Mức độ không chắc chắn
- **Phụ thuộc**: Số lượng dependencies với stories/systems khác

---

## Bước 5: Phân loại Priority (MoSCoW)

| Priority | Ý nghĩa | Tỷ lệ khuyến nghị |
|:---:|---|:---:|
| **Must Have** | Bắt buộc phải có, hệ thống không hoạt động nếu thiếu | ~60% |
| **Should Have** | Quan trọng nhưng không critical, có thể workaround | ~20% |
| **Could Have** | Nice-to-have, nâng cao trải nghiệm | ~15% |
| **Won't Have** | Không làm trong phạm vi này, cân nhắc sau | ~5% |

---

## Bước 6: Xử lý Non-Functional Requirements (NFRs)

NFRs được chuyển thành các **Technical Stories** hoặc **Enabler Stories**:

```
### [TECH-XXX] - [Tiêu đề]

**Loại:** Technical Story / Enabler Story
**NFR Category:** [Performance | Security | Scalability | Usability | Reliability]

#### Mô tả
[Mô tả yêu cầu phi chức năng]

#### Acceptance Criteria
- [ ] [Metric đo lường cụ thể, VD: Response time < 2s cho 95% requests]

#### Ảnh hưởng đến Stories
- [Danh sách Story IDs bị ảnh hưởng]
```

---

## Output Format

### Bảng tổng hợp Stories (Summary Table)

Sau khi phân rã, tạo bảng tổng hợp:

| Story ID | Epic | Tiêu đề | Priority | Story Points | Dependencies | Status |
|:---:|:---:|---|:---:|:---:|---|:---:|
| US-001 | EPIC-001 | ... | Must Have | 5 | - | New |
| US-002 | EPIC-001 | ... | Should Have | 3 | US-001 | New |

### Thống kê tổng quan

```
📊 Tổng quan Backlog:
├── Tổng số Epics: X
├── Tổng số User Stories: X
├── Tổng số Technical Stories: X
├── Tổng Story Points: X
├── Phân bổ Priority:
│   ├── Must Have: X stories (X points)
│   ├── Should Have: X stories (X points)
│   ├── Could Have: X stories (X points)
│   └── Won't Have: X stories (X points)
└── Dependencies Map: [Có/Không có vòng lặp]
```

---

## Checklist Chất lượng Story (INVEST)

Mỗi story phải đạt tiêu chí **INVEST**:

- [ ] **I**ndependent: Story có thể phát triển độc lập (tối đa có thể)
- [ ] **N**egotiable: Có thể thương lượng scope/approach
- [ ] **V**aluable: Mang lại giá trị cho user/business
- [ ] **E**stimable: Có thể ước lượng được effort
- [ ] **S**mall: Đủ nhỏ để hoàn thành trong 1 sprint
- [ ] **T**estable: Có tiêu chí kiểm thử rõ ràng

---

## Ví dụ minh họa

### EPIC-001 - Quản lý Chatbot AI

#### US-001 - Người dùng gửi tin nhắn đến Chatbot

**Epic:** EPIC-001 - Quản lý Chatbot AI
**Module:** Chat Interface
**Priority:** Must Have
**Story Points:** 5

#### Mô tả (User Story Format)
> **As a** khách hàng truy cập website,
> **I want** gửi câu hỏi bằng ngôn ngữ tự nhiên cho chatbot,
> **So that** tôi nhận được câu trả lời nhanh chóng mà không cần liên hệ nhân viên hỗ trợ.

#### Mô tả chi tiết
Người dùng có thể nhập tin nhắn text vào ô chat và gửi đi. Hệ thống sẽ xử lý tin nhắn thông qua AI model và trả về câu trả lời phù hợp. Hỗ trợ tiếng Việt và tiếng Anh.

#### Acceptance Criteria
- [ ] **AC1:** Given người dùng đang ở trang chat, When nhập tin nhắn và nhấn Enter/nút Gửi, Then tin nhắn được gửi và hiển thị trong khung chat
- [ ] **AC2:** Given tin nhắn đã được gửi, When hệ thống xử lý xong, Then câu trả lời từ AI hiển thị trong vòng 3 giây
- [ ] **AC3:** Given tin nhắn rỗng, When người dùng nhấn Gửi, Then hiển thị thông báo "Vui lòng nhập tin nhắn"
- [ ] **AC4:** Given người dùng gửi tin nhắn bằng tiếng Việt hoặc tiếng Anh, When AI xử lý, Then phản hồi đúng ngôn ngữ đầu vào

#### Business Rules
- Tin nhắn tối đa 1000 ký tự
- Hệ thống phải lưu lịch sử hội thoại trong phiên (session)
- Nếu AI không thể trả lời, chuyển sang nhân viên hỗ trợ

#### Dependencies
- Không có (story đầu tiên)

#### Technical Notes
- API endpoint: `POST /api/v1/chat/messages`
- Sử dụng WebSocket cho real-time communication
- AI model: GPT-4 / tương đương

#### Ghi chú từ SRS
- **Tham chiếu SRS:** Section 3.1 - Chat Interface Requirements
- **Trích dẫn:** "Hệ thống phải cho phép người dùng gửi tin nhắn và nhận phản hồi từ AI chatbot trong thời gian thực"

---

## Lưu ý khi sử dụng Skill này

1. **Luôn đọc kỹ SRS trước** khi bắt đầu phân rã
2. **Hỏi user khi không rõ** yêu cầu hoặc scope
3. **Tập trung vào giá trị user** thay vì chi tiết kỹ thuật khi viết story description
4. **Acceptance Criteria phải đo lường được** - tránh dùng từ mơ hồ như "tốt", "nhanh"
5. **Đánh dấu assumptions** rõ ràng nếu SRS thiếu thông tin
6. **Xem xét tách story** nếu story points > 8
7. **Output bằng tiếng Việt** trừ khi user yêu cầu khác
8. **Trích dẫn nguồn SRS** để đảm bảo traceability

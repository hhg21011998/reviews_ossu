# Hướng dẫn cho Codex

## Tổng quan dự án

Đây là repository cá nhân ghi lại hành trình học Computer Science theo lộ trình OSSU. Nội dung chính gồm review khóa học, ghi chú học tập, bài tập và project.

Tiến độ hiện tại:

- Đã hoàn thành Python for Everybody, MIT 6.0001 và How to Code: Simple Data.
- Đang học How to Code: Complex Data thuộc Core Programming.
- Khóa tiếp theo dự kiến là Programming Languages Part A.

## Cấu trúc chính

- `README.md`: review và tiến độ OSSU tổng quan.
- `1.Intro_CS/`: các khóa nhập môn, hiện có Python for Everybody và MIT 6.0001.
- `2.Core_CS/1.Core_Programming/`: các khóa Core Programming và ghi chú How to Code.
- `.agents/skills/learning-course/`: skill hỗ trợ công việc liên quan đến lộ trình OSSU.
- `.codex/`: hướng dẫn dành riêng cho Codex.

Khi thêm khóa học mới, ưu tiên cấu trúc `GiaiĐoạn/ThứTự.Nhóm/ThứTự.Tên_Khóa_Học/` và làm theo cấu trúc đang có thay vì đổi tên hàng loạt các thư mục cũ.

## Quy tắc làm việc

1. Giao tiếp và viết ghi chú chủ yếu bằng tiếng Việt; giữ thuật ngữ kỹ thuật bằng tiếng Anh khi cách đó rõ nghĩa hơn.
2. Trước khi sửa một khu vực, đọc `README.md` gần nhất và các file Markdown liên quan để giữ đúng ngữ cảnh, giọng văn và cấu trúc.
3. Không sửa bài tập hoặc ghi chú ngoài phạm vi yêu cầu. Không ghi đè thay đổi chưa commit của người dùng.
4. Khi hỗ trợ bài tập, ưu tiên giải thích concept, gợi ý từng bước và Design Recipe; không đưa đáp án hoàn chỉnh nếu người dùng chưa yêu cầu rõ ràng.
5. Với bài How to Code, tuân theo quy trình: signature → purpose → stub → examples/tests → template → implementation → test. Ưu tiên test base case và case có ít nhất hai phần tử đối với dữ liệu tự tham chiếu.
6. Khi thêm ghi chú, đặt file trong đúng thư mục lecture/chủ đề của khóa học. Dùng Markdown có heading rõ ràng, ví dụ code có fenced code block và bảng chỉ khi giúp so sánh dễ hơn.
7. Khi thêm review khóa học vào `README.md`, cập nhật cả mục lục/anchor, link khóa học, nội dung cảm nhận và certificate nếu có. Giữ giọng văn cá nhân của tác giả.
8. Không tự ý thay đổi certificate, link cá nhân, Trello hoặc nhận định cá nhân trong review.
9. Không thêm dependency, generated file hoặc cấu hình editor nếu nhiệm vụ không cần đến chúng.

## Kiểm tra trước khi hoàn tất

- Xác nhận file nằm đúng giai đoạn, nhóm khóa học và lecture.
- Kiểm tra link Markdown, anchor và fenced code block vừa thay đổi.
- Chạy test phù hợp nếu có sửa code; nếu không có test tự động, nêu rõ đã kiểm tra thủ công điều gì.
- Dùng `git diff --check` để phát hiện lỗi whitespace và chỉ báo cáo những file đã thực sự thay đổi.

## Nguồn thông tin ưu tiên

Khi thông tin mâu thuẫn, ưu tiên theo thứ tự:

1. Yêu cầu hiện tại của người dùng.
2. `README.md` hoặc ghi chú gần nhất trong thư mục đang làm việc.
3. File hướng dẫn này.
4. `.agents/skills/learning-course/SKILL.md`.


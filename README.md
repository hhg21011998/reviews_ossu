# Cảm nhận về các khóa học theo chương trình của OSSU
LƯU Ý: Đây là ý kiến cá nhân của mình và được viết dựa trên cảm nhận của mình. Hãy tự trải nghiệm và đưa ra nhận định riêng của bạn.

My [Trello](https://trello.com/invite/b/6272869e21ecc905ef6558fb/d204d6f164c4cc2be2f355e7860dcad9/ossu-hhg).

Nếu bạn chưa bao giờ nghe đến OSSU. [Nhấn vào đây](https://github.com/ossu/computer-science/).

Bắt đầu viết vào Tháng 9-2022

- [Python for Everybody](#py4e)
- [Intro to CS and Programming with Python](#mit6001x)
- [How to Code 1 & 2](#how-to-code)

### <a name="py4e"></a> Python for Everybody

https://www.coursera.org/specializations/python

Đây là khóa học đầu tiên của mình, bắt đầu vào tháng 4-2022. mình nhận thấy đây là một khóa học rất cơ bản và chi tiết dành cho những người chưa bao giờ lập trình, thậm chí là chưa bao giờ chạm vào code. Mình cũng thường giới thiệu cho bạn bè khóa học này làm khóa học nhập môn.


Chúng ta sẽ được làm quen với ngôn ngữ Python, các cấu trúc dữ liệu cơ bản của 1 ngôn ngữ lập trình, cách giao tiếp với 1 tệp văn bản ở bên ngoài, cách lấy dữ liệu từ các file XML và JSON, làm việc với SQL. Nghe có vẻ hơi nhiều nhưng có vẻ mọi thứ chỉ dừng lại ở mức độ giới thiệu mà thôi. Có các bài tập trắc nghiệm và tự luận, không quá khó khăn ngoại trừ các phần giao tiếp với web service có vẻ sẽ làm các bạn mới gặp trắc trở 1 chút (theo chương trình OSSU thì từ phần web service trở đi chỉ cần tham khảo qua).


*Certificate:*
[Python for Everybody](https://www.coursera.org/account/accomplishments/specialization/certificate/3XG2HBCX2YQE)

### <a name="mit6001x"></a> Intro to CS and Programming with Python

https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/


Khóa học tiếp theo của mình sau khi hoàn thành PY4E. Thật sự rất thích cách thiết kế các bài tập trong khóa học này, nó khiến cho các bài tập không hề khô khan. Mất khoảng 2 tháng để mình hoàn thành khóa học này, mức độ thử thách là vừa phải. Bắt đầu từ những kiểu dữ liệu cho đến những thuật toán điển hình như bisection search và những thuật toán sắp xếp cơ bản.

Các bài tập: Tìm kiếm lãi suất tốt nhất, Hangman game, Trò chơi đoán ô chữ, Giải mã các kí tự bị mã hóa, etc...


### <a name="how-to-code"></a> How to Code 1 & 2

https://www.edx.org/course/how-to-code-simple-data

https://learning.edx.org/course/course-v1:UBCx+SPD1x+2T2015/home


Đây là khoá học thiết kế chương trình, không phải khoá học ngôn ngữ lập trình. Mình được tiếp xúc với ngôn ngữ Racket, khá giống với Lisp (được viết vào khoảng năm 1960, là ngôn ngữ high-level lâu đời thứ 2 vẫn còn được sử dụng đến bây giờ). Đặc điểm là sử dụng hàng tấn dấu (), thật sự rất nhiều dấu (), làm mình liên tưởng đến việc học toán hơn là học lập trình, do đó mình tiết kiệm được rất nhiều thời gian để tập trung vào phương pháp thiết kế thay vì phải tìm hiểu ngôn ngữ. Khóa học xoay quanh chủ đề về đệ quy.

Sử dụng Dr.Racket IDE, thứ đã khiến ngôn ngữ này không hề nhàm chán, nó cài đặt sẵn mọi thứ từ ngôn ngữ, debugger, code editer.

Những phần đầu của khóa học, bạn sẽ được hướng dẫn viết code một cách kỉ luật, tuân thủ 1 khuôn mẫu mà người hướng dẫn đề ra. Đầu tiên bạn sẽ viết một cái signature (kiểu dữ liệu của đầu vào/ra) của hàm, sau đó sẽ viết một cái ví dụ của hàm, rồi sẽ viết các test cho hàm đó (nếu tham số là thế này thì hàm phải trả về kết quả thế này...), khi mọi test đều ok thì bạn mới bắt đầu viết logic cho hàm, và khi chạy thử nếu hàm đáp ứng được các yêu cầu của test thì done. Khá giống với phương pháp [TDD](https://en.wikipedia.org/wiki/Test-driven_development#:~:text=Test-driven%20development%20(TDD),software%20against%20all%20test%20cases.).

Đây là một bài tập nhỏ cuối khóa (thứ khiến mình thấy khoá học này hấp dẫn, kết quả của những dòng code mà bạn viết ra không chỉ là những con số hay chữ cái hay kí tự hiển thị trên shell mà là cả một trò chơi):

![final-htc-simple-data](https://user-images.githubusercontent.com/90635389/218292358-0a7ce3db-213c-4c46-95a9-0d22c7f3cb42.PNG)




# 7b: Local

**1. Dù ít code mới, việc thiết kế và cải thiện cấu trúc chương trình là kỹ năng quan trọng của good programmers.**

**Mục tiêu học tập (Learning Goals):**

- Viết local expressions đúng cú pháp.

- Vẽ sơ đồ lexical scoping trên các biểu thức sử dụng local.

- Thực hiện hand-evaluation (đánh giá thủ công) các biểu thức local.

- Sử dụng local để encapsulate (đóng gói) các hàm phụ trợ (private helper functions).

- Sử dụng local để tránh redundant computation (tính toán lặp lại không cần thiết).

**2. Khái niệm chính**

**Encapsulation là gì?**

Định nghĩa: Encapsulation là kỹ thuật đóng gói các thành phần chương trình (functions, constants, structures) vào một đơn vị (capsule), chỉ để lộ giao diện công khai (public interface).

**Mục đích:**

- Namespace management: Tránh xung đột tên trong hệ thống lớn.

- Ẩn chi tiết triển khai: Ngăn gọi nhầm hàm phụ trợ hoặc phụ thuộc vào logic nội bộ.

- Tăng tính module hóa: Làm code dễ bảo trì, tái sử dụng, rõ ràng.

**Cơ chế với local:**

- Cú pháp: (local [define ... define ...] body)

- Định nghĩa trong local chỉ khả dụng trong body.

- body gọi hàm nội bộ để bắt đầu xử lý, gọi là trampoline (thuật ngữ vui ám chỉ việc "nhảy" vào logic nội bộ).

**Redundant Computation và Exponential Growth**

Định nghĩa: 

Redundant Computation: Tính toán cùng một giá trị nhiều lần trong chương trình, gây lãng phí thời gian và tài nguyên.

Trong các trường hợp đơn giản (như (+ x 1) lặp lại), tác động nhỏ, thường được ngôn ngữ tối ưu tự động.
Trong các hàm đệ quy, redundant computation có thể dẫn đến exponential growth, làm chương trình chạy chậm đáng kể khi dữ liệu lớn.

Exponential Growth: Thời gian chạy tăng theo lũy thừa (thường là 2^n) khi kích thước dữ liệu tăng.

Cú pháp mẫu: (local [(define name expr)] body)

Lưu ý quan trọng:

Chỉ nên dùng local cho redundant computation trong các trường hợp đệ quy gây exponential growth.
Tránh dùng local cho các tính toán đơn giản (như (+ x 1) lặp lại), vì:

- Làm code phức tạp hơn, khó đọc.

- Ngôn ngữ thường tối ưu các tính toán nhỏ tự động.

Refactoring principle: Thay đổi cấu trúc (thêm local), giữ nguyên hành vi, kiểm tra kỹ.

# 8: Abstraction Module

**Khái niệm chính: Abstraction và Higher-Order Functions**

*Abstraction là gì?*

Abstraction là quá trình tạo ra một hàm tổng quát hơn từ các biểu thức/hàm cụ thể bằng cách thay thế các điểm khác biệt (points of variance) bằng tham số.

*Mục đích:*

1. Loại bỏ lặp lại: Giảm code trùng lặp, làm code ngắn gọn.

2. Tăng tính tổng quát: Hàm trừu tượng áp dụng được cho nhiều trường hợp.

3. Dễ bảo trì: Chỉ cần sửa hàm trừu tượng thay vì nhiều hàm cụ thể.

*Higher-Order Functions là gì?*

Hàm nhận hoặc trả về hàm khác làm tham số/kết quả.

**Using Built in Abstract Functions**

*Dựa trên hành vi:*

- map: Áp dụng hàm, giữ độ dài danh sách.

- filter: Lọc, có thể giảm độ dài.

- foldr: Kết hợp thành một giá trị.

- andmap/ormap: Kiểm tra điều kiện.

- build-list: Tạo danh sách từ số.

*Tầm quan trọng:*

- Built-in abstract functions làm code ngắn gọn, đáng tin cậy, và tổng quát.

- So sánh signature là kỹ năng cốt lõi để chọn công cụ phù hợp.

- Bỏ base-case test tiết kiệm thời gian, nhưng vẫn cần test đặc trưng.


# Hello 6/19/2025*
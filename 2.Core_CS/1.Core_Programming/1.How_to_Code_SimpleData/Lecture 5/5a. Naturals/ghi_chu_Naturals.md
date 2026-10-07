# Ghi chú: Naturals — Số tự nhiên dưới góc nhìn Self-Reference

> **Khóa học:** How to Code: Simple Data  
> **Giảng viên:** Gregor Kiczales  
> **Chủ đề:** Lecture 5 — 5a. Naturals (Số tự nhiên)

---

## 1. Insight cốt lõi: Số tự nhiên là Arbitrary Sized Data

Trước đây, chúng ta thường coi `Natural` (số tự nhiên: 0, 1, 2, ...) là kiểu dữ liệu nguyên bản (primitive data). Tuy nhiên:
- Có bao nhiêu số tự nhiên? Số tự nhiên biểu diễn vị trí của một người trong hàng chờ có thể lớn đến mức nào?
- Câu trả lời là: **Không biết trước được** $\rightarrow$ Số tự nhiên là **kích thước tùy ý (arbitrary-sized)**.
- Do đó, chúng ta hoàn toàn có thể xây dựng một **well-formed self-referential data definition** cho số tự nhiên!

Khi coi số tự nhiên là dữ liệu tự tham chiếu, chúng ta có thể áp dụng toàn bộ sức mạnh của HtDD và HtDF để thiết kế các hàm đệ quy trên số tự nhiên một cách có hệ thống.

---

## 2. Các hàm Primitive mới trong BSL: `add1` và `sub1`

Trong BSL (và Racket nói chung), ta có 2 primitive functions đặc biệt tương ứng với việc "xây dựng lên" và "bóc tách xuống" số tự nhiên:

- **`add1`**: Nhận một số tự nhiên và cộng thêm 1 $\rightarrow$ xây dựng số tự nhiên lớn kế tiếp.
  ```racket
  0             ;; 0
  (add1 0)      ;; 1
  (add1 (add1 0)) ;; 2
  ```
- **`sub1`**: Nhận một số tự nhiên và trừ đi 1 $\rightarrow$ hạ xuống số tự nhiên nhỏ kế tiếp.
  ```racket
  (sub1 2)      ;; 1
  (sub1 (sub1 2)) ;; 0
  ```

### Sự tương đồng kỳ diệu giữa List và Natural

Gregor chỉ ra mối tương quan cấu trúc tương đương 1-1 giữa List và Natural:

| Thao tác / Khái niệm | List (Danh sách) | Natural (Số tự nhiên) |
|---|---|---|
| **Base case (Điểm dừng)** | `empty` | `0` |
| **Kiểm tra base case** | `empty?` | `zero?` |
| **Constructor (Xây dựng)** | `cons` (thêm 1 phần tử) | `add1` (tăng thêm 1 đơn vị) |
| **Lấy phần còn lại** | `rest` (danh sách ngắn đi 1) | `sub1` (số giảm đi 1 đơn vị) |
| **Lấy giá trị hiện tại** | `first` | Chính là giá trị `n` |

---

## 3. Data Definition: `Natural`

Dưới đây là định nghĩa chuẩn theo HtDD cho kiểu `Natural`:

```racket
;; =================
;; Data Definitions:

;; Natural is one of:
;;  - 0
;;  - (add1 Natural)
;; interp. a natural number

(define N0 0)          ; 0
(define N1 (add1 N0))  ; 1
(define N2 (add1 N1))  ; 2

#;
(define (fn-for-natural n)
  (cond [(zero? n) (...)]
        [else
         (... n                           ; <-- Giá trị n hiện tại
              (fn-for-natural (sub1 n)))])) ; <-- Natural recursion

;; Template rules used:
;;  - one-of: 2 cases
;;  - atomic distinct: 0
;;  - compound: (add1 Natural)
;;  - self-reference: (sub1 n) is Natural
```

### 💡 Lưu ý quan trọng về Template:
- Về mặt lý thuyết cơ học của template rules, bóc tách `(add1 Natural)` chỉ sinh ra `(sub1 n)` và lời gọi đệ quy `(fn-for-natural (sub1 n))`.
- Tuy nhiên, trong hầu hết bài toán thực tế, chúng ta cần dùng chính giá trị hiện tại `n` (ví dụ: cộng `n`, `cons` `n`).
- Vì `n` luôn có sẵn dưới dạng tham số đầu vào của hàm, **Gregor chủ động bổ sung `n` vào template** để người lập trình thuận tiện sử dụng.

---

## 4. Ví dụ 1: Thiết kế hàm `sum-n`

**Đề bài:** Thiết kế hàm nhận vào một số tự nhiên `n` và tính tổng các số tự nhiên từ 0 đến n ($0 + 1 + 2 + ... + n$).

### Bước 1: Signature, Purpose, Stub
```racket
;; Natural -> Natural
;; produce sum of natural numbers from 0 to n inclusive
(define (sum-n n) 0) ; stub
```

### Bước 2: Examples / Tests
> Nhớ quy tắc: Base case test trước tiên!

```racket
(check-expect (sum-n 0) 0)
(check-expect (sum-n 1) 1)
(check-expect (sum-n 3) (+ 3 2 1 0)) ; = 6
```

### Bước 3: Template & Implementation
Copy template của `Natural` và đổi tên:

```racket
(define (sum-n n)
  (cond [(zero? n) 0]
        [else
         (+ n (sum-n (sub1 n)))]))
```

- **Phân tích:**
  - Khi `n = 0` (base case) $\rightarrow$ tổng bằng `0`.
  - Ở nhánh `else`: Ta cộng `n` với kết quả đệ quy `(sum-n (sub1 n))`. Tin tưởng rằng `(sum-n (sub1 n))` sẽ tính đúng tổng từ 0 đến $n-1$.

---

## 5. Ví dụ 2: Thiết kế hàm `to-list`

**Đề bài:** Thiết kế hàm nhận vào số tự nhiên `n` và tạo ra một danh sách các số giảm dần từ `n` về `1` (dạng `(cons n (cons n-1 ... empty))`), **không bao gồm 0**.

### Bước 1: Signature, Purpose, Stub
```racket
;; Natural -> ListOfNatural
;; produce (cons n (cons n-1 ... empty)) down to 1 (not including 0)
(define (to-list n) empty) ; stub
```

> *Ghi chú:* Ta không cần viết data definition cho `ListOfNatural` vì hàm chỉ sản sinh (produce) chứ không tiêu thụ (consume) list này.

### Bước 2: Examples / Tests
```racket
(check-expect (to-list 0) empty)
(check-expect (to-list 1) (cons 1 empty))
(check-expect (to-list 2) (cons 2 (cons 1 empty)))
```

### Bước 3: Template & Implementation
```racket
(define (to-list n)
  (cond [(zero? n) empty]
        [else
         (cons n (to-list (sub1 n)))]))
```

- **Phân tích:**
  - Base case `n = 0`: Đề bài yêu cầu không lấy 0 $\rightarrow$ trả về `empty`.
  - Nhánh đệ quy: `cons` giá trị `n` vào danh sách kết quả trả về từ đệ quy tự nhiên `(to-list (sub1 n))`.

---

## 6. Tổng kết

1. **Số tự nhiên là cấu trúc đệ quy:** Giống như cấu trúc số tự nhiên Peano trong toán học, mọi số tự nhiên đều được tạo nên từ số `0` và phép toán `add1`.
2. **Quy trình HtDF không đổi:**
   - Base case: `(zero? n)` $\rightarrow$ trả về giá trị cơ sở.
   - Recursive case: Kết hợp `n` với kết quả đệ quy trên `(sub1 n)`.
3. **Template hoàn thiện:** Khi gặp hàm nhận tham số `Natural`, hãy luôn nhớ mẫu template:
   ```racket
   (define (fn-for-natural n)
     (cond [(zero? n) (...)]
           [else
            (... n
                 (fn-for-natural (sub1 n)))]))
   ```

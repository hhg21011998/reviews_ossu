# Ghi chú: Cowabunga v.2 & v.3 — Thiết kế `next-cow`, `render-cow` & Helper Functions

> **Khóa học:** How to Code: Simple Data  
> **Giảng viên:** Gregor Kiczales  
> **Chủ đề:** Interactive Programs — Compound Data (Cow bouncing)

---

## 1. Bối cảnh bài toán

Cowabunga là chương trình mô phỏng **con bò di chuyển qua lại** trên màn hình:
- Bò di chuyển theo trục ngang (x)
- Khi chạm mép phải hoặc mép trái → **đổi hướng** (bounce)
- Người dùng nhấn **space bar** → đổi hướng di chuyển

### Data Definition — Kiểu `Cow`

```racket
(define-struct cow (x dx))
;; Cow is (make-cow Natural Integer)
;; interp. (make-cow x dx) is a cow with x-coordinate x
;;         moving dx pixels per tick
```

- `x` → vị trí ngang hiện tại
- `dx` → vận tốc (dương = sang phải, âm = sang trái)

---

## 2. Cấu trúc chương trình — `big-bang`

```racket
(define (main c)
  (big-bang c
    [on-tick   next-cow]      ;; Cow -> Cow        — di chuyển bò mỗi tick
    [to-draw   render-cow]    ;; Cow -> Image      — vẽ bò lên màn hình
    [on-key    handle-key]))  ;; Cow KeyEvent -> Cow — xử lý phím
```

> 💡 **Quan sát:** Khi đã biết world state được biểu diễn bởi kiểu `Cow`, tất cả signature đều **tự động** suy ra được — đây là tính "formulaic" của Design Recipe.

### Purposes (mục đích) — phần cần SUY NGHĨ kỹ

| Hàm | Purpose |
|-----|---------|
| `next-cow` | Tăng `cow-x` theo `dx`, **bounce** khi chạm mép |
| `render-cow` | Vẽ hình bò **phù hợp** (trái/phải) tại vị trí hiện tại |
| `handle-key` | **Đảo chiều** di chuyển khi nhấn space bar |

> Từ khóa "bounces off edges" và "appropriate cow image" trong purpose là **gợi nhớ** quan trọng cho lúc code.

---

## 3. Thiết kế `next-cow` (v.2) — Ví dụ / Test Cases

### Bước 1: Skeleton — Cấu trúc chung của mọi example

```racket
(check-expect (next-cow (make-cow ... ...)) (make-cow ... ...))
;;             input: một Cow               output: một Cow
```

### Bước 2: Liệt kê các trường hợp

Gregor phân tích ra **6 examples** chia thành **3 nhóm**:

#### 🟢 Nhóm 1: Bò ở GIỮA màn hình (keep going)

```racket
;; di chuyển sang phải (dx > 0)
(check-expect (next-cow (make-cow 20 3))
                        (make-cow 23 3))

;; di chuyển sang trái (dx < 0)
(check-expect (next-cow (make-cow 20 -3))
                        (make-cow 17 -3))
```

#### 🟡 Nhóm 2: Bò VỪA CHẠM MÉP (vẫn keep going, chưa bounce)

```racket
;; chạm mép phải
(check-expect (next-cow (make-cow (- WIDTH 3) 3))
                        (make-cow WIDTH 3))

;; chạm mép trái
(check-expect (next-cow (make-cow 3 -3))
                        (make-cow 0 -3))
```

> Quy tắc: Bò được phép đi **đến** mép, chưa cần bounce. Bounce xảy ra ở tick tiếp theo.

#### 🔴 Nhóm 3: Bò VƯỢT QUA MÉP (bounce!)

```racket
;; vượt mép phải → đưa về mép, đảo chiều
(check-expect (next-cow (make-cow (- WIDTH 2) 3))
                        (make-cow WIDTH -3))

;; vượt mép trái → đưa về mép, đảo chiều
(check-expect (next-cow (make-cow 2 -3))
                        (make-cow 0 3))
```

### 🔑 Insight quan trọng

> 6 examples → thực chất chỉ có **3 cases** logic:
> 1. Vượt mép phải → bounce
> 2. Vượt mép trái → bounce
> 3. Còn lại → keep going
> 
> **Viết examples trước** giúp nhìn rõ cấu trúc bài toán TRƯỚC KHI code!

---

## 4. Từ Template đến Code (`next-cow`)

### Template gốc (từ data definition của Cow)

```racket
(define (fn-for-cow c)
  (... (cow-x c)      ;; Natural
       (cow-dx c)))   ;; Integer
```

### Xây dựng `cond` — 3 cases

```racket
(define (next-cow c)
  (cond [(> (+ (cow-x c) (cow-dx c)) WIDTH)    ;; vượt mép phải?
         (make-cow WIDTH (- (cow-dx c)))]

        [(< (+ (cow-x c) (cow-dx c)) 0)        ;; vượt mép trái?
         (make-cow 0 (- (cow-dx c)))]

        [else                                    ;; keep going
         (make-cow (+ (cow-x c) (cow-dx c))
                   (cow-dx c))]))
```

### Giải thích từng phần

| Biểu thức | Ý nghĩa |
|-----------|---------|
| `(+ (cow-x c) (cow-dx c))` | Vị trí **dự kiến** nếu bò cứ đi tiếp |
| `(> ... WIDTH)` | Vượt quá mép phải? |
| `(< ... 0)` | Vượt quá mép trái? |
| `(- (cow-dx c))` | **Đảo dấu** vận tốc → đổi hướng |
| `(make-cow WIDTH ...)` | Đặt bò ngay tại mép phải |
| `(make-cow 0 ...)` | Đặt bò ngay tại mép trái |

> 💡 Trong Racket, `(- n)` với một tham số sẽ **đổi dấu**: `(- 3)` → `-3`, `(- -6)` → `6`

---

## 5. Thiết kế `render-cow` (v.3) — Helper Functions & Wish List

### Examples cho `render-cow`

```racket
;; bò đi sang phải (dx > 0) → dùng hình bò quay phải
(check-expect (render-cow (make-cow 99 3))
              (place-image RCOW 99 CTR-Y MTS))

;; bò đi sang trái (dx < 0) → dùng hình bò quay trái
(check-expect (render-cow (make-cow 33 -3))
              (place-image LCOW 33 CTR-Y MTS))
```

> 💡 Gregor **cố ý dùng x khác nhau** (99 và 33) trong 2 test — tránh trường hợp vô tình hardcode đúng giá trị.

### Nhận diện "hai nhiệm vụ" trong một hàm

Khi bắt đầu code `render-cow`, Gregor nhận ra hàm này phải làm **2 việc**:
1. **Quyết định** dùng hình bò nào (phải hay trái) ← chọn image
2. **Đặt** hình bò vào đúng vị trí trên nền ← place image

> ⚠️ **Nguyên tắc quan trọng: Mỗi hàm chỉ nên làm MỘT nhiệm vụ!**

### Kỹ thuật Wish List — "Ước" cho helper tồn tại

Thay vì nhét `if` vào trong `render-cow`, Gregor **ước** (wish) có sẵn một hàm helper:

```racket
;; render-cow: Cow -> Image
;; place the appropriate cow image on MTS at its position and CTR-Y
(define (render-cow c)
  (place-image (choose-image c) (cow-x c) CTR-Y MTS))
;;              ^^^^^^^^^^^^^^^
;;              "Ước" hàm này tồn tại — viết wish list entry ngay!
```

**Tại sao viết wish list ngay?**  
→ Vì **ngay lúc vừa ước**, bạn hiểu rõ nhất mình cần hàm đó làm gì. Ghi lại signature + purpose ngay kẻo quên!

### Wish List Entry cho `choose-image`

```racket
;; choose-image: Cow -> Image
;; produce RCOW or LCOW depending on direction cow is going
(define (choose-image c)   ;; stub
  RCOW)
```

> 🎯 **Điều thú vị**: Khi chạy test với stub luôn trả về `RCOW`, 1 trong 2 test của `render-cow` sẽ **pass ngẫu nhiên** (test bò quay phải). Đây là hành vi bình thường của stub.

### Thiết kế `choose-image` — Hoàn thành wish

```racket
;; choose-image: Cow -> Image
;; produce RCOW or LCOW depending on direction cow is going

(check-expect (choose-image (make-cow 10  3)) RCOW)  ;; dx > 0 → phải
(check-expect (choose-image (make-cow 20 -4)) LCOW)  ;; dx < 0 → trái

(define (choose-image c)
  (if (> (cow-dx c) 0)
      RCOW
      LCOW))
```

> Khi `dx = 0` → mặc định dùng `LCOW` (quyết định thiết kế tùy ý, Gregor chọn vậy).

### Kết quả: Tất cả test pass!

Khi `choose-image` hoàn thành:
- 2 test của `choose-image` → ✅
- 2 test của `render-cow` → ✅ (vì `render-cow` gọi `choose-image`)
- 6 test của `next-cow` → ✅

> Helper function hoạt động → hàm gọi nó cũng tự động hoạt động!

---

## 6. Quy trình Wish List — Tóm tắt

```
Đang code hàm A
    → Nhận ra cần hàm B (nhiệm vụ riêng)
    → Viết wish list entry cho B (signature + purpose + stub)
    → Dùng B trong A như thể nó đã tồn tại
    → Hoàn thành A
    → Tìm "!!!" hoặc stub → Ồ, B chưa xong!
    → Thiết kế B theo Design Recipe đầy đủ
    → Chạy test → tất cả pass (cả A lẫn B)
```

### Khi nào nên dùng helper function?

| Trường hợp | Dùng helper? |
|-------------|-------------|
| Hàm đang làm **2 nhiệm vụ riêng biệt** | ✅ Có |
| Logic chọn lựa phức tạp bên trong hàm | ✅ Có |
| Nhiệm vụ phụ rất nhỏ (1 dòng) | 🤔 Tùy — có lập trình viên sẽ không tách |
| Code dễ đọc hơn khi tách ra | ✅ Có |

> Gregor: *"Trong trường hợp này, không có quy tắc cứng nhắc. Bạn phải tự nhận ra rằng `choose-image` là một nhiệm vụ riêng biệt."*

---

## 7. Chạy chương trình & Bonus

### Chạy thử

```racket
(main (make-cow 0 3))  ;; bò bắt đầu ở mép trái, di chuyển 3px/tick sang phải
```

→ Con bò xuất hiện và di chuyển qua lại trên màn hình! 🐄

### Bonus: Hiệu ứng "waddle" (lắc lư)

Gregor gợi ý một cải tiến thú vị:
1. Xoay hình bò vài độ sang trái/phải → tạo 2 hình bò nghiêng
2. Dùng tốc độ là số lẻ (ví dụ 3)
3. Chọn hình bò dựa vào **vị trí chẵn/lẻ** → bò trông như đang **lắc lư** khi đi!

> 🐄 Đây là bài tập tự làm thêm — tốt cho luyện tập trước khi làm homework.

### Bài tập còn lại: `handle-key`

Hàm `handle-key` được để lại cho sinh viên tự hoàn thành (đáp án ở Cowabunga v.5).

---

## 8. Bài học rút ra

### Từ v.2: Design Recipe thực sự hiệu quả

```
Signature → Purpose → Stub → Examples → Template → Code → Test
```

1. **Examples trước, code sau**: 6 examples cụ thể giúp phân tích rõ boundary cases TRƯỚC KHI viết logic
2. **Từ examples → nhận ra pattern**: 6 examples nhưng chỉ có 3 cases → cấu trúc `cond` 3 nhánh
3. **Template là điểm khởi đầu**: Template cho biết mình có `(cow-x c)` và `(cow-dx c)` để làm việc
4. **Domain knowledge là phần khó**: Logic code thực ra đơn giản, cái phức tạp là hiểu bài toán hình học (di chuyển, bounce)

### Từ v.3: Helper Functions & Single Responsibility

5. **Mỗi hàm một nhiệm vụ**: Khi phát hiện hàm làm 2 việc → tách ra helper
6. **Wish List là công cụ mạnh**: Ước cho helper tồn tại → viết signature + purpose ngay → code tiếp → quay lại hoàn thành sau
7. **Code dễ đọc hơn**: `(place-image (choose-image c) ...)` tự giải thích — "đặt hình, ai đó chọn hình giùm"
8. **Test lan truyền**: Helper pass → hàm gọi nó cũng pass

### Liên hệ với TDD & Software Engineering

- Quy trình HtC rất giống **Test-Driven Development**: viết test → fail → code → pass
- Nguyên tắc **mỗi hàm một nhiệm vụ** chính là **Single Responsibility Principle** (SRP) trong OOP
- Kỹ thuật **wish list** giống **top-down design** — thiết kế từ trên xuống, triển khai từ dưới lên

---

## 9. Thuật ngữ chính

| Thuật ngữ | Giải thích |
|-----------|-----------|
| **Compound Data** | Dữ liệu kết hợp, ở đây `Cow` gồm 2 trường `x` và `dx` |
| **big-bang** | Framework tương tác trong Racket — xử lý tick, draw, key events |
| **Boundary case** | Trường hợp biên — ở đây là khi bò chạm/vượt mép |
| **Template** | Bộ khung hàm tự động sinh từ data definition |
| **`cond`** | Biểu thức điều kiện trong Racket (tương tự if-else if-else) |
| **Stub** | Hàm giả (dummy) để test chạy được trước khi viết logic thật |
| **Helper function** | Hàm phụ trợ — tách nhiệm vụ riêng ra khỏi hàm chính |
| **Wish list** | Danh sách các hàm cần thiết kế — ghi signature + purpose + stub, hoàn thành sau |
| **Single Responsibility** | Nguyên tắc: mỗi hàm chỉ nên làm **một** nhiệm vụ duy nhất |

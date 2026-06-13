#lang htdp/bsl
(require 2htdp/image)

;; boxify-starter-tests.rkt
;;
;; Comprehensive tests for the boxify function from boxify-starter.rkt.
;;
;; boxify : Image -> Image
;; Produce an image that is the given image with a black outline box around it.
;; The outline rectangle is 2 pixels wider and 2 pixels taller than the input image
;; (1 pixel of border on each side), using overlay to center the image inside.

;; Implementation under test (mirrors boxify-starter.rkt):
(define (boxify img)
  (overlay img
           (rectangle (+ (image-width img) 2)
                      (+ (image-height img) 2)
                      "outline"
                      "black")))


;; ---------- Test constants ----------

(define RED-ELLIPSE   (ellipse 60 30 "solid" "red"))
(define BLUE-CIRCLE   (circle 10 "solid" "blue"))
(define GREEN-RECT    (rectangle 40 20 "solid" "green"))
(define YELLOW-SQUARE (rectangle 50 50 "solid" "yellow"))
(define SMALL-CIRCLE  (circle 1 "solid" "black"))
(define WIDE-RECT     (rectangle 200 10 "solid" "orange"))
(define TALL-RECT     (rectangle 10 200 "solid" "purple"))
(define OUTLINE-RECT  (rectangle 30 30 "outline" "blue"))
(define PINK-STAR     (star 20 "solid" "pink"))
(define NESTED        (boxify (rectangle 30 30 "solid" "gray")))


;; ---------- Existing course tests (from boxify-starter.rkt) ----------

;; Test 1: ellipse 60x30 - the course example
(check-expect (boxify RED-ELLIPSE)
              (overlay RED-ELLIPSE
                       (rectangle 62 32 "outline" "black")))

;; Test 2: circle with radius 10 (bounding box 20x20)
(check-expect (boxify BLUE-CIRCLE)
              (overlay BLUE-CIRCLE
                       (rectangle 22 22 "outline" "black")))


;; ---------- Output dimensions ----------

;; Test 3: output width is image-width + 2
(check-expect (image-width (boxify GREEN-RECT))
              42)

;; Test 4: output height is image-height + 2
(check-expect (image-height (boxify GREEN-RECT))
              22)

;; Test 5: output width for a square image
(check-expect (image-width (boxify YELLOW-SQUARE))
              52)

;; Test 6: output height for a square image
(check-expect (image-height (boxify YELLOW-SQUARE))
              52)

;; Test 7: very small image (circle radius 1, bounding box 2x2)
(check-expect (image-width (boxify SMALL-CIRCLE))
              4)

(check-expect (image-height (boxify SMALL-CIRCLE))
              4)

;; Test 8: wide image — width grows by 2, height grows by 2
(check-expect (image-width (boxify WIDE-RECT))
              202)

(check-expect (image-height (boxify WIDE-RECT))
              12)

;; Test 9: tall image — height grows by 2, width grows by 2
(check-expect (image-width (boxify TALL-RECT))
              12)

(check-expect (image-height (boxify TALL-RECT))
              202)


;; ---------- Rectangle image tests ----------

;; Test 10: green rectangle — explicit expected value
(check-expect (boxify GREEN-RECT)
              (overlay GREEN-RECT
                       (rectangle 42 22 "outline" "black")))

;; Test 11: yellow square — explicit expected value
(check-expect (boxify YELLOW-SQUARE)
              (overlay YELLOW-SQUARE
                       (rectangle 52 52 "outline" "black")))

;; Test 12: wide rectangle — non-square aspect ratio
(check-expect (boxify WIDE-RECT)
              (overlay WIDE-RECT
                       (rectangle 202 12 "outline" "black")))

;; Test 13: tall rectangle — non-square aspect ratio
(check-expect (boxify TALL-RECT)
              (overlay TALL-RECT
                       (rectangle 12 202 "outline" "black")))

;; Test 14: small image
(check-expect (boxify SMALL-CIRCLE)
              (overlay SMALL-CIRCLE
                       (rectangle 4 4 "outline" "black")))


;; ---------- Outline style and color ----------

;; Test 15: the surrounding rectangle uses "outline" mode, not "solid"
;; An "outline" rectangle with the same dimensions as a "solid" one has the same bounding box.
;; We verify by comparing with an equivalent overlay using outline mode.
(check-expect (boxify (rectangle 20 10 "solid" "red"))
              (overlay (rectangle 20 10 "solid" "red")
                       (rectangle 22 12 "outline" "black")))

;; Test 16: the border rectangle is explicitly black
;; Verify that using "outline" + "black" matches, not another color.
(check-expect (boxify (rectangle 10 10 "solid" "white"))
              (overlay (rectangle 10 10 "solid" "white")
                       (rectangle 12 12 "outline" "black")))


;; ---------- Input image with outline style ----------

;; Test 17: input image that is itself an outline rectangle
(check-expect (boxify OUTLINE-RECT)
              (overlay OUTLINE-RECT
                       (rectangle 32 32 "outline" "black")))


;; ---------- Star (non-rectangular bounding box) ----------

;; Test 18: star image — bounding box dimensions
(check-expect (image-width (boxify PINK-STAR))
              (+ (image-width PINK-STAR) 2))

(check-expect (image-height (boxify PINK-STAR))
              (+ (image-height PINK-STAR) 2))

;; Test 19: star image — full structural check
(check-expect (boxify PINK-STAR)
              (overlay PINK-STAR
                       (rectangle (+ (image-width PINK-STAR) 2)
                                  (+ (image-height PINK-STAR) 2)
                                  "outline"
                                  "black")))


;; ---------- Idempotence / nesting ----------

;; Test 20: boxifying an already-boxified image adds another layer of outline
;; The result should be a box around the already-boxed image.
(check-expect (boxify NESTED)
              (overlay NESTED
                       (rectangle (+ (image-width NESTED) 2)
                                  (+ (image-height NESTED) 2)
                                  "outline"
                                  "black")))

;; Test 21: each level of nesting adds 2 pixels in each direction
(check-expect (image-width (boxify NESTED))
              (+ (image-width NESTED) 2))


;; ---------- Regression / boundary cases ----------

;; Test 22: calling boxify with inline anonymous expressions (no named constant)
(check-expect (boxify (rectangle 1 1 "solid" "blue"))
              (overlay (rectangle 1 1 "solid" "blue")
                       (rectangle 3 3 "outline" "black")))

;; Test 23: non-square ellipse, verify both dimensions change by exactly 2
(check-expect (image-width (boxify (ellipse 100 50 "solid" "green")))
              102)

(check-expect (image-height (boxify (ellipse 100 50 "solid" "green")))
              52)

;; Test 24: overlay argument order — image must be ABOVE the rectangle (first arg to overlay)
;; We verify by testing a known fully-transparent-background image: the original image
;; should be visible on top, meaning the result equals overlay(img, rect) not overlay(rect, img).
;; A solid colored square boxified should look like the square with a border, not a plain rect.
(check-expect (boxify (rectangle 40 40 "solid" "red"))
              (overlay (rectangle 40 40 "solid" "red")
                       (rectangle 42 42 "outline" "black")))

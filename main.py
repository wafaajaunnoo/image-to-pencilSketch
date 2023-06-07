import cv2

image1 = cv2.imread('image/path')
window_name = 'Original picture'

cv2.imshow(window_name_image1)
grey_img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(grey_img)

blur = cv2.GaussianBlur(invert, (21, 21), 0)
invertedblur = cv2.bitwise_not(blur)
sketch = cv2.divide(grey_img, invertedblur, scale=256.0)

cv2.imwrite("image/path", sketch)

image = cv2.imread("image/path")
window_name = 'Sketch'

cv2.imshow(window_name, image)
cv2.waitkey(0)
cv2.destroyAllWindows()

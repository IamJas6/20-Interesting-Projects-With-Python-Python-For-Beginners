import cv2
img = cv2.imread("body.jpg")
grey = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
invert = cv2.bitwise_not(grey)
blur = cv2.GaussianBlur(invert, (21,21),0)
invertblur = cv2.bitwise_not(blur)
sketch = cv2.divide(grey, invertblur, scale=256.0)
cv2.imwrite("suhailbody.png", sketch)
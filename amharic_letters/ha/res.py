import cv2

for i in range(124):
    s = str(i) + '.jpg'
    im = cv2.imread(s)
    im = cv2.resize(im,(28,28))
    cv2.imwrite(s,im)

import cv2
import os
os.system('mogrify -format jpg *.ps')
os.system('rm *.ps')

for i in range(100):
    s = str(i) + '.jpg'
    im = cv2.imread(s)
    im = cv2.resize(im,(28,28))
    cv2.imwrite(s,im)

import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\user\PycharmProjects\PythonStudy\tesseractOCR\picture\blackAndWhitePic\BWhandwrittenSample3Edit.jpg")
# アパーチャーサイズ 3, 5, or 7 など 1 より大きい奇数。数値が大きいほどぼかしが出る。
ksize = 11
# 中央値フィルタ
img_mask = cv2.medianBlur(img, ksize)
plt.imshow(img_mask)

cv2.imwrite(r"C:/Users/user/PycharmProjects/PythonStudy/tesseractOCR/picture/blackAndWhitePic/noiseRemovalBWhandwrittenSample3Edit.jpg", img_mask)

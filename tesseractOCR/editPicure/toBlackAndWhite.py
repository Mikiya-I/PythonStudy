# opencvとnumpyのimport
import cv2
import numpy as np

# 画像の読み込み
origin_file_dir = "picture/"
origin_file_name = 'handwrittenSample3Edit.jpg'
# img = cv2.imread(origin_file_dir + origin_file_name)
img = cv2.imread("C:/Users/user/PycharmProjects/PythonStudy/tesseractOCR/picture/handwrittenSample3Edit.jpg")

# グレースケール変換
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# 閾値の設定
threshold_value = 129

# 配列の作成（output用）
threshold_img = gray.copy()

# 実装(numpy)
threshold_img[gray < threshold_value] = 0
threshold_img[gray >= threshold_value] = 255

# Output
cv2.imwrite("C:/Users/user/PycharmProjects/PythonStudy/tesseractOCR/picture/blackAndWhitePic/BWhandwrittenSample3Edit.jpg", threshold_img)
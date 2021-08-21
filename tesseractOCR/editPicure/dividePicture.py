# 画像分割　sepa.py
import os
import cv2
import numpy as np

# 画像読み込み
image = cv2.imread('./picture/handwrittenSample3Edit.jpg')
# 画像サイズを調べる（高さ：h 、幅：w）
h, w = image.shape[:2]
n = 10  # 画像分割数
y0 = int(h / n)
x0 = int(w / n)
# 分割した画像を内包表記でリスト化
c = [image[x0 * x:x0 * (x + 1), y0 * y:y0 * (y + 1)] for x in range(n) for y in range(n)]
# c のリストから1つづつ取り出して
# ファイル番号（0.jpg、1.jpg、・・）を付けて、sepaフォルダに保存
for i, img in enumerate(c):
    cv2.imwrite(os.path.join('./picture/dividedpic', '{}.jpg'.format(i)), img)

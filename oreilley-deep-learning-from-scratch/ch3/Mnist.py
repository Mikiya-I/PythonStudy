import numpy as np
import sys, os

# 親ディレクトリのファイルをインポートするための設定
sys.path.append(os.pardir)
from dataset.mnist import load_mnist
from pillow import Image


def img_show(image):
    pil_img = Image.fromarray(np.unit8(image))
    pil_img.show()


# データの呼び出し
(xTrain, yTrain), (xTest, yTest) = \
    load_mnist(flatten=True, normalize=False)

img = xTrain[0]
label = yTrain[0]
print(label)

print(img.shape)
img = img.rehape(28, 28)
print(img.shape)

img_show(img)

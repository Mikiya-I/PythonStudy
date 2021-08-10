import numpy as np
import sys, os

# 親ディレクトリのファイルをインポートするための設定
sys.path.append(os.pardir)
from dataset.mnist import load_mnist

# データの呼び出し
(xTrain, yTrain), (xTest, yTest) = \
    load_mnist(flatten=True, normalize=False)

# それぞれのデータの形状を出力
print(xTrain.shape)
print(yTrain.shape)
print(xTest.shape)
print(yTest.shape)

import numpy as np
import cv2
import matplotlib.pyplot as plt


def opening():
    # 膨張・収縮処理
    img = cv2.imread(
        r"C:/Users/user/PycharmProjects/PythonStudy/tesseractOCR/picture/blackAndWhitePic/noiseRemovalBWhandwrittenSample3Edit.jpg")
    # 近傍の定義
    neiborhood = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]],
                          np.uint8)
    # 収縮
    img_erode = cv2.erode(img, neiborhood, iterations=7)
    # 膨張
    img_dilate = cv2.dilate(img_erode, neiborhood, iterations=7)

    plt.imshow(img_erode)
    # plt.show()
    cv2.imwrite(
        r"C:/Users/user/PycharmProjects/PythonStudy/tesseractOCR/picture/blackAndWhitePic/ErodeBWhandwrittenSample3Edit.jpg",
        img_erode)

def closing():
    # 膨張・収縮処理
    img = cv2.imread(
        r"C:/Users/user/PycharmProjects/PythonStudy/tesseractOCR/picture/blackAndWhitePic/noiseRemovalBWhandwrittenSample3Edit.jpg")
    # 近傍の定義
    neiborhood = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]],
                          np.uint8)
    # 膨張
    img_dilate = cv2.dilate(img, neiborhood, iterations=3)
    # 収縮
    img_erode = cv2.erode(img_dilate, neiborhood, iterations=3)

    plt.imshow(img_dilate)
    # plt.show()


opening()
closing()

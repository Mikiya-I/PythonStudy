import os
from PIL import Image
import pyocr
import pyocr.builders


def main():
    # 1.インストール済みのTesseractのパスを通す
    path_tesseract = "C:\\Program Files\\Tesseract-OCR"
    if path_tesseract not in os.environ["PATH"].split(os.pathsep):
        os.environ["PATH"] += os.pathsep + path_tesseract

    # pyocrへ利用するOCRエンジンをTesseractに指定する。
    tools = pyocr.get_available_tools()
    tool = tools[0]

    builder = pyocr.builders.DigitBuilder(tesseract_layout=10)
    f = open('resultTxt/dividedResult.txt', 'w')
    dir_path = "./picture/dividedpic/"
    file_list = os.listdir(dir_path)
    i = 1
    for fname in file_list:
        path = os.path.join(dir_path, fname)
        if os.path.isfile(path):
            img = Image.open(path)
            img = img.convert("L")
            result = tool.image_to_string(img, lang="eng", builder=builder)
            # 読み込めなかった場合はx
            if result == '':
                result = 'x'
            print(fname + ':' + result)
            f.write(result + ' ')
            if i % 10 == 0:
                f.write('\n')
        i += 1
    f.close()


if __name__ == '__main__':
    main()

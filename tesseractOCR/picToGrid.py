import os
from PIL import Image
import pyocr
import pyocr.builders


def main():
    path_tesseract = "C:\\Program Files\\Tesseract-OCR"
    if path_tesseract not in os.environ["PATH"].split(os.pathsep):
        os.environ["PATH"] += os.pathsep + path_tesseract

    tools = pyocr.get_available_tools()
    tool = tools[0]

    builder = pyocr.builders.TextBuilder(tesseract_layout=6)
    f = open('/resultTxt/resultGrid.txt', 'w')
    dir_path = "./img_src/"
    file_list = os.listdir(dir_path)
    i = 1
    for fname in file_list:
        path = os.path.join(dir_path, fname)
        if os.path.isfile(path):
            img = Image.open(path)
            img = img.convert("L")
            result = tool.image_to_string(img, lang="eng", builder=builder)
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

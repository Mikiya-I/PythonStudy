import os
from PIL import Image
import pyocr


# 1.インストール済みのTesseractのパスを通す
path_tesseract = "C:\\Program Files\\Tesseract-OCR"
if path_tesseract not in os.environ["PATH"].split(os.pathsep):
    os.environ["PATH"] += os.pathsep + path_tesseract

# pyocrへ利用するOCRエンジンをTesseractに指定する。
tools = pyocr.get_available_tools()
tool = tools[0]

# OCR対象の画像ファイルを読み込む
img = Image.open("tesseract-3.jpg")
img = Image.open("handWrittenSample.png")

# 画像から文字を読み込む
builder = pyocr.builders.TextBuilder(tesseract_layout=6)
text = tool.image_to_string(img, lang="jpn", builder=builder)

print(text)
# f = open('tesseract-3Result.txt', 'w',encoding='utf-8')
f = open('handWrittenSampleResult.txt', 'w',encoding='utf-8')
f.write(text)
f.close()

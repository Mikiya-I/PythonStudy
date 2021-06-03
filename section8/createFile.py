# coding=utf-8
# f = open('test.txt', 'a')
# ファイルに上書き
# f = open('test.txt', 'w')
# javaでいうtry with resource
'''
with open('test.txt', 'w') as f:
    f.write('Test\n')
    print('print', file=f)
'''
# f.close()

# with open('test.txt', 'r') as f:
    # while True:
    #     chunk = 2
    #     # 引数に入れた文字の分だけ読み込む
    #     line = f.read(chunk)
    #     #       line = f.readline()
    #     #　      printのデフォルトでの改行をしない
    #     print(line, end='')
    #     if not line:
    #         break
    # 現在の文字の位置
    # print(f.tell())
    # print(f.read(1))
    # # 引数の指定の文字に移動
    # f.seek(5)
    # print(f.read(1))

#   ファイルの読み書きを両方やる(開いた時に全て消えるから注意)
with open('test.txt' ,'w+') as f:
    print(f.read())
    f.write("print\n")
    f.write("test")






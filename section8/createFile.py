# coding=utf-8
# f = open('test.txt', 'a')
f = open('test.txt', 'w')  # ファイルに上書き
f.write('Test\n')
print('print', file=f)
f.close()

import string

#　テンプレート
with open('test/templateTest.txt') as f:
    t = string.Template(f.read())

# テンプレートの可変部分に文字列を入れる（javaでいう{1}みたいなもの）
contents = t.substitute(name='tmp1', contents='tmp2')
print(contents)
print('aaa')

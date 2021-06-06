# windowsでいう所のzipみたいなもの
import tarfile
import os
import pathlib

# ディレクトリ/ファイル生成
# os.mkdir('testDir')
# pathlib.Path('testDir/testFile').touch()
# with open('testDir/testFile', 'w') as f:
#     f.write('test')
# print(os.getcwd())
# os.mkdir('testDir2')
# pathlib.Path('testDir2/testFile2').touch()
# with open('testDir2/testFile2', 'w') as f:
#     f.write('test2')
# print(os.getcwd())

# with tarfile.open('test.tar.gz', 'w:gz') as tr:
#     tr.add('testDir')

# ファイル名とライブラリ名が競合するとAttributeErrorが発生する
# with tarfile.open('test.tar.gz', 'w:gz') as tr:
#     tr.add('testDir')

with tarfile.open('test.tar.gz' , 'r:gz')as tr:
#     tr.extractall(path= 'testTar')
    with tr.extractfile('testDir/testFile') as f:
        print(f.read())


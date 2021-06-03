import os
import pathlib
import glob
import shutil

# print(os.path.exists('test.txt'))
# print(os.path.isfile('test.txt'))
# print(os.path.isdir('test'))

#  ファイル名の書き換え
# os.rename('test.txt', 'renamed.txt')
# 指定したファイルにリンクしたファイルを作成(片方の変更がもう片方にも反映される)
# os.symlink('renamed.txt','sysmlinked.txt')

#  フォルダの作成/削除
# os.mkdir('testDir')
# 中身がはいっていると無理
# os.rmdir('testDir')

# ファイル生成/削除
# pathlib.Path('empty.txt').touch()
# os.remove('empty.txt')


# os.mkdir('textDir')
# os.mkdir('textDir/dir2')
# フォルダの構造
# print(os.listdir('textDir'))
# pathlib.Path('textDir/dir2/empty.txt').touch()
# フォルダの中身のファイルを調べる
# print(glob.glob('textDir/dir2/*'))
# # ファイルのコピー
# shutil.copy('textDir/dir2/empty.txt', 'textDir/dir2/empty2.txt')
# print(glob.glob('textDir/dir2/*'))

# 中身が入っていても消せる
# shutil.rmtree('textDir')

# 現在の実行されているディレクトリ
print(os.getcwd())
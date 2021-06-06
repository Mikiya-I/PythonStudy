import zipfile

with zipfile.ZipFile('test.zip','w')as z:
    z.write('testDir2')
    z.write('testDir2/test.txt')
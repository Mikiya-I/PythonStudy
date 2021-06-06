import string
import csv


def main():
    print('input your name')
    name = input()

    with open('textDir/tmp1.txt')as tmp:
        tmp1 = string.Template(tmp.readline())
        tmp2 = string.Template(tmp.readline())
        tmp3 = string.Template(tmp.readline())
        tmp4 = string.Template(tmp.readline())

    sentence1 = tmp1.substitute(name=name)
    print(sentence1)

    arr = readCsv()
    findword = False
    for i in range(1, len(arr)):
        print(tmp2.substitute(wordTmp=arr[i][0]))
        ans = input()
        if ans == 'yes':
            # wordcount(row['word'])
            newcnt = int(arr[i][1]) + 1
            arr[i][1] = newcnt
            findword = True
            break
        #     csvFile.write()
        #     print('finish')
        #     return
    if findword:
        with open('csvDIr/count.csv', 'w') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(arr)
            print('finish')
            return

    print(tmp3.substitute())
    word1 = input()
    with open('csvDIr/count.csv', 'a') as csvfile:
        fieldnames = ['word', 'cnt']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'word': word1, 'cnt': 1})

    print(tmp4.substitute(word=word1))


# def wordcount(word):
#     with open('csvDir/count.csv', 'wt', newline='')as cntCsv:
#         # fields = ['word', 'cnt']
#         # writer = csv.DictWriter(cntCsv, fieldnames=fields)
#         # writer.writeheader()
#         data = csv.DictReader(cntCsv)
#         for row in data:
#             if row['name'] == word:
#                 row['cnt'] +=1
#                 break

def readCsv():
    with open('csvDIr/count.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        lis = []
        for i in reader:
            lis.append(i)
        return lis


main()

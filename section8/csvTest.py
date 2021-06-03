import csv

with open('test/test.csv', 'w') as csvFile:
    fieldnames = ['name', 'count']
    writer = csv.DictWriter(csvFile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'name': 'A', 'count': 1})
    writer.writerow({'name': 'B', 'count': 2})

with open('test/test.csv' ,'r') as csvFile:
    reader = csv.DictReader(csvFile)
    for row in reader:
        print(row['name'], row['count'])


import csv

def swap(list1, j):
    temp = list1[j]
    list1[j] = list1[j+1]
    list1[j+1] = temp

def sort(list1, list2):
    length = len(list1)
    for i in range(0, length):
        for j in range(0, length - 1):
            if(list1[j] > list1[j+1]):
                swap(list1, j)
                swap(list2, j)


firstNames = []
lastNames = []

with open("C:\\Users\\cbedn\\Desktop\\SE126.02\\Lab 9\\Lab9.csv") as csvfile:
    file = csv.reader(csvfile)
    for row in file:
        firstNames.append(row[0])
        lastNames.append(row[1])
        sort(lastNames, firstNames)
    csvfile.close()

with open("Lab9Write.csv", 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(lastNames)
    writer.writerow(firstNames)
    csvfile.close()



    
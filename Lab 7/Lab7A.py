import csv


def swap(tList, x):
    temp = tList[x]
    tList[x] = tList[x+1]
    tList[x+1] = temp

def BackwardSwap(tList, x):
    temp = tList[x]
    tList[x] = tList[x-1]
    tList[x-1] = temp



def lowestToHighest(list1, list2, list3, list4, list5, length):
    for i in range(0, length):
        for j in range(0, length - 1):
            if (list1[j] > list1[j + 1]):
                swap(list1, j)
                swap(list2, j)
                swap(list3, j)
                swap(list4, j)
                swap(list5, j)

def highestToLowest(list1, list2, list3, list4, list5, length):
    for i in range(0, length):
        for j in range(0, length-1):
            if (list1[j] < list1[j+1]):
                swap(list1, j)
                swap(list2, j)
                swap(list3, j)
                swap(list4, j)
                swap(list5, j) 

                

def getAverageSalaryForMIS(length):
    sum = 0
    count = 0
    for x in range(0, length):
        if (departments[x] == "MIS"):
            sum += salaries[x]
            count += 1
        else:
            sum += 0   
    avg = sum / count
    return avg


def getRaise(list1, length):
    sum = 0
    for x in range(0, length):
        raised = list1[x] * .05
        sum += raised
    
    return sum
    
    

firstNames = []
lastNames = []
departments = []
positions = []
salaries = []


with open("C:\\Users\\cbedn\\Desktop\\SE126.02\\Lab 7\\Lab7.csv") as csvfile:
    file = csv.reader(csvfile)
    for row in file:
        firstNames.append(row[0])
        lastNames.append(row[1])
        departments.append(row[2])
        positions.append(row[3])
        salaries.append(int(row[4]))

length = len(salaries)
lowestToHighest(salaries, lastNames, firstNames, departments, positions, length)
average = getAverageSalaryForMIS(length)
raiseCost = getRaise(salaries, length)

print("10 Lowest Salaries:")
for x in range(0, 10):
    print("Salary: {}\tLast Name: {:10} Department: {:10}".format(salaries[x], lastNames[x], departments[x]))

highestToLowest(salaries, lastNames, firstNames, departments, positions, length)

print()

print("10 Highest Salaries")
for x in range(0, 10):
    print("Salary: {}\tLast Name: {:10} Department: {:10}".format(salaries[x], lastNames[x], departments[x]))

print("\nAverage Salary for MIS Department: {:.2f}".format(average))



print("\nCompany raise cost: {:.2f}".format(raiseCost))

print("\n\nAlphabetically Sorted, first 5:")
lowestToHighest(departments, lastNames, salaries, firstNames, positions, length)


for x in range(0, 5):
    print("Department: {:10}\tLast Name: {:10}".format(departments[x], lastNames[x]))

print("\nAlphabetically Sorted, last 5:")
highestToLowest(departments, lastNames, salaries, firstNames, positions, length)
for x in range(0, 5):
    print("Department: {:10}\tLast Name: {:10}".format(departments[x], lastNames[x]))
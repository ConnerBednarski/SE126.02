# Conner Bednarski
# Lab 3b
# SE126.02
#
#Variables Used:
# desktopCost       Cost of the total desktops
# Laptop Cost       Cost of the total laptops
# replacedDesktop   Number of replaced desktops
# replaced laptop   Number of replaced Laptops
# yr                current year
# compTypeList      Computer Type Data List
# brandList         Brand Data List
# processorList     Processor Data List
# ramList           RAM Data List
# sizeofHddOneList  Size of the first HDD Data List
# numOfHddList      Number of HDD Data List
# osList            Os Data List
# yearList          Year Data List
# sizeOfHdd2List    Size of the second HDD Data List
# compType          Computer type
# brand             Computer brand
# numOfHDD          Number Of HDD on Computer
# year              Holds the Computers year

#================================================================

import csv
from datetime import date

yr = date.today().year
yr -= 2000

desktopCost = 0
laptopCost = 0
replacedDesktop = 0
replacedLaptop = 0

compTypeList = []
brandList = []
processorList = []
ramList = []
sizeofHddOneList = []
numOfHddList = []
osList = []
yearList = []
sizeOfHdd2List = []

with open("C:\\Users\\cbedn\\Downloads\\lab3a.csv") as csvfile:
    file = csv.reader(csvfile)
    for row in file:
        compType = row[0]
        if compType == "D":
            compType = "Desktop"
        elif compType == "L":
            compType = "Laptop"

        compTypeList.append(compType)

        brand = row[1]
        if brand == "DL":
            brand = "Dell"
        elif brand == "GW":
            brand = "Gateway"

        brandList.append(brand)

        numOfHDD = int(row[5])

        processorList.append(row[2])
        ramList.append(row[3])
        sizeofHddOneList.append(row[4])
        numOfHddList.append(numOfHDD)

        if numOfHDD == 1:

            osList.append(row[6])
            year = int(row[7])
            yearList.append(year)

        elif numOfHDD == 2:

            sizeOfHdd2List.append(row[6])
            osList.append(row[7])
            year = int(row[8])
            yearList.append(int(row[8]))

        if (yr - 2) > year:
            if compType == "Desktop":
                desktopCost += 2000
                replacedDesktop += 1
            if compType == "Laptop":
                laptopCost += 1500
                replacedLaptop += 1

print("To replace {0} it will cost ${1:5}".format(replacedDesktop, desktopCost))
print("To replace {0} it will cost ${1:5}".format(replacedLaptop, laptopCost))


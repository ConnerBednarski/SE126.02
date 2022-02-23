# Conner Bednarski
# Lab 3a
# SE126.02
#
#Variables Used:
# desktopCost       Cost of the total desktops
# Laptop Cost       Cost of the total laptops
# replacedDesktop   Number of replaced desktops
# replaced laptop   Number of replaced Laptops
# yr                current year
# compType          Computer type
# brand             Computer brand
# ram               Computer RAM
# sizeOfHDD         Computer HDD1 size
# numOfHDD          Number Of HDD on Computer
# os                Computer OS
# sizeOfHDD2        Computer HDD2 size
# year              Holds the Computers year

#================================================================

import csv
import datetime

yr = datetime.datetime.now().year
yr -= 2000

desktopCost = 0
laptopCost = 0
replacedDesktop = 0
replacedLaptop = 0

with open("C:\\Users\\cbedn\\Downloads\\lab3a.csv") as csvfile:
    file = csv.reader(csvfile)
    for row in file:
        compType = row[0]
        if compType == "D":
            compType = "Desktop"
        elif compType == "L":
            compType = "Laptop"

        brand = row[1]
        if brand == "D":
            brand = "Dell"
        elif brand == "GW":
            brand = "Gateway"

        processor = row[2]
        ram = row[3]
        sizeOfHDD = row[4]
        numOfHDD = int(row[5])

        if numOfHDD == 1:
            os = row[6]
            year = int(row[7])
        elif numOfHDD == 2:
            sizeOfHDD2 = row[6]
            os = row[7]
            year = int(row[8])

        if (yr - 2) > year:
            if compType == "Desktop":
                desktopCost += 2000
                replacedDesktop += 1
            if compType == "Laptop":
                laptopCost += 1500
                replacedLaptop += 1

print("To replace {0} it will cost ${1:5}".format(replacedDesktop, desktopCost))
print("To replace {0} it will cost ${1:5}".format(replacedLaptop, laptopCost))
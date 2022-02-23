#   Conner Bednarski
#   SE126
#   Lab 2b
#
#   file    is the file stored in the location defined in open
#   row     is used to read one row ar a time from file
# 
#   row[0] refers to the type of computer (Desktop or Laptop)
#   row[1] refers to the brand of the computer (Dell, HP, or Gateway)
#   row[2] refers to the cpu in the computer
#   row[3] refers to the amount of RAM
#   row[4] refers to the storage on the first disk
#   row[5] refers to the number of HDD in the device
#   row[6] refers to the amount of storage on the second disk
#   row[7] refers to the OS
#   row[8] refers to the Year
#
#   numComputers   Number of computers in the file
#   compType       Type of device
#   brand          Brand of the device
#   cpu            Type of CPU on device
#   ram            Amount of RAM on device
#   diskOne        Storage on the first disk
#   hdd            Number of HDD on device
#   diskTwo        Storage on second disk (if applicable)  
#   os             Type of OS 
#   yr             year
#
#
#======================================================

import csv


numComputers = 0

# Prints the header for the information
print("Type\t Brand\t   CPU      RAM  1st Disk     No HDD    2nd Disk     OS  YR")

# Opens the file
with open("C:\\Users\\008014568\\Desktop\\SE126 CSV Files\\lab2b-1.csv") as csvfile:
    file = csv.reader(csvfile)

    # Loops through all the rows in the file
    for row in file:
        numComputers += 1
        compType = row[0]

        # Changes compType depending on what letter it's set to
        if (compType == "L"):
            compType = "Laptop"
        elif (compType == "D"):
            compType = "Desktop"

        brand = row[1]

        # Changes brand depending on what letters it's currently set to
        if (brand == "DL"):
            brand = "Dell"
        elif (brand == "GW"):
            brand = "Gateway"

        cpu = row[2]
        ram = row[3]
        diskOne = row[4]
        hdd = int(row[5])

        # Detects if there is another OS. If so, sets diskTwo to whatever the file has for row[6]. If nothing, then it sets diskTwo to an empty variable and continues.
        if (hdd > 1):
            diskTwo = row[6]
            os = row[7]
            yr = row[8]
        else:
            diskTwo = ""
            os = row[6]
            yr = row[7]

        # Prints all the information
        print("{0:7}  {1:9} {2:8} {3:4} {4}{5:10}   \t{6:10}  {7} {8}".format(compType, brand, cpu, ram, diskOne, hdd, diskTwo, os, yr))

# Prints the number of computers in the file
print("Number of Computers: {}".format(numComputers))
    


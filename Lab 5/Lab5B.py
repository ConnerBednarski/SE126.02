# Conner Bednarski
# SE126.02
# Lab5B
#
# Variables:
#  
# firstNames        Holds the list of first names
# lastNames         Holds the list of last names
# phoneNumbers      Holds the list of phone numbers
# emails            Holds the list of emails
# department        Holds the list of departments
# position          Holds the list of positions


import csv

firstNames = []
lastNames = []
phoneNumbers = []
emails = []
department = []
position = []

def findEmail():
    '''Aearches through the file for each person with MIS as a department and changes their emails from .com to .net'''
    count = 0
    length = len(department)
    for pos in range(0, length):
        if department[pos] == "MIS":
            count += 1
            emails[pos] = changeEmail(emails[pos])
    return count

def changeEmail(email):
    '''Changes the email and replaces .com with .net'''
    email = email.replace(".com", ".net")
    return email

with open("C:\\Users\\cbedn\\Downloads\\Lab5B.txt") as csvfile:
    file = csv.reader(csvfile)
    for row in file:
      firstNames.append(row[0])
      lastNames.append(row[1])
      phoneNumbers.append(row[2])
      emails.append(row[3])
      department.append(row[4])
      position.append(row[5])

addressesChanged = findEmail()

for x in range(0, len(firstNames)):
    print("{}, {}, {}, {}, {}, {}".format(firstNames[x], lastNames[x], phoneNumbers[x], emails[x], department[x], position[x]))

print("Number of Addresses Changed: {}".format(addressesChanged))




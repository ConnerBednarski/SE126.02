# Conner Bednarski
# SE126.02
# Final Exam
#
# Variables:
# firstNames        Holds the first names from the file
# lastNames         Holds the last names from the file
# states            Holds the states from the file
# phoneNumbers      Holds the phone numbers from the file
# length            Holds the length of lastNames
#
# Everything with t in front of it is temporary
#
# found             Holds a string depending on if the searched name is in the select list
# searchFor         Holds the name the file is searching for
# location          Holds the location of the name searching for if found
#
#==Imports=================================================================
import csv

#===Functions==============================================================

def swap(tList, x):
    '''Swaps two elements in a list'''
    temp = tList[x]
    tList[x] = tList[x+1]
    tList[x+1] = temp

def sort(tLastNames, tFirstNames, tStates, tPhoneNumbers):
    '''Sorts the lists depending on the fist one'''
    length = len(tLastNames)
    for i in range(0, length):
        for j in range(0, length - 1):
            if (tLastNames[j] > tLastNames[j+1]):
                swap(tLastNames, j)
                swap(tFirstNames, j)
                swap(tStates, j)
                swap(tPhoneNumbers, j)

def search(tList1, tList2, tList3, tList4):
    '''Searches for a select name in a file'''
    found = "False"
    searchFor = input("\nWhat name would you like to search for: ")
    for x in range(0, len(tList1)):
        if tList1[x] == searchFor:
            found = "True"
            location = x

    if (found == "True"):
        print("\n", tList1[location], tList2[location], tList3[location], tList4[location])
    else:
        print("Not Found!!!")

#===Main Code====================================================================

# Creating Lists
firstNames = []
lastNames = []
states = []
phoneNumbers = []

# Opening the file and appending the elements to lists
with open("Final Exam\exam1.txt") as csvfile:
    file = csv.reader(csvfile)
    for row in file:
        firstNames.append(row[0])
        lastNames.append(row[1])
        states.append(row[2])
        phoneNumbers.append(row[3])

# Sorting all the lists
sort(lastNames, firstNames, states, phoneNumbers)

# Printing the first 15 records alphabetically
print("First 15 in alphabetical order by last name:\n")
for x in range(0, 15):
    print(lastNames[x], firstNames[x], phoneNumbers[x], states[x])

# Searching for whatever name the user enters
search(lastNames, firstNames, phoneNumbers, states)
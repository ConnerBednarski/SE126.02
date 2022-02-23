# Conner Bednarski
# SE126.02
# Lab 6A
#
# Variables:
#  
# firstNames        Holds the list of first names
# lastNames         Holds the list of last names
# phoneNumbers      Holds the list of phone numbers
# emails            Holds the list of emails
# departments       Holds the list of departments
# positions         Holds the list of positions
# searchName        Gets the name to search for
# min, max, guess   Used to search through the list

#===Imports & Functions=======================================
import csv

def setLists():
    '''Opens the Lab file and adds the data to lists'''
    with open("C:\\Users\\cbedn\\Desktop\\SE126.02\\Lab 6\\Lab6a-2.csv") as csvfile:
        file = csv.reader(csvfile)
        for row in file:
            firstNames.append(row[0])
            lastNames.append(row[1])
            phoneNumbers.append(row[2])
            emails.append(row[3])
            departments.append(row[4])
            positions.append(row[5])



def search():
    '''Asks the user to enter a name and searches the list for that name'''
    searchName = input("Enter name: ")

    min = 0
    max = len(lastNames)

    guess = int((min + max)/2)

    while (searchName != lastNames[guess] and min <= max):
        if (searchName < lastNames[guess]):
            max = guess - 1
        else:
            min = guess + 1
        
        guess = int((min + max)/2)

    if (searchName == lastNames[guess]):
        return "Name was found", guess
    else:
        return "Name was not found", guess


#===Main Code============================================


firstNames = []
lastNames = []
phoneNumbers = []
emails = []
departments = []
positions = []


setLists()
found, guess = search()

# Prints information based on if the person was found or nor
if (found == "Name was found"):
    print("First Name: {}\nLast Name: {}\nPhone Number: {}\nEmail: {}\nDepartment: {}\nPosition: {}".format(firstNames[guess], lastNames[guess], phoneNumbers[guess], emails[guess], departments[guess], positions[guess]))
else:
    print(found)

# Prints the number of records that were searched
print("\nNumber of records searched: {}".format(guess))

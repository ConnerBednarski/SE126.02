#   Conner Bednarski
#   SE126
#   Lab 2a
#
#   file        file stored in the location defined in open
#   row         used to read one row at a time from file
#   
#   row[0] refers to the first piece of fata in the row --- room name
#   row[1] refers to the second piece of data in the row -- max people
#   row[2] refers to the third piece of data in the row --- number of people registered
#
# Variables used:
#
#   numRooms        Number of rooms counter
#   overLimit       Number of rooms over limit
#   roomName        Name of the rooms
#   maxPeople       Max people the room can hold
#   numRegistered   Number of people registered for select room
#   numOver         Number of people over limit
#
#
#
#================================================================

import csv

numRooms = 0
overLimit = 0

# Prints the Header for information
print("Room\t\t\t       Max\t       Min\t\tOver")

# Opens the file
with open("C:\\Users\\008014568\\Desktop\\SE126 CSV Files\\lab2a.csv") as csvfile:
    file = csv.reader(csvfile)

    # Loops through the rows in the file
    for row in file:
        roomName = row[0]
        maxPeople = int(row[1])
        numRegistered = int(row[2])

        # If the number of people registered is higher than the max number of people it adds to the limit counter and creates a numOver variable. After, it prints the room to the console.
        if (numRegistered > maxPeople):
            numOver = numRegistered - maxPeople
            overLimit += 1
            print("{0:18} {1:15} {2:15} {3:15}".format(roomName, maxPeople, numRegistered, numOver))
        
        numRooms += 1

# Prints the number of records it processed and the number of rooms that went over the limit.
print("\nProcessed   {}  records".format(numRooms))
print("There are   {}  room overs the limit.".format(overLimit))
        


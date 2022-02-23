# Conner Bednarski
# Lab 1B
# SE 126.02

# Variables Used:
# answer            Used to loop through the program
# maxCapacity       Max number of people that can be in a room
# numPeople         Number of people in the room
# numAllowed        Number of people that can still enter the room
# numOver           Number of people that need to leave the room

# =============================================

answer = "Y"


while (answer == "Y"):
    maxCapacity = int(input("What is the max number of people that can be in the room: "))
    numPeople = int(input("How many people are attending: "))

    # gets the number of people that can enter the room still.
    numAllowed = maxCapacity - numPeople

    # saves the number of people that need to leave in the numOver variable.
    if (numAllowed < 0):
        numOver = abs(numAllowed)

    # Checks how many people are in the room relative to the capacity and asks however many people to enter or leave depending on the number of pepole in the room
    if (numPeople < maxCapacity):
        print("You are allowed to hold the meeting. {} more people can attend.".format(numAllowed))
    elif (numPeople > maxCapacity):
        print("This meeting cannot be held, it violates the fire regulation. {} people need(s) to leave in order to hold the meeting.".format(numOver))
    
    # Asks if user wants to check more rooms
    answer = input("Do you want to check anymore rooms (y/n)? ").upper()
    while (answer != "Y" and answer != "N"):
        answer = input("Do you want to check anymore rooms (y/n)? ").upper()
# Conner Bednarski
# Lab 1C
# SE 126.02

# Variables Used:
# answer            Used to loop through the program
# maxCapacity       Max number of people that can be in a room
# numPeople         Number of people in the room
# numAllowed        Number of people that can still enter the room
# numOver           Number of people that need to leave the room

# =============================================

def capacity():
    '''Prompts the user to enter a capacity and returns it to the main code'''
    maxCapacity = int(input("What is the capacity of the room? "))

    return maxCapacity

def attendees():
    '''prompts the user to enter the ammount of people attending and returns it to the main code'''
    numPeople = int(input("How many people want to attend the event? "))
    
    return numPeople

def register(maxPeople, peopleAttending):
    '''Determines how many people can still enter or how many need to leave'''
    numAllowed = maxPeople - peopleAttending
    return numAllowed

def check():
    '''asks the user if they want to check another room'''
    newAnswer = input("Do you want to check anymore rooms (y/n)? ").upper()
    while (newAnswer != "Y" and newAnswer != "N"):
        newAnswer = input("Do you want to check anymore rooms (y/n)? ").upper()
    
    return newAnswer

answer = "Y"

while (answer == "Y"):
    maxCapacity = capacity()
    numPeople = attendees()
    numAllowed = register(maxCapacity, numPeople)

    if (numAllowed < 0):
        numOver = abs(numAllowed)
    
    if (numPeople < maxCapacity):
        print("You are allowed to hold the meeting. {} more people can attend.".format(numAllowed))
    elif (numPeople > maxCapacity):
        print("This meeting cannot be held, it violates the fire regulation. {} people need(s) to leave in order to hold the meeting.".format(numOver))
    
    answer = check()
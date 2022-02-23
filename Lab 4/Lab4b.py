# Conner Bednarski
# Lab 4B
# SE 126.02
#
#
# Variables:
# 
# a & aA                Holds the list of seat "A"s
# b & bB                Holds the list of seat "B"s
# c & cC                Holds the list of seat "C"s
# d & dD                Holds the list of seat "D"s
# r & row               Holds the row entered by the user
# s & seat              Holds the seat entered by the user
# customer & answer     Holds the control variable to exit the main loop
#
#===Main========================================================================================

def display(aA, bB, cC, dD):
    '''Displays the seat pattern to the user'''
    for x in range(1, 8):
        print("     ", x, " ", aA[x], " ", bB[x], "     ", cC[x], " ", dD[x])

def selectRow():
    '''Asks the user for what row they want to choose and returns that to the main program'''
    r = int(input("What row would you like to sit in: "))
    return r

def selectSeat():
    '''Asks the user what seat they want to choose and returns it to the main program'''
    s = input("What seat would you like (A/B/C/D): ")
    s = s.upper()

    while (s != "A" and s != "B" and s != "C" and s != "D"):
        print("INVALID RESPONSE. PLEASE CHOOSE ONE OF THE FOUR LETTERS.")
        s = input("What seat would you like (A/B/C/D): ")
        s = s.upper()

    return s

def checkSeat(r, s, aA, bB, cC, dD):
    '''Checks to make sure the seat chosen is available'''
    if (s == "A") and (aA[r] != "X"):
        print("Your seat has been chosen.")
        aA[r] = "X"
    elif (s == "B") and (bB[r] != "X"):
        print("Your seat has been chosen.")
        bB[r] = "X"
    elif (s == "C") and (cC[r] != "X"):
        print("Your seat has been chosen.")
        cC[r] = "X"
    elif (s == "D") and (dD[r] != "X"):
        print("Your seat has been chosen.")
        dD[r] = "X"
    else:
        print("That seat is already taken.")

def choice():
    '''Asks the user if they want to pick another seat'''
    answer = input("Would you like to choose another seat (Y/N): ").upper()

    while (answer != "Y" and answer != "N"):
        print("INVALID ANSWER")
        answer = input("Would you like to choose another seat (Y/N): ")

    return answer

a = ["", "A", "A", "A", "A", "A", "A", "A"]
b = ["", "B", "B", "B", "B", "B", "B", "B"]
c = ["", "C", "C", "C", "C", "C", "C", "C"]
d = ["", "D", "D", "D", "D", "D", "D", "D"]

customer = "Y"
while(customer == "Y"):
    display(a, b, c, d)
    row = selectRow()
    seat = selectSeat()
    checkSeat(row, seat, a, b, c, d)
    display(a, b, c, d)
    customer = choice()



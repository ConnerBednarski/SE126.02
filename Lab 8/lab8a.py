# Row 1 - 5 = $200.00
# Row 6 - 10 = $175.00
# Row 11 - 15 = $150.00
# Available = #
# Taken = *

#seats = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4']
#rows = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']

def display(aA, bB, cC, dD, eE, fF, gG, hH, iI, jJ, kK, lL, mM, nN, oO, pP, qQ, rR, sS, tT, uU, vV, wW, xX, yY, zZ, row1, row2, row3, row4):
    '''Displays the seat pattern to the user'''
    print("Row                                  Seats                  ")
    print("\tA B C D E F G H I J K L M N O P Q R S T U V W X Y Z 1 2 3 4\n")
    for x in range(1, 16):
        print(" {:2}\t{} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {}".format(x, aA[x], bB[x], cC[x], dD[x], eE[x], fF[x], gG[x], hH[x], iI[x], jJ[x], kK[x], lL[x], mM[x], nN[x], oO[x], pP[x], qQ[x], rR[x], sS[x], tT[x], uU[x], vV[x], wW[x], xX[x], yY[x], zZ[x], row1[x], row2[x], row3[x], row4[x]))

def selectRow():
    '''Asks the user for what row they want to choose and returns that to the main program'''
    r = int(input("\nWhat row would you like to sit in: "))
    if (r >= 1 and r <= 5):
        cost = 200.00
    elif (r >= 6 and r <= 10):
        cost = 175.00
    elif (r >= 11 and r <= 15):
        cost = 150.00
    else:
        print("NOT A VALID ROW")
        selectRow()
    return r, cost

def selectSeat():
    '''Asks the user what seat they want to choose and returns it to the main program'''
    s = input("What seat would you like (Case-Sensitive): ")

    while (s != "A" and s != "B" and s != "C" and s != "D" and s != "E" and s != "F" and s != "G" and s != "H" and s != "I" and s != "J" and s != "K" and s != "L" and s != "M" and s != "N" and s != "O" and s != "P" and s != "Q" and s != "R" and s != "S" and s != "T" and s != "U" and s != "V" and s != "W" and s != "X" and s != "Y" and s != "Z"and s != "1" and s != "2" and s != "3" and s != "4"):
        print("INVALID RESPONSE. PLEASE CHOOSE ONE OF THE VALID SEAT CHOICES")
        s = input("What seat would you like: ")
        

    return s

def checkSeat(r, s, aA, bB, cC, dD, eE, fF, gG, hH, iI, jJ, kK, lL, mM, nN, oO, pP, qQ, rR, sS, tT, uU, vV, wW, xX, yY, zZ, row1, row2, row3, row4):
    '''Checks to make sure the seat chosen is available'''
    if (s == "A") and (aA[r] != "*"):
        print("Your seat has been chosen.")
        aA[r] = "*"
    elif (s == "B") and (bB[r] != "*"):
        print("Your seat has been chosen.")
        bB[r] = "*"
    elif (s == "C") and (cC[r] != "*"):
        print("Your seat has been chosen.")
        cC[r] = "*"
    elif (s == "D") and (dD[r] != "*"):
        print("Your seat has been chosen.")
        dD[r] = "*"
    elif (s == "E") and (eE[r] != "*"):
        print("Your seat has been chosen.")
        eE[r] = "*"
    elif (s == "F") and (fF[r] != "*"):
        print("Your seat has been chosen.")
        fF[r] = "*"
    elif (s == "G") and (gG[r] != "*"):
        print("Your seat has been chosen.")
        gG[r] = "*"
    elif (s == "H") and (hH[r] != "*"):
        print("Your seat has been chosen.")
        hH[r] = "*"
    elif (s == "I") and (iI[r] != "*"):
        print("Your seat has been chosen.")
        iI[r] = "*"
    elif (s == "J") and (jJ[r] != "*"):
        print("Your seat has been chosen.")
        jJ[r] = "*"
    elif (s == "K") and (kK[r] != "*"):
        print("Your seat has been chosen.")
        kK[r] = "*"
    elif (s == "L") and (lL[r] != "*"):
        print("Your seat has been chosen.")
        lL[r] = "*"
    elif (s == "M") and (mM[r] != "*"):
        print("Your seat has been chosen.")
        mM[r] = "*"
    elif (s == "N") and (nN[r] != "*"):
        print("Your seat has been chosen.")
        nN[r] = "*"
    elif (s == "O") and (oO[r] != "*"):
        print("Your seat has been chosen.")
        oO[r] = "*"
    elif (s == "P") and (pP[r] != "*"):
        print("Your seat has been chosen.")
        pP[r] = "*"
    elif (s == "Q") and (qQ[r] != "*"):
        print("Your seat has been chosen.")
        qQ[r] = "*"
    elif (s == "R") and (rR[r] != "*"):
        print("Your seat has been chosen.")
        rR[r] = "*"
    elif (s == "S") and (sS[r] != "*"):
        print("Your seat has been chosen.")
        sS[r] = "*"
    elif (s == "T") and (tT[r] != "*"):
        print("Your seat has been chosen.")
        tT[r] = "*"
    elif (s == "U") and (uU[r] != "*"):
        print("Your seat has been chosen.")
        uU[r] = "*"
    elif (s == "V") and (vV[r] != "*"):
        print("Your seat has been chosen.")
        vV[r] = "*"
    elif (s == "W") and (wW[r] != "*"):
        print("Your seat has been chosen.")
        wW[r] = "*"
    elif (s == "X") and (xX[r] != "*"):
        print("Your seat has been chosen.")
        xX[r] = "*"
    elif (s == "Y") and (yY[r] != "*"):
        print("Your seat has been chosen.")
        yY[r] = "*"
    elif (s == "Z") and (zZ[r] != "*"):
        print("Your seat has been chosen.")
        zZ[r] = "*"
    elif (s == "1") and (row1[r] != "*"):
        print("Your seat has been chosen.")
        row1[r] = "*"
    elif (s == "2") and (row2[r] != "*"):
        print("Your seat has been chosen.")
        row2[r] = "*"
    elif (s == "3") and (row3[r] != "*"):
        print("Your seat has been chosen.")
        row3[r] = "*"
    elif (s == "4") and (row4[r] != "*"):
        print("Your seat has been chosen.")
        row4[r] = "*"
    else:
        print("That seat is already taken.")

def seatInfo(totalSeats, seatsSold):

    print("Seats Sold: {}".format(seatsSold))
    print("Seats Available In Theater: {}".format(totalSeats - seatsSold))

def ticketInfo(total, ticketSold):

    print("Tickets Sold: {}".format(ticketSold))
    print("Total Cost: {:.2f}".format(total))

def choice(totalSeats, totalCost, seatsSold):
    '''Asks the user if they want to pick another seat'''
    view = input("Would you like to see the seat information (Y/N): ").upper()
    if (view == "Y"):
        seatInfo(totalSeats, seatsSold)

    view = input("Would you like to see the price of the tickets (Y/N): ").upper()
    if (view == "Y"):
        ticketInfo(totalCost, seatsSold)

    answer = input("Would you like to choose another seat (Y/N): ").upper()

    while (answer != "Y" and answer != "N"):
        print("INVALID ANSWER")
        answer = input("Would you like to choose another seat (Y/N): ")

    return answer

a = ['', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
b = ['', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
c = ['', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
d = ['', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
e = ['', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
f = ['', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
g = ['', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
h = ['', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
i = ['', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
j = ['', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
k = ['', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
l = ['', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
m = ['', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
n = ['', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
o = ['', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
p = ['', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
q = ['', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
r = ['', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
s = ['', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
t = ['', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
u = ['', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
v = ['', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
w = ['', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
x = ['', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
y = ['', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
z = ['', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
one = ['', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
two = ['', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
three = ['', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
four = ['', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']


answer = "Y"
sold = 0
total = 0
seatTotal = 450
while (answer == "Y"):
    sold += 1
    display(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,one,two,three,four)
    row, cost = selectRow()
    total += cost
    seat = selectSeat()
    checkSeat(row,seat,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,one,two,three,four)
    display(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,one,two,three,four)
    answer = choice(seatTotal, total, sold)
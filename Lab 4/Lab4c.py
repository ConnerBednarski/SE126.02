# Conner Bednarski
# Lab 4C
# SE 126.02
#
#
# Variables
#
# employeeFirstName     Holds the first name of all employees
# employeeLastName      Holds the last name of all employees
# employeePhoneNumber   Holds the phone number of all employees
# employeeEmailAddress  Holds the email address of all employees
# employeeDepartment    Holds the department of all employees
# employeePosition      Holds the position in the department of each employee
# numEmployees          Number of employees at the company
# file                  Holds the csvfile
# length                Holds the length of the last name list
# searchLastName        Holds the name entered by the user to search the list

#======Main=============================================================================


import csv

employeeFirstName = []
employeeLastName = []
employeePhoneNumber = []
employeeEmailAddress = []
employeeDepartment = []
employeePosition = []
numEmployees = 0



with open("C:\\Users\\cbedn\\Downloads\\Lab4c.txt") as csvfile:
    file = csv.reader(csvfile)
    for row in file:
        numEmployees += 1
        employeeFirstName.append(row[0])
        employeeLastName.append(row[1])
        employeePhoneNumber.append(row[2])
        employeeEmailAddress.append(row[3])
        employeeDepartment.append(row[4])
        employeePosition.append(row[5])
        

length = len(employeeLastName)
searchLastName = input("Enter the last name of the employee: ")

for pos in range(0, length):
    if (searchLastName == employeeLastName[pos]):
        found = "True"
        position = pos

        if found == "True":
            print()
            print("First Name: {}".format(employeeFirstName[position]))
            print("Last Name: {}".format(employeeLastName[position]))
            print("Phone Number: {}".format(employeePhoneNumber[position]))
            print("Email Address: {}".format(employeeEmailAddress[position]))
            print("Employee Department: {}".format(employeeDepartment[position]))
            print("Employee Position In The Department: {}".format(employeePosition[position]))

        else:
            print("Name not on list")

print("\nNumber of Employees: {}".format(numEmployees))



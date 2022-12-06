# Nikolas S Fisher
# date: 11/29/2022
#
# Description: This program contains all the functions for Module 8. I decided to do it this way since we are working
# with functions. This gives the user the ability to test out different functions depending on their first choice.
#          1. Checks whether two inputs equal one another.
#          2. Compares sum of two inputs two see if it greater than, less than or equal to 10.
#          3. Takes 5 inputs and appends them to a list, and checks whether 5 is in that list.
#          4. Takes a year as an input and checks if it is a leap year
#
#
#


# This function has two variables input1 and input2. It uses an If statement to check if the two inputs are equal to
# one another.


def inputs():
    input1 = int(input("Please enter a number:\n"))
    input2 = int(input("Please enter a number:\n"))

    if input1 == input2:
        return True

    else:
        return False

# This function has three variables inputa, inputb, and output1. The inputs are given by the user while the output1 is
# the sum of the two given inputs. Using an If-Else statement it checks whether output is the greater, less than or,
# equal to 10. Returning a statement on the outcome.


def greaterorless():
    inputa = int(input("Please enter a number:\n"))
    inputb = int(input("Please enter a number:\n"))

    output1 = inputa + inputb

    if output1 > 10:
        return print("The sum of you", inputa, "and", inputb, "is greater than 10")

    elif output1 < 10:
        return print("The sum of you", inputa, "and", inputb, "is less than 10")

    elif output1 == 10:
        return print("The sum of you", inputa, "and", inputb, "is equal to 10")


# This function was designed with one variable, year. This variable is given by the user and is than used in nested
# If-Else statement to check all the parameter on whether the year is a leap year.


def leaps():
    year = int(input("please input a year:\n"))
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return False

    else:
        return False

# This function takes a list of inputs and appends them to list. After taking 5 inputs, the function checks the list for
# the integer 5. If 5 is in the list it will return True and False if it is not.


def listcheck():

    list = []

    for i in range(5):
        num = int(input("Please insert a number:\n"))
        list.append(num)

    print(list)

    if 5 in list:
        return True
    else:
        return False

# This is the start of the main code, and this variable will be used to check which function will be used. Also has the
# option to use all the functions in order in one run of the program.


choice1 = int(input("What Function would you like to use?\n"
                    "1. Check whether two numbers equal each other.\n"
                    "2. Check whether input of two numbers are equal to,\n"
                    "   greater than or less than 10.\n"
                    "3. Take a list of values and checks whether there is a 5\n"
                    "   or not in the list\n"
                    "4. Take year as an input and check if it is a leap year or not.\n"
                    "5. Go through all of them in order\n\n"
                    "Pleaser enter your choice:\n"))

# If-Else Statement that checks choice1 against integers corresponding with their given options. Depending on the choice
# a different or all of the functions will be called.
if choice1 == 1:
    print(inputs())

elif choice1 == 2:
    print(greaterorless())

elif choice1 == 3:
    print(listcheck())

elif choice1 == 4:
    print(leaps)

elif choice1 == 5:
    print("Choice 1:")
    print(inputs())
    print()
    print()
    print("Choice 2:")
    print(greaterorless())
    print()
    print()
    print("Choice 3:")
    print(listcheck())
    print()
    print()
    print("Choice 4:")
    print(leaps())






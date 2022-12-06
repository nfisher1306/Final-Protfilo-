# Nikolas S Fisher
#
# Date: 11/15/2022
#
#
# Description:This program will take list of numbers and multiply them all together.
# returning the result to the user.
#
#


def resultlist(ulist):
    result = 1
    for x in ulist:
        result = result * x
    print("The product of the given list is:", result)


user_list = list(map(int, input("Please enter a list of numbers:").split()))
print(user_list)
resultlist(user_list)






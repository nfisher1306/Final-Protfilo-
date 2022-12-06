# Nikolas S Fisher
# 11/1/2022
#
# This program will display the numbers 1-50.
#   For numbers evenly divisible by 3, print “Divisible by 3” instead of the number
#   For numbers evenly divisible by 5, print “Divisible by 5” instead of the number
#   For numbers evenly divisible by both 3 and 5, print “Divisible by both"
#
#
#

for i in range(1,51):

    if i % 3 == 0 and i % 5 ==0:
        print("Divisble by both 3 and 5")

    elif i % 5 == 0:
        print("Divisble by 5")

    elif i % 3 == 0:
        print("Divisible by 3")
    else:
        print(i)


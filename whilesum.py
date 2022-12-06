# Nikolas S Fisher
#
# Date: 12/6/2022
#
# Description: : Using a while loop, ask the user to enter a number. Append each entered number to a list and add them
# together. Continue asking for a number until the sum of the list of numbers is greater than 100.
#
#
#
import time
sum = 0
listsum = []
while sum < 100:
    num = int(input("\nPlease enter a number:"))
    listsum.append(num)
    #if len(listsum) != 1:

    sum = num +sum


    print(listsum)
    print("The sum of the list is:", sum)

print("The sum of the list is greater than 100....\n\n"
      "END OF CODE")
time.sleep(2)


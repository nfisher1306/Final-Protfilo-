# Nikolas S Fisher
#
# 11/08/2022
#
# Description: Takes user input and returns two values. The two values from the calculated factorial
#
#
import math

factinput = int(input("Please insert a value:"))

result = 1
for x in range(1, factinput+1):
    result = x * result
    print(result)



print(math.factorial(factinput))


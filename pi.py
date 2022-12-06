# Nikolas S Fisher
#
# 11/08/2022
#
#
# Checks the area of a circle in the radius value inputted using the math function.
#
#
#

import math

radius = int(input("Enter a radius in cm: "))

#pi = 3.1415926535

area = radius**2 * math.pi

print("The area of the circle is",float(area) ,"cm squared.")
# Nikolas S Fisher
#
# 11/08/2022
#
# Description: To print an odd integer between 0 and 100
#
#
#
#

import random

test = random.randrange(0, 100)

if test % 2 == 0:
    print("This number is even")
else:
    print(test)

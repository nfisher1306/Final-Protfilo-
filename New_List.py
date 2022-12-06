# Nikolas S Fisher
#
# Date: 11/15/2022
#
#
#
#
#
import random


def newlist(flist):
    # print(random.sample(ulist, k=5))
    uqlist = []
    for x in flist:
        if x not in uqlist:
            uqlist.append(x)

    print(uqlist)


user_list = list(map(int, input("Please enter at list of numbers:\n"
                                "(Separate numbers with space)").split()))

newlist(user_list)

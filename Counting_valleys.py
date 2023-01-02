#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    count = 0


    summation = 0 

    for i in path:
        if i == "D":
            summation -=1
        elif i == "U":
            summation +=1
        if summation > 0:
            Down = False
        elif summation < 0:
            Down = True

        if summation == 0 and Down == True:
            count +=1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()

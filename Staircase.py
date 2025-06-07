import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    for i in range(1, n+1):
        spaces = n - i
        print(' '* spaces + '#' * i)
        
if __name__ == '__main__':
    n = int(input("Enter the number of stairs you want: "))


    staircase(n)

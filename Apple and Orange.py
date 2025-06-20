import math
import os
import random
import re
import sys


#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):

    pos_of_apple = [x + a for x in apples]
    print(pos_of_apple)
    
    pos_of_orange = [x + b for x in oranges]
    print(pos_of_orange)

    # in_range = [x for x in pos_of_apple + pos_of_orange if s <= x <= t]
    # print(in_range)

    counts_apples = sum(1 for x in pos_of_apple if s <= x <= t )
    print(counts_apples)
    counts_oranges = sum(1 for x in pos_of_orange if s <= x <= t )
    print(counts_oranges)
    
    

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))
    
    countApplesAndOranges(s, t, a, b, apples, oranges)
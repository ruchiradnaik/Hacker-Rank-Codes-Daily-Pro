import math
import os
import random
import re
import sys
from functools import reduce

def getTotalX(a, b):
    # Write your code here
    # print(f"This is the first array: {a}")
    # print(f"This is the second array: {b}")
    
    # l = reduce(math.lcm, a)
    # g = reduce(math.gcd, b)
    # print(f"This is the lcm of first array: {l}")
    # print(f"This is the gcd of second array: {g}")

    # multiples = [x for x in range(l, g+1, l)]
    # print(f"these are the multiples: {multiples}")

    # valid = [x for x in multiples if g % x == 0]

    # print(f"Valid numbers: {valid} ")

    # print(len(valid))

    l = reduce(math.lcm, a)
    g = reduce(math.gcd, b)
    
    multiples = [x for x in range(l, g+1, l)]
   
    valid = [x for x in multiples if g % x == 0]

    print(len(valid))
    

if __name__ == '__main__':
    
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0]) # 2

    m = int(first_multiple_input[1]) # 3

    arr = list(map(int, input().rstrip().split())) # 2 4

    brr = list(map(int, input().rstrip().split())) # 16 32 96

    total = getTotalX(arr, brr)

    # print(total)

    
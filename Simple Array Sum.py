import math
import os
import random
import re
import sys


def simpleArraySum(ar):
    
    return sum(ar)
    # Write your code here

if __name__ == '__main__':
    

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    print(result)

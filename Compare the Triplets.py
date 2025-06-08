import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    alice_score = 0
    bob_score = 0
    for i in range(3):
        if a[i] > b[i]:
            alice_score += 1
        elif a[i] < b[i]:
            bob_score += 1
        else:
            a[i] == b[i]
            pass
    return [alice_score, bob_score]

if __name__ == '__main__':
    
    print("Enter Alice's ratings (3 integers):")
    a = list(map(int, input().strip().split()))
    
    print("Enter Bob's ratings (3 integers):")
    b = list(map(int, input().strip().split()))

    result = compareTriplets(a, b)
    print("Result:", result)

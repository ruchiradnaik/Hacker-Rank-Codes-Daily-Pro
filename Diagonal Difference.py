import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    n = len(arr)
    primary_diagnol = 0
    secondary_diagnol = 0
    
    for i in range(n):
        primary_diagnol+=arr[i][i]
        secondary_diagnol+=arr[i][n-1-i]
        
    return abs(primary_diagnol - secondary_diagnol)
    # Write your code here

if __name__ == '__main__':
    
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    print(result)
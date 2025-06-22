import math
import os
import random
import re
import sys

#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

def divisibleSumPairs(n, k, ar):
    count = 0
    print(n)
    print(k)
    print(ar)
    # Write your code here

    for i in range(n):
        for j in range(n):
            if (i < j) and (ar[i] + ar[j]) % k == 0:
                count += 1
    return count


if __name__ == '__main__':
    
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    print(result)
    
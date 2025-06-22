import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    highest = lowest = scores[0]
    high_breaks = lowest_breaks = 0
    # print(f"These are the scores: {scores}")
    # start la jo score asel tr toch highest and lowest la set karaycha

    for score in scores[1:]:
        if score > highest:
            highest = score
            high_breaks+=1
        elif score < lowest:
            lowest = score
            lowest_breaks+=1

    return [high_breaks, lowest_breaks]
    



if __name__ == '__main__':

    n = int(input().strip())    #10

    scores = list(map(int, input().rstrip().split()))   #3 4 21 36 10 28 35 5 24 42

    result = breakingRecords(scores)

    print(result)
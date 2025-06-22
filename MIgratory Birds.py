import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
   
    counts = Counter(arr)

    

    max_count = max(counts.values())
    most_frequent = [bird_id for bird_id, count in counts.items() if count == max_count]
    result = min(most_frequent)
    return result
    
    



if __name__ == '__main__':
    
    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)
    print(result)

 

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    candles.sort()

    count_of_tall_candles = candles.count(max(candles))

    return count_of_tall_candles

if __name__ == '__main__':
   

    candles_count = int(input("Enter the total number of candles: "))

    candles = list(map(int, input("Enter candle heights: ").split()))

    result = birthdayCakeCandles(candles)

    print(result)

    

import math
import os
import random
import re
import sys

min_list = []
max_list = []

def miniMaxSum(arr):
    arr.sort()
    min_sum = sum(arr[:4])
    max_sum = sum(arr[1:])
    print(f"Min sum: {min_sum}")
    print(f"Max sum: {max_sum}")


if __name__ == '__main__':

    arr = [1, 3, 5, 7, 9]
    miniMaxSum(arr)
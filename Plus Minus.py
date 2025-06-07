from collections import Counter

# arr = [1,1,0,-1,-1]
# n = 5
# counts = Counter(arr)

# print(counts)

# array contains 2 positives, 2 negatives, 1 zero so their ratios are
# 2/5 = 0.400000, 2/5 = 0.400000, 1/5 = 0.200000




def plus_minus(arr):
  n = len(arr)
  counts = Counter(arr)
  print(counts)
  print(type(counts))

  pos_count = len([x for x in arr if x>0])
  neg_count = len([x for x in arr if x<0])
  zero_count = len([x for x in arr if x == 0])

  pos_ratio = pos_count/n
  neg_ratio = neg_count/n
  zero_ratio = zero_count/n

  print(f"{pos_ratio:.6f}")
  print(f"{neg_ratio:.6f}")
  print(f"{zero_ratio:.6f}")




#   ratio = n / counts

#   print(ratio)

if __name__ == '__main__':

    n = int(input("Enter total no. in array: "))
    arr = []
    for i in range(n):
        arr_ele = int(input("Enter element: "))
        arr.append(arr_ele)
    # n = int(input().strip())

    # arr = list(map(int, input().rstrip().split()))

    plus_minus(arr)
    
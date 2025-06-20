import os

def kangaroo(x1, v1, x2, v2):
    if v1 != v2:
        t = (x2 - x1) / (v1 - v2)
        if t.is_integer() and t >= 0:
            return "YES"
    if x1 == x2:
        return "YES"
    return "NO"

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # first_multiple_input = input().rstrip().split()

    x1 = 0
    v1 = 3
    x2 = 4
    v2 = 2

    result = kangaroo(x1, v1, x2, v2)
    print(result)

    # fptr.write(result + '\n')
    # fptr.close()

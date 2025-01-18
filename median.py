import math
import os
import random
import re
import sys
#
# Complete the 'findMedian' function below.

print(7 // 2-1)


# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def findMedian(arr):
    
    arr.sort()
    if n % 2 == 1:
        median = arr[n // 2]
    else:
        median = (arr[n // 2 - 1] + arr[n // 2]) / 2
    return median

if __name__ == '__main__':
    n = int(input().strip())
arr = list(map(int, input().rstrip().split()))
result = findMedian(arr)
print(result)
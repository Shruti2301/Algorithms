import math
import os
import random
import re
import sys

# Complete the aVeryBigSum function below.
def aVeryBigSum(ar):
    sum = 0
    for i in range(len(ar)):
        sum+=ar[i]
    return sum

ar = list()
num = input("Enter n:")
for i in range(int(num)):
    n = input('num:')
    ar.append(int(n))

print('ARRAY:',ar)
print('SUM :', aVeryBigSum(ar))

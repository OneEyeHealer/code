# input format: 
# 1st line: n-> number of days of transaction data, d-> number of trailing days' data
# 2nd line: expenditure[i]-> contains  space-separated non-negative integers

# output: alert count;


import math
import os
import random
import re
import sys
from bisect import bisect_left as bl, insort_right as ir

# Complete the activityNotifications function below.
def isEven(value):
    if value % 2 == 0:
        return True
    else:
        False
# meidan of arr_list: trailing_expenditure
def median(arr_list, mid, size):
    if isEven(size):
        return (sum(arr_list[mid-1: mid+1])/2)
    else:
        return arr_list[mid]

def activityNotifications(expenditure, d):
    notifyCount = 0
    trailing_expenditure = sorted(expenditure[0:d])
    mid_index = d//2

    for i in range(d, n):
        day_expenditure = expenditure[i]
        if (day_expenditure >= 2 * median(trailing_expenditure, mid_index, d)):
            notifyCount += 1
        
        del trailing_expenditure[bl(trailing_expenditure, expenditure[i-d])]
        ir(trailing_expenditure, day_expenditure)
    return notifyCount
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
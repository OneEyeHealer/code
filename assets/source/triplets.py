# input: 
# firs_line: n-> size of array, r-> comman ratio.
# secound_line: array-> elements of array.

left_c = 0 # left_count
right_c = 0  # right_count
total_c = 0 # total_count


def tripletsCount(arr, r):
    global left_c, right_c, total_c
    leftMap = {} # hashmap(Dictionary)
    rightMap = {} # hashmap(Dictionary)
    n = len(arr)

    for ele in arr:  # counting frequency of each element
        rightMap[ele] = rightMap.get(ele, 0) + 1

    for a in range(0, n - 1): # looping though each ele.
        mid = arr[a]

        # decrementing the freq by 1
        rightMap[mid] = rightMap.get(mid, 0) - 1
        rightMap.update(rightMap) # update Dictionary

        aMULr = mid * r
        aDIVr = mid // r
        if aDIVr in leftMap.keys() and mid % r == 0:
            # contain the (arr.index(a) - 1) or cont of 'a/r'
            left_c = int(leftMap.get(aDIVr, 0))
        else:
            left_c = 0

        if aMULr in rightMap.keys():
            # contain the (arr.index(a) + 1) or count of 'ar' in rightMap
            right_c = int(rightMap.get(aMULr, 0))
        else:
            right_c = 0

        total_c += left_c * right_c 
        # counting the leftMap and incrementing the feq by 1
        leftMap[mid] = leftMap.get(mid, 0) + 1
        leftMap.update(leftMap) # updating the leftmap
    return total_c

if __name__ == "__main__":
    nr = input().rstrip().split()
    n,r = list(map(int, nr))
    arr = list(map(int, input().rstrip().split()))
    result = tripletsCount(arr, r)
    print(result)



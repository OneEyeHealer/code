# Alternate Approach

 Geometic Progration
>$i = a,_\ j = ar,_\ k = ar^2$ 
>$where _\ (i<j<k)$

## Time complexity
> $ order(n^3)$

```python
# pseudo code approach
tripletsTotal = 0

def triplets(arr, r):
    global tripletsTotal

    n = len(arr)
    for j in range(1, n - 1):
        i = j - 1
        k = j + 1

        while i >= 0 and k < n and r > 0:

            while ( arr[j] % arr[i] == 0 and 
                    arr[k] % arr[j] == 0 and 
                    arr[j] // arr[i] == r and 
                    arr[k] // arr[j] == r):
                tripletsTotal += 1

                k += 1
                i -= 1

                if k == n:
                    k = j - 1
                if i < 0:
                    i = j - 1

            if (arr[j] % arr[i] == 0 and 
                arr[k] % arr[j] == 0):

                if (arr[j] // arr[i] < arr[k] // arr[j]):
                    i -= 1
                else:
                    k += 1
            elif arr[j] % arr[i] == 0:
                k += 1
            else:
                i -= 1
    return tripletsTotal
```

# Yet another approach with better time complexity
 Geometic Progration
>$i = a/r,_\ j = a,_\ k = ar$ 
>$where _\ (i<j<k)$

## Time complexity
>$ order(n)$
```python
# Hasmap and Dictionary Data structure is used.
left_c = 0
right_c = 0
total_c = 0

def tripletsCount(arr, r):
    global left_c, right_c, total_c
    leftMap = {}
    rightMap = {}
    n = len(arr)

    for ele in arr:  # counting frequency of each element
        rightMap[ele] = rightMap.get(ele, 0) + 1

    for a in range(0, n - 1):
        mid = arr[a]

        rightMap[mid] = rightMap.get(mid, 0) - 1     # decrementing the freq by 1
        rightMap.update(rightMap)

        aMULr = mid * r
        aDIVr = mid // r
        if aDIVr in leftMap.keys() and mid % r == 0:
            left_c = int(leftMap.get(aDIVr, 0))  # contain the (arr.index(a) - 1) or cont of 'a/r'
        else:
            left_c = 0

        if aMULr in rightMap.keys():
            right_c = int(rightMap.get(aMULr, 0))  # contain the (arr.index(a) + 1) or count of 'ar' in rightMap
        else:
            right_c = 0

        total_c += left_c * right_c
        leftMap[mid] = leftMap.get(mid, 0) + 1
        leftMap.update(leftMap)
    return total_c
```

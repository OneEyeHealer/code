## Pseudo Code Approach
> Time Complexity: O( n<sup>s</sup> ), 
>where s : no of time list sorted( ) i.e. expenditure.



```python
def even(value):
    if value % 2 == 0:
         return True 
    return False
    
transaction_data, trailing_day = 9, 5
notifyCount = 0
expenditure = list(map(int, input().rstrip().split()))

# at day trailingData + 1 (or d + 1)
for i in range(0, transaction_data - trailing_day, 1):
    # sub-list
    trailing_expenditure = sorted(list(expenditure[i : i + trailing_day]))
    day_expenditure = expenditure[i + trailing_day ]
    mid_index = (len(trailing_expenditure) // 2)
    if even(trailing_day):
        median = (trailing_expenditure[mid_index] + trailing_expenditure[mid_index + 1]) // 2
    else:
        median = trailing_expenditure[mid_index]
    if day_expenditure >= (2 * median):
        notifyCount += 1
    # print("traling: {}, day's: {}, median: {}".format(trailing_expenditure, day_expenditure, median))
    # print("Alert: {}".format(notifyCount))
```

# Yet another better Appoach using: `deque`
> <b>deque</b>: "Deque (Doubly Ended Queue) in Python is implemented using the module “collections“. Deque is preferred over list in the cases where we need quicker append and pop operations from both the ends of container, as deque provides an O(1) time complexity for append and pop operations as compared to list which provides O(n) time complexity."

## Apporach 
>1. I try to keep the sorting at one place and at the beginning program i.e.
`trailing_expenditure = sorted(expenditure[0:trailing_day])`.

>2. while maintaning the `sorted order` we add the day's expenditure i.e
`day_expenditure = expenditure[i]`
where `i` is `d -> d+1 -> d+2... upto n`.

>3. `if` twice of median` <= `expenditure
 then we notify the user, 
`else` 
we delete the elements one by one at each iteration of for loop i.e.
`del trailing_expenditure[bisect_left(trailing_expenditure, expenditure[i-trailing_day])]`.

>4. insert the day's_expenditure while maintaing the sorted order i.e. 
`insort(trailing_expenditure, day_expenditure)`.

# code
```python
# Note: bydefault insort is insort_right
from bisect import bisect_left, insort

# iseven
def isEven(value):
    if value % 2 == 0:
         return True 
    return False

# median in given arr_list
def median(arr_list, mid, size):
    #size: len(arr_list or trailing_expenditure)
    if isEven(size): # even
        return (sum(arr_list[mid-1:mid+1])/2)
    else: # odd
        return arr_list[mid]

transaction_data, trailing_day = n, d
notifyCount = 0
expenditure = list(map(int, input().rstrip().split()))
# temparory arr to for setting inital 'trailing_expenditure'
trailing_expenditure = sorted(expenditure[0:trailing_day])

mid_index = trailing_day//2

# check the each sub - trailing_expenditure
for i in range(trailing_day, transaction_data):
    day_expenditure = expenditure[i]
    if day_expenditure >= 2*median(trailing_expenditure, mid_index, trailing_day):
        notifyCount += 1
    # delet element in seq like expenditure while keeping the sorted array so we use bisect module.
    # i.e. 2-> 3-> 4-> 2-> 3-> 6-> 8-> 4-> 5 
    del trailing_expenditure[bisect_left(trailing_expenditure, expenditure[i-trailing_day])]
    insort(trailing_expenditure, day_expenditure)
print(notifyCount)
```
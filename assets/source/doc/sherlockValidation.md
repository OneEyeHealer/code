# Apporach

### Creating [ Key, value ] Pairs

```python
# using dict()
for ele in string:
    sherlockMap[ele] = sherlockMap.get(ele, 0) + 1
```

### Unique Frequency List
##### Frequency List of SherlockMap
```python
# gives value only from dict()
sherlockMap.values()
```

##### Unique value of Frequency
```python
# set():
# takes only distinct values form the given data.
set(sherlockMap.values())

# To make it easy to perform opeation,
# we convert it into List:
list(set(sherlockMap.values()))
```
##### Calculate [ minFreq, MaxFreq ]
```python
# For Seperate Calculation
minFreq = min(uniqueFreq)
maxfreq = max(uniqueFreq)
 
# or compress the calculation
minFreq, maxFreq = min(uniqueFreq), max(uniqueFreq)
```
### Sherlock Conditions
#### Case - 1
>When string has equal no of occurance ( frequency) 
``` if len(uniqueFreq) == 1```
>then `print 'YES'`

#### Case - 2
> When frequency does't matach
> We Calculate `minFreqCount` and `maxFreqCount`
```python
# calculte totalcount of minFreqCount and maxFreqCount
for value in sherlockMap.values():
    if value == minFreq:
        minFreqCount += 1
    elif value == maxFreq:
        maxFreqCount += 1
 ```
#### case - 2.a
> if `minFreqCount == maxFreqCount`
```python
# 2 or less char in uniqueFreq set().
if len(sherlockMap.keys()) <= 2:
    print('YES')
else: # more than 2 char in uniqueFreq set().
    print('NO')
```
> then check `if` count of key <= 2  `print 'YES'`
>i.e. `"aab"` -> `a` can be remove 
>`len(sherlockMap.keys()) <= 2`
>`else` `print 'NO'`
>i.e. `"abbac"` -> `c` can be remove here

#### case - 2.b
> if `maxFreqCount == 1` and `maxFreq - minFreq == 1`
then  `print 'YES'`
i.e. `"aabbcccdd"` -> `c` can be removed

#### case -2.c
> 
```python 
if minFreqCount == 1:
    if minFreq == 1: # for one removable item i.e aab
        print ('YES')
    else: # more than one removalbel item.
        print('NO')
```

## isValid()
```python
# string is valid if freq of charaters are equal or 
# remove 1 index 
# to make the freq equal 
# which make the stirng valid as well. 
# else not.

string = 'abbac' # pass your string.
sherlockMap = {}
minFreqCount = maxFreqCount = 0 # inital value.
# Calculating frequency - using dict()
for ele in string:
    sherlockMap[ele] = sherlockMap.get(ele, 0) + 1

# unique list of freq - (no repeation)
uniqueFreq = list(set(sherlockMap.values()))
# calculte max, min totalCount of maxFreq and minFreq char.
minFreq, maxFreq = min(uniqueFreq), max(uniqueFreq)

if len(uniqueFreq) == 1: # at single type of char in list.
    print('valid-1')
else:
    # calculte totalcount of minFreqCount and maxFreqCount
    for value in sherlockMap.values():
        if value == minFreq:
            minFreqCount += 1
        elif value == maxFreq:
            maxFreqCount += 1
    diff = maxFreq - minFreq  
    if minFreqCount == maxFreqCount:
        # 2 or less char in uniqueFreq set().
        if len(sherlockMap.keys()) <= 2: 
            print('valid-2')
        else: # more than 2 char in uniqueFreq set().
            print('invalid-1')
    elif maxFreqCount == 1 and diff == 1:
        print('valid-3')        
    elif minFreqCount == 1:
        if minFreq == 1: # for one removable item.
            print('valid-4')
        else: # more than one removalbel item.
            print('invalid-2')
    else:
        print('invalid-3')

```
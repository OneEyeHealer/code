# string is valid if freq of charaters are equal or 
# remove 1 index to make the freq equal which make the stirng valid as well 
# else not.

def isValid(string):
    sherlockMap = {}
    minFreqCount = maxFreqCount = 0 # inital value.
    for ele in string:
        sherlockMap[ele] = sherlockMap.get(ele, 0) + 1

    uniqueFreq = list(set(sherlockMap.values()))
    minFreq, maxFreq = min(uniqueFreq), max(uniqueFreq)

    if len(uniqueFreq) == 1: # at single type of char in list.
        return('YES')
    else:
        # calculte totalcount of minFreqCount and maxFreqCount
        for value in sherlockMap.values():
            if value == minFreq:
                minFreqCount += 1
            elif value == maxFreq:
                maxFreqCount += 1
        diff = maxFreq - minFreq  
        if minFreqCount == maxFreqCount:
            if len(sherlockMap.keys()) <= 2:
                return('YES')
            else:
                return('NO')
        elif maxFreqCount == 1 and diff == 1:
            return('YES')        
        elif minFreqCount == 1:
            if minFreq == 1:
                return ('YES')
            else:
                return('NO')
        else:
            return('NO')

if __name__ == "__main__":
    string = input()
    result = isValid(string)
    print(result)   
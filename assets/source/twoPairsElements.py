# N: no of elements in array
# A: array of elements
# (Ai = Aj + 1) -> (Aj = Ai + 1) === (Ai = Aj)
# (Ai - 1= Aj) -> (Aj - 1 = Ai) === (Ai = Aj)

# my approach-> start the loop form 1 to N
    # so Ai = array[i] where i = 1 to N
    # therefore: Ai == A(i-1) then count++
    # else Ai == (A(i-1) + 1) or say Aj then count++ as well as distintCount++
    # else count and distintCount >= 2 (so. find nC2 = n!/((n-2)!*2!)) 
# then find the nC2 agin for the totalPairs because above nC2 give you only half of the total pair and its revers is also true i.e (1,2) , (2, 3) but also count (3, 2) (2,1)
def hasPairAnotherApproach(array_list):
    countCommanPairs, countPairsDistinct = 1, 1
    totalPairs = 0
    for i in range(1, N):
        if array_list[i] == array_list[i - 1]:  # for Ai == Aj i.e. (Aj == Ai - 1) where Ai = array[i] and Aj = array[i-1] (or array[i] - 1 in sorted array)
            countCommanPairs += 1 
        elif array_list[i] == array_list[i - 1] + 1:    # for Ai == Aj + 1
            countCommanPairs += 1 
            countPairsDistinct += 1
        else:
            if countCommanPairs >= 2 and countPairsDistinct >= 2: # condition for nC2
                totalPairs += ((countCommanPairs * (countCommanPairs - 1)) // 2) # nC2
            countCommanPairs = countPairsDistinct = 1

    if countCommanPairs >= 2 and countPairsDistinct >= 2:
        totalPairs += ((countCommanPairs * (countCommanPairs - 1)) // 2)
    return totalPairs


if __name__ == "__main__":
    N = int(input())
    array = list(map(int, input().rstrip().split()))[:N]
    # result = hasPair(array)
    result = hasPairAnotherApproach(sorted(array))
    print(result)

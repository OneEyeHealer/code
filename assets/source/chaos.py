def swap(queue, num1, num2):
    queue[num1], queue[num2] = queue[num2], queue[num1]
    return queue

def minimumBribes(queue):
    bribeCount = 0
    for index in range(len(queue)-1, -1, -1):  # going backward like orginal queue
        sticker, person_pos = queue[index], index + 1
        # case 1: when we don't bribe
        if(sticker != person_pos):
            # case 2: when you bribe
            onePos, twoPos = index - 1, index - 2
            # case 2.1: bribe by one person
            if ((onePos >= 0) and queue[onePos] == person_pos):
                bribeCount += 1
                swap(queue, index, onePos)
            # case 2.2: bribe by two person
            elif ((twoPos >= 0) and queue[twoPos] == person_pos):
                bribeCount += 2
                swap(queue, twoPos, onePos)  # for first swap
                swap(queue, onePos, index)  # for second swap
            else:  # case 2.3: bribe more than 2 person
                print("Too chaotic")    # i.e (queue[onePos] != twoPos and queue[twoPos] != onePos)
                return   # no need to count all cases 
    print(bribeCount)
        
        
if __name__ == "__main__":
    test_case = int(input())
    
    for t in range(test_case):
        n = int(input())
        queue = list(map(int, input().rstrip().split()))
        minimumBribes(queue)
            
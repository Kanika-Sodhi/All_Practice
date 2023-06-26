def containsNearbyDuplicate(nums):
    dictt = {}
    for n in nums:
        dictt[n] = dictt.get(n, 0) + 1
    print(dictt)
    for idx, value in dictt.items():
        if value > 1:
            return True
    return False


print(containsNearbyDuplicate([1, 2, 3, 1]))


def maxsubarray(num):
    curSum = 0
    maxSub = num[0]
    for i in num:
        if curSum < 0:
            curSum = 0
        print(curSum)
        curSum += i
        maxSub = max(maxSub, curSum)
    return maxSub

# print(maxsubarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

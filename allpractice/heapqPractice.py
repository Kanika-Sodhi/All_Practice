# importing "heapq" to implement heap queue
import heapq
from collections import defaultdict

nums = [2, 2, 3, 1, 1, 1]
k = 2


def topKFrequent(nums, k):
    dict1 = {}
    for item in nums:
        if item not in dict1:
            dict1[item] = 1
        else:
            dict1[item] += 1

    hq = [(value, key) for key, value in dict1.items()]
    print(type(hq))
    print(type(dict1))

    largest = heapq.nlargest(k, hq)

    res = []

    for i in range(k):
        res.append(largest[i][1])

    return res


print(topKFrequent(nums, k))

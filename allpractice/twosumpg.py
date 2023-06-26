def twoSum(list1, target):
    left = 0
    right = len(list1) - 1

    tempSum = 0
    res = []

    while left < right:
        tempSum = list1[left] + list1[right]
        if tempSum == target:
            return res.append([left, right])  # list((left, right))
        elif tempSum > target:
            right -= 1
        elif tempSum < target:
            left += 1

    return (-1, -1)


#print(twoSum([1, 4, 3, 5, 0, 1], 6))
print(twoSum([1, 4, 5, 8, 0, 8], 9))

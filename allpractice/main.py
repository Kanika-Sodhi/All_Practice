def twoSum(nums, target):
    '''for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return i, j'''
    val = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in val:
            return [i, val[diff]]

        val[num] = i


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(twoSum([5, 9, 1, 2, 3], 10))

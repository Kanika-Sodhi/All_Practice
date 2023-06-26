nums = [5, 7, 7, 8, 0, 10]
target = 8


def searchRange(nums, target):
    res = []
    if target not in nums or len(nums) == 0:
        return [-1, -1]
    for i in range(len(nums)):
        if nums[i] == target:
            res.append(i)
    if len(res) == 1:
        res.append(0)
    return res


print(searchRange(nums, target))

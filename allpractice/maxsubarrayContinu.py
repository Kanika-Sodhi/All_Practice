nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
maxnum = nums[0]
total_sum = nums[0]

for i in nums[1:]:
    total_sum = max(i, total_sum + i)
    maxnum = max(total_sum, maxnum)
print(maxnum)

nums = [1, 2, 3, 4, 5]
target = 5
start = 3
a = []
for i in range(len(nums)):
    if nums[i] == target:
        value = i-start
        print(abs(value))
        #a.append(abs(start - i))

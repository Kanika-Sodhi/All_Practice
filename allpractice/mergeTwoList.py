nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

num1 = nums1[0:m]
num2 = nums2[0:n]
mergelist = num1 + num2
print(mergelist)
sortedmergelist = sorted(mergelist)
print(sortedmergelist)

nums = [-4, -1, 0, 3, 10]
res = []
for i in nums:
    res.append(i * i)
print(sorted(res))

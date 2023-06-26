'''nums = [-1, 0, 1, 2, -1, -4]
nums.sort()
ans = set()
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        for k in range(j + 1, len(nums)):
            if nums[i] + nums[j] + nums[k] == 0:
                ans.add((nums[i], nums[j], nums[k]))
print(ans)'''
###############################################################
# sum of 3

def find3Numbers(A, arr_size, sum):
    # Sort the elements
    A.sort()

    for i in range(0, arr_size - 2):
        l = i + 1
        # index of the last element
        r = arr_size - 1
        while (l < r):
            if (A[i] + A[l] + A[r] == sum):
                print("Triplet is", A[i], ', ', A[l], ', ', A[r])
                return True
            elif (A[i] + A[l] + A[r] < sum):
                l += 1
            else:  # A[i] + A[l] + A[r] > sum
                r -= 1

    return False
# Driver program to test above function
A = [1, 4, 45, 6, 10, 8]
sum = 22
arr_size = len(A)

find3Numbers(A, arr_size, sum)


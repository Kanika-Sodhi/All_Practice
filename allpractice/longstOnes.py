def longestOnes(nums, k):
    zeroes_in_window = 0
    max_len = 0
    slow = 0

    for fast, f in enumerate(nums):
        if f == 0:
            zeroes_in_window += 1

        # I.E If Number of zeroes has exceeded k shrink from left till zeroes_in_window<=k
        while zeroes_in_window > k:
            # Decrement count of zeroes in window
            if nums[slow] == 0:
                zeroes_in_window -= 1
            slow += 1

        # Update max window if current window is larger
        max_len = max(fast - slow + 1, max_len)
    return max_len


# print(longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))


def findMaxConsecutiveOnes(nums):
    maxConsOnes = 0
    length = len(nums)

    ones = 0
    for i in range(length):
        if nums[i] == 1:
            ones += 1
        else:
            maxConsOnes = max(maxConsOnes, ones)
            ones = 0
            print(ones)
    maxConsOnes = max(maxConsOnes, ones)
    return maxConsOnes


print(findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))

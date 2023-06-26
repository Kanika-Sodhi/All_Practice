def minsizeSubarray(nums, k):
    l = 0
    total = 0
    res = float("inf")
    for r in range(len(nums)):
        total += nums[r]
        # rint(nums[i])
        while total >= k:
            res = min(r - l + 1, res)  # 1
            total -= nums[l]
            l += 1

    return 0 if res == float("inf") else res


print(minsizeSubarray([2, 3, 1, 2, 4, 3], 8))

def maxCharcount(s, k):
    num = list(s)
    dictn = {}
    maxval = 0
    for i in range(len(num)):
        dictn[num[i]] = 1 + dictn.get(num[i], 0)

    for ind, value in dictn.items():
        if value >= k:
            maxval = max(value, maxval)

    return maxval


print(maxCharcount("aaabbbb", 3))

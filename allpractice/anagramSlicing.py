def findAnagrams(s, p):
    if len(p) > len(s):
        return []
    sCount = {}
    pCount = {}
    for i in range(len(p)):
        pCount[p[i]] = 1 + pCount.get(p[i], 0)
        sCount[s[i]] = 1 + sCount.get(s[i], 0)
    # print(pCount, sCount)
    res = [0] if pCount == sCount else []

    l = 0
    for r in range(len(p), len(s)):
        sCount[s[r]] = 1 + sCount.get(s[r], 0)
        sCount[s[l]] -= 1
        # print(sCount[s[r]] ,sCount[s[l]])
        # print(sCount[s[l]] - 1)
        if sCount[s[l]] == 0:
            del sCount[s[l]]
        l += 1
        if sCount == pCount:
            res.append(l)
    return res


print(findAnagrams('cbaebabacdbcabbca', 'abc'))

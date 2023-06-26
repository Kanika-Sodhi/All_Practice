def lengthOfLongestSubstring(s):
    # T/S: O(n)
    seen = set()
    l = res = 0
    for r in range(len(s)):
        while s[r] in seen:
            seen.remove(s[l])
            l += 1
            # print(l)
        seen.add(s[r])
        res = max(res, r - l + 1)
    return res


print(lengthOfLongestSubstring('abcabcccb'))
########################################################################################
def LongestSubstring(s):
    # T/S: O(n)
    seen = set()
    l = res = 0
    for r in range(len(s)):
        seen.add(s[r])
        l -= 1
        # print(res, r - l + 1)
        res = max(res, r - l + 1)
    return s[l],s[r]

#print(LongestSubstring('abcbdbdbbdcdabd'))

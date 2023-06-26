def groupAnagrams(strs):
    sorted_anagrams = {}
    for i in strs:
        if ''.join(sorted(i)) not in sorted_anagrams.keys():
            sorted_anagrams[''.join(sorted(i))] = [i]
            print(sorted_anagrams)
        else:
            sorted_anagrams[''.join(sorted(i))].append(i)
    return sorted_anagrams.values()


print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
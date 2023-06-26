from collections import Counter


def findAnagrams(s, p):
    result = []
    counterS = Counter(s[:len(p) - 1])
    #print(counterS)
    counterP = Counter(p)
    #print(counterP)
    for index in range(len(s) - len(p) + 1):
        #print(counterS[s[index + len(p) - 1]])
        counterS[s[index + len(p) - 1]] += 1
        if counterS == counterP:
            result.append(index)
        counterS[s[index]] -= 1
        if counterS[s[index]] == 0:
            counterS.pop(s[index])
    return result

print(findAnagrams('cbaebabacdbcabbca', 'abc'))

'''res = []
    for i in range(len(s) - len(p) + 1):
        if anagram(s[i:i + len(p)], p):
            res.append(i)
        else:
            continue
    return res'''


'''def anagram(a, b):
    lista = list(a)
    lista.sort()
    listb = list(b)
    listb.sort()
    return lista == listb'''




from collections import Counter


def areAlmostEqual(s1, s2):
    set1 = Counter(list(s1))
    set2 = Counter(list(s2))

    if set1 != set2:
        return False

    differences = 0

    for i, j in zip(s1, s2):
        if i != j:
            differences += 1
        print(differences)
    return differences <= 2


print(areAlmostEqual('kank', 'kakn'))

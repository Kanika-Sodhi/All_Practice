import itertools

nums = [5, 9, 1, 2, 3, 5]
simple_dict = {}
newlist = []

for i in nums:
    counter = simple_dict.get(i)
    if simple_dict.get(i) is None:
        simple_dict[i] = 1
    else:
        simple_dict[i] = simple_dict[i] + 1
print(simple_dict)

for key, value in simple_dict.items():
    if value >= 1:
       newlist.append(key)
print(newlist)
newlist.sort()
print(newlist)
print(newlist[3-1])

'''numbs = [5, 7, 0, 5, 6, 1, 9]
for n in range(len(numbs)):
    for p in itertools.combinations(numbs, 2):
        if sum(p) == 10:
            print(p)'''

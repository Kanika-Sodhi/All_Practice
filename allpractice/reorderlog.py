res1 = []
res2 = []
logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
for i in logs:
    if (i.split()[1]).isdigit():
        res2.append(i)
    else:
        res1.append(i.split())

res1.sort(key=lambda x: x[0])
res1.sort(key=lambda x: x[1:])

for i in range(len(res1)):
    res1[i] = (" ".join(res1[i]))
a = res1.extend(res2)
print(a)

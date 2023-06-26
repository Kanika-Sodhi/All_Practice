arr = [1, 1, 1, 2, 2, 2, 8, 8, 9]
dicarr = {}
for i in arr:
    counter = dicarr.get(i)
    if counter is None:
        dicarr[i] = 1
    else:
        dicarr[i] = dicarr[i] + 1

l = []
max_val = sorted(dicarr.values())[len(dicarr) - 3:]
#print(sorted(dicarr.values()))
#print(len(dicarr))
#print(max_val)
for i, j in dicarr.items():
    if j in max_val:
        l.append([i, j])
print(l)

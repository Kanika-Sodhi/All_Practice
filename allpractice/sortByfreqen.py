import heapq

s = 'tree'
dic = {}
for num in range(len(s)):
    if s[num] not in dic:
        dic[s[num]] = 1
    else:
        dic[s[num]] = dic[s[num]] + 1
# fin_max = max(dic, key=dic.get)
# print("Maximum value:", fin_max)

'''d = sorted(dic, key=lambda x: s.count(x), reverse=True)
print(d)
res = ''
for char in d:
    #print(char)
    #print(dic[char])
    res += char * dic[char]
print(res)'''
ans = []
heap = []
heapq.heapify(heap)
for i, j in dic.items():
    heapq.heappush(heap, (j, i))

while heap:
    val = heapq.heappop(heap)
    print(val)
    ans.append(val[0] * val[1])
    print(val[0] , val[1])
ans = ans[::-1]
print(ans)
print(''.join(ans))

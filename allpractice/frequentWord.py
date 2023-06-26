from collections import Counter

s = 'the day is sunny the the the sunny is is'
splline = s.split(' ')
print(splline)
count = Counter(splline)
print(count)

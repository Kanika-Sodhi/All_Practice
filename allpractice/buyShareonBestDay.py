prices = [7, 1, 5, 3, 6, 4]
# Output: 5
minp = prices[0]
profit = 0
for i in prices:
    if i < minp:
        minp = i
    elif i - minp > profit:
        profit = i - minp
print(profit)

'''prices2 = [3, 3, 5, 0, 0, 3, 1, 4]
# Output: 6
minpr = prices2[0]
for price in prices2:
    if price < minpr:
        minpr = price
    elif price > minpr:'''


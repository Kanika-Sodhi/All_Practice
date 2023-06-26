text1 = "abc"
text2 = "def"
count = 0
for i in range(len(text1)):
    for j in range(len(text2)):
        print(text1[i], text1[j])
        if text1[i] in text2[j]:
            count += 1


# print(count)

def getSum(n):
    sum = 0
    while n != 0:
        sum = sum + int(n % 10)
        n = int(n / 10)

    return sum


# Driver code
n = 8527087841
print(getSum(n))

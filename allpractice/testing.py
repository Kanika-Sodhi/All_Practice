def interchange(newList):
    n2 = len(newList)
    print(n2)
    tem = newList[0]
    newList[0] = newList[n2 - 1]
    newList[n2 - 1] = tem
    return newList


newList = [12, 35, 9, 56, 24]

print(interchange(newList))


def swapPositions(lis, pos1, pos2):
    temp = lis[pos1]
    lis[pos1] = lis[pos2]
    lis[pos2] = temp
    return lis


# Driver function
List = [23, 65, 19, 90]
pos1, pos2 = 1, 3

print(swapPositions(List, pos1 - 1, pos2 - 1))


def maxnum(lst):
    maxval = lst[0]
    for i in lst:
        if maxval < i:
            maxval = i
    return maxval


print(maxnum([3, 8, 0, 1, 9]))


def reversestring(nwlst):
    res = []
    for i in range(len(nwlst))[::-1]:
        res.append(nwlst[i])
    return res


print(reversestring("kanika"))


def calc_largest(arr):
    second_largest = arr[0]
    largest_val = arr[0]
    for i in range(len(arr)):
        if arr[i] > largest_val:
            largest_val = arr[i]

    for i in range(len(arr)):
        if arr[i] > second_largest and arr[i] != largest_val:
            second_largest = arr[i]

    return second_largest


def calc_2ndlargest(arr):
    lt = sorted(set(arr))
    return lt[-2]


print(calc_2ndlargest([20, 30, 40, 25, 10]))


def uniqueelement(lt):
    count = 0
    newlt = []
    count = 0
    for i in lt:
        if i not in newlt:
            count += 1
            newlt.append(i)
    return count


print(uniqueelement([20, 30, 40, 25, 10, 40, 30, 30, 40]))


def kth_frequency(lst, k):
    dct = {}
    ls = []
    for i in lst:
        if dct is None:
            dct[i] = 1
        else:
            dct[i] = dct.get(i, 0) + 1

    for key, value in dct.items():
        if value == k:
            ls.append([key, value])
    return ls


print(kth_frequency([20, 30, 40, 25, 10, 40, 30, 30, 40], 3))

arr = [1, 1, 1, 64, 23, 64, 22, 22, 22]

# size of the list
size = len(arr)

# looping till length - 2
for i in range(size - 2):
    if arr[i] == arr[i + 1] and arr[i + 1] == arr[i + 2]:
        print(arr[i])


def maxadjacent(arr1):
    ls = []
    for i in range(len(arr1) - 1):
        if arr1[i] < arr1[i + 1]:
            ls.append(arr1[i + 1])
    return ls


print(maxadjacent([1, 2, 2, 3, 4, 5]))

import re


def lengthOfLastWord(s):
    sname = re.sub(' +', " ", s)
    cleanname = sname.strip()
    splitword = cleanname.split(' ')
    print(splitword)
    lstlen = len(splitword) - 1
    return len(splitword[lstlen])


print(lengthOfLastWord(" kanika  sodhi "))


def divideString(s, k, fill):
    final_list = []
    for r in range(0, len(s), k):
        part = s[r:r + k]
        print(part)
        if len(part) == k:
            final_list.append(part)
        else:
            while len(part) != k:
                part += fill
            final_list.append(part)

    return final_list


print(divideString("KanikaSodhiivv", 3, '&'))


def removeelement(nums):
    idx = len(nums) - 1
    while idx > 0:
        if nums[idx] == nums[idx - 1]:
            nums.pop(idx)
        idx = idx - 1
    return nums


print(removeelement([1, 1, 2, 2, 2, 3]))


def moveZeroes(nums):
    for i in range(len(nums)):
        if nums[i] == 0:
            nums.append(0)
            nums.remove(0)
    return nums


print(moveZeroes([0, 1, 0, 3, 12]))


def tringle(nums):
    ls = []
    a = len(nums)-2
    for i in range(a):
        if nums[i] < nums[i + 1] <= nums[i + 2]:
            ls.append([nums[i], nums[i + 1], nums[i + 2]])
    return ls


print(tringle([1, 2, 4, 6, 4, 9, 1, 2, 3]))

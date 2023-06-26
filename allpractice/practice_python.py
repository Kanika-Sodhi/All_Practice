'''1. Write a Python Program to print Prime Numbers between 2 numbers
2. Write a Sort function to sort the elements in a list
3. Write a sorting function without using the list.sort function
4. Write a Python program to print Fibonacci Series
5. Write a Python program to print a list in reverse
6. Write a Python program to check whether a string is a Palindrome or not
7. Write a Python program to print set of duplicates in a list
8. Write a Python program to print number of words in a given sentence
9. Given an array arr[] of n elements, write a Python function to search a given element x in arr[].
10. Write a Python program to implement a Binary Search
11. Write a Python program to plot a simple bar chart
12. Write a Python program to join two strings (Hint: using join())
13. Write a Python program to extract digits from given string
14. Write a Python program to split strings using newline delimiter
15. Given a string as your input, delete any reoccurring character, and return the new string.'''


def primeORnot(start, end):
    for number in range(start, end + 1):
        if number > 0:
            for i in range(2, number):
                if number % i == 0:
                    break
                else:
                    print(number)


# print(primeORnot(1, 10))


def sortfunc(my_list):
    new_list = []
    while my_list:
        min = my_list[0]
        for x in my_list:
            if x < min:
                min = x
        new_list.append(min)
        my_list.remove(min)
    return new_list

print(sortfunc([-15, -26, 15, 1, 23, -64, 23, 76]))

def reverseList(mylist):
    res = []
    for x in range(len(mylist) - 1, 0, -1):
        res.append(mylist[x])
    return res


print(reverseList([-15, -26, 15, 1, 23, -64, 23, 76]))


def duplicates(mylist):
    dictt = {}
    for i in mylist:
        if dictt is None:
            dictt[i] = 1
        else:
            dictt[i] = dictt.get(i, 0) + 1
    res = []
    for i, j in dictt.items():
        if j > 1:
            res.append(i)

    return res


print(duplicates([15, -26, 15, 1, 23, -64, 23]))


def wordinSentence(s):
    count = 0
    for i in s.split():
        count = count + 1

    return count
print(wordinSentence("I want to be best data engineer"))

import re


def extractstringonly(s):
    res = ''
    res1 = ''
    res = re.sub("\D", "", s)
    res1 = re.sub(r'[^a-zA-Z]', ' ', s)
    return res, res1


# initializing string
print(extractstringonly("I want to be best data engineer8980987"))

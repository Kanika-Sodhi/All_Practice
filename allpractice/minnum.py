from numpy import sort

list1 = [4, 3, 1, 0, 9, 5, 5]

#list1 = sort(list1)

largest = list1[0]
secondlargest = list1[1]

if secondlargest >= largest:
    temp = largest
    largest = secondlargest
    secondlargest = temp

for i in range(2, len(list1)):
    if list1[i] < secondlargest:
        secondlargest = list1[i]
    if secondlargest < largest:
        temp = largest
        largest = secondlargest
        secondlargest = temp
print(largest, secondlargest)
a = (largest + secondlargest)
print(a)

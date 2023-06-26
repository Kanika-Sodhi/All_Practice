def solution(a, b):
    n = len(a)
    # create C array
    c = [a[i] + b[i] / 1000000 for i in range(n)]
    print(c)
    count = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if c[i] * c[j] >= c[i] + c[j]:
                # check if current element multiplied by the next element is greater than or equal to the sum of the
                # current element and the next element
                count += 1
    return min(count, 1000000000)
    # return the count, but if it is greater than 1,000,000,000, return 1,000,000,000


A = [0, 1, 2, 2, 3, 5]
B = [500000, 500000, 0, 0, 0, 20000]


# print(solution(A, B))

def minimal_cost(arr):
    n = len(arr)
    min_cost = float('inf')
    # Iterate through all possible breaking points
    for i in range(1, n - 1):
        cost1 = sum(arr[:i])
        cost2 = sum(arr[i:n - 1])
        cost3 = sum(arr[n - 1:])
        min_cost = min(min_cost, cost1, cost2, cost3)
    return min_cost


arr = [10, 20, 30, 40, 30]
print(minimal_cost(arr))

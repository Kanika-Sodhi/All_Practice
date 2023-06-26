# Function to find sum of digits
def digitSum(n):
    sum = 0
    while n:
        sum += (n % 10)
        n = n // 10
    return sum


# Function to find maximum sum pair
# having the same sum of digits
def findMax(arr, n):
    # Map to store the sum of digits
    # in a number as the key and
    # the maximum number having
    # that sum of digits as the value
    mp = {}
    ans = -1
    pairi = 0
    pairj = 0
    for i in range(n):

        # Store the current sum of digits
        # of the number in temp
        temp = digitSum(arr[i])

        # If temp is already present
        # in the map then update
        # ans if the sum is greater
        # than the existing value
        if (temp not in mp):
            mp[temp] = 0

        if (mp[temp] != 0):
            if (arr[i] + mp[temp] > ans):
                pairi = arr[i]
                pairj = mp.get(temp)
                ans = pairi + pairj

        # Change the value in the map
        mp[temp] = max(arr[i], mp[temp])
    print(f"{pairi} {pairj} {ans}")


# Driver Code Starts.
arr = [55, 23, 32, 46, 88]
n = len(arr)
findMax(arr, n)

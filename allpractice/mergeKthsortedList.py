import heapq

from singlylist import ListNode

data = [[1, 6, 9], [4], [8, 2, 3, 1, 7], [5, 3]]
ls = []
results = []


def makesimplelist(mainlist):
    for lst in mainlist:
        for x in lst:
            results.append(x)
    return results


def print_list(the_list):
    ls = makesimplelist(the_list)
    print(set(ls))


print_list(data)

lists = [[1, 4, 5], [1, 3, 4], [2, 6]]

def mergeKLists(lists):
    h = []
    for i in lists:
        while i:
            heapq.heappush(h, i.val)
            i = i.next

    head = ans = ListNode()
    while h:
        head.next = ListNode(heapq.heappop(h))
        head = head.next
    return ans.next

print(mergeKLists(lists))
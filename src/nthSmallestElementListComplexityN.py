# This is the case where average complexity will be O(N)
# and the worst case complexity will be O(n2)
# List is unsorted and does not contain dulpicate elements
# It partially uses quick sort algorithm and the technique below is called quick select
#
#
def findkthSmallestElement(list1:list, k:int)->int:
    if k > 0 and  k <= len(list1):
        position = partition(list1)
        if position == k:
            return list1[position]
        elif position< k:
            findkthSmallestElement()



def partition(list1:list)-> int:
    lastElement = list1[-1]
    i = 0
    for j in range(len(list1)):
        if list1[j]<= lastElement:
            list1[i], list1[j] = list1[j], list1[i]
            i += 1
    list1[i], list1[lastElement] = list1[lastElement],  list1[i]
    return i


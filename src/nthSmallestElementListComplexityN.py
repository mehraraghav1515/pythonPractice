# This is the case where average complexity will be O(N)
# and the worst case complexity will be O(n2)
# List is unsorted and does not contain dulpicate elements
# It partially uses quick sort algorithm and the technique below is called quick select
#
#
# def findkthSmallestElement(list1:list, k:int)->int:
#     if k > 0 and  k <= len(list1):
#         position = partition(list1)
#         if position == k:
#             return list1[position]
#         elif position< k:
#             findkthSmallestElement()
#
#
#
# def partition(list1:list)-> int:
#     lastElement = list1[-1]
#     i = 0
#     for i in range(len(list1)):
#         if list1[i]<= lastElement:
#             i +=1



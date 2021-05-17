# Solution to find the kth element in the list where complexity is O(nlogn)
import sys
def nThSmallestElement(list1:list,position:int)->int:
    list1.sort()
    previous = list1[0]
    rank = 1
    if position > 0 and position <=len(list1):

        for i in range(len(list1)):
            if list1[i] != previous:
                rank += 1

            if rank == position:
                return list1[i]

            previous = list1[i]

    return sys.maxsize



if __name__ == '__main__':
    print(nThSmallestElement([2,4,2,8,5,67,1], 3) )





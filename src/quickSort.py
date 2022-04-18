def partition(alist:list)->int:
    pivotPoint = alist[0]
    leftmarker = alist[1]
    rightmarker = alist[-1]
    temp = 0
    length = len(alist)
    counter = 1
    while leftmarker < rightmarker:
        if leftmarker > pivotPoint > rightmarker:
            temp = rightmarker
            rightmarker= leftmarker
            leftmarker = temp

        leftmarker = alist[counter +1]
        rightmarker = alist[length - counter]




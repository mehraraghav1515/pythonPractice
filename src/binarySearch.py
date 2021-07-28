def binarySearch(inputList:[], numberToLook:int)->bool:

    if len(inputList) == 0:
        return False
    else:
        middle = len(inputList) // 2
    if numberToLook == inputList[middle]:
        return True
    elif numberToLook > inputList[middle]:
        return (inputList[middle + 1:], numberToLook)
    elif numberToLook < inputList[middle]:
        return (inputList[:middle], numberToLook)



if __name__ == '__main__':
    testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    if(binarySearch(testlist, 8)):
        print('Found')
    else:
        print('not found')




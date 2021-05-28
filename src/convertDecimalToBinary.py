def getBinaryFromDecimal(decimalInput : int)->str:
    list1 = []
    binOutput = ''
    while(decimalInput > 0):
        list1.append(decimalInput%2)
        decimalInput = decimalInput//2

    for i in list1:
        binOutput = binOutput + str(i)

    return binOutput




if __name__ == '__main__':
    print(getBinaryFromDecimal(233))

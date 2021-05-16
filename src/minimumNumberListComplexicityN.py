


def minimumNumberList(list1: list )-> int:
    minimumNumber = list1[0]
    for i in list1:
        if i < minimumNumber:
            minimumNumber = i

    return minimumNumber

if __name__ == '__main__':
    minimum = minimumNumberList([5, 2, 7, 9, 3, 5, 76])
    print(minimum)







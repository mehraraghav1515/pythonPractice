class Stack():
    def __init__(self):
        self.operators = []

    def push(self, token):
        self.operators.append(token)

    def pop(self):
        return self.operators.pop()
    def peek(self):
        return self.operators[len(self.operators) - 1]
    def isEmpty(self):
        return self.operators == []




def convertInfixToPostFix(expression : str)->str:
    outputList = []
    tokenList = expression.split()

    # dictionary to define the precedence order
    prec = { "("  : 1,
              "+" : 2,
              "-" : 2,
              "*" : 3,
              "/" : 3 }
    s = Stack()
    for i in tokenList:
        if i == '(':
            s.push(i)
        elif i == ')':
            topToken = s.pop()
            while topToken != '(':
                outputList.append(topToken)
                topToken = s.pop()
        elif i in "ABCDEGHIJKLMNOPQRSTUVWXYZ" or i in "0123456789":
            outputList.append(i)
        else:
            while not (s.isEmpty()) and prec[s.peek()] >= prec[i]:
                outputList.append(s.pop())
            s.push(i)

    while not s.isEmpty():
        outputList.append(s.pop())

    return "".join(outputList)


if __name__ == '__main__':
    inputString = " ( A + B ) * C "
    print(convertInfixToPostFix(inputString))

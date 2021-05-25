class ImplementStack():
    def __init__(self):
        self.stack = []

    def push(self,element):
        self.stack.append(element)

    def pop(self):
        self.stack.pop()

    def peep(self):
        return self.stack(len(stack))

    def isEmpty(self):
         return stack == []

    def size(self):
         return len(self.stack)



s = ImplementStack()
s.push('hello')
s.push(10)
print(s.size())







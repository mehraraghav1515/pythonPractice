class stack:
    def __init__(self):
        self.binaries = []
    def push(self,item):
        self.binaries.append(item)
    def pop(self):
        return self.pop()
    def peep(self):
        return self[self.size() -1]
    def isEmpty(self):
        return (self.binaries == [])
    def size(self):
        return len(self.binaries)

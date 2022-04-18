# class implementQueue:
#     def __init__(self):
#         self.queue = []
#
#     def enqueue(self,item):
#         self.queue.insert((0,item))
#
#     def dequeue(self):
#         return self.queue.pop()
#
#
#
#
#


def testWordMatching():
    list1 = ['pope', 'rope', 'nope', 'hope','lope','mope', 'cope']
    d = {}
    for i in list1:
        word = i
        for j in range(len(word)):
            bucket = word[:j] + '-' + word[j+1:]
            # print(bucket)
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]
        # print(d)
    print(d)



testWordMatching()





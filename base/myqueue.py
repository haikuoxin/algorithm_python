'''
@Author: haikuoxin  
@Date: 2020-11-02 05:42:06  
@Last Modified by:   haikuoxin  
@Last Modified time: 2020-11-02 05:42:06 
'''
class MyQueue(object):
    def __init__(self, capacity):
        self.list = [None] * capacity
        self.front = 0
        self.rear = 0

    def indeque(self, element):
        if (self.rear+1) % len(self.list) == self.front:
            raise Exception('队列已满')
        self.list[self.rear] = element
        self.rear = (self.rear+1) % len(self.list)

    def dequeue(self):
        if (self.rear+1) % len(self.list) == self.front:
            raise Exception('队列已满')
        dequeue_element = self.list[self.front]
        self.front = (self.front+1) % len(self.list)
        return dequeue_element

    def output(self):
        i = self.front
        while i != self.rear:
            print(self.list[i])
            i = (i+1) % len(self.list)


if __name__ == "__main__":
    myqueue = MyQueue(6)
    myqueue.indeque(3)
    myqueue.indeque(5)
    myqueue.indeque(6)
    myqueue.dequeue()
    myqueue.dequeue()
    myqueue.indeque(2)
    myqueue.indeque(3)
    myqueue.output()
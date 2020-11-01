'''
@Author: haikuoxin  
@Date: 2020-11-01 05:18:45  
@Last Modified by:   haikuoxin  
@Last Modified time: 2020-11-01 05:18:45 
'''
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.last = None
        self.size = 0

    def get(self, index):
        if index < 0 or index > self.size:
            raise Exception("超出链表范围！")
        p = self.head
        for i in range(index):
            p = p.next
        return p

    def insert(self, data, index):
        if index < 0 or index > self.size:
            raise Exception("超出链表范围！")
        node = Node(data)
        if self.size == 0:
            self.head = node
            self.last = node
        elif index == 0:
            node.next = self.head
            self.head = node
        elif index == self.size:
            self.last.next = node
            self.last = node
        else:
            prenode = self.get(index-1)
            node.next = prenode.next
            prenode.next = node
        self.size += 1

    def remove(self, index):
        if index < 0 or index > self.size:
            raise Exception("超出链表范围！")
        if index == 0:
            removed_node = self.head
            self.head = removed_node.next
        elif index == self.size:
            prenode = self.get(index-1)
            removed_node = self.last
            self.last = prenode
        else:
            prenode = self.get(index-1)
            nextnode = prenode.next.next
            removed_node = prenode.next
            prenode.next = nextnode
        self.size -= 1
        return removed_node

    def output(self):
        p = self.head
        while p is not None:
            print(p.data)
            p = p.next


if __name__ == "__main__":
    linekedlist = LinkedList()
    linekedlist.insert(3, 0)
    linekedlist.insert(4, 0)
    linekedlist.insert(9, 2)
    linekedlist.insert(5, 3)
    linekedlist.insert(6, 1)
    linekedlist.remove(0)
    linekedlist.output()
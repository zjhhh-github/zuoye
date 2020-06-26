# -*- coding:utf-8 -*-
class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f"Node({self.data})"

class LinkStack:
    def __init__(self):
        self.top = None
        self.size = 0

    def ssize(self):
        return self.size

    def push(self,x):
        node = Node(x)
        self.size += 1
        if self.top is None:
            self.top = node
        else:
            node.next = self.top
            self.top = node


    def pop(self):
        self.size -= 1
        if self.top is None:
            raise IndexError('pop from empty stack')
        else:
            node = self.top
            self.top = node.next
            return node.data

    def empty(self):
        return self.top is None

    def __repr__(self):
        cur = self.top
        string_re = ''
        while cur:
            string_re += f"{cur} ->"
            cur = cur.next
        return string_re + 'END'
if __name__ == '__main__':
    stack = LinkStack()
    for i in range(5):
        stack.push(i)
    print(stack)
    print(stack.ssize())
    stack.pop()
    print(stack)
    print(stack.ssize())

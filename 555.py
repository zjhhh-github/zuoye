# -*- coding:utf-8 -*-
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def circle(head):
    curr = head
    pre = head
    while curr and curr.next:
        pre = pre.next
        cur = curr.next.next
        if pre == curr:
            return True
    return False
if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node3
    print(circle(node1))
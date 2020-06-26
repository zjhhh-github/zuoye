# -*- coding:utf-8 -*-
class Node :
    def __init__(self,data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"

class LinkList :
    def __init__(self):
        self.head = None

    def insert_head(self,data):
        new_node = Node(data)
        if self.head :
            new_node.next = self.head
        self.head = new_node

    def print_list(self): #只打印链表里面的值
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def __repr__(self):
        current = self.head
        result = ""
        while current :
            result += f"{current} -->"
            current = current.next
        return result + "END"



    def append(self,data):
        if self.head :
            self.insert_head(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)


if __name__ == '__main__':
    J = LinkList()
    J.insert_head(1)
    J.append(2)
    J.append(3)
    J.print_list()
    print('---------------')
    print(J)
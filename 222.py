# -*- coding:utf-8 -*-
"""
:author:
:create: 2020/6/19 10:18

"""


class Array:
    def __init__(self, capacity):
        self.array = [None] * capacity
        self.size = 0

    def remove(self, index):
        for i in range(index, self.size - 1):
            self.array[i] = self.array[i + 1]
        self.size -= 1

    def insert(self, index, element):
        if index < 0 or index > self.size:
            raise Exception('数组越界')
        if len(self.array) <= self.size:
            self.addcapacity()
        for i in range(self.size - 1, index - 1, -1):
            self.array[i + 1] = self.array[i]
        self.array[index] = element
        self.size += 1

    def addcapacity(self):
        new_array = [None] * (len(self.array) + 1)
        for i in range(len(self.array)):
            new_array[i] = self.array[i]
        self.array = new_array

    def output(self):
        for i in range(self.size):
            if i < len(self.array) - 1:
                print(self.array[i], end='->')
            else:
                print(self.array[i])
        # print(len(self.array))


if __name__ == '__main__':
    array = Array(3)
    array.insert(0, 10)
    array.insert(1, 20)
    array.insert(2, 30)
    # array.insert(0, 40)
    array.output()
    array.remove(1)
    array.output()

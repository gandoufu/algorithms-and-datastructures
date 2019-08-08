"""
循环队列代码实现，特点：
1. 入队/出队时间复杂度 O(1)
2. 支持动态扩容缩容
"""


class CircularQueue(object):
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.entries = [None] * (capacity + 1)  # 创建数组时多加了一个位置，是为了区分队列为空和队列为满的情况
        self.head = 0
        self.tail = 0
        self.size = 0
    
    def get_size(self):
        """队列中元素个数"""
        return self.size

    def get_capacity(self):
        return self.capacity

    def enqueue(self, item):
        # 如果队列已满，先扩容
        if (self.tail + 1) % len(self.entries) == self.head:
            self.resize(self.capacity * 2)
        self.entries[self.tail] = item
        self.tail = (self.tail + 1) % len(self.entries)
        self.size += 1
    
    def dequeue(self):
        if self.head == self.tail:
            print("Can't dequeue from an empty queue")
            return
        dequeued = self.entries[self.head]
        self.entries[self.head] = None
        self.head = (self.head + 1) % len(self.entries)
        self.size -= 1
        
        # 队列不为空且有有效元素个数小于可容纳元素的1/4时，缩容
        if self.size and self.size < self.capacity // 4:
            self.resize(self.capacity // 2)
        
        return dequeued

    def resize(self, new_capacity):
        new_entries = [None] * (new_capacity + 1)
        for i in range(self.size):
            new_entries[i] = self.entries[(i + self.head) % len(self.entries)]
        self.capacity = new_capacity
        self.entries = new_entries
        self.head = 0
        self.tail = self.size
    
    def traversal(self):
        """遍历输出队列中元素"""
        for i in range(self.size):
            print(self.entries[(self.head+i) % len(self.entries)], end=' ')
        print()

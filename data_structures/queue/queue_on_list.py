class Queue(object):
    """
    基于列表实现的队列，可指定队列大小
    出队的方法中，没有使用列表的pop方法，只是改变head的指向，时间复杂度为 O(1)
    """
    def __init__(self, capacity=10):
        # capacity 队列大小，默认为10
        self.capacity = capacity
        self.entries = [None] * capacity
        self.size = 0
        # head 表示队头下标，tail 表示队尾下标
        self.head = 0
        self.tail = 0

    def __str__(self):
        printed = '<' + str(self.entries[self.head:self.tail]) + '>'
        return printed

    def enqueue(self, item):
        # 队列末位没有空间了
        if self.tail == self.capacity:
            # 队列已满
            if self.head == 0:
                print("The queue is already full")
                return
            # 数据搬移
            for i in range(self.head, self.tail):
                self.entries[i-self.head] = self.entries[i]
            # 搬移完成之后更新 tail 和 head
            self.tail -= self.head
            self.head = 0
        self.entries[self.tail] = item
        self.size += 1
        self.tail += 1

    def dequeue(self):
        if self.size == 0:
            print("Can't dequeue from an empty queue")
            return None
        dequeued = self.entries[self.head]
        self.size -= 1
        self.head += 1
        return dequeued

    def traversal(self):
        for i in range(self.head, self.tail):
            print(self.entries[i], end=' ')
        print()

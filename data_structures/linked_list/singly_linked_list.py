class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):
    def __init__(self, item=None):
        self._head = None if not item else item
    
    def __len__(self):
        """链表长度"""
        if self._head is None:
            return 0
        else:
            cnt = 1
            cur = self._head
            while cur.next:
                cnt += 1
                cur = cur.next
            return cnt
    
    def insert_head(self, item):
        """头部插入新节点"""
        if self._head is None:  # 链表为空
            self._head = item
        else:
            item.next = self._head
            self._head = item

    def insert_tail(self, item):
        """尾部插入新节点"""
        if self._head is None:  # 链表为空
            self._head = item
        else:
            cur = self._head
            while cur.next:
                cur = cur.next
            cur.next = item

    def remove(self, value):
        """删除节点"""
        if self._head is None:  # 链表为空
            return
        prev = None
        cur = self._head
        if cur.data == value and self._head.next is None:  # 只有一个节点且为要删除的
            self._head = cur.next
            return
        while cur.next:
            if cur.data == value:
                prev.next = cur.next
                return
            prev = cur
            cur = cur.next
        if cur.data == value:  # 判断最后一个节点的值
            prev.next = None

    def traversal(self):
        """遍历链表"""
        cur = self._head
        if not cur:  # 链表为空
            return
        while cur.next:
            print(cur.data, end=", ")
            cur = cur.next
        print(cur.data)

    def is_empty(self):    
        """判断是否为空"""
        return self._head is None
    
    def search(self, value):
        """判断指定的节点是否存在"""
        if self._head is None:
            return False
        else:
            cur = self._head
            while cur.next:
                if cur.data == value:
                    return True
                cur = cur.next
            return cur.data == value  # 跳出 while 循环后，验证最后一个节点
    
    def reverse(self):
        """链表反转"""
        if self._head is None or self._head.next is None:  # 链表为空或只有一个节点
            return
        prev = None
        cur = self._head
        while cur:
            # 记录当前节点的下一个节点
            next_node = cur.next
            # 当前节点回指到上一个节点
            cur.next = prev
            # prev 和 cur 游标前移
            prev = cur
            cur = next_node
        self._head = prev


def main():
    L = LinkedList()
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(5)
    n4 = Node(6)

    # 判断链表是否为空
    print(L.is_empty())
    # 从头部插入节点
    L.insert_head(n1)
    L.insert_head(n2)
    # 从尾部插入节点
    L.insert_tail(n3)
    L.insert_tail(n4)
    # 遍历链表
    L.traversal()
    # 链表反转
    L.reverse()
    L.traversal()
    print(L.is_empty())
    # 链表节点个数
    print(len(L))
    # 查找值
    print(L.search(5))
    # 删除节点
    L.remove(5)
    L.traversal()


if __name__ == "__main__":
    main()


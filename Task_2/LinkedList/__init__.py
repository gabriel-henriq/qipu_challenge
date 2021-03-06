class OutOfBoundsException(Exception):
    pass


class LinkedListNode(object):
    def __init__(self, value, next=None):
        self._value = value
        self._next = next

    def __repr__(self):
        return f"{self._value}"

    @property
    def value(self):
        return self._value

    @property
    def next(self):
        return self._next

    @next.getter
    def next(self):
        return self._next

    @next.setter
    def next(self, node):
        self._next = node

    def hasNext(self):
        return self._next is not None


class LinkedList(object):
    def __init__(self):
        self._head = None
        self._tail = None
        self._len = 0

    def __repr__(self):
        return f"Linkedlist(head={self.head}, tail={self.tail}, len={self._len})"

    def __len__(self):
        return self._len

    @property
    def len(self):
        return self._len

    @len.getter
    def len(self):
        return self._len

    @property
    def head(self):
        return self._head

    @head.getter
    def head(self):
        if self._head is not None:
            return self._head.value

    @property
    def tail(self):
        return self._tail

    @tail.getter
    def tail(self):
        if self._tail is not None:
            return self._tail.value

    def append(self, value):
        new_node = LinkedListNode(value)
        if self._len == 0:
            self._head = new_node
        else:
            self._tail.next = new_node
        self._tail = new_node
        self._len += 1

    def insert(self, value):
        new_node = LinkedListNode(value)
        temp = self._head
        self._head = new_node
        new_node.next = temp
        self._len += 1

        if self._len == 1:
            self._tail = self._head

    def removeFirst(self):
        if self._len == 0:
            raise OutOfBoundsException
        else:
            temp = self._head
            self._head = self._head.next
            self._len -= 1
            if self._len == 0:
                self._tail = None
            return temp.value

    def getValueAt(self, index):
        if index > self._len:
            raise OutOfBoundsException
        else:
            node = self._head
            for _ in range(index):
                node = node.next
            return node.value

    def toList(self):
        return [self.getValueAt(i) for i in range(self._len)]

    def get_values_and_ref(self):
        node = self._head
        nodeList = []
        for index in range(0, self.len):
            value_ref = {"index": index, "value": node.value, "ref": node.next}
            nodeList.append(value_ref)
            node = node.next
        return nodeList

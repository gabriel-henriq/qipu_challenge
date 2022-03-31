#!/usr/bin/python
# -*- coding: utf-8 -*


class OutOfBoundsException(Exception):
    pass


class LinkedListNode(object):
    def __init__(self, value, next=None):
        self._value = value
        self._next = next

    def __repr__(self):
        return str(self._value, self._next)

    @property
    def value(self):
        return self._value

    @property
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

    def __len__(self):
        if self._len is not None:
            return self._len

    def __repr__(self):
        return str(self.head, self.tail, self._len)

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


if __name__ == "__main__":
    """
    Gabarito de execução e testes. Se o seu código passar e chegar até o final,
    possivelmente você implementou tudo corretamente
    """
    ll = LinkedList()
    assert ll.head is None
    assert ll.tail is None
    assert ll.toList() == []
    ll.append(1)
    assert ll.head == 1
    assert ll.tail == 1
    assert len(ll) == 1
    assert ll.toList() == [1]
    ll.append(2)
    assert ll.head == 1
    assert ll.tail == 2
    assert len(ll) == 2
    assert ll.toList() == [1, 2]
    ll.append(3)
    assert ll.head == 1
    assert ll.tail == 3
    assert len(ll) == 3
    assert ll.toList() == [1, 2, 3]
    ll.insert(0)
    assert ll.head == 0
    assert ll.tail == 3
    assert len(ll) == 4
    assert ll.toList() == [0, 1, 2, 3]
    ll.insert(-1)
    assert ll.toList() == [-1, 0, 1, 2, 3]
    v = ll.removeFirst()
    assert v == -1
    assert ll.toList() == [0, 1, 2, 3]
    v = ll.removeFirst()
    assert v == 0
    assert ll.toList() == [1, 2, 3]
    v = ll.removeFirst()
    assert v == 1
    assert ll.toList() == [2, 3]
    v = ll.removeFirst()
    assert v == 2
    assert ll.toList() == [3]
    v = ll.removeFirst()
    assert v == 3
    assert ll.toList() == []
    assert len(ll) == 0
    print("100%")

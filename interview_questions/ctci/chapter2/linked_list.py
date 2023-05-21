import random


class LinkedListNode:
    def __init__(self, value, next_node=None, prev_node=None)-> None:
        self.value = value
        self.next = next_node
        self.prev = prev_node

    
    def __str__(self) -> str:
        return str(self.value)
    

class LinkedList:
    def __init__(self, values=None) -> None:
        self.head = None
        self.tail = None
        if values is not None:
            self.append_all(values)


    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next


    def __str__(self) -> str:
        values = [str(x) for x in self]
        return " -> ".join(values)
    

    def __len__(self):
        result = 0
        node = self.head
        while node:
            result += 1
            node = node.next
        return result
    

    def values(self):
        return [x.value for x in self]
    

    def add(self, value):
        if self.head == None:
            self.tail = self.head = LinkedListNode(value)
        else:
            self.tail.next = LinkedListNode(value)
            self.tail = self.tail.next
        return self.tail
    

    def prepend(self, value):
        if self.head == None:
            self.tail = self.head = LinkedListNode(value)
        else:
            self.head = LinkedListNode(value)
        return self.head
    

    def append_all(self, values):
        for v in values:
            self.add(v)


    @classmethod
    def generate(cls, k, min_value, max_value):
        return cls(random.choices(range(min_value, max_value), k=k))
    

class DoublyLinkedList(LinkedList):
    def add(self, value):
        if self.head in None:
            self.tail = self.head = LinkedListNode(value)
        else:
            self.tail.next = LinkedListNode(value, None, self.tail)
            self.tail = self.tail.next
        return self
    

        
        
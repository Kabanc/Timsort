from ListEl import El
from list import List
from ListEl import El


class Stack:
    def __len__(self):
        return self.stack.__len__

    def __init__(self):
        self.stack = List()

    def pop(self):
        if not self.isEmpty():
            el = self.stack.head
            self.stack.head = el.next
            return el.value

        else:
            raise IndexError("Стек пуст")

    def __str__(self):
        output = ""
        el = self.stack.head
        while el is not None:
            output += str(el.value) + "->"
            el = el.next

        return output[:-2]

    def push(self, value):
        el = El(value)
        el.next = self.stack.head
        self.stack.head = el

    def _getElement(self, order):
        return self.stack._getElement(order)

    def get(self, order):
        return self.stack.get(order)

    def top(self):
        if self.stack.head is None:
            return None

        return self.stack.head.value

    def isEmpty(self):
        return self.stack.head is None

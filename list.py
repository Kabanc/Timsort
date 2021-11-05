from ListEl import El


class List(object):

    def __init__(self):
        self.head = None

    def __len__(self):
        el = self.head
        i = 0
        while el is not None:
            i += 1
            el = el.next
        return i

    def __str__(self):
        output = ""
        el = self.head
        while el is not None:
            output += str(el.value) + "->"
            el = el.next

        return output[:-2]

    def lastElement(self):
        el = self.head
        if el is None:
            return el

        while el.next is not None:
            el = el.next

        return el

    def _getElement(self, order):
        if order < 0:
            raise IndexError("Вы ввели некорректный номер элемента")
        if order == 0:
            return self.head

        el = self.head
        for i in range(order):
            el = el.next
            if el is None:
                raise IndexError("Элемента с введённым номером не существует")
        return el

    def get(self, order):
        return self._getElement(order).value

    def add(self, value):
        if self.head is None:
            self.head = El(value)
        else:
            self.lastElement().next = El(value)

    def set(self, order, value):
        self._getElement(order).value = value

    def orderOf(self, value):
        el = self.head
        i = 0
        while el is not None:
            if el.value == value:
                return i
            el = el.next
            i += 1

        return -1

    def remove(self, value):
        order = self.orderOf(value)
        if order == -1:
            raise ValueError("Значение не найдено")

        self.removeAt(order)

    def removeAt(self, order):
        if order < 0:
            raise IndexError("Вы ввели некорректный номер элемента")
        if order == 0:
            self.head = self.head.next
            return

        el = self._getElement(order - 1)
        if el.next is None:
            raise IndexError("Этого элемента не существует")

        el.next = el.next.next



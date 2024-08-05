class Stack:
    """
    Класс стека.
    Временная сложность методов O(1)

    Поля:
    Поле items - список элементов стека

    Методы:
    - is_empty() - возвращает истину, если стек пуст
    - push(item) - добавляет элемент в стек
    - pop() - удаляет элемент из стека
    - peek() - возвращает верхний элемент стека
    - size() - возвращает количество элементов в стеке
    """
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

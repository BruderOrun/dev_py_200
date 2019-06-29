# -*- coding: utf-8

#
# Курс DEV-PY200. Объектно-ориентированное программирование на языке Python
# Тема 1.1 Основы ООП. Понятие класса, объекта. Создание экземпляра класса

# Лабораторная работа № 1.1 (4 ак.ч.)

# Слушатель (ФИО): Серкин А.П.

# ---------------------------------------------------------------------------------------------
# Задание 11.
import weakref


class LinkedList:
    """
    
    """
    class __Node:
        """
        Describe node - the element with some parameters and methods. 
        Each node consist of 3 items: stored data in this object -> Any, 
        reference to the next element, reference to the previous element.
        """
        def __init__(self, data=None, prev=None, next_=None):
            self.__next = next_
            self.__prev = weakref.ref(prev) if prev is not None else None
            self.data = data

        @property
        def node_data(self):
            return self.data

        @node_data.setter
        def node_data(self, value):
            self.data = value

        @property
        def next_node(self):
            return self.__next

        @next_node.setter
        def next_node(self, node):
            self.__next = node

        @property
        def prev_node(self):
            return self.__prev() if self.__prev is not None else None

        @prev_node.setter
        def prev_node(self, node):
            self.__prev = weakref.ref(node) if node is not None else None

        def __str__(self):
            return f'{self.data}'

    def __init__(self):
        self.__head = self.__Node()
        self.__tail = self.__Node(None, self.__head)
        self.__head.next_node = self.__tail

    def __str__(self):
        new_node = self.__head.next_node
        result = []
        while new_node is not self.__tail:
            result.append(new_node.node_data)
            new_node = new_node.next_node
        return str(result)

    @classmethod
    def __push(cls, current_node, data):
        new_node = cls.__Node(data, current_node, current_node.next_node)
        current_node.next_node.prev_node = new_node
        current_node.next_node = new_node

    def __pop(self, current_node):
        if isinstance(current_node, self.__Node) and current_node is not None:
            current_node.prev_node.next_node = current_node.next_node
            current_node.next_node.prev_node = current_node.prev_node
            return current_node.data

    def __find_data(self, data):
        """
        If data in class instance returns tuple of data position (index) and data.
        Otherwise returns tuple (length, None) of the instance.
        :param data: any value, list tuple and so on
        :return: tuple
        """
        length = -1
        pos = - 1
        current_node = self.__head
        while current_node is not self.__tail:
            if data == current_node.data:
                return pos, current_node
            current_node = current_node.next_node
            pos += 1
            length += 1
        return length, None
    
    def __find_index(self, index):
        current_node = self.__head
        for _ in range(index+1):
            current_node = current_node.next_node
            if current_node is self.__tail:
                current_node = self.__tail.prev_node
                break
        return current_node if current_node != self.__head else None
    
    def insert(self, data, index=0):
        """
        Insert Node to any place of LinkedList
        node - Node
        index - position of node
        """
        self.__push(self.__find_index(self, index), data)

    def append(self, data):
        '''
        Append Node to tail of LinkedList
        node - Node
        '''
        self.__push(self.__tail.prev_node, data)

    def clear(self):
        '''
        Clear LinkedList
        '''
        self.__tail.prev_node = self.__head
        self.__head.next_node = self.__tail

    def find(self, data) -> int:
        return self.__find(data)[0] if self.__find(data)[1] is not None else f'Элемент {data} не найден.'

    def remove(self, data):
        length, result = self.__find_data(data)
        return self.__pop(result) if result is not None else f'Элемент {data} не найден.'

    def delete(self, index):
        return self.__pop(self.__find_index(index))

        
print(f'step11:')
mylist = LinkedList()
element = [2, 8]
mylist.append(element)
print(mylist)
element = 6
mylist.append(element)
print(mylist)
print(mylist.remove(5))
print(mylist)
print(mylist.remove(7))
print(mylist)
print(mylist.remove([2, 8]))
print(mylist)
print(mylist.delete(0))
print(mylist)
print(mylist.delete(0))
print(mylist)

class Glass:

    def __init__(self, capacity_volume, occupied_volume):
        '''


        '''

        # self.is_valid_date(year, month, day)
        self.capacity_volume = capacity_volume
        self.occupied_volume = occupied_volume

    @classmethod
    def is_valid_glass(cls, capacity_volume, occupied_volume):
        if not isinstance(capacity_volume, int):
            raise TypeError('capacity_volume must be int')
        if not isinstance(occupied_volume, int):
            raise TypeError('occupied_volume must be int')

        if not 0 < capacity_volume or capacity_volume > 10.0:
            raise ValueError('capacity_volume must be >0 and < 10.0')

        if not 0 < occupied_volume or occupied_volume > 10.0:
            raise ValueError('occupied_volume must be >0 and < 10.0')


glass_1 = Glass(8, 10)
# print(glass_1.capacity_volume)
glass_2 = Glass(2.0, 9.0)


# print(glass_2.capacity_volume)


class GlassDefaultArg:
    def __init__(self, occupied_volume=0):
        self.occupied_volume = occupied_volume

    @classmethod
    def is_valid_deffault(cls, occupied_volume):
        if not isinstance(occupied_volume, int):
            raise TypeError('occupied_volume must be int')
        if not 0 < occupied_volume or occupied_volume > 10.0:
            raise ValueError('occupied_volume must be >0 and < 10.0')


glas_def_arg_1 = GlassDefaultArg()
glas_def_arg_2 = GlassDefaultArg(200)


# print(glas_def_arg_1.occupied_volume)
# print(glas_def_arg_2.occupied_volume)

class GlassDefaultListArg:

    def __init__(self, capacity_volume, occupied_volume=[]):
        self.capacity_volume = capacity_volume
        self.occupied_volume = occupied_volume
        self.occupied_volume.append(capacity_volume)


#
# glassDefaultListAr_1 = GlassDefaultListArg(2)
#
# print(glassDefaultListAr_1.occupied_volume)
#
# glassDefaultListAr_2 = GlassDefaultListArg(2)
# print(glassDefaultListAr_2.occupied_volume)
#
# glassDefaultListAr_3 = GlassDefaultListArg(2)
# print(glassDefaultListAr_3.occupied_volume)
# print(glassDefaultListAr_1.occupied_volume)
# print(glassDefaultListAr_2.occupied_volume)
# glassDefaultListAr_3 = GlassDefaultListArg(6)
# print(glassDefaultListAr_2.occupied_volume)


class GlassAddRemove:
    def __init__(self, occupied_volume=0, water=0):
        print(dir(self))
        self.occupied_volume = occupied_volume
        print(dir(self))
        self.water = water
        print(dir(self))
        '''
        По мере инициализации мы видим новые инициализированные переменные сперва occupied_volume, потом water
        '''

    def add_water(self, water):
        self.occupied_volume += water
        return self.occupied_volume

    def remove_water(self, water):
        self.occupied_volume -= water
        return self.occupied_volume


glassAddRemove_1 = GlassAddRemove(0, 20)
# print(glassAddRemove_1.add_water())
print(glassAddRemove_1.add_water(3))
print(glassAddRemove_1.remove_water(3))
glassAddRemove_2 = GlassAddRemove(1, 40)
glassAddRemove_3 = GlassAddRemove(2, 60)

print(glassAddRemove_1.__dir__())
print(glassAddRemove_2.__dir__())
print(glassAddRemove_2.__dir__())
print(GlassAddRemove.__dir__(2))
print(type(glassAddRemove_2))
# print(isinstance(GlassAddRemove))


glass_00 = Glass
glass_01 = Glass
glass_02 = Glass

print(id(glass_00))
print(id(glass_01))
print(id(glass_02))


# 9. Корректно ли следующее объявление класса с точки зрения:
#     - интерпретатора Python;
#     - соглашения о стиле кодирования
#    Запустите код.
class d:
	def __init__(f, a=2):
		f.a = a

	def print_me(p):
		print(p.a)

d.print_me(d())
'''
Да корректно, хотя и с нарушениями pep 8
'''
# 10. Исправьте
class A:
	def __init__(self, a):
		if 10 < a < 50:
			return
		self.a = a  #todo тут

# Объясните так реализовывать __init__ нельзя?

#todo Можно, но не нужно


# 11 задание просто не понимаю.
# Возникает масса вопросов по реализации, которые не уточнить
#

# 11. Циклическая зависимость (стр. 39-44)
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

    def __find_index(self, index, data = None):
        current_node = self.__head
        for _ in range(index + 1):
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



mylist = LinkedList()
element = [2, 8,5,6,7,8,]
mylist.append(element)
print(mylist)
element = 6
mylist.append(element)
print(mylist)
print(mylist.remove(5))

print(mylist)
print(mylist.clear())
print(mylist)


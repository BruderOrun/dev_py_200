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
#

class Node:
    def __init__(self, prev=None, next_=None):
        self.__prev = prev
        self.__next = next_
    def set_next(self, next_):
        self.__next = next_

    def set_prev(self, prev):
        self.__prev = prev

    def __str__(self):
        ...

    def __repr__(self):
        ...

class LinkedList:



    def insert(self, node, index=0):
        '''
        Insert Node to any place of LinkedList
        node - Node
        index - position of node
        '''
        ...
        counter = 1
        if index == 0:
            node.set_next(self.head)
            self.head = node

        else:
            node = self.head
            while node.next is not None:
                if counter == index:
                    node.set_next(node.next)
                    node.set_next(node)
                    return
                node = node.next
                counter = counter + 1




    def append(self, node):
        '''
        Append Node to tail of LinkedList
        node - Node
        '''
        new_node = Node(node)
        new_node.next = self.head
        self.head = new_node

    def clear(self):
        '''
        Clear LinkedList
        '''



    def find(self, node):
        ...


    def remove(self, node):
        ...

    def delete(self, index):
        ...

#
# Курс DEV-PY200. Объектно-ориентированное программирование на языке Python
# Тема 2. Инкапсуляция, наследование, полиморфизм

# Лабораторная работа № 2.2 (1 ак.ч.)

# ---------------------------------------------------------------------------------------------

# 1
# Создайте следующую цепочку наследования
# A
# |
# B
# |
# C
# Создайте объект C. Получите кортеж всех родителей
print("#1")


class A:
    pass


class B(A):
    pass


class C(B):
    pass


ob = C

print(ob.mro())

print('#2')

# 2
# Создайте следующую цепочку наследования
# A
# | \
# B  C
# | /
# D
# Создайте объект D. Получите кортеж всех родителей
print('Задание № 2: НАЧАЛО')


class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


ob = D

print(ob.mro())

# 3
# Создайте следующую цепочку наследования
#  A
# / \
# B  C
# |  |
# |  D
# | /
# F
# Создайте объект F. Получите кортеж всех родителей
print("#3")


class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(C):
    pass


class F(B, D):
    pass


ob = F
print(ob.mro())

# 4
# Создайте следующую цепочку наследования
# A
# |
# B  C
# \ /
#  F
# Создайте объект A.
# Добавьте методов класс A f, который печатает атрибут (public name, protected _name и private __name)
# экземпляра класса A. Аналогичные атрибуты для классов B, C, F.
# Вызовите все методы из объектов классов A, B, C, F
print('#4')


class A:
    name = 'A'
    _name = 'AA'
    __name = 'AAA'

    @classmethod
    def qwe(cls):
        print(cls.name)

    @classmethod
    def qwea(cls):
        print(cls._name)

    @classmethod
    def qweas(cls):
        print(cls.__name)


class B(A):
    name = 'B'
    _name = 'BB'
    __name = 'BBB'

    @classmethod
    def qwe(cls):
        print(cls.name)

    @classmethod
    def qwea(cls):
        print(cls._name)

    @classmethod
    def qweas(cls):
        print(cls.__name)


class C:
    name = 'C'
    _name = 'CC'
    __name = 'CCC'

    @classmethod
    def qwe(cls):
        print(cls.name)

    @classmethod
    def qwea(cls):
        print(cls._name)

    @classmethod
    def qweas(cls):
        print(cls.__name)


class F(B, C):
    name = 'F'
    _name = 'FF'
    __name = 'FFF'

    @classmethod
    def qwe(cls):
        print(cls.name)

    @classmethod
    def qwea(cls):
        print(cls._name)

    @classmethod
    def qweas(cls):
        print(cls.__name)

aa = A
bb = B
cc = C
ff = F

aa.qwe()
aa.qwea()
aa.qweas()

bb.qwe()
bb.qwea()
bb.qweas()

cc.qwe()
cc.qwea()
cc.qweas()

ff.qwe()
ff.qwea()
ff.qweas()

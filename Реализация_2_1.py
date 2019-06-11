# """
# DEV-PY200. Объектно-ориентированное программирование на языке Python
# Страница 1 из 1
# Тема 2. Инкапсуляция, наследование, полиморфизм
# Всего на тему 2: 12 ак.ч. (3 занятия)
# Часть 1 (4 ак.ч.)
# 1. В Python нет возможности объявления константных переменных. Реализуйте
# с помощью @property константный атрибут. Пусть класс возвращает число
# пи. Попытайтесь применить @property к @staticmethod и @classmethod. Если
# не получается, то примените к обычному методу. (Тема 1. Слайды 1-43)
class P:
    def __init__(self, a):
        self.a = a

    # @property
    # @staticmethod  #todo TypeError: 'staticmethod' object is not callable
    # @classmethod #TypeError: 'classmethod' object is not callable
    def pp(self):
        self.a = 3.14
        return self.a


pi = P(22)
print(pi.pp())
print(P.pp)


# 2. Создайте классы A и B(A).
#  a. В классе А создайте атрибуты класса, атрибуты
# объекта, @staticmethod, @classmethod и методов со всеми видами областями
# видимости.
#   b. Продемонстрируете их видимость внутри класса, вне класса и в
# классе потомке.
#    c. Получите доступ вне класса к псевдозащищённым
# псевдоприватным атрибутам и методам. (Тема 2. Слайды 1-43)
class A:
    def __init__(self, aper1, aper2, aper3):
        self.aper1 = aper1
        self._aper2 = aper2
        self.__aper3 = aper3

    def metod1(self):
        return f'{self.aper1},{self._aper2},{self.__aper3}'

    @staticmethod
    def metod2(self):
        a = 3 + 2
        return a

    def metod3(self):
        pass


dr = A(3, 4, 4)
print(A.metod1(dr))
print(dr.metod1())

print(A.metod2(3))


class B():

    def aper_1(self):
        self.aper1 = 12

    def aper_2(self):
        return print(dr.metod1())


b = B()
b.aper_2()

# 3. Реализуйте классы Figure, Rectangle, Ellipse. Нужен метод получения
# координат x, y, размеров фигур w и h, также нужно, чтобы можно было
# получить периметр и площадь фигуры. Интерфейс Figure определить из
# файла figure_painter.py, т.е. изучаете код, а затем пишете интерфейс класса
# Figure так, чтобы он работал. Для запускай файла figure_painter.py
# необходимо установить библиотеку pip install pyside2. (Тема 2. Слайды 44-47)

from abc import ABCMeta, abstractmethod


class Figure(metaclass=ABCMeta):
    def __init__(self, x, y, width, height):
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height

    def x(self):
        return self.__x

    def y(self):
        return self.__y

    def width(self):
        return self.__width

    def height(self):
        return self.__height

    # @abstractmethod
    def perimeter(self):
        pass

    # @abstractmethod
    def square(self):
        pass


class Rectangle(Figure):

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)

    def perimeter(self):
        return 2 * (self.width() + self.height())

    def square(self):
        return self.width() * self.height()


class Ellipse(Figure):

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)

    def perimeter(self):
        return 2 * (self.width() + self.height())

    def square(self):
        return self.width() * self.height()


# 4. Переработайте иерархию классов Figure так, чтобы можно было рисовать
# произвольные замкнутые фигуры CloseFigure. Если Rectangle или Ellipse, то
# использовать другие методы, а не данные из CloseFigure.
class CloseFigure(Figure):

    def __init__(self, point):
        self.point = point
        self.ofs = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.ofs == len(self.point):
            raise StopIteration
        point = self.point[self.ofs]
        self.ofs += 1
        return point


# 5. В Python 3 все классы являются классами нового стиля. Классы нового стиля
# – это классы, которые являются наследниками от класса object. Убедитесь,
# что класс А является наследником от object. (Тема 2. Слайды 48-52)
# """
class A:
    pass


class B:
    pass


class C(A, B):
    def __init__(self):
        print(str(self.__class__.__bases__))
        print(C.__mro__)


import os

print(os.environ)

if __name__ == '__main__':
    C()

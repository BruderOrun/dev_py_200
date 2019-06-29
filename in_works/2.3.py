
# 1
# Разработайте два абстрактных класса:
# - IReader с абстрактным методом read, который принимает строку с названием файла,
#   а возвращает словарь с ключами и их значениями или None;
# - IWriter с методом write, который принимает строку с названием файла и
#   словарь со ключами и их значениями. Возвращает True, если запись успешно выполнена,
#   иначе False
# Метод IReader.read читает данные из файла
# Метод IWriter записывает данные в файла
# Наследуйтесь от класса IReader:
# - JSONReader: читает файл формата json;
# - CSVReader: читает файл формата csv;
# Наследуйтесь от класса IWriter:
# - JSONWriter: записывает файл формата json;
# - CSVWriter: записывает файл формата csv;

from abc import ABCMeta, abstractmethod
import json
import csv


class IReader(metaclass=ABCMeta):
    @abstractmethod
    def read(self, param):
        pass


class IWriter(metaclass=ABCMeta):
    @abstractmethod
    def write(self, param, param_2):
        pass


class JSONReader(IReader):

    def read(self, param):
        with open(param, 'r') as j_f:
            self.j_d = json.load(j_f)
        return self.j_d


class CSVReader(IReader):
    def __init__(self):
        self.__csv_d = []

    def read(self, param):
        with open(param, 'r') as csv_f:
            csv_reader = csv.DictReader(csv_f, delimiter=';')
            for line in csv_reader:
                self.__csv_d.append(dict(line))
        return self.__csv_d


class JSONWiter(IWriter):

    def write(self, param, param_2):
        with open(param, 'w') as jf:
            try:
                json.dump(param_2, jf)
            except:
                return False
        return True


class CSVWriter(IWriter):

    def write(self, param, param_2):
        with open(param, 'w', newline='') as cv:
            try:
                writer = csv.DictWriter(cv, delimiter=';', fieldnames=param_2.keys())
                writer.writeheader()
                writer.writerow(param_2)
            except:
                return False
        return True



class ReadClient:
    def __init__(self):
        self.__readers = {'json': JSONReader(), 'csv': CSVReader()}
        self.__alg = None

    def read_file(self, name):

        try:
            self.__alg = self.__readers[name.rsplit('.', 1)[1].lower()]
        except:
            print('Вы ввели некорретный формат файла')
        if self.__alg is None:
            return False

        return self.__alg.read(param=name)


class WriteClient:
    def __init__(self):
        self.__writers = {'json': JSONWiter(), 'csv': CSVWriter()}
        self.__alg = None

    def write_file(self, name, data):
        if self.__alg is None:
            return 'Не выбрано расширение записываемого файла (json/csv)'

        return self.__alg.write(name, data)

    def set_driver(self, driver_name):

        try:
            self.__alg = self.__writers[driver_name]
        except:
            return 'Введен неверное расширение файла'
        return True




# 4
# Интерактивное взаимодействие с ReadClient и WriteClient.
# С помощью input() пользователь может выбрать ReadClient или WriteClient.
# Далее пользователь пишет название файл. Если WriteClient, то запрашивает формат.
# Если ReadClient, то автоматически читает файл с нужным форматом и выводит на экран в виде словаря.
# Если WriteClient, то пользователь пишет словарь в виде строки, а затем передаётся в exec.

if __name__ == "__main__":
    print('\n''Чтение или запись файла?')
    action = input('Введите> ').lower()

    if action in ('чтение', 'fff'):
        reader_client = ReadClient()
        print(reader_client.read_file(input('Название файла> ')))
    elif action in ('запись', 'fffrt'):
        write_client = WriteClient()
        param = input('Введите название файла> ')
        f_exten = input('Введите расширение файла (json/csv> ')
        s = input('Введите словарь для записи в файл> ')
        try:
            exec(f'data = {s}')
        except:
            print('Некорректный ввод словаря')
        write_client.set_driver(f_exten)
        write_client.write_file('.'.join([param, f_exten]), data=data)



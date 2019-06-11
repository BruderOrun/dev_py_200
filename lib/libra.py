import os
import shutil
from itertools import count
import json
import sqlite3

list_for_analysis = []  # todo Временное хранение списка на разбор и добавление
directory_choice = os.getcwd() + '/the_choice'  # todo  директория хранящая файлы на разбор и добавление
directory_added_books = os.getcwd() + '/the_added_books'  # todo директория хранения файлов бибилиотеки
list_added_books = []  # todo Временное хранение списка бибилиотеки


class Book:
    def __init__(self):
       self.listt = list_for_analysis

    def view_add(self, directory, listt):  # todo  вывод списка библиотеки или списка на разбор
        files = os.listdir(directory)
        files = sorted(files, reverse=True)
        for i in range(len(files)):
            if files[i].endswith('.txt') or files[i].endswith('.doc'):
                listt.append(files[i])
                print(f'{i+1}. {files[i]}')
        return self.listt


    def add(self):
        # dirr = os.listdir(os.getcwd())
        # if 'libmydatabase.db' not in dirr:
        conn = sqlite3.connect(os.getcwd() + "_mydatabase.db")  # или :memory: чтобы сохранить в RAM
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS core_fes(id integer,
                                                                 name_book text, 
                                                                 autor_book text,
                                                                 create_year_book text,
                                                                 summary_book text
                                                                 )
                           """)
        cursor.execute('INSERT  INTO core_fes VALUES ("01", "Primer", "Avtor", "1970", "Я помню чудное мгновенье")')

        conn.commit()

        cursor.close()
        conn.close()
#
#
# class Json:
#     name_book = "dfdfdfdfdf"
#     autor_book = "2222222"
#     create_year_book = "33333"
#     summary_book = "4444"
#
#     json_model = {
#         "Books_lib": {"Name_book": f"{name_book}", "Autor_book": f"{autor_book}",
#                       "Create_year_book": f"{create_year_book}",
#                       "Summary_book": f"{summary_book}"}}
#
#     # with open(json_model, "w") as jsm:
#     # print(json.dumps(json_model, sort_keys=True, indent=4))

    # pass


class Pars:
    pass


if __name__ == '__main__':
    book = Book()
    print(book.view_add( directory_choice, list_for_analysis))
    book.add()
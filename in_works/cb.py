# import urllib
# from xml.etree import ElementTree as ET
#
# id_dollar = "R01235"
# id_evro = "R01239"
#
#
# help(urllib.open)
# #
# # valuta = ET.parse(not urllib.urlopen("http://www.cbr.ru/scripts/XML_daily.asp?date_req"))
# #
# # for line in valuta.findall('Valute'):
# #     id_v = line.get('ID')
# #     if id_v == id_dollar:
# #         rub = line.find('Value').text
# #         print("\nКурс доллара", rub, "рублей")
# #     if id_v == id_evro:
# #         rub = line.find('Value').text
# #         print("\nКурс евро", rub, "рублей")

import math
fun = lambda x : 1 if x == 1 else math.ceil(math.sinh(fun (x-1)))

fun(5)  
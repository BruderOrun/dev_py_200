"""Калькулятор в процедурном стиле"""


def calculator():
	ops = {'+': lambda l, r: l+r, '_': lambda l, r: l-r}
	while True:
		s = input('Input expression ->')
		if 'exit' == s:
			break

		l = s.split()
		print(l)

		if len(l) != 3:
			print('invalid format')
			continue

		a, op, b = l

		try:
			a = float(a)
			b = float(b)
			c = ops[op](a, b)

		except ValueError:
			print('Invalid format: a or b are not float')
			continue

		except KeyError:
			print(f'invalid format: operation {op} is not defined.')
			continue

		print(f'{a}{op}{b} = {c}')


"""Пример - обращение к атрибуту класса"""


class ExampleClass:

	inc = 0

	def __init__(self, a):
		self.a = a
		self._b = a + 1
		self.__c = a + 2
		cls = type(self)
		cls.inc += 1
		# ExampleClass.inc += 1  # так тоже работает


	def get_c_plus_inc(self):
		return self.__c + self.inc

	@classmethod
	def get_inc(cls):
		return cls.inc


"""ООП калькулятор простой"""


class BackendCalc:
	a: int = 5

	@staticmethod
	def addition(l, r):
		if not(isinstance(l, (int, float)) and isinstance(r, (int, float))):
			raise TypeError('l or r must be int or float')
		return l+r

	@staticmethod
	def substraction(l, r):
		if not (isinstance(l, (int, float)) and isinstance(r, (int, float))):
			raise TypeError('l or r must be int or float')
		return l - r

	@staticmethod
	def multiplication(l, r):
		if not (isinstance(l, (int, float)) and isinstance(r, (int, float))):
			raise TypeError('l or r must be int or float')
		return l * r

	@staticmethod
	def division(l, r):
		if not (isinstance(l, (int, float)) and isinstance(r, (int, float))):
			raise TypeError('l or r must be int or float')
		return l / r


class SimpleCalcFrontend:
	@staticmethod
	def execute():
		while True:
			s = input('Input an expression and press Enter ->')
			if s == "exit":
				break
			l = s.split()
			if len(l) != 3:
				print("equation must consist of 2 numbers and 1 operator")
				continue
			a, op, b = l
			try:
				a = int(a)
				b = int(b)
			except TypeError('a or b must be int or float'):
				a = float(a)
				b = float(b)

			if op == '+':
				print(BackendCalc.addition(a, b))
				continue
			if op == '-':
				print(BackendCalc.substraction(a, b))
				continue
			if op == '*':
				print(BackendCalc.multiplication(a, b))
				continue
			if op == '/':
				print(BackendCalc.division(a, b))
				continue
			else:
				print("Incorrect operator")
			continue


"""ООП калькулятор со счетчиком вызовов функций"""


class BackendLogCalc:
	__add_cnt = 0
	__sub_cnt = 0
	__mul_cnt = 0
	__div_cnt = 0

	@classmethod
	def addition(cls, l, r):
		cls.__add_cnt +=1
		if not(isinstance(l, (int, float)) and isinstance(r, (int, float))):
			raise TypeError('l or r must be int or float')
		print("add counter ->", cls.__add_cnt)
		return l+r


	@classmethod
	def substraction(cls, l, r):
		cls.__sub_cnt += 1
		if not (isinstance(l, (int, float)) and isinstance(r, (int, float))):
			raise TypeError('l or r must be int or float')
		print("sub counter ->",cls.__sub_cnt)
		return l - r

	@classmethod
	def multiplication(cls, l, r):
		cls.__mul_cnt += 1
		if not (isinstance(l, (int, float)) and isinstance(r, (int, float))):
			raise TypeError('l or r must be int or float')
		print("mul counter ->", cls.__mul_cnt)
		return l * r



	@classmethod
	def division(cls, l, r):
		cls.__div_cnt += 1
		if not (isinstance(l, (int, float)) and isinstance(r, (int, float))):
			raise TypeError('l or r must be int or float')
		print("div counter ->", cls.__div_cnt)
		return l / r


class SimpleCalcLogFrontend:
	@staticmethod
	def execute():
		while True:
			s = input('Input an expression and press Enter ->')
			if s == "exit":
				break
			l = s.split()
			if len(l) != 3:
				print("equation must consist of 2 numbers and 1 operator")
				continue
			a, op, b = l
			try:
				a = int(a)
				b = int(b)
			except TypeError('a or b must be int or float'):
				a = float(a)
				b = float(b)

			if op == '+':
				print(BackendLogCalc.addition(a, b))
				continue
			if op == '-':
				print(BackendLogCalc.substraction(a, b))
				continue
			if op == '*':
				print(BackendLogCalc.multiplication(a, b))
				continue
			if op == '/':
				print(BackendLogCalc.division(a, b))
				continue
			else:
				print("Incorrect operator")
			continue


"""ООП калькулятор  со счетчиком вызовов функций для типа фронтенда"""


class BackendLogTypeCalc:
	__add_cnt = {}
	__sub_cnt = {}
	__mul_cnt = {}
	__div_cnt = {}

	@classmethod
	def addition (cls, frontend,  l, r):
		try:
			cls.__add_cnt[frontend] += 1
		except:
			cls.__add_cnt[frontend] = 1
		if not(isinstance(l,(int, float)) and isinstance(r,(int, float))):
			raise TypeError ('l or r must be int or float')
		print(f" {frontend} add counter ->", cls.__add_cnt[frontend])
		return l+r


	@classmethod
	def substraction(cls, frontend, l, r):
		try:
			cls.__sub_cnt[frontend] += 1
		except:
			cls.__sub_cnt[frontend] = 1
		if not (isinstance(l, (int, float)) and isinstance(r, (int, float))):
			raise TypeError('l or r must be int or float')
		print(f" {frontend} sub counter ->", cls.__sub_cnt[frontend])
		return l - r

	@classmethod
	def multiplication(cls, frontend, l, r):
		try:
			cls.__mul_cnt[frontend] += 1
		except:
			cls.__mul_cnt[frontend] = 1
		if not (isinstance(l, (int, float)) and isinstance(r, (int, float))):
			raise TypeError('l or r must be int or float')
		print(f" {frontend} mul counter ->", cls.__mul_cnt[frontend])
		return l * r



	@classmethod
	def division(cls, frontend, l, r):
		try:
			cls.__div_cnt[frontend] += 1
		except:
			cls.__div_cnt[frontend] = 1
		if not (isinstance(l, (int, float)) and isinstance(r, (int, float))):
			raise TypeError('l or r must be int or float')
		print(f" {frontend} div counter ->", cls.__div_cnt[frontend])
		return l / r


class SimpleCalcLogTypeFrontendOne:
	name = "FrontendOne"
	@classmethod
	def execute(cls):
		while True:
			s = input('Input an expression and press Enter ->')
			if s == "exit":
				break
			l = s.split()
			if len(l) != 3:
				print("equation must consist of 2 numbers and 1 operator")
				continue
			a, op, b = l
			try:
				a = int(a)
				b = int(b)
			except TypeError('a or b must be int or float'):
				a = float(a)
				b = float(b)

			if op == '+':
				print(BackendLogTypeCalc.addition(cls.name, a, b))
				continue
			if op == '-':
				print(BackendLogTypeCalc.substraction(cls.name, a, b))
				continue
			if op == '*':
				print(BackendLogTypeCalc.multiplication(cls.name, a, b))
				continue
			if op == '/':
				print(BackendLogTypeCalc.division(cls.name, a, b))
				continue
			else:
				print("Incorrect operator")
			continue


class SimpleCalcLogTypeFrontendTwo:
	name = "FrontendTwo"
	@classmethod
	def execute(cls):
		while True:
			s = input('Input an expression and press Enter ->')
			if s == "exit":
				break
			l = s.split()
			if len(l) != 3:
				print("equation must consist of 2 numbers and 1 operator")
				continue
			a, op, b = l
			try:
				a = int(a)
				b = int(b)
			except TypeError('a or b must be int or float'):
				a = float(a)
				b = float(b)

			if op == '+':
				print(BackendLogTypeCalc.addition(cls.name, a, b))
				continue
			if op == '-':
				print(BackendLogTypeCalc.substraction(cls.name, a, b))
				continue
			if op == '*':
				print(BackendLogTypeCalc.multiplication(cls.name, a, b))
				continue
			if op == '/':
				print(BackendLogTypeCalc.division(cls.name, a, b))
				continue
			else:
				print("Incorrect operator")
			continue


"""ООП калькулятор со счетчиком вызовов функций для  каждого типа и для каждого экземпляра фронтенда"""


class FlexibleBackend:
	__add_cnt = {}
	__sub_cnt = {}
	__mul_cnt = {}
	__div_cnt = {}

	@classmethod
	def addition(cls, frontend,  l, r):
		try:
			cls.__add_cnt[frontend] += 1
		except:
			cls.__add_cnt[frontend] = 1
		if not(isinstance(l, (int, float)) and isinstance(r, (int, float))):
			raise TypeError('l or r must be int or float')
		print(f"'{frontend}' add counter ->", cls.__add_cnt[frontend])
		return l+r

	@classmethod
	def substraction(cls, frontend, l, r):
		try:
			cls.__sub_cnt[frontend] += 1
		except:
			cls.__sub_cnt[frontend] = 1
		if not (isinstance(l, (int, float)) and isinstance(r, (int, float))):
			raise TypeError('l or r must be int or float')
		print(f"{frontend} sub counter ->", cls.__sub_cnt[frontend])
		return l - r

	@classmethod
	def multiplication(cls, frontend, l, r):
		try:
			cls.__mul_cnt[frontend] += 1
		except:
			cls.__mul_cnt[frontend] = 1
		if not (isinstance(l, (int, float)) and isinstance(r, (int, float))):
			raise TypeError('l or r must be int or float')
		print(f"'{frontend}' mul counter ->", cls.__mul_cnt[frontend])
		return l * r

	@classmethod
	def division(cls, frontend, l, r):
		try:
			cls.__div_cnt[frontend] += 1
		except:
			cls.__div_cnt[frontend] = 1
		if not (isinstance(l, (int, float)) and isinstance(r, (int, float))):
			raise TypeError('l or r must be int or float')
		print(f"{frontend} div counter ->", cls.__div_cnt[frontend])
		return l / r


class FlexibleFrontendOne:

	def __init__(self, name):
		self.name = name

	def execute(self):
		while True:
			s = input('Input an expression and press Enter ->')
			if s == "exit":
				break
			l = s.split()
			if len(l) != 3:
				print("equation must consist of 2 numbers and 1 operator")
				continue
			a, op, b = l
			try:
				a = int(a)
				b = int(b)
			except TypeError('a or b must be int or float'):
				a = float(a)
				b = float(b)

			if op == '+':
				print(" ClassName is:", self.__class__)
				print(" Result =", BackendLogTypeCalc.addition(self.name, a, b))
				continue
			if op == '-':
				print(" ClassName is:", self.__class__)
				print(" Result =", BackendLogTypeCalc.substraction(self.name, a, b))
				continue
			if op == '*':
				print(" ClassName is:", self.__class__)
				print(" Result =", BackendLogTypeCalc.multiplication(self.name, a, b))
			if op == '/':
				print(" ClassName is:", self.__class__)
				print(" Result =", BackendLogTypeCalc.division(self.name, a, b))
			else:
				print("Incorrect operator")
			continue


b = FlexibleFrontendOne('B')
c = FlexibleFrontendOne('C')

b.execute()
c.execute()



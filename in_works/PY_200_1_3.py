class FrontendCalc:
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    @staticmethod
    def get_num():
        num_1 = int(input('Enter first number: '))
        num_2 = int(input('Enter second number: '))
        if not (isinstance(num_1, (int, float)) and isinstance(num_2, (int, float))):
            raise TypeError("num_1 and num_2 must be float")
        return num_1, num_2

    @staticmethod
    def get_operator():
        operator = input("Enter operator (+, -, *, /): ")
        return operator

    @classmethod
    def calc(cls):
        num_1, num_2 = cls.get_num()
        operator = cls.get_operator()
        if operator == '+':
            print(BackendCalc.test_add(cls, num_1, num_2))
        elif operator == '-':
            print(BackendCalc.test_sub(num_1, cls, num_2))
        elif operator == '*':
            print(BackendCalc.test_mul(num_1, cls, num_2))
        elif operator == '/':
            print(BackendCalc.test_div(num_1, cls, num_2))


class BackendCalc:
    frontends = {}

    def __init__(self, num_1, num_2):
        super().__init__(num_1, num_2)

    @classmethod
    def test_add(cls, frontend_type, num_1, num_2):
        try:
            cls.frontends[frontend_type] += 1
        except:
            cls.frontends[frontend_type] = 1
        if not (isinstance(num_1, (int, float)) and isinstance(num_2, (int, float))):
            raise TypeError("num_1 and num_2 must be float")
        return num_1 + num_2

    @classmethod
    def test_sub(cls, num_1, num_2, frontend_type):
        try:
            cls.frontends[frontend_type] += 1
        except:
            cls.frontends[frontend_type] = 1
        if not (isinstance(num_1, (int, float)) and isinstance(num_2, (int, float))):
            raise TypeError("num_1 and num_2 must be float")
        return num_1 - num_2

    @classmethod
    def test_mul(cls, num_1, num_2, frontend_type):
        try:
            cls.frontends[frontend_type] += 1
        except:
            cls.frontends[frontend_type] = 1
        if not (isinstance(num_1, (int, float)) and isinstance(num_2, (int, float))):
            raise TypeError("num_1 and num_2 must be float")
        return num_1 * num_2

    @classmethod
    def test_div(cls, num_1, num_2, frontend_type):
        try:
            cls.frontends[frontend_type] += 1
        except:
            cls.frontends[frontend_type] = 1
        if not (isinstance(num_1, (int, float)) and isinstance(num_2, (int, float))):
            raise TypeError("num_1 and num_2 must be float")
        return num_1 // num_2

act = FrontendCalc


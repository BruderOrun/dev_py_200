class FrontendCalc:
    def __init__(self, A, B):
        self.A = A
        self.B = B

    @staticmethod
    def get_num():
        A = int(input('Enter first number: '))
        B = int(input('Enter second number: '))
        if not (isinstance(A, (int, float)) and isinstance(B, (int, float))):
            raise TypeError("A and B must be float")
        return A, B

    @staticmethod
    def get_operator():
        operator = input("Enter operator (+, -, *, /): ")
        return operator

    @classmethod
    def calc(cls):
        A, B = cls.get_num()
        operator = cls.get_operator()
        if operator == '+':
            print(BackendCalc.test_add(cls, A, B))
        elif operator == '-':
            print(BackendCalc.test_sub(A, cls, B))
        elif operator == '*':
            print(BackendCalc.test_mul(A, cls, B))
        elif operator == '/':
            print(BackendCalc.test_div(A, cls, B))


class BackendCalc:
    frontends = {}

    def __init__(self, A, B):
        super().__init__(A, B)

    @classmethod
    def test_add(cls, frontend_type, A, B):
        try:
            cls.frontends[frontend_type] += 1
        except:
            cls.frontends[frontend_type] = 1
        if not (isinstance(A, (int, float)) and isinstance(B, (int, float))):
            raise TypeError("A and B must be float")
        return A + B

    @classmethod
    def test_sub(cls, A, B, frontend_type):
        try:
            cls.frontends[frontend_type] += 1
        except:
            cls.frontends[frontend_type] = 1
        if not (isinstance(A, (int, float)) and isinstance(B, (int, float))):
            raise TypeError("A and B must be float")
        return A - B

    @classmethod
    def test_mul(cls, A, B, frontend_type):
        try:
            cls.frontends[frontend_type] += 1
        except:
            cls.frontends[frontend_type] = 1
        if not (isinstance(A, (int, float)) and isinstance(B, (int, float))):
            raise TypeError("A and B must be float")
        return A * B

    @classmethod
    def test_div(cls, A, B, frontend_type):
        try:
            cls.frontends[frontend_type] += 1
        except:
            cls.frontends[frontend_type] = 1
        if not (isinstance(A, (int, float)) and isinstance(B, (int, float))):
            raise TypeError("A and B must be float")
        return A // B

act = FrontendCalc


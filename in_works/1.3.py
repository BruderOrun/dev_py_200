def calculator():
    ops = {'+': lambda l, r: l + r, '_': lambda l, r: l - r}
    while True:
        s = input('Input ->')
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


class Frontend:
    def __init__(self, name, backend):
        self.backend = backend
        self.name = name

    @staticmethod
    def execute(backend):
        while True:
            exp = input('Enter number operator number')
            if exp == 'exit':
                break
            num = exp.split()
            if 3 != len(num):
                print('Expression have: element operator element')
                continue
            A, op, B = num
            try:
                A = int(A)
                B = int(B)
            except TypeError('A or B must be int or float'):
                A = float(A)
                B = float(B)

            if op == '+':
                print(backend.test_add(A, B))
            elif op == '-':
                print(backend.test_sub(A, B))
            elif op == '*':
                print(backend.test_mul(A, B))
            elif op == '/':
                print(backend.test_div(A, B))


class Backend:
    frontends = {}

    @staticmethod
    def staticmethod(frontends=None):
        return frontends

    def __init__(self, A, B):
        super().__init__(A, B)

    def test_add(self, frontend_type, A, B):
        try:
            self.frontends[frontend_type] += 1
        except TypeError('A or B must be int or float'):
            self.frontends[frontend_type] = 1
        if not (isinstance(A, (int, float)) and isinstance(B, (int, float))):
            raise TypeError("A and B must be float")

        return A + B

    def test_sub(self, A, B, frontend_type):
        try:
            self.frontends[frontend_type] += 1
        except TypeError('A or B must be int or float'):
            self.frontends[frontend_type] = 1
        if not (isinstance(A, (int, float)) and isinstance(B, (int, float))):
            raise TypeError("A and B  float")
        return A - B

    def test_mul(self, A, B, frontend_type):
        try:
            self.frontends[frontend_type] += 1
        except TypeError('A or B float'):
            self.frontends[frontend_type] = 1
        if not (isinstance(A, (int, float)) and isinstance(B, (int, float))):
            raise TypeError("A and B float")
        return A * B

    def test_div(self, A, B, frontend_type):
        try:
            self.frontends[frontend_type] += 1
        except TypeError('A or B float'):
            self.frontends[frontend_type] = 1
        if not (isinstance(A, (int, float)) and isinstance(B, (int, float))):
            raise TypeError("A and B float")
        return A // B
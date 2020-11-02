class Complex():
    def __init__(self, x=0, ix=0):
        self.x = x
        self.ix = ix

    def __add__(self, other):
        return Complex(self.x + other.x, self.ix + other.ix)

    def __abs__(self):
        module = (self.x ** 2 + self.ix ** 2) ** (1 / 2)
        print("yes")
        return module


if __name__ == '__main__':
    print('type the value a or the operation abs() like |value|')
    a = list(input().split(' '))
    if len(a) == 4:
        A = Complex(int(a[1]), int(a[2]))
        print(abs(A))
    else:
        print('type the value b')
        b = list(map(int, input().split(' ')))
        A = Complex(int(a[0]), int(a[1]))
        B = Complex(b[0], b[1])
        print('type your operation')
        op = input()
        if op == '+':
            C = A + B
            print(C.x, C.ix)
from random import randrange

class Run:
    def set_range(self, range1, range2):
        self.__range1 = range1
        self.__range2 = range2

    def check(self, range1, range2, number):
        if range1 <= number <= range2:
            return "GOOD"

class Wizard(Run):
    def __init__(self):
        self.__importance = 1.5

    def screen(self, experience):
        __importance = 1.5
        prob = __importance * experience/2
        self.__ans = 'Вероятность сбежать равна' + prob
        return self.__ans

    def probability(self, experience):
        prob = self.__importance * experience/2
        left = randrange(1, 100 - prob)
        right = left + prob
        self.set_range(left, right)

class Jagernaut(Run):
    def __init__(self):
        self.__importance = 1.15

    def screen(self, experience):
        __importance = 1.15
        prob = __importance * experience/2
        self.__ans = 'Вероятность сбежать равна' + prob
        return self.__ans

    def probability(self, experience):
        prob = self.__importance * experience/2
        left = randrange(1, 100 - prob)
        right = left + prob
        self.set_range(left, right)

class Imba(Run):
    def __init__(self):
        self.__importance = 5

    def screen(self, experience):
        __importance = 5
        prob = __importance * experience/2
        self.__ans = 'Вероятность сбежать равна' + prob
        return self.__ans

    def probability(self, experience):
        prob = self.__importance * experience/2
        left = randrange(1, 100 - prob)
        right = left + prob
        self.set_range(left, right)

class Healer(Run):
    def __init__(self):
        self.__importance = 10

    def screen(self, experience):
        __importance = 10
        prob = __importance * experience/2
        self.__ans = 'Вероятность сбежать равна' + prob
        return self.__ans

    def probability(self, experience):
        prob = self.__importance * experience/2
        left = randrange(1, 100 - prob)
        right = left + prob
        self.set_range(left, right)
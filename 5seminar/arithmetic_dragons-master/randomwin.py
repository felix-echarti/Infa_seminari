from hero import *
from random import randint


class Random(Hero):

    def check(self, exp):
        randomnum = randint(1, 100)
        if randomnum <= exp:
            p = 1
        else:
            p = -1
        return p > 0
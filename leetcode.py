"""
@author : rabbit
@Date : 2022/3/9  18:10
"""
import random


def program():
    i = 10
    while i > 0:
        a = random.randint(0, 100)
        x = random.randint(0, 1)
        if x == 0:
            b = random.randint(0, 100 - a)
            print("%s+%s=%s" % (a, b, a + b))
            i -= 1
        else:
            b = random.randint(0, a)
            print("%s-%s=%s" % (a, b, a - b))
            i -= 1


program()

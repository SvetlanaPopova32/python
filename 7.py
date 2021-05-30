from itertools import count
from math import factorial

def fact():
    for i in range(1, 5):
        yield factorial(i)


for i in fact():
    print(i)


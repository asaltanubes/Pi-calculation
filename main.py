import random
from numba import njit
import math
from os import system


precision = 10000000
total = 0
coprimes = 0

@njit(fastmath = True)
def coprime(a, b):
    if b>a:
        a, b = b, a
    r = a % b
    if r == 0:
        return b
    else:
        return coprime(b, r)

@njit(fastmath = True)
def pi_from_data(total, coprimes):
    return math.sqrt(6*total/coprimes)

def main():
    global precision, total, coprimes
    while True:
        for i in range(10000):
            numbs = [random.randrange(1, precision) for i in range(2)]
            a = coprime(*numbs)
            if a == 1:
                coprimes += 1
            total += 1
        system('cls')
        PIE = pi_from_data(total, coprimes)
        print(PIE)
main()

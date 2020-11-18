import random
from typing import Callable
import time
from matplotlib import pyplot as plt


def timed(f, *args, n_iter=100):
    acc = float("inf")
    for i in range(n_iter):
        t0 = time.perf_counter()
        f(*args)
        t1 = time.perf_counter()
        acc = min(acc, t1 - t0)
    return acc

def test(gcd: Callable, n_iter: int = 100):
    for i in range(n_iter):
        c = random.randint(0, 1024)
        a = c * random.randint(0, 128)
        b = c * random.randint(0, 128)
        assert gcd(a, a) == gcd(a, 0) == a
        assert gcd(b, b) == gcd(b, 0) == b
        assert gcd(a, 1) == gcd(b, 1) == 1
        d = gcd(a, b)
        assert a % d == b % d == 0


def gcd1(a: int, b: int):
    assert a >= 0 and b >= 0
    for d in reversed(range(max(a, b) + 1)):
        if d == 0 or a % d == 0 and b % d == 0:
            return d


def gcd2(a: int, b: int):
    while a and b:
        if a >= b:
            a %= b
        else:
            b %= a
    return max(a, b)

# calls = []
# for a in range(0, 10000):
#     calls.append(timed(gcd1, a, a))

plt.plot(range(0, 10000), [timed(gcd1, 13, a) for a in range(0, 10000)])
plt.plot(range(0, 10000), [timed(gcd2, 13, a) for a in range(0, 10000)])
plt.savefig('gcd.png')


#def f(a, b):
#    pass

#print([timed(gcd1, a, b) for a in range(0, 100) for b in range(0, 100)])
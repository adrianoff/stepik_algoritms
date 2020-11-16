def fib1(n: int):
    assert n >= 0
    return n if n <= 1 else fib1(n -1) + fib1(n - 2)

#print(fib1(20))


cache = {}
def fib2(n: int):
    assert n >= 0
    if n not in cache:
        cache[n] = n if n <= 1 else fib2(n - 1) + fib2(n - 2)
    return cache[n]


#print(fib2(800))

def fib3(n: int):
    assert n >= 0
    f0, f1 = 0, 1
    for i in range(n - 1):
        f0, f1 = f1, f0 + f1
    return f1

#print(fib3(8000))

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

#cache = {}
#plt.plot(range(0, 100), [timed(fib3, arg) for arg in range(0, 100)])
#cache = {}
#plt.plot(range(0, 10000), [timed(fib2, arg) for arg in range(0, 10000)])
#plt.savefig('foo.png')

a = [timed(fib3, arg) for arg in range(0, 1000)]
b = [timed(fib2, arg) for arg in range(0, 1000)]

print('{:.20f}'.format(a[-1]))
print('{:.20f}'.format(b[-1]))
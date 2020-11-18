import random
from typing import Callable
import time
from matplotlib import pyplot as plt


def timed(f, *args, n_iter=1):
    acc = float("inf")
    print(len(*args))
    for i in range(n_iter):
        t0 = time.perf_counter()
        f(*args)
        t1 = time.perf_counter()
        acc = min(acc, t1 - t0)
    return acc


def sort1(list_for_sort):
    return sorted(list_for_sort)


k = 10000
plt.plot(range(0, k), [timed(sort1, [random.randint(1, 10000) for _ in range(n)]) for n in range(0, k)])
plt.savefig('sort.png')
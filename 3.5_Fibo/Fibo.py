def fib1(n: int):
    assert n >= 0
    return n if n <= 1 else fib1(n -1) + fib1(n - 2)

print(fib1(20))
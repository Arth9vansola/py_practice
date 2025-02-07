from functools import lru_cache

@lru_cache(None)

def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n-1) + fib(n - 2)
c = int(input())
for i in range(c+1):
    print(fib(i),end=",")

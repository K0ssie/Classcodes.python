# def fibonacci(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     elif n > 2:
#         return fibonacci(n-1) + fibonacci(n-2)

# for i in range(1, 15):
#     print(i , ":", fibonacci(i))

# cache = {}

# value = 0

# def fibonacci2(n):
#     if n in cache:
#         return cache[n]
#     if n == 1 or n == 2:
#         value = 1
#     elif n > 2:
#         value = fibonacci2(n-1) + fibonacci2(n-2)
#         cache[n] = value
#         return value

# for i in range(1, 11):
#     print(f"{i} Term: {fibonacci2(i)}")


from functools import lru_cache

# LRU cache memoization
@lru_cache(maxsize=2000)
def fib3(n):
    if n < 1:
        return 0
    elif n == 1 or n == 2:
        return 1
    return fib3(n - 1) + fib3(n - 2)

# Print first 20 Fibonacci numbers
for i in range(1, 10000):
    print(f"{i} Term: {fib3(i)}")
from functools import wraps
from datetime import datetime

try:
    from functools import lru_cache
except ImportError:
    def lru_cache(user_function):
        cache = {}

        @wraps(user_function)
        def wrapper(*args):
            key = tuple(args)
            if key not in cache:
                cache[key] = user_function(*args)
            return cache[key]

        return wrapper


def fib(n):
    if n in (1, 2):
        return 1
    else:
        return fib(n - 2) + fib(n - 1)


@lru_cache
def fib2(n):
    if n in (1, 2):
        return 1
    else:
        return fib2(n - 2) + fib2(n - 1)


def time_fn(fn, *args):

    s = datetime.now()
    print(fn(*args))

    e = datetime.now()
    print(e - s)


time_fn(fib, 15)
time_fn(fib2, 15)

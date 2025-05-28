from time import perf_counter

def fibonacci(n: int) -> int:
    t1_start = perf_counter()
    if n < 2:
        return n
    t1_stop = perf_counter()
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(30))

if __name__ == '__main__':
    assert fibonacci
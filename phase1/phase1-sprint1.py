# import random
from functools import reduce

# rand_list = [random.randint(-100, 100) for _ in range(15)]
# print(rand_list)

def double_list(xs: list[int]) -> list[int]:
    return list(map(lambda x: x * 2, xs))

# stringer = "I am actually so HUNGRY, why has no one COOKED yet, I think I could eat New York."

def capitals_list(listing: list) -> list:
    assert len(listing) > 0
    m = []
    for i in listing:
        if i.isupper():
            m.append(i)
    return(m)

# optimisation
def extract_uppercase(s: str) -> list[str]:
    return list(filter(str.isupper, s))

def facty(n: int) -> int:
    assert n >= 0
    list_n = list(range(1, n+1))
    fact = reduce(lambda x, y: x * y, list_n)
    return fact

# optimisation
def factorial(n: int) -> int:
    assert n >= 0
    return reduce(lambda x, y: x * y, range(1, n + 1), 1)


if __name__ == "__main__":
    assert factorial(0) == 1
    assert factorial(5) == 120
    assert double_list([1, -2, 3]) == [2, -4, 6]
    assert extract_uppercase("PyTHon") == ["P", "T", "H"]

    import time
    start = time.perf_counter()
    double_list(list(range(10_000)))
    elapsed_ms = (time.perf_counter() - start) * 1_000
    print(f"double_list on 10k elements: {elapsed_ms:.2f} ms")
    assert elapsed_ms < 100, f"Took too long: {elapsed_ms:.2f} ms"

from math import factorial


def combinasiya(n: int, k: int) -> int:
    if n < k or k < 0:
        raise ValueError("Xahis olunur musbt ededler daxil edin")
    return int(factorial(n) / ((factorial(k)) * (factorial(n - k))))

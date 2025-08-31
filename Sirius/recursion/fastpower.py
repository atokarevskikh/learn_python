def FastPower(x: float, n: int) -> float:
    if n == 0:
        return 1.0
    elif n == 1:
        return x
    elif n % 2 == 1:
        return FastPower(x, n - 1) * x
    else:
        y = FastPower(x, n // 2)
        return y * y


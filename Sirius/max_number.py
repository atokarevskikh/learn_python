def max_number(x :int, y :int) -> int:
    """Возвращает максимальное из двух чисел."""
    z = ((x - y) ** 2) ** 0.5
    a = (x + y + z) / 2
    return int(a)

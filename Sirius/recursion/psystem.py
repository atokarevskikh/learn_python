def ToPSystem(x: int, y: int, p: int, a: str) -> str:
    if x == 0 or x == 1:
        return str(x) + a
    if y > x:
        return a
    z = y * p
    d = x % z // y
    a = str(d) + a
    return ToPSystem(x, z, p, a)


    

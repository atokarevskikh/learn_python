def CaesarCipherChar(c: str, k: int) -> str:
    a = ord(c)
    if 65 <= a <= 90:
        a = a - 65
        a = ((a + k) % 26) + 65
    elif 97 <= a <= 122:
        a = a - 97
        a = ((a + k) % 26) + 97
    return chr(a)


def CaesarCipher(s: str, k:int) -> str:
    res = []
    for c in s:
        res.append(CaesarCipherChar(c, k))
    return ''.join(res)




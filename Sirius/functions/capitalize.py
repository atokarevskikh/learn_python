def Capitalize(S: str) -> str:
    """Изменяет регистр символов в строке так,
    чтобы первая буква каждого слова была заглавной,
    а остальные буквы — строчными."""
    isPrevAlpha = False
    res = []
    for ch in S:
        if not ch.isalpha():
            res.append(ch.upper())
        elif not isPrevAlpha:
            res.append(ch.upper())
        else:
            res.append(ch.lower())
        isPrevAlpha = ch.isalpha()
    return ''.join(res)

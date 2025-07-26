

def search4vowels(phrase:str) -> set:
    """Возвращает множество глассных, найденных в указанном слове или фразе"""
    vowels = set('aeoiu')
    return vowels.intersection(set(phrase.casefold()))


def search4letters(phrase:str, letters:str = 'aeoiu') -> set:
    """Возвращает множество букв (без учёта регистра),
       найденных в переданной фразе."""
    return set(letters.casefold()).intersection(set(phrase.casefold()))


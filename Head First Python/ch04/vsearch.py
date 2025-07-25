def search4vowels(phrase:str) -> set:
    """Возвращает множество глассных, найденных в указанном слове или фразе"""
    vowels = set('aeoiu')
    return vowels.intersection(set(phrase.casefold()))


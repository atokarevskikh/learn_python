def CaseChange(c: str) -> str:
    """Меняет регистр латинских символов."""
    if 'A' <= c <= 'Z':
        return chr(ord(c) + ord('a') - ord('A'))
    elif 'a' <= c <= 'z':
        return chr(ord(c) - ord('a') + ord('A'))
    else:
        return c

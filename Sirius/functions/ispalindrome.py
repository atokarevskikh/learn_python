def IsPalindrome(S: str) -> bool:
    a = S.upper()
    b = [c for c in a]
    b.reverse()
    c = ''.join(b)
    if a == c:
        return True
    else:
        return False


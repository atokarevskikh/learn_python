def PrintReverse():
    c = input()
    if c == '0':
        print(c)
        return
    PrintReverse()
    print(c)
    return

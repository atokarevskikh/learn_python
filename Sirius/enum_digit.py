x = 1122334455
for n in range(10):
    print(x // (10 ** n) % 10)
y = x
for n in range(10):
    print(y % 10)
    y = y // 10

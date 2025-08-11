n = int(input())
m = 2000000001
i = 1
fib = 1
prev = 0
res = -1
while fib < m:
    fib, prev = fib + prev, fib
    i += 1
    if fib == n:
        res = i
        break
print(res)

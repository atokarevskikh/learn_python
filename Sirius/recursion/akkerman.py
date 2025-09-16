import sys
sys.setrecursionlimit(100000)

def Akkerman(m: int, n: int) -> int:
    if m == 0:
        return n + 1
    elif n == 0:
        return Akkerman(m - 1, 1)
    else:
        return Akkerman(m - 1, Akkerman(m, n - 1))


(m, n) = [int(k) for k in input().split()]
res = Akkerman(m, n)
print(res)

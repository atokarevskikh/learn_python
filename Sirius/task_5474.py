a = int(input())
b = int(input())
c = int(input())
d = int(input())
for n in range((a - c + d - 1) // d * d + c, b + 1, d):
    print(n)

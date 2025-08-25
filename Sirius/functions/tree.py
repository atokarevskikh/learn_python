def makeLevel(n):
    for i in range(1, n + 2):
        print('*' * i)


def tree(n):
    for i in range(1, n + 1):
        makeLevel(i)

n = int(input())
tree(n)

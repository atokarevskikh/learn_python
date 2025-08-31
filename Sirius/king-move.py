a = input()
b = input()
ver = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
x = abs(ver.index(a[0]) - ver.index(b[0]))
y = abs(int(a[1]) - int(b[1]))
if  x == 0 and y == 0:
    print('NO')
elif x > 1 or y > 1:
    print('NO')
else:
    print('YES')


       

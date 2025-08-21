n = int(input())
A = [[(int)((j - i) > 0 and int((j + i - n + 1) < 0)) +
  2 * (int)((j - i) > 0 and int((j + i - n + 1) > 0)) +
  3 * (int)((j - i) < 0 and int((j + i - n + 1) > 0)) +
  4 * (int)((j - i) < 0 and int((j + i - n + 1) < 0)) 
  for j in range(n)] 
  for i in range(n)]
for i in range(n):
    for j in range(n):
        print(A[i][j], end = ' ')
    print()

s = input()
letters = []
counts = []
maxcnt = 0
for ch in s:
    if ch.isalpha():
        ch = ch.upper()
        if letters.count(ch) == 0:
            letters.append(ch)
            counts.append(1)
            if maxcnt < 1:
                maxcnt = 1
        else:
            i = letters.index(ch)
            counts[i] += 1
            if maxcnt < counts[i]:
                maxcnt = counts[i]
res = []
for i in range(len(letters)):
    if counts[i] == maxcnt:
        res.append(letters[i])
res.sort()
print(''.join(res))
print(maxcnt)


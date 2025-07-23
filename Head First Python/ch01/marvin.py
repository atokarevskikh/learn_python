phrase = 'Marvin, the paranoid android'
letters = list(phrase)
for ch in letters[:6]:
    print('\t', ch)
for ch in letters[12:20]:
    print('\t'*2, ch)
for ch in letters[-7:]:
    print('\t'*3, ch)

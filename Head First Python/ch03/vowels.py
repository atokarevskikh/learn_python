vowels = ["а", "е", "ё", "э", "о", "ы", "ю", "и", "я"]
phrase = (input("Введите фразу на русском языке: ")).casefold()
found = {}
for letter in phrase:
    if letter in vowels:
        found.setdefault(letter, 0)
        found[letter] += 1
print("Всего найдено", len(found), "гласных, а именно:")
for k, v in sorted(found.items()):
    print(f'{k}: {v}')

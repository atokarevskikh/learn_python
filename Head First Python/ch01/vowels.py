vowels = ["а", "е", "ё", "э", "о", "ы", "ю", "и", "я", "А", "Е", "Ё", "Э", "О", "Ы", "Ю", "И", "Я"]
phrase = input("Введите фразу на русском языке: ")
found = []
for letter in phrase:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
print("Всего найдено", len(found), "гласных, а именно:")
for ch in found:
    print(ch)

vowels = set("аеёэоыюиуя")
phrase = (input("Введите фразу на русском языке: ")).casefold()
found = vowels.intersection(set(phrase))
print("Всего найдено", len(found), "гласных, а именно:")
for ch in sorted(found):
    print(ch)

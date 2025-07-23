
for num in range(99, 0, -1):
    if num >= 11 and num <= 19:
        word = "бутылок"
    elif num % 10 == 1:
        word = "бутылка"
    elif num % 10 in (2, 3, 4):
        word = "бутылки"
    else:
        word = "бутылок"
    print(num, word, "пива на стене,")
    print(num, word, "пива.")
    print("Возьми одну.")
    print("Пусти её по кругу.")
    print()
    if num == 1:
        print("Нет бутылок пива на стене.")
        print("Нет бутылок.")
        print("Сходи в магазин, купи ещё.")
        print("99 бутылок пива на стене.")
        print()
    

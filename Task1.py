txt = input("Введите текст через пробел:\n")
print(f"Исходный текст: {txt}")
seek_txt = "абв"
lst = [i for i in txt.split() if seek_txt not in i]
print(f'Полученный текст: {" ".join(lst)}')
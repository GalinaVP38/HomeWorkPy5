# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

txt = input("Введите текст через пробел:\n")
print(f"Исходный текст: {txt}")
seekTxt = "абв"
lst = [i for i in txt.split() if seekTxt not in i]
print(f'Полученный текст: {" ".join(lst)}')
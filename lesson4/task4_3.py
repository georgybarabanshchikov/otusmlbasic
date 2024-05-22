# Написать упрощенную версию алгоритма RLE. Алгоритм RLE объединяет подряд идущие символы в коэффициент и символ.
# Пример:
# aaabbbbccccc -> 2a4b5c
# asssdddsssddd -> 1a3s3d3s3d
# abcba -> 1a1b1c1b1a

userdata = input("Введите строку: ")
result = ''
last_letter = ''
letter_number = 0

for letter in userdata:
    if letter == last_letter:
        letter_number += 1
    else:
        if last_letter != '':
            result += str(letter_number) + last_letter
        last_letter = letter
        letter_number = 1
result += str(letter_number) + last_letter
print(result)

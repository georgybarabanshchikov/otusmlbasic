# Шифр Цезаря. Пользователь вводит строку и ключ шифра, программа должна вывести зашфированную строку (со сдвигом по ключу). Сдвиг циклический. Используем только латинский алфавит, пробелы не шифруются.
# Пример:
# Dog, 2 -> Fqi
# Zak zak -> Cdn cdn
# Python is the BEST -> Udymts nx ymj GJXY
ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
total_letters = 26

user_input = input('Введите строку: ')
shift = int(input('Введите смещение: '))
result = ''

for letter in user_input:
    if letter in ascii_lowercase:
        result += ascii_lowercase[(ascii_lowercase.index(letter)+shift) % 26]
    elif letter in ascii_uppercase:
        result += ascii_uppercase[(ascii_uppercase.index(letter)+shift) % 26]
    else:
        result += letter

print(result)




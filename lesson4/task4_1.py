# Пользователь вводит целое число, программа складывает все цифры числа, с полученым числом - тоже самое и так до тех пор, пока не получится однозначное число.
# Пример:
# 545 -> 5
# 12345 -> 6

number = input('Введите строку: ')

while len(number) > 1:
    sum = 0
    for num in number:
        sum += int(num)
    number = str(sum)
else:
    print(number)

# Пользователь вводит пятизначное число. Программа должна зеркально отразить центральные три цифры. Первая и последняя остаются на местах.
# Пример:
# 23456 -> 25436
# 30789 -> 38709

number = int(input("Введите пятизначное число"))
second_digit = number % 100 // 10
fourth_digit = number % 10000 // 1000
print(number - second_digit * 10 - fourth_digit * 1000 + fourth_digit * 10 + second_digit * 1000)

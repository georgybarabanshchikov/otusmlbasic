# Пользователь вводит данные, проверить - являються ли они положительным вещественным числом.
# Не использовать встроенные функции для проверки, только методы данных и конструкцию IF.
# (Дополнительное задание, по желанию - проверка на отрицательные вещественные числа)
# Пример:
# 5.6 -> True
# .78 -> True
# .67. -> False
# 5 -> True

number = input("Введите число для проверки: ")

result = ((number.count('.') <= 1) and
          (number.count('0') +
           number.count('1') +
           number.count('2') +
           number.count('3') +
           number.count('4') +
           number.count('5') +
           number.count('6') +
           number.count('7') +
           number.count('8') +
           number.count('9') +
           number.count('.')
           == len(number)))
print(result)

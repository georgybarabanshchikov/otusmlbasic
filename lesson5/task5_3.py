# Функция проверки на простое число. Простое число - число, которое имеет всего 2 делителя еденица и оно само.
# Пример:
# 17 -> True
# 20 -> False
# 23 -> True


def check_number(num_for_check):
    for i in range(2, num_for_check // 2):
        if num_for_check % i == 0:
            return False
    else:
        return True



print(check_number(17))
print(check_number(20))
print(check_number(23))

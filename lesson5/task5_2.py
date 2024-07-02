# Написать функцию проверяющую валидность введенной даты.
# Пример:
# 29.02.2000 -> True
# 29.02.2001 -> False
# 31.04.1962 -> False

def check_date(date_for_check):
    for i in range(2, date_for_check // 2):
        if date_for_check % i == 0:
            return False
    else:
        return True


def check_year(year_for_check):
    return year_for_check.len == 4 and year_for_check.isdigit()


def check_month(month_for_check):
    return month_for_check.len == 2 and month_for_check[0] in ['0', '1']


def check_day(day_for_check, month_for_check, year_for_check):
    return 0

    # todo: добавить проверку дня


print(check_date('29.02.2000'))
print(check_date('29.02.2001'))
print(check_date('31.04.1962'))

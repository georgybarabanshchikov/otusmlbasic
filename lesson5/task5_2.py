# Написать функцию проверяющую валидность введенной даты.
# Пример:
# 29.02.2000 -> True
# 29.02.2001 -> False
# 31.04.1962 -> False


def check_year(year_for_check):
    return len(year_for_check) == 4 and year_for_check.isdigit()


def check_month(month_for_check):
    return len(month_for_check) == 2 and month_for_check.isdigit() and int(month_for_check) >= 1 and int(
        month_for_check) <= 12


def check_day(day_for_check, month_for_check, year_for_check):
    return (len(day_for_check) == 2 and day_for_check.isdigit() and int(day_for_check) >= 1) and (
        (int(month_for_check) in [1, 3, 5, 7, 8, 10, 12] and int(day_for_check) <= 31) or
        (int(month_for_check) in [4, 6, 9, 11] and int(day_for_check) <= 30) or
        (int(month_for_check) == 2 and (
            int(year_for_check) % 4 != 0 or (int(year_for_check) % 100 == 0 and int(year_for_check) % 400 != 0))
         and int(day_for_check) <= 28) or
        (int(month_for_check) == 2 and (
            int(year_for_check) % 4 == 0 and (int(year_for_check) % 100 != 0 or int(year_for_check) % 400 == 0)
            and int(day_for_check) <= 29)))


def check_date(dt):

    if (len(dt) != 10) or dt[2] != '.' or dt[5] != '.':
        return False
    return check_year(dt[6:10]) and check_month(dt[3:5]) and check_day(dt[0:2], dt[3:5], dt[6:10])

print(check_date('29.02.2000'))
print(check_date('29.02.2001'))
print(check_date('31.04.1962'))

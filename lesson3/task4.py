# Пользователь вводит целое положительное число, программа должна вернуть строку в виде римского числа
# Пример:
# 3 -> III
# 15 -> XV
# 234 -> CCXXXIV

# IVXLCDM
number = int(input("Введите целое положительное четырехзначное число: "))
result = ''
forthright = number % 10000 // 1000
if forthright == 1:
    result += 'M'
elif forthright == 2:
    result += 'MM'
elif forthright == 3:
    result += 'MMM'
elif forthright == 4:
    result += 'MV'
elif forthright == 5:
    result += 'V'
elif forthright == 6:
    result += 'VM'
elif forthright == 7:
    result += 'VMM'
elif forthright == 8:
    result += 'VMMM'
elif forthright == 9:
    result += 'MX'

thirddigit = number % 1000 // 100
if thirddigit == 1:
    result += 'C'
elif thirddigit == 2:
    result += 'CC'
elif thirddigit == 3:
    result += 'CCC'
elif thirddigit == 4:
    result += 'CD'
elif thirddigit == 5:
    result += 'D'
elif thirddigit == 6:
    result += 'DC'
elif thirddigit == 7:
    result += 'DCC'
elif thirddigit == 8:
    result += 'DCCC'
elif thirddigit == 9:
    result += 'CM'

seconddigit = number % 100 // 10
if seconddigit == 1:
    result += 'X'
elif seconddigit == 2:
    result += 'XX'
elif seconddigit == 3:
    result += 'XXX'
elif seconddigit == 4:
    result += 'XL'
elif seconddigit == 5:
    result += 'L'
elif seconddigit == 6:
    result += 'LX'
elif seconddigit == 7:
    result += 'LXX'
elif seconddigit == 8:
    result += 'LXXX'
elif seconddigit == 9:
    result += 'XC'

firstdigit = number % 10
if firstdigit == 1:
    result += 'I'
elif firstdigit == 2:
    result += 'II'
elif firstdigit == 3:
    result += 'III'
elif firstdigit == 4:
    result += 'IV'
elif firstdigit == 5:
    result += 'V'
elif firstdigit == 6:
    result += 'VI'
elif firstdigit == 7:
    result += 'VII'
elif firstdigit == 8:
    result += 'VIII'
elif firstdigit == 9:
    result += 'IX'

print(result)

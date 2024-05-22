# Табель успеваемости. Пользователь в бесконечном цикле (пока не будет введена пустая строка) вводит строки вида: 'название предмета' 'фамилия ученика' 'оценка'. После окончания ввода программа выводит в консоль Название предмета, далее список учеников и все их оценки в виде таблицы
#
# Математика Иванов 5
# Математика Иванов 4
# Литература Иванов 3
# Математика Петров 5
# Литература Сидоров 3
# Литература Петров 5
# Литература Иванов 4
# Математика Сидоров 3
# Математика Петров 5
#
# Математика
# Иванов 5 4
# Петров 5 5
# Сидоров 3
#
# Литература
# Ивванов 3 4
# Сидоров 3
# Петров 5

result = {}

while True:
    user_input = input("Введите строку вида 'Предмет Фамилия оценка: ")
    if user_input == '':
        break
    splitted = user_input.split(" ")
    if splitted[0] in result:
        if splitted[1] in result[splitted[0]]:
            result[splitted[0]][splitted[1]].append(splitted[2])
        else:
            result[splitted[0]][splitted[1]] = list(splitted[2])
    else:
        result[splitted[0]] = {splitted[1]: list(splitted[2])}

for subj in result.keys():
    print(subj)
    for student in result[subj].keys():
        print(student + " " + " ".join(str(element) for element in result[subj][student]))
    print("")

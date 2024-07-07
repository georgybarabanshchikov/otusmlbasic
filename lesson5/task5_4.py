# Пользователь в бесконечном цикле вводит данные пользователей: имя, затем фамилию, возраст и ID. Ввод продолжается
# до тех пор пока не будет введено пустое поле. Пользователи заносятся в словарь, где ключ это ID пользователя,
# а остальные данные записываются в виде кортежа. Так же программа должна проверять,
# что имя и фамилия состоят только из символов и начинаются с большой буквы,
# если не с большой, то заменяет на большую, возраст должен быть числом от 18 до 60,
# ID - целое число, дополненое до 8 знаков незначащими нолями, ID должен быть уникальным
# Дополнительно написать функцию, которая будет выводить полученный словарь в виде таблицы




def print_out(dict_users):
    print(type(dict_users))
    print("-" * 54)
    print("|       id | firstname       | secondname      | age |")
    for idv, user in dict_users.items():
        print("|", idv, "|", user[0]+" "*(15-len(user[0])), "|", user[1]+" "*(15-len(user[1])), "|", user[2]," |")
    print("-" * 54)


def fix_name(name):
    if not name.isalpha() or len(name) == 0:
        return
    name = name.lower()
    name = name[0].upper() + name[1:]
    return name


def check_age(age):
    if (age.isdigit()) and 18 <= int(age) <= 60:
        return int(age)
    else:
        return


def fix_id(idv):
    if (len(idv) > 8) or (len(idv) == 0) or not idv.isdigit():
        return
    idv = '0' * (8 - len(idv)) + idv
    return idv


def put_into_dict(fname, sname, age, id):
    if fname is not None and sname is not None and age is not None and id is not None:
        if id not in users:
            users[id] = [fname, sname, age]


users = {}

while True:
    fname = input("Input first name: ")
    if fname == '':
        break
    else:
        fname = fix_name(fname)
    sname = fix_name(input("Input second name: "))
    age = check_age(input("Input age: "))
    id = fix_id(input("Input id: "))

    put_into_dict(fname, sname, age, id)

print_out(users)




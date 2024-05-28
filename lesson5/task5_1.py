# Написать функцию, которая будет перводит снейк_кейс в КэмелКейс и наоборот. Функция сама определяет - какой формат ей передали. Можно добавить ключевой аргумент, который будет принудительно возвращать один из форматов.
# Пример:
# otus_course -> OtusCourse
# PythonIsTheBest -> python_is_the_best


def chang_case(input_str):
    if input_str.find('_') == -1:
        return make_snake_case(input_str)
    else:
        return make_camel_case(input_str)


def make_camel_case(input_str):
    result_str = ''
    make_next_upper = True
    for letter in input_str:
        if make_next_upper:
            result_str += letter.capitalize()
            make_next_upper = False
        elif letter == '_':
            make_next_upper = True
        else:
            result_str += letter
    return result_str


def make_snake_case(input_str):
    result_str = ''
    first_letter = True
    for letter in input_str:
        if letter.isupper():
            if not first_letter:
                result_str += '_'
                first_letter = False

            result_str += letter.casefold()
        else:
            result_str += letter
    return result_str


print(chang_case('otus_course'))
print(chang_case('PythonIsTheBest'))

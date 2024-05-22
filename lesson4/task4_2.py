# Кинотеатр. Дан список списков, каждый вложенный список состоит из 1 и 0,
# Количество вложенных списков - количество рядов.
# Пользователь вводит сколько билетов ему требуется.
# Программа должна найти ряд, где можно приобрести нужно количество билетов (места должны быть рядом).
# Если таких рядов несколько то ближайший к экрану (ближайшим считается нулевой ряд). Ели таких мест нет, то вывести False
# Пример:
# [[0,1,1,0], [1, 0, 0, 0], [0,1,0,0]], 2 -> 1
# [[0,1,1,0], [1, 0, 1, 0], [1,1,0,1]], 2 -> False

places = [[0,1,1,0], [1, 0, 1, 0], [1,1,0,1]]
free_seats = 2
print(type(places))

for row in places:
    free_seat_this_row = 0
    result = False
    for seat in row:
        if seat:
            free_seat_this_row = 0
        else:
            free_seat_this_row += 1
        if free_seat_this_row == free_seats:
            result = True
            break
    if result:
        print(places.index(row))
        break
else:
    print(False)

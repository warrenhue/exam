def calc_distance(cmds):
    total = 0.0         # суммирование будет в метрах
    for line in cmds:
        command = line.lower()
        for index_pointer in range(len(command)):
            if command[index_pointer].isdigit(): #наткнулся на цифру
                num_end = index_pointer
                dot = False #точка в этом числе еще не найдена

                while num_end < len(command) and (command[num_end].isdigit() or (command[num_end] == '.' and not dot)): #двигаемся по 1, пока символ - число или символ точка (если точка еще не найдена)
                    if command[num_end] == '.':
                        dot = True #нашли точку ЙОООУ
                    num_end += 1

                number = float(command[index_pointer:num_end]) #когда символ на котором указатель не явл числом, запоми наем позицию указателя как конец числа
                # а это берем срез со строки от начала числа до конца числа и преобразуем во float

                distance_unit = None
                if command[num_end:num_end+2] == 'km':
                    distance_unit = 'km'
                elif command[num_end:num_end+1] == 'm':
                    distance_unit = 'm'
                # после числа стоит km или m = единица измерения

                if distance_unit:
                    if distance_unit == 'km':
                        number *= 1000
                    total += number
                    break # строку проверили, выход из цикла и идем в следующую строку
    return int(total) # переводим в инт чтобы убрать .0 в конце

cmds = [
    "100m to intersection",
    "turn right",
    "straight 300m",
    "enter motorway",
    "straight 5km",
    "exit motorway",
    "500m straight",
    "turn sharp left",
    "continue 100m to destination"
]

print(calc_distance(cmds))
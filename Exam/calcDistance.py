def calc_distance(cmds):
    total = 0.0         # суммирование будет в метрах
    for line in cmds:
        command = line.lower()
        for index_pointer in range(len(command)):
            if command[index_pointer].isdigit():
                num_end = index_pointer
                dot = False

                while num_end < len(command) and (command[num_end].isdigit() or (command[num_end] == '.' and not dot)):
                    if command[num_end] == '.':
                        dot = True
                    num_end += 1

                number = float(command[index_pointer:num_end])

                distance_unit = None
                if command[num_end:num_end+2] == 'km':
                    distance_unit = 'km'
                elif command[num_end:num_end+1] == 'm':
                    distance_unit = 'm'

                if distance_unit:
                    if distance_unit == 'km':
                        number *= 1000
                    total += number
                    break
    return int(total)

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
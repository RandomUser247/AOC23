import csv
from math import prod

FILE_DIR = "../input_files"


def day2():
    game_dict = {}
    with open('%s/advent_game.csv' % FILE_DIR) as adventfile:
        advent_reader = csv.reader(adventfile, delimiter=';')
        for i, line in enumerate(advent_reader, start=1):
            # remove first part of line 
            line = [line[0].split(':')[1]] + line[1:]
            # initialize an entry for max draws in game per colour
            game_dict[i] = {"blue": 0, "red": 0, "green": 0}
            for entry in line:
                for part in entry.split(','):
                    part = part.strip()
                    if part.find("green") != -1:
                        game_dict[i]["green"] = max(int(part.split(' ')[0]), game_dict[i]['green'])
                    if part.find("red") != -1:
                        game_dict[i]["red"] = max(int(part.split(' ')[0]), game_dict[i]["red"])
                    if part.find("blue") != -1:
                        m = max(int(part.split(' ')[0]), game_dict[i]["blue"])
                        game_dict[i]["blue"] = m
    id_sum = 0
    min_set_power = 0
    # part 1 : calculate the sum of valid game IDs
    for key, values in game_dict.items():
        if values["green"] <= 13 and values["red"] <= 12 and values["blue"] <= 14:
            id_sum += key

    # part 2 : add product of minimal needed cubes to the result
        min_set_power += prod(values.values())

    print("part 1: ",id_sum)
    print("part 2: ",min_set_power)

FILE_DIR = "../input_files"

def day6():
    with open("%s/day6Input.txt" % FILE_DIR) as advent_file:
        races = list(zip(*[[int(item.strip()) for item in line.split(" ") if item.strip().isnumeric()] for line in advent_file]))
        advent_file.seek(0)
        time, distance = map(int, [line.replace(" ", "").split(":")[1] for line in advent_file])

    win_prods = 1
    long_race_wins = 0
    for race in races:
        win_dist = [d * (race[0]-d) for d in range(race[0]+1) if (d * (race[0]-d)) > race[1]]
        win_prods *= len(win_dist)

    press_for = time / (1 - distance)
    print(win_prods)
    print(press_for)
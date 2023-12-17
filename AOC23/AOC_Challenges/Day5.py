import re

FILE_DIR = "../input_files"

def day5():
    with open("%s/day5Input.txt" % FILE_DIR) as advent_file:
        seed_pattern = re.compile(r"seeds:(?:\s+\d+)+")
        map_pattern = re.compile(r"map:\n(?:\d+\s+\d+\s+\d+\n)+")
        num_pattern = re.compile(r"(\s+\d+)")
        file_content = advent_file.read()
        seeds = list(map(int, num_pattern.findall(seed_pattern.findall(file_content)[0])))
        maps = [list(map(lambda s: [int(num) for num in s.split()], line.split("\n")[1:-1])) for line in map_pattern.findall(file_content)]
        locations = []
        new_seeds = []
        seeds = [[seeds[x], seeds[x] + seeds[x+1]] for x in range(0, len(seeds)-1, 2)]

        for map_ in maps:
            for dest, source, window in map_:
                start = source
                end = source + window
                move = dest - source
                for seed in seeds:
                    print(start)
                    if seed[0] < start:
                        if seed[1] <= start:
                            new_seeds.append(seed)
                            seed = 0
                            break
                        else:
                            new_seeds.append([seed[0], start])
                            seed[0] = start
                    if start <= seed[0] < end:
                        new_seeds.append([seed[0] + move, min(seed[1], end) + move])
                        if seed[1] <= end:
                            seed = 0
                            break
                        else:
                            seed[0] = end
                    if seed:
                        new_seeds.append(seed)

        print(min(seeds))
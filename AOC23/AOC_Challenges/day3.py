import re

FILE_DIR = "../input_files"


def day3():
    gondola_set = set()
    # regex pattern to find numbers of any length and stars
    num_pattern = re.compile(r'\d+')
    gear_pattern = re.compile(r'\*')
    lines = []
    added_values = 0
    gear_sum = 0
    with open("%s/advent_gondola" % FILE_DIR, mode="r") as gondola_file:
        # fill gondola_set with all special characters
        for line in gondola_file:
            gondola_set.update(list(line.strip()))
        gondola_set = gondola_set - {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.'}
        # create a regex pattern with every special character excluding "."
        special_char_pattern = re.compile('[' + re.escape(''.join(gondola_set)) + ']')
        gondola_file.seek(0)
        # find every special character(with *), number and gear
        for i, line in enumerate(gondola_file):
            spec_matches = special_char_pattern.finditer(line)
            num_matches = num_pattern.finditer(line)
            found_gear_candidates = gear_pattern.finditer(line)
            found_nums = [(int(match.group()), match.start(), match.end()) for match in num_matches]
            found_char = [match.start() for match in spec_matches]
            gear_candidates = [match.start() for match in found_gear_candidates]
            # put them into a list of lines
            lines.append({'index': i, "nums": found_nums, "chars": found_char, "gears": gear_candidates})
    for line in lines:
        idx = line["index"]
        list_range = lines[idx - 1: idx + 2]
        # helper sets of indices of chars and nums of the current, preceding and following line.
        char_range = {index
                      for sublist in list_range
                      for index in sublist['chars']}
        num_range = {index
                      for sublist in list_range
                      for index in sublist['nums']}
        # Part 1: if any number has a special character as a neighbor add it to added_values
        for num in line['nums']:
            num_value, num_start, num_end = num
            for char_index in char_range:
                if num_start -1 <= char_index <= num_end:
                    added_values += num_value
                    break
        # Part 2 : look if any gear has some "number neighbors" if it has two, add the product to gear_sum
        for gear in line["gears"]:
            num_candidates = []
            for num in num_range:
                num_value, num_start, num_end = num
                if num_start -1 <= gear <= num_end:
                    num_candidates.append(num_value)
            if len(num_candidates) == 2:
                gear_sum += num_candidates[0] * num_candidates[1]

    print("Part 1: ", added_values)
    print("Part 2: ", gear_sum)

from itertools import cycle
import math

instruction = ""
network = {}


def part1():
    # just traverse the network via the directions til the node we arrive is "ZZZ"
    # count the steps and return the necessary steps
    steps = 0
    current_loc = "AAA"
    while current_loc != "ZZZ":
        for step in directions:
            if current_loc == "ZZZ":
                break
            current_loc = network[current_loc][step]
            steps += 1
    return steps


def part2():
    # look at cycles from starting nodes, calculate LCM for the cycles in direction
    starting_nodes = [node for node in network if node[2] == "A"]
    cycles = []
    for node in starting_nodes:
        for steps, direc in enumerate(cycle(directions), start=1):
            node = network[node][direc]
            if node[2] == "Z":
                cycles.append(steps)
                break
    return math.lcm(*cycles)


if __name__ == '__main__':
    with open("../input_files/Day8Input.txt") as advent_file:
        # read first line - turn instructions
        instructions = advent_file.readline().strip()
        # skip second line
        advent_file.readline()
        # read rest of the file
        for line in advent_file:
            parts = line.strip().split(" = ")
            network[parts[0]] = parts[1].replace("(", "").replace(")", "").split(", ")
            directions = [1 if direc == "R" else 0 for direc in instructions]



    print("Part 1:", part1())
    print("Part 2:", part2())

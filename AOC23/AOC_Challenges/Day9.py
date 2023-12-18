if __name__ == '__main__':
    next_sum = 0
    prev_sum = 0
    with open("../input_files/Day9Input.txt", "r") as input_file:
        for line in input_file:
            values = [[int(val) for val in line.strip().split()]]
            while any(values[-1]):
                values.append([values[-1][i+1] - values[-1][i] for i in range(len(values[-1])-1)])

            ## extrapolate
            # rotate for easier access
            rotated_values = values[::-1]
            for i in range(len(values)-1):
                lower_last = rotated_values[i][-1]
                upper_last = rotated_values[i+1][-1]
                lower_first = rotated_values[i][0]
                upper_first = rotated_values[i+1][0]
                next_last = lower_last + upper_last
                next_first =  upper_first - lower_first
                # insert values in upper level
                rotated_values[i+1].insert(0, next_first)
                rotated_values[i+1].append(next_last)

            # accumulate the sum of predictions of the previous and next values
            next_sum += rotated_values[-1][-1]
            prev_sum += rotated_values[-1][0]

    print("Part1: ", next_sum)
    print("Part2: ", prev_sum)
FILE_DIR = "../input_files"

def day4():
    winning_sum = 0

    with open("%s/day4Input.txt" % FILE_DIR) as advent_file:
        copy_table = [1] * sum(1 for _ in advent_file)
        advent_file.seek(0)
        for i, line in enumerate(advent_file):

            left, right = line.split(':')[1].split('|')
            left_nums = [int(x.strip()) for x in left.split(' ') if x.strip().isnumeric()]
            right_nums = [int(x.strip()) for x in right.split(' ') if x.strip().isnumeric()]

            for _ in range(copy_table[i]):
                win = 0
                for num in left_nums:
                    if num in right_nums:
                        win += 1
                winning_sum += 0 if win == 0 else 2 ** (win - 1)
                for idx in range(i + 1, i + win + 1):
                    copy_table[idx] += 1
            print(f"{i:<3}| cop:{copy_table[i]:<10} | wins:{win:<4}", range(i + 1, i + win))
    print(winning_sum)
    print(sum(copy_table))
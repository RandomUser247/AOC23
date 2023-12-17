import io
import re
import colorama

FILE_DIR = "./input_files"
String_iterable = list[str] | io.FileIO


def day1(full_output=False):
    colorama.init()

    # replace the inner parts of digit word-substrings with digits, return new list
    def filter_once(strings: String_iterable) -> list[str]:
        digitizer = {
            'one': 'o1e',
            'two': 't2o',
            'three': 't3e',
            'four': 'f4r',
            'five': 'f5e',
            'six': 's6x',
            'seven': 's7n',
            'eight': 'e8t',
            'nine': 'n9e'
        }
        pattern = re.compile(r'|'.join(re.escape(word) for word in digitizer.keys()))
        return [pattern.sub(lambda x: digitizer.get(x.group()), line) for line in strings]

    # prints everything in a nice coloured output
    def print_output() -> None:
        cr = colorama.Fore.RESET
        if full_output:
            for x, y, z, a in zip(advent_list, file_content, nums, more_nums):
                color = colorama.Fore.RED if x != y else ""
                print(color + f"{x[:29]:<30} == {y[:29]:<30}  {a}  {z} " + cr)
        print(f"Code is: {sum(more_nums)}")

    # open and parse file to list of lines
    with open("%s/advent_list.txt" % FILE_DIR, "r") as advent_file:
        file_content = [line.strip() for line in advent_file]

    # part 1
    advent_list = file_content
    nums = [[char for char in line if char.isdigit()] for line in advent_list]
    more_nums = [int(line[0] + line[-1]) for line in nums]
    print_output()

    # part 2
    advent_list = filter_once(filter_once(file_content))
    nums = [[char for char in line if char.isdigit()] for line in advent_list]
    more_nums = [int(line[0] + line[-1]) for line in nums]
    print_output()

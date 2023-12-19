import re
from functools import reduce


# Part One
def check_color(c: str, n: int):
    if n > 15:
        return False
    elif c == "green" and n > 13:
        return False
    elif c == "red" and n > 12:
        return False
    elif c == "blue" and n > 14:
        return False
    else:
        return True


def determine_possible_game(s: list):
    pattern: str = "([0-9]+|red|green|blue)"
    total: int = 0
    for game in s:
        data: list = re.findall(pattern, game)
        for i, x in enumerate(data):
            if x.isalpha():
                check: bool = check_color(x, int(data[i - 1]))
                if check is False:
                    break
                elif len(data) == i + 1 and check is True:
                    total += int(data[0])
    return total


# Part Two
def find_fewest(s: list):
    pattern: str = "([0-9]+|red|green|blue)"
    new_list: list = []
    for game in s:
        color_tracker = ColorTracker()
        data: list = re.findall(pattern, game)
        for i, x in enumerate(data):
            if x.isalpha():
                color_tracker.find_lowest_number(x, int(data[i - 1]))
            if len(data) == i + 1:
                new_list.append(color_tracker.get_highest_number())
    return find_cube_power(new_list)


def find_cube_power(s: list):
    total: int = 0
    for x in s:
        new_list: list = list(x.values())
        total += reduce(lambda x, y: x * y, new_list)
    return total


class ColorTracker:
    def __init__(self):
        self.highest_number = {}

    def find_lowest_number(self, color, number):
        if color not in self.highest_number or number > self.highest_number[color]:
            # print(f"{color} {number}")
            self.highest_number[color] = number

    def get_highest_number(self):
        return self.highest_number


if __name__ == "__main__":
    with open("input.txt") as f, open("test_input_one.txt") as t1:
        data = f.readlines()
        test_one = t1.readlines()

    print(f"First Test Result equals 8: {determine_possible_game(test_one)}")
    print(f"First Puzzle Result: {determine_possible_game(data)}")
    print(f"Second Test Result equals 2286: {find_fewest(test_one)}")
    print(f"Second Puzzle Data Result: {find_fewest(data)}")

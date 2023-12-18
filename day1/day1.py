import re


def find_first_last(s: list):
    num_list: list = [re.sub("[^0-9]", "", x) for x in s]
    total: int = 0
    for num in num_list:
        temp_num = int(num[0] + num[-1])
        total += temp_num
    return total


def find_words_fl(s: list):
    return find_first_last(convert_to_number(s))


def convert_to_number(s: list):
    pattern: str = "(?:one|two|three|four|five|six|seven|eight|nine|zero)"
    result_list: list = []
    number_map = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    for x in s:
        matches = re.sub(pattern, lambda match: number_map[match.group(0)], x)
        result_list.append(matches)
    return result_list


if __name__ == "__main__":
    with open("input.txt") as f, open("testinput.txt") as t1, open("testinput2.txt") as t2:
        data = f.readlines()
        test_data_1 = t1.readlines()
        test_data_2 = t2.readlines()

    print(f"First and Last minus text: {find_first_last(data)}")
    print(f"First and Last minus text Test: {find_first_last(test_data_1)}")
    print(f"First and Last with Text Test: {find_words_fl(test_data_2)}")
    print(f"First and Last with Text: {find_words_fl(data)}")

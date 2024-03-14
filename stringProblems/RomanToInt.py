
def roman_to_int(roman_nums: str) -> str:
    map_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    initial_num = map_dict[roman_nums[len(roman_num) - 1]]
    for i in range(len(roman_nums) - 2, -1, -1):
        if map_dict[roman_nums[i]] < map_dict[roman_nums[i + 1]]:
            initial_num = initial_num - map_dict[roman_nums[i]]
        else:
            initial_num = initial_num + map_dict[roman_nums[i]]
    return initial_num


if __name__ == '__main__':
    roman_num = "MMMCMXCIX"
    parsed_int = roman_to_int(roman_num)
    print(parsed_int)

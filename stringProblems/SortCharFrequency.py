# https://leetcode.com/problems/sort-characters-by-frequency/
from collections import Counter


def frequency_sort(input_str: str) -> str:
    counter = Counter(input_str)
    output_str = ''
    for i in counter.most_common():
        output_str = output_str + i[0] * i[1]

    return output_str


# def frequency_sort_2(input_str: str) -> str:
#     inpt_dict = {}
#     arr_sorted=[]
#     for c in input_str:
#         if c in input_str:
#             inpt_dict[c] += 1
#         else:
#             inpt_dict[c] = 0
#

if __name__ == '__main__':
    text = 'Aaabbbbcccc'
    char_frq_sort = frequency_sort(text)
    print(char_frq_sort)

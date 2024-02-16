import sys
from collections import Counter


def second_most_occur(input_text: str) -> str:
    inpt_dict = {}
    most_common = (None, -sys.maxsize)
    second_most_common = (None, -sys.maxsize)
    for c in input_text:
        if c in inpt_dict:
            inpt_dict[c] += 1
        else:
            inpt_dict[c] = 0

    for elem in inpt_dict:

        if inpt_dict[elem] > most_common[1]:
            second_most_common = most_common
            most_common = (elem, inpt_dict[elem])

        elif second_most[1] < inpt_dict[elem] < most_common[1]:
            second_most_common = (elem, inpt_dict[elem])

    return second_most_common[0]


# Time Complexity : O(n)
# Space : O(n)


def second_most_occur_2(input_text: str) -> str:
    i = 0
    second_most_appr_2 = ''
    k = Counter(text)

    for k in k.most_common():
        if i == 1:
            second_most_appr_2 = k[0]
            break
        i += 1
        continue
    return second_most_appr_2


# time Complexity: O(n)
# Space Complexity:O(1)


if __name__ == '__main__':
    text = 'AAaabbb'
    second_most = second_most_occur_2(text)
    print(second_most)

from collections import Counter


def second_most_occur(input_text: str) -> str:
    inpt_dict = {}

    for c in input_text:
        if c in inpt_dict:
            inpt_dict[c] += 1
        else:
            inpt_dict[c] = 0
    output_array = sorted(inpt_dict.items(), key=lambda x: x[1], reverse=True)

    return (output_array[0])[0]


# Time Complexity : O(n+nlog(n))
# Space : O(2n)


def second_most_occur_2(input_text: str) -> str:
    i = 0
    second_most_appr_2 = ''
    for k in Counter(text):
        if i == 1:
            second_most_appr_2 = k
            break
        i += 1
        continue
    return second_most_appr_2
# time Complexity: O(n)
# Space Complexity:O(1)


if __name__ == '__main__':
    text = 'aabbbbbbccccaac'
    second_most = second_most_occur(text)


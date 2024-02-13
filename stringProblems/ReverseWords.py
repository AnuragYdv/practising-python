def reverse_words(input_str: str) -> str:
    arr = input_str.split()
    return " ".join(arr[::-1])


def reverse_words_appr_2(s: str) -> str:
    end = len(s)
    resp = ""
    while end > 0:
        while s[end - 1] == ' ' and end > 0:
            end = end - 1

        start = end - 1

        while s[start] != " " and start >= 0:
            start -= 1
        if end == 0:
            break
        if resp != "":
            resp += " "
        resp += s[start + 1:end]
        end = start + 1
    return resp


if __name__ == '__main__':
    # output_str = reverse_words("hello dark   life")
    output_str=reverse_words_appr_2("hello dark   life")
    print(output_str)

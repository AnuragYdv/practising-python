# Problem:https://leetcode.com/problems/remove-outermost-parentheses/description/
def remove_outermost_parenthesis(s: str) -> str:
    res, chr_arr = 0, []
    for c in s:

        if c == "(" and res > 0:
            chr_arr.append(c)
        if c == ")" and res > 1:
            chr_arr.append(c)
        res += 1 if c == "(" else -1
    return "".join(chr_arr)


def remove_outermost_optimised(s: str) -> str:
    queue1 = []
    s1 = ''
    s2 = ''
    for i in s:
        if i == '(':
            queue1.append(i)
        else:
            queue1.pop()
        if not queue1:
            s1 = s1[1:len(s1)]
            s2 += s1
            s1 = ''
        else:
            s1 += i
    return s2


if __name__ == '__main__':
    input_str = "(())"
    output_str = remove_outermost_optimised(input_str)
    print(output_str)

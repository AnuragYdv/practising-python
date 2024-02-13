def largest_odd_number(num: str) -> str:
    largest_odd = ''
    for i in range(len(num) - 1, -1, -1):
        if int(num[i]) % 2 == 1:
            largest_odd = num[:i + 1]
            break

    return largest_odd


if __name__ == '__main__':
    num = "123456789"
    odd = largest_odd_number(num)
    # another approach can be using rstrip
    print(num.rstrip("02468"))
    print(odd)

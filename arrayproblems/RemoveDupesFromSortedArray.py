def remove_duplicate(arr: []) -> []:
    d = {}
    dedup_arr = list(d.fromkeys(arr))  # d.fromKeys -> O(n) and initialising again O(n) O(2n). Space Complexity (2d)

    return dedup_arr


def remove_dedupe_inplace(arr: []) -> ([], int):
    i = 0
    for j in range(1, len(arr)):
        if (arr[i] != arr[j]):
            arr[i + 1] = arr[j]
            i = i + 1
    return (arr, i)


if __name__ == '__main__':
    dedup_arr = remove_duplicate([1, 1, 2, 2, 2, 3, 3, 3, 4])
    inplace = remove_dedupe_inplace([1, 1, 2, 2, 2, 3, 3, 3, 4])
    print(inplace)
    print(dedup_arr)

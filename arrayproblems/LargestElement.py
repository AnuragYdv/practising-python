# Problem statement1:
# Given an array ‘arr’ of size ‘n’ find the largest element in the array.
#      Example:
#      Input: 'n' = 5, 'arr' = [1, 2, 3, 4, 5]
#      Output: 5
#      Explanation: From the array {1, 2, 3, 4, 5}, the largest element is 5.
def largest_element(arr: [], n: int) -> int:
    largest_elm = arr[0]
    for i in range(0, n):
        if arr[i] > largest_elm:
            largest_elm = arr[i]
    return largest_elm


if __name__ == '__main__':
    largest_ele = largest_element([1, 2, 3, 4, 5, 6, 7, 8, 50], 9)
    print(largest_ele)

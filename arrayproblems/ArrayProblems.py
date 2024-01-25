

# Problem statement1:
# Given an array ‘arr’ of size ‘n’ find the largest element in the array.
#      Example:
#      Input: 'n' = 5, 'arr' = [1, 2, 3, 4, 5]
#      Output: 5
#      Explanation: From the array {1, 2, 3, 4, 5}, the largest element is 5.
def largestElement(arr: [], n: int) -> int:
    largestElem=arr[0]
    for i in range(0,n):
        if arr[i] > largestElem:
            largestElem=arr[i]
    return largestElem

if __name__=='__main__':
    largestElem=largestElement([1,2,3,4,5,6,7,8,50],9)
    print(largestElem)
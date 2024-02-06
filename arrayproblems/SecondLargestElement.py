# Easiest Way to find the Second Largest Element is to Sort the Array and print n-2
# MergeSort can be implemented here. Time complexity for merge sort is nlog(n).
# Solution
#Step1: variable Largest and second_largest_element as arr[0] and -1.
#Start iterating through the array and if a[i]> largest_elm . Update the value and value of largest will become
#second largest. If it is less than a[i] and greater than 2nd largest update that number . Complexity : O(n)

def second_largest_element(arr: [], arrayLen: int) -> int:
    lgt_elm = arr[0]
    scd_lgt_elm = -1
    for i in range(1, arrayLen):
        if arr[i] > lgt_elm:
            scd_lgt_elm=lgt_elm
            lgt_elm = arr[i]
        elif arr[i]<lgt_elm and arr[i]>scd_lgt_elm:
            scd_lgt_elm=arr[i]

    return scd_lgt_elm


if __name__ == '__main__':
    scd_lgt_elm = second_largest_element([70, 51, 51, 51, 51, 51, 51, 51, 51], 9)
    print(scd_lgt_elm)

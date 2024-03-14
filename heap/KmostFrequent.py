# LeetCode:https://leetcode.com/problems/top-k-frequent-elements/description/
# Description:
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
#
# Example 1:
#
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:
#
# Input: nums = [1], k = 1
# Output: [1]
#
# Constraints:
#
# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
#
# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
from collections import Counter


def topKFrequent(nums: list[int], k: int) -> list[int]:
    count = {}
    freq = [[] for i in range(len(nums) + 1)]

    for num in nums:
        count[num] = 1 + count.get(num, 0)
    print(count)
    print(count.items())
    for n, c in count.items():
        print(freq)
        freq[c].append(n)
    res = []
    print(freq)
    for i in range(len(freq) - 1, 0, -1):
        print(freq[i])
        for p in freq[i]:
            res.append(p)
            if len(res) == k:
                return res


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    cnt = Counter(nums)
    arr = []
    k_common = cnt.most_common()

    for i in range(0, k):
        arr.append((k_common[i])[0])
    return arr


if __name__ == '__main__':
    nums = [5, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4]
    k = 2
    # op = top_k_frequent(nums, k)
    op = topKFrequent(nums , 2)
    print(op)

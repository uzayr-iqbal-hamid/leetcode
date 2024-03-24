from typing import *

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0] * 5001

        for num in nums:
            count[num] += 1

        sortedNums = []

        for i in range(len(count)):
            for j in range(count[i]):
                sortedNums.append(i)

        left = (len(sortedNums) - 1) // 2
        right = len(sortedNums) - 1

        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = sortedNums[left]
                left -= 1
            else:
                nums[i] = sortedNums[right]
                right -= 1

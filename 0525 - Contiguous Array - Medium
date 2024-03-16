class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = {0: -1} 
        maxLength = 0
        count0 = 0
        count1 = 0

        for i, num in enumerate(nums):
            if num == 0:
                count0 += 1
            else:
                count1 += 1

            diff = count0 - count1

            if diff in count:
                maxLength = max(maxLength, i - count[diff])
            else:
                count[diff] = i

        return maxLength

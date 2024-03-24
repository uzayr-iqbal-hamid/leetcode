class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        add = sum(nums)
        n = len(nums)
        count = 0
        for i in range(n+1):
            count += i

        return count - add


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        Set = set(nums)
        for i in range(1, len(nums) + 1):
            if i not in Set:
                return i

        return len(nums) + 1

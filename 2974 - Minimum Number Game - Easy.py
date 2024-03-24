class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        return [nums[i^1] for i in range(len(nums))]

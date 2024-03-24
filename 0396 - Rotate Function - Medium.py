class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        total = sum(i * num for i, num in enumerate(nums))
        ans = total

        total_sum = sum(nums)

        for a in reversed(nums):
            total += total_sum - len(nums) * a
            ans = max(ans, total)
        
        return ans

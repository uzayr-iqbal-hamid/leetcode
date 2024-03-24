from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        nums.sort()

        dp = [1] * len(nums)
        max_len, max_index = 1, 0

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], dp[j] + 1)

            if dp[i] > max_len:
                max_len = dp[i]
                max_index = i

        result = []
        current_len, current_mod = max_len, nums[max_index]
        for i in range(max_index, -1, -1):
            if current_len > 0 and current_mod % nums[i] == 0 and dp[i] == current_len:
                result.append(nums[i])
                current_mod = nums[i]
                current_len -= 1

        return result

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        
        left = 0
        longest = 0
        count = defaultdict(int)

        for right in range(len(nums)):
            count[nums[right]] += 1
            while count[nums[right]] > k:
                count[nums[left]] -= 1
                left += 1

            longest = max(longest, right - left + 1)
        return longest

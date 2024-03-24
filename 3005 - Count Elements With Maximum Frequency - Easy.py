class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        highest = max(counter.values())
        ans = highest
        for num, val in counter.items():
            if val == highest:
                ans += highest

        return ans-highest

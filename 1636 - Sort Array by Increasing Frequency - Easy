class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = collections.Counter(nums)
        ans = sorted(nums, key=lambda x: (-count[x], x))
        ans.reverse()
        return ans

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count =collections.Counter(nums)
        for key, val in count.items():
            if val == 1:
                return key

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        return sum([num for num, val in collections.Counter(nums).items() if val == 1])

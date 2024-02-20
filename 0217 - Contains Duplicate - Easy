class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if nums == set(nums):
            return False

        count = collections.Counter(nums)
        for freq in count.values():
            if freq > 1:
                return True

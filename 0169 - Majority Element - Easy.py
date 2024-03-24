class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        count = collections.Counter(nums)
        majority_element = len(nums) / 2

        for num, freq in count.items():
            if freq > majority_element:
                return num

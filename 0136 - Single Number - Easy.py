class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = {}
        
        for i in range(len(nums)):
            if nums[i] in counter.keys():
                counter[nums[i]] += 1
            else:
                counter[nums[i]] = 1

        for k, v in counter.items():
            if v < 2:
                return k

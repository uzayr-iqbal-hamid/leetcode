class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = []
        count = collections.Counter(nums)
        majority = len(nums) / 3

        for num, freq in count.items():
            if freq > majority:
                ans.append(num)

        return ans

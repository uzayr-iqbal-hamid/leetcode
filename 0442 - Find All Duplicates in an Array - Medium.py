class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        count = collections.Counter(nums)
        ans = []
        for num, val in count.items():
            if val > 1:
                ans.append(num)
        return ans

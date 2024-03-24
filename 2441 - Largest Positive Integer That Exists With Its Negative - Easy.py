class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        ans = []
        for i in nums:
            if -i in nums:
                ans.append(i)
        if ans:
            return max(ans)
        return -1

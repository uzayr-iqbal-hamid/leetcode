class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        ans = []
        for i in count.keys():
            ans.append(i)
        ans.sort(reverse=True)
        if len(ans) >= 3:
            return ans[2]
        
        return max(ans)

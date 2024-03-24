class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = []
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                ans.append(count)
                count = 0
            ans.append(count)
        
        return max(ans)

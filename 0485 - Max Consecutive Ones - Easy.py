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

# Alternate solution:

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i = 0
        
        max_count = 0
        while i < len(nums):
            count = 0
            if nums[i] == 1:
                while i < len(nums) and nums[i] == 1: 
                    count += 1
                    i += 1
                        
                if count > max_count:
                    max_count = count
            else:
                i += 1

        return max_count

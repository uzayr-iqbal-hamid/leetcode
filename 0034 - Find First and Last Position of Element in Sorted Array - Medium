class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = []
        start = 0
        end = len(nums)-1

        while start <= end:
            if nums[start] == target:
                ans.append(start)
                break
            start += 1

        start = 0
        while end >= start:            
            if nums[end] == target:
                ans.append(end)
                break
            end -= 1

        if len(ans) == 1:
            return ans.append(ans[0])

        if ans:
            return ans

        return [-1, -1]

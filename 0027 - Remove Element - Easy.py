class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        for num in range(len(nums)):
            if nums[num] == val:
                nums[num] = -1
        nums.sort()
        nums.reverse()

        i = len(nums) - 1

        while i > -1:
            if nums[i] == -1:
                nums.pop()
            i -= 1

        nums.sort()

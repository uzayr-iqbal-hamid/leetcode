class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        total = sum(nums)

        for num in nums:
            total -= num
            
            if total > num:
                return total + num

        return -1

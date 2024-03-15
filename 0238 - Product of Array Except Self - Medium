class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1] * n 
        right = [1] * n
        result = [0] * n 

        for i in range(1, n): 
            left[i] = left[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1): # i = 0
            right[i] = right[i + 1] * nums[i + 1] 

        for i in range(n): 
            result[i] = left[i] * right[i]

        return result

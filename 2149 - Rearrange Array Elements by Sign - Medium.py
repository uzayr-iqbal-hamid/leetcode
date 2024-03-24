class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = [num for num in nums if num >= 0]
        negative = [num for num in nums if num < 0]

        ans = [positive[i // 2] if i % 2 == 0 else negative[i // 2] for i in range(len(nums))]  
        return ans

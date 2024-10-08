class Solution:
    def check(self, nums: List[int]) -> bool:
        rotation_count = 0
        n = len(nums)
        for i in range(n):
            if nums[i] > nums[(i+1) % n]:
                rotation_count += 1
        
        return rotation_count <= 1

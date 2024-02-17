class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:

        n = len(nums) #length of the array nums
        begin_from = self.beginning(nums) #this is the beginning index

        if begin_from == 0:
            return n * (n + 1) // 2 #no. of maximum incremovable subarrays possible.

        ans = n - begin_from + 1 #this is the minimum most valid incremovable subarrays that will exist.

        for i in range(begin_from):
            if i > 0 and nums[i] <= nums[i - 1]:
                break

            ans += n - bisect.bisect_right(nums, nums[i], begin_from) + 1 #the bisect_right() method returns the position where when nums[i] is inserted in nums, nums will remain sorted.
        
        return ans

    def beginning(self, nums):
        
        for i in range(len(nums)-2, -1, -1):
            if nums[i] >= nums[i + 1]:
                return i + 1 

        return 0 #when beginning is 0 -> nums is sorted, i.e., on removing any subarray, nums is always increasing.

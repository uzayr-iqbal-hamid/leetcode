"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4
 
Constraints:
1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        ans = 0

        while left <= right:
            mid = (left + right) // 2
           
            if target == nums[mid]:
                return mid

            elif target > nums[mid]:
                left = mid + 1
            
            elif target < nums[mid]:
                right = mid - 1
            
        else:
            if target > nums[-1]:
                return n 
            for i in range(n):
                if target > nums[i] and target < nums[i + 1]:
                    ans = i + 1
        
        return ans

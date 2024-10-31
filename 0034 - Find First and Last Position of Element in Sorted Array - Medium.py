"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]
 
Constraints:
0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
"""

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

# Alternate Solution

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def first_occurrence(n):

            first = -1
            left, right = 0, n - 1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    first = mid
                    right = mid - 1
                
                elif nums[mid] > target:
                    right = mid - 1

                else:
                    left = mid + 1

            return first

        def last_occurrence(n):
            
            last = -1
            left, right = 0, n - 1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    last = mid
                    left = mid + 1
                
                elif nums[mid] < target:
                    left = mid + 1
                
                else:
                    right = mid - 1

            return last
        
        n = len(nums)
        res = []
        left, right = 0, n - 1

        first = first_occurrence(n)
        last = last_occurrence(n)

        return [first, last]

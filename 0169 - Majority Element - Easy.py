"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 
Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        count = collections.Counter(nums)
        majority_element = len(nums) / 2

        for num, freq in count.items():
            if freq > majority_element:
                return num

# Alternate solution

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        is_majority = len(nums) / 2

        counter = {}

        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        for num, freq in counter.items():
            if freq > is_majority:
                return num

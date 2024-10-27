"""
You are given an integer array nums.
The factor score of an array is defined as the product of the LCM and GCD of all elements of that array.
Return the maximum factor score of nums after removing at most one element from it.
Note that both the LCM and GCD of a single number are the number itself, and the factor score of an empty array is 0.
The term lcm(a, b) denotes the least common multiple of a and b.
The term gcd(a, b) denotes the greatest common divisor of a and b.

Example 1:
Input: nums = [2,4,8,16]
Output: 64
Explanation:
On removing 2, the GCD of the rest of the elements is 4 while the LCM is 16, which gives a maximum factor score of 4 * 16 = 64.

Example 2:
Input: nums = [1,2,3,4,5]
Output: 60
Explanation:
The maximum factor score of 60 can be obtained without removing any elements.

Example 3:
Input: nums = [3]
Output: 9

Constraints:
1 <= nums.length <= 100
1 <= nums[i] <= 30
"""

class Solution:        
    def maxScore(self, nums: List[int]) -> int:
        def gcd_calc(nums):
            gcd = nums[0]
            for i in nums:
                gcd = math.gcd(gcd, i)
    
            return gcd

        def lcm_calc(nums):
            lcm = 1
            for i in nums:
                lcm = (lcm * i)//math.gcd(lcm, i)
    
            return lcm

        if len(nums) == 1:
            return nums[0] * nums[0]

        gcd = gcd_calc(nums)
        lcm = lcm_calc(nums)
        max_result = gcd * lcm
        
        for i in range(len(nums)):
            skipping = nums[:i] + nums[i+1:]

            if not skipping:
                continue

            new_gcd = gcd_calc(skipping)
            new_lcm = lcm_calc(skipping)
            
            max_result = max(max_result, new_gcd * new_lcm)
            
        return max_result
        

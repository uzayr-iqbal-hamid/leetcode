"""
You are given an array nums of non-negative integers and an integer k.
An array is called special if the bitwise OR of all of its elements is at least k.
Return the length of the shortest special non-empty 
subarray of nums, or return -1 if no special subarray exists.

Example 1:
Input: nums = [1,2,3], k = 2
Output: 1
Explanation:
The subarray [3] has OR value of 3. Hence, we return 1.

Example 2:
Input: nums = [2,1,8], k = 10
Output: 3
Explanation:
The subarray [2,1,8] has OR value of 11. Hence, we return 3.

Example 3:
Input: nums = [1,2], k = 0
Output: 1
Explanation:
The subarray [1] has OR value of 1. Hence, we return 1.

Constraints:
1 <= nums.length <= 2 * 105
0 <= nums[i] <= 109
0 <= k <= 109
"""

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        res = float("inf")
        bits = [0] * 32

        def bits_update(bits, n, diff):
            for i in range(32):
                if n & (1 << i):
                    bits[i] += diff

        def bits_to_int(bits):
            res = 0
            for i in range(32):
                if bits[i]:
                    res += (1 << i)
            return res
        
        l = 0
        for r in range(len(nums)):
            bits_update(bits, nums[r], 1)
            cur_or = bits_to_int(bits)
            while l <= r and cur_or >= k:
                res = min(res, r-l+1)
                bits_update(bits, nums[l], -1)
                cur_or = bits_to_int(bits)
                l += 1
        
        return -1 if res == float("inf") else res

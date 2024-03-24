class Solution:
    def countDigits(self, num: int) -> int:
        nums = str(num)
        ans = 0
        for i in nums:
            if int(nums) % int(i) == 0:
                ans += 1

        return ans

class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        num = [str(i) for i in nums]
        ele_sum = 0
        digits = "".join(num)
        dig_sum = 0
        for i in num:
            ele_sum += int(i)
        for i in digits:
            dig_sum += int(i)

        return abs(ele_sum - dig_sum)

class Solution:
    def addDigits(self, num: int) -> int:
        def find_sum(nums):
            add = 0
    
            for i in nums:
                add += int(i)
    
            if len(str(add)) == 1:
                return add
    
            return find_sum(str(add))

        nums = str(num)
        ans = find_sum(nums)
        return ans

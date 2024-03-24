class Solution:
    def countEven(self, num: int) -> int:
        def digits_sum(i):
            i = str(i)
            add = 0
            for j in i:
                add += int(j)
            
            return add
        ans = 0
        for i in range(num, 0, -1):
            if digits_sum(i) % 2 == 0:
                ans += 1

        return ans

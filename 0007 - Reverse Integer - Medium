class Solution:
    def reverse(self, x: int) -> int:

        limit = 2**31 - 1
        ans = 0
        if x > 0:
            ans = int(str(x)[::-1])
        elif x < 0:
            ans = int(str(x)[:0:-1]) * -1

        if ans < limit and ans > -limit:
            return ans                
        
        return 0              

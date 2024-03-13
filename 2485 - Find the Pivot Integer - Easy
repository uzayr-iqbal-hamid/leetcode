class Solution:
    def pivotInteger(self, n: int) -> int:
        #to find sum of n numbers, the following formula
        total = (n * (n + 1)) // 2
        
        left = 0
        for i in range(1, n+1):
            left += i 
            right = total - left + i
            if left == right:
                return i
        
        return -1

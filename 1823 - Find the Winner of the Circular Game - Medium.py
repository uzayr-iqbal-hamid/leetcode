class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
    
        def remove_loser(n, k):
            ans = 0
            for i in range(2, n + 1):
                ans = (ans + k) % i
            return ans
        
        return remove_loser(n, k) + 1

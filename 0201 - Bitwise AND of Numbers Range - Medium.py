class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:

        moves = 0
        while left!=right:
            left = left // 2
            right = right // 2
            moves += 1
        
        return right << moves

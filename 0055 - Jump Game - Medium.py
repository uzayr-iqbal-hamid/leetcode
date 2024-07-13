class Solution:
    def canJump(self, nums: List[int]) -> bool:
        energy = 0
        for n in nums:
            if energy < 0:
                return False
            
            elif n > energy:
                energy = n
            
            energy -= 1

        return True
            

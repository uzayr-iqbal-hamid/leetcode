class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        all_destroyed = mass + sum(asteroids)
        for i in range(len(asteroids)):
            if asteroids[i] <= mass:
                mass += asteroids[i]
        
        if mass == all_destroyed:
            return True
        else:
            return False

class Solution:
    def isHappy(self, n: int) -> bool:
        count = set()
        while n != 1:
            if n in count:
                return False
            count.add(n)
            n = sum(int(digit) ** 2 for digit in str(n))

        return True

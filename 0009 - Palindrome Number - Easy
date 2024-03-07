class Solution:
    def isPalindrome(self, x: int):

        org = x
        rev = 0
        while x > 0:
            rem = x % 10
            rev = rev * 10 + rem
            x //= 10
        if rev == org:
            return True
        else:
            return False

class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans=""
        for i in s:
            if i.isalnum():
                if i.isupper():
                    ans += i.lower()
                else:
                    ans +=i
        return ans == ans[::-1]

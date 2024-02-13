class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def palindrome(word):
            if len(word) < 1:
                return True
            else:
                if word[0] == word[-1]:
                    return palindrome(word[1:-1])
                else:
                    return False

        ans = ""
        for word in words:
            if palindrome(word):
               ans += word
               break
        return ans

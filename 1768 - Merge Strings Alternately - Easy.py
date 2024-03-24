class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        i = 0
        j = 0
        while i < len(word1) and j < len(word2):
            ans += word1[i]
            ans += word2[j]
            i += 1
            j += 1
        if len(word1) > len(word2):
            ans += word1[i:]
        else:
            ans += word2[j:]
        return ans

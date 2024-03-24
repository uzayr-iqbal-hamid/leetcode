class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ans = ""
        s_count = collections.Counter(s)
        t_count = collections.Counter(t)
        
        for char, freq in t_count.items():
            if s_count[char] != freq:
                ans = char
        return ans

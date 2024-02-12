class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = collections.Counter(s)
        ans = []

        for char, freq in count.items():
            if freq == 1:
                ans.append(char)

        if ans: 
            return s.index(ans[0])
        else:
            return -1
        

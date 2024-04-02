class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_t = {}
        t_s = {}

        for sChar, tChar in zip(s, t):
            if sChar not in s_t:
                s_t[sChar] = tChar
            else:
                if s_t[sChar] != tChar:
                    return False
            if tChar not in t_s:
                t_s[tChar] = sChar
            else:
                if t_s[tChar] != sChar:
                    return False
        return True

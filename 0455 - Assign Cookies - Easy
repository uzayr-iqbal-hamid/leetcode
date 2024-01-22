class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        content_children = 0

        i = 0
        j = 0

        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                content_children += 1
                i += 1
            j += 1

        return content_children

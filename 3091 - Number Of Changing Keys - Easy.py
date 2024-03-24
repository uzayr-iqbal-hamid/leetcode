class Solution:
    def countKeyChanges(self, s: str) -> int:
        small = s.lower()
        ans = 0

        for i in range(len(small)-1, 0, -1):
            if small[i] != small[i-1]:
                ans += 1
        return ans

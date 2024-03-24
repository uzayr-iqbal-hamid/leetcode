class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustworthy = [0] * (n + 1)

        for people, judge in trust:
            trustworthy[people] -= 1
            trustworthy[judge] += 1

        for i in range(1, n+1):
            if trustworthy[i] == n - 1:
                return i

        return -1

class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        LCM = math.lcm(divisor1, divisor2)
        l = 0
        r = 2**31 - 1

        def isPossible(m: int) -> bool:
            cnt1 = m - m // divisor1
            cnt2 = m - m // divisor2
            totalCnt = m - m // LCM
            return cnt1 >= uniqueCnt1 and cnt2 >= uniqueCnt2 and \
                totalCnt >= uniqueCnt1 + uniqueCnt2

        while l < r:
            m = (l + r) // 2
            if isPossible(m):
                r = m
            else:
                l = m + 1

        return l

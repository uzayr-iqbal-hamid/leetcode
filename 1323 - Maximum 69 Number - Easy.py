class Solution:
    def maximum69Number (self, num: int) -> int:
        s_num = str(num)
        s = list(s_num)
        poss = []
        for i in range(len(s)):
            if s[i] == '6':
                s[i] = '9'
            poss.append(s)
            s = list(s_num)

        for i in range(len(poss)):
            poss[i] = "".join(poss[i])

        for i in range(len(poss)):
            poss[i] = int(poss[i])

        return max(poss)

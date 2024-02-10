class Solution:
    def replaceDigits(self, s: str) -> str:
        def shift(c: str, x: int) -> str:
            dic = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8,'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21,'v':22, 'w':23, 'x':24, 'y':25, 'z':26}
            return list(dic.keys())[list(dic.values()).index(x+dic[c])]
        s = list(s)
        for index in range(1, len(s), 2):
            s[index] = shift(s[index-1], int(s[index]))
        return "".join(s)

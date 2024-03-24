class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for i in range(left, right+1):
            i = str(i)
            count = 0
            for j in i:
                if int(j) == 0 or int(i) % int(j) != 0:
                    break
                else:
                    count += 1
            if count == len(i): 
                ans.append(int(i))
        return ans

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        even = [i for i in nums if i % 2 == 0] #even integers
        count = collections.Counter(even) #frequency
        
        #to check the highest frequency amongst the even elements
        ans = []
        for num, freq in count.items():
            if freq == max(count.values()):
                ans.append(num)
        
        if ans:
            return min(ans)
        return -1

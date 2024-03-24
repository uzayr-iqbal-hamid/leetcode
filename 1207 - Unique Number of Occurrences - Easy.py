class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        ans = []
        count = collections.Counter(arr)
        for freq in count.values():
            ans.append(freq)

        ans_count = collections.Counter(ans)
        for freq in ans_count.values():
            if freq > 1:
                return False
        
        return True

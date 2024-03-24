class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        priority_q = []
        heapq.heapify(priority_q)
        for i in range(len(nums)):
            heapq.heappush(priority_q, [nums[i], i])
            if len(priority_q) > k:
                heapq.heappop(priority_q)
        priority_q.sort(key = lambda x: x[1])
        ans = []
        for i in range(len(priority_q)):
            ans.append(priority_q[i][0])
        return ans

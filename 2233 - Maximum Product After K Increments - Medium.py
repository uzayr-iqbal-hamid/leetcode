class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        mod = 10**9 + 7

        heapq.heapify(nums)
        ans = 1

        for _ in range(k):
            smallest = heapq.heappop(nums)
            heapq.heappush(nums, smallest + 1)

        while nums:
            ans *= heapq.heappop(nums)
            ans %= mod

        return ans

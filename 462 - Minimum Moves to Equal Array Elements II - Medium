class Solution:
    def minMoves2(self, nums: List[int]) -> int:

        median = statistics.median(nums)

        moves = 0
        for num in nums:
            moves += abs(num - median)

        return int(moves)

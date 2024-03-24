class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        ans = []

        for i, (a, b) in enumerate(itertools.pairwise(heights)):
            diff = b - a
            if diff <= 0:
                continue
            heapq.heappush(ans, diff)

            if len(ans) > ladders:
                bricks -= heapq.heappop(ans)
            if bricks < 0:
                return i

        return len(heights) - 1

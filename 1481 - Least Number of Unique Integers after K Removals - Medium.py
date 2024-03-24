class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        mheap = list(collections.Counter(arr).values())
        heapq.heapify(mheap)

        while k > 0:
            k -= heapq.heappop(mheap) # to ensure that we remove the integers with lesser frequencies.

        return len(mheap) + (1 if k < 0 else 0)

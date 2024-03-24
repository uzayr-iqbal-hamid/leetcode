class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        for i in range(n):
            for j in range(m+n):
                if nums1[j] == 0:
                    nums1[j] = nums2[i]
                    break

        nums1.sort()

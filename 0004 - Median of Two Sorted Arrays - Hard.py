class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        ans = nums1 + nums2
        ans.sort()
        if len(ans) % 2 != 0:
            return ans[len(ans)//2]
        else:
            right = len(ans) // 2
            left = right - 1
            return (ans[right] + ans[left])/2

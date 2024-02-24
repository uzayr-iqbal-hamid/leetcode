class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        noOfZero = 0
        for num in nums:
            if num == 0:
                noOfZero += 1

        for i in range(noOfZero):
            nums.remove(0)
            nums.append(0)

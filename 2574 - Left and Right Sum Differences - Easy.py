class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftSum = []
        rightSum = []

        for i in range(len(nums)):
            if i == 0:
                leftSum.append(i)
            leftSum.append(nums[i] + leftSum[i])
        leftSum.pop()

        for i in range(1, len(nums)):
            rightSum.append(sum(nums[i:]))
        rightSum.append(0)

        return [abs(leftSum[i]-rightSum[i]) for i in range(len(nums))]

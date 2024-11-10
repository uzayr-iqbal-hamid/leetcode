"""
Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears at most twice, return an array of all the integers that appears twice.
You must write an algorithm that runs in O(n) time and uses only constant auxiliary space, excluding the space needed to store the output

Example 1:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]

Example 2:
Input: nums = [1,1,2]
Output: [1]

Example 3:
Input: nums = [1]
Output: []
 
Constraints:
n == nums.length
1 <= n <= 105
1 <= nums[i] <= n
Each element in nums appears once or twice.
"""

class Solution {
    public List<Integer> findDuplicates(int[] nums) {
        List<Integer> result = new ArrayList<>();

        int i = 0;
        while(i < nums.length) {
            int correctIndex = nums[i] - 1;
            if(nums[i] != nums[correctIndex]){
                swap(nums, i, correctIndex);
            } else {
                i++;
            }
        }
        for (int j = 0; j<nums.length; j++) {
            if (nums[j] != j + 1)
                result.add(nums[j]);
        }
        return result;
    }

    void swap(int[] arr, int a, int b) {
        int temp = arr[a];
        arr[a] = arr[b];
        arr[b] = temp;
    }
}

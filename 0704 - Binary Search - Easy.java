// Recursive approach

class Solution {
    public int search(int[] nums, int target) {
        return recursiveSearch(nums, target, 0, nums.length-1);
    }

    int recursiveSearch(int[] nums, int target, int left, int right) {

        if (left > right) {
            return -1;
        }

        int mid = left + (right - left) / 2;
        if (nums[mid] == target) {
            return mid;
        }
        if (nums[mid] > target) {
            return recursiveSearch(nums, target, left, mid - 1);
        }

        return recursiveSearch(nums, target, mid + 1, right);
    }
}

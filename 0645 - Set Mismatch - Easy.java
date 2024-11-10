"""
You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.
You are given an integer array nums representing the data status of this set after the error.
Find the number that occurs twice and the number that is missing and return them in the form of an array.

Example 1:
Input: nums = [1,2,2,4]
Output: [2,3]

Example 2:
Input: nums = [1,1]
Output: [1,2]

Constraints:
2 <= nums.length <= 104
1 <= nums[i] <= 104
"""

class Solution {
    public int[] findErrorNums(int[] nums) {
        int i = 0;
        while (i < nums.length) {
            int correctIndex = nums[i] - 1;

            if(nums[i] != nums[correctIndex]) {
                swap(nums, i, correctIndex);
            } else {
                i++;
            }
        }
      
        for (int j = 0; j < nums.length; j++) {
            if (nums[j] != j + 1)
                return new int[]{nums[j], j + 1};
        }

        return new int[]{-1, -1};
        
    }

    void swap(int[] arr, int a, int b) {
        int temp = arr[a];
        arr[a] = arr[b];
        arr[b] = temp;
    }
}

// Solution Using HashSEt

class Solution {
    public int[] findErrorNums(int[] nums) {
        HashSet<Integer> set = new HashSet<>();
        int duplicate = -1, missing = -1;

        for(int num : nums) {
            if(!set.add(num))
                duplicate = num;
        }

        for(int i = 1; i<=nums.length; i++) {
            if(!set.contains(i)){
                missing = i;
                break;
            }
        }
        return new int[]{duplicate, missing};
    }
}

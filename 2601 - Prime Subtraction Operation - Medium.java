"""
You are given a 0-indexed integer array nums of length n.
You can perform the following operation as many times as you want:
Pick an index i that you haven’t picked before, and pick a prime p strictly less than nums[i], then subtract p from nums[i].
Return true if you can make nums a strictly increasing array using the above operation and false otherwise.
A strictly increasing array is an array whose each element is strictly greater than its preceding element.

Example 1:
Input: nums = [4,9,6,10]
Output: true
Explanation: In the first operation: Pick i = 0 and p = 3, and then subtract 3 from nums[0], so that nums becomes [1,9,6,10].
In the second operation: i = 1, p = 7, subtract 7 from nums[1], so nums becomes equal to [1,2,6,10].
After the second operation, nums is sorted in strictly increasing order, so the answer is true.

Example 2:
Input: nums = [6,8,11,12]
Output: true
Explanation: Initially nums is sorted in strictly increasing order, so we don't need to make any operations.

Example 3:
Input: nums = [5,8,3]
Output: false
Explanation: It can be proven that there is no way to perform operations to make nums sorted in strictly increasing order, so the answer is false.
 
Constraints:
1 <= nums.length <= 1000
1 <= nums[i] <= 1000
nums.length == n
"""

class Solution {
    public boolean primeSubOperation(int[] nums) {
        boolean[] isPrime = sieveOfEratosthenes(1000);
        List<Integer> primes = new ArrayList<>();

        for (int i = 2; i < isPrime.length; i++) {
            if (isPrime[i]) primes.add(i);
        }

        int prev = 0;

        for (int i = 0; i < nums.length; i++) {
            int current = nums[i];

            int target = current - prev;
            if (target <= 0) return false;

            int primeToSubtract = -1;
            int left = 0;
            int right = primes.size() - 1;

            while (left <= right) {
                int mid = left + (right - left) / 2;

                if (primes.get(mid) < target) {
                    primeToSubtract = primes.get(mid);
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }

            if (primeToSubtract != -1) {
                current -= primeToSubtract;
            }

            if (current <= prev) return false;
            prev = current;
        }
        
        return true;
    }

    static boolean[] sieveOfEratosthenes(int max) {
        boolean[] isPrime = new boolean[max + 1];
        Arrays.fill(isPrime, true);
        isPrime[0] = false;
        isPrime[1] = false;

        for (int p = 2; p * p <= max; p++) {
            if (isPrime[p]) {
                for (int multiple = p * p; multiple <= max; multiple += p) {
                    isPrime[multiple] = false;
                }
            }
        }
        return isPrime;
    }
}

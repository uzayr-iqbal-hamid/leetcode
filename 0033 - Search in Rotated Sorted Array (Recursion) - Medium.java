class Solution {
    public int search(int[] nums, int target) {
        return searcher(nums, target, 0, nums.length-1);
    }

    static int searcher(int[] arr, int target, int s, int e) {
        if (s > e) {
            return -1;
        }
        int m = s + (e - s) / 2;

        if(arr[m] == target){
            return m;
        }

        if(arr[m] >= arr[s]) {
            if(target >= arr[s] && target <= arr[m]) {
                return searcher(arr, target, s, m-1);
            } else {
                return searcher(arr, target, m+1, e);
            }
        }

        if (target >= arr[m] && target <= arr[e]) {
            return searcher(arr, target, m+1, e);
        }
        return searcher(arr, target, s, m-1);
    }
}

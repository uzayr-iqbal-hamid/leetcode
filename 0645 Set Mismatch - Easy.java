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

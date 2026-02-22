class Solution {
    public List<String> buildArray(int[] target, int n) {
        List<String> list = new ArrayList<>();

        int i = 0;
        int num = 1;

        while (i < target.length) {
            if (num == target[i]) {
                list.add("Push");
                i++;
                num++;
            } else {
                list.add("Push");
                list.add("Pop");
                num++;
            }
        }

        return list;
    }
}

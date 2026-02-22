class Solution {
    public int[] finalPrices(int[] prices) {
        int[] result = prices.clone();
        Stack<Integer> stack = new Stack<>();

        int n = prices.length;

        for (int i = 0; i < n; i++) {
            while (!stack.isEmpty() && result[stack.peek()] >= prices[i]) {
                int idx = stack.pop();
                result[idx] -= prices[i];
            }
            stack.push(i);
        }

        return result;
    }
}

class Solution {
    public int maxProfit(int[] prices) {
        int maxProfit = 0;
        int curProfit = 0;
        int minPrice = prices[0];

        for (int i = 0; i < prices.length; i++) {
            curProfit = prices[i] - minPrice;
            maxProfit = Math.max(curProfit, maxProfit);
            minPrice = Math.min(minPrice, prices[i]);
        }

        return maxProfit;
    }
}

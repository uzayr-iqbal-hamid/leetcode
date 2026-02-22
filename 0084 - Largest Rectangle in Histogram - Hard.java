class Solution {
    public int largestRectangleArea(int[] heights) {
        int maxArea = 0;
        Stack<Integer> index = new Stack<>();
        Stack<Integer> height = new Stack<>();

        for (int i = 0; i < heights.length; i++) {
            int start = i;
            while (!height.isEmpty() && height.peek() > heights[i]) {
                int hgt = height.pop();
                int ind = index.pop();

                maxArea = Math.max(maxArea, hgt * (i - ind));
                start = ind;
            }
            index.push(start);
            height.push(heights[i]);
        }

        while (!height.isEmpty() || !index.isEmpty()) {
            maxArea = Math.max(maxArea, height.pop() * (heights.length - index.pop()));
        }

        return maxArea;
    }
}

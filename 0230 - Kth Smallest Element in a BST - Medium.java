class Solution {
    public int kthSmallest(TreeNode root, int k) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        inorder(root, pq);
        int smallest = -1;
        for (int i = 0; i < k; i++) {
            smallest = pq.poll();
        }
        return smallest;
    }
    public void inorder(TreeNode root, PriorityQueue pq) {
        if (root == null) {
            return;
        }
        inorder(root.left, pq);
        pq.add(root.val);
        inorder(root.right, pq);
    }
}

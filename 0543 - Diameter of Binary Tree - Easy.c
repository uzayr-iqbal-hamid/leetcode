/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int max(int a, int b){
    return (a > b) ? a : b;
}

int dfs(struct TreeNode *root, int *diameter){
    if(root == NULL)
        return 0;
    
    int leftDepth = dfs(root->left, diameter);
    int rightDepth = dfs(root->right, diameter);

    *diameter = max(*diameter, leftDepth+rightDepth);

    return 1 + max(leftDepth, rightDepth);
}

int diameterOfBinaryTree(struct TreeNode* root) {
    if(root == NULL)
        return 0;
    
    int diameter = 0;
    dfs(root, &diameter);
    return diameter;
}

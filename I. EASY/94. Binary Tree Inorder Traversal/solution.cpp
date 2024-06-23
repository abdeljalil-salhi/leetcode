/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution
{
public:
    void rec(TreeNode *node, vector<int> &r)
    {
        if (!node)
            return;
        if (node->left)
            rec(node->left, r);
        r.push_back(node->val);
        if (node->right)
            rec(node->right, r);
    }
    vector<int> inorderTraversal(TreeNode *root)
    {
        vector<int> r;
        rec(root, r);
        return r;
    }
};

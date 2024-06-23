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
    void inorderTraversal(TreeNode *root, vector<int> &inorder)
    {
        if (!root)
            return;
        inorderTraversal(root->left, inorder);
        inorder.push_back(root->val);
        inorderTraversal(root->right, inorder);
    }
    vector<int> findMode(TreeNode *root)
    {
        vector<int> inorder, ans;
        unordered_map<int, int> mp;
        int mx = INT_MIN;

        inorderTraversal(root, inorder);
        for (int i = 0; i < inorder.size(); i++)
        {
            mp[inorder[i]]++;
            mx = max(mp[inorder[i]], mx);
        }
        for (auto it : mp)
            if (it.second == mx)
                ans.push_back(it.first);
        return ans;
    }
};

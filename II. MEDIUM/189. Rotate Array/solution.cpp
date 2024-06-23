class Solution
{
public:
    void rotate(vector<int> &nums, int k)
    {
        const int n = nums.size();
        while (k > n)
            k -= n;

        vector<int> tmp(k, 0);
        for (int i = n - k, j = 0; i < n; i++, j++)
            tmp[j] = nums[i];

        vector<int> backup = nums;
        for (int i = 0; i < k; i++)
            nums[i] = tmp[i];

        for (int i = k; i < n; i++)
            nums[i] = backup[i - k];
    }
};

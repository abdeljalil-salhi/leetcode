class Solution
{
public:
    int majorityElement(vector<int> &nums)
    {
        const int n = nums.size();
        int count = 0, nb = 0;
        sort(nums.begin(), nums.end());

        for (int i = 0; i < n; i++)
        {
            if (nb == nums[i])
            {
                count++;
                if (count > n / 2)
                    return nums[i];
            }
            else
                nb = nums[i], count = 1;
        }

        return nums[0];
    }
};

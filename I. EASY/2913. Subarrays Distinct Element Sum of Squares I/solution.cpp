#include <vector>
#include <unordered_set>

class Solution
{
public:
    int sumCounts(std::vector<int> &nums)
    {
        int n = nums.size();
        int ans = 0;
        for (int i = 0; i < n; i++)
        {
            unordered_set<int> unique;
            int distinct = 0;
            for (int j = i; j < n; j++)
            {
                if (unique.find(nums[j]) == unique.end())
                    unique.insert(nums[j]), distinct++;
                ans += pow(distinct, 2);
            }
        }
        return ans;
    }
};

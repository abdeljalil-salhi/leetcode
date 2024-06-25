class Solution
{
public:
    bool containsDuplicate(std::vector<int> &nums)
    {
        std::unordered_map<int, bool> table;

        for (int n : nums)
        {
            if (table.find(n) != table.end())
                return true;
            table[n] = true;
        }

        return false;
    }
};

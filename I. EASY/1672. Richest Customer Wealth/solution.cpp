class Solution
{
public:
    int maximumWealth(vector<vector<int>> &accounts)
    {
        int max = 0;

        for (int x = 0; x < accounts.size(); x++)
        {
            int tmp = 0;

            for (int y = 0; y < accounts[x].size(); y++)
                tmp += accounts[x][y];

            if (tmp > max)
                max = tmp;
        }

        return max;
    }
};

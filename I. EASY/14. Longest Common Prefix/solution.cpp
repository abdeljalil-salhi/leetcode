class Solution
{
public:
    string longestCommonPrefix(vector<string> &strs)
    {
        if (strs.empty())
            return "";

        string prefix = strs[0];
        int size = strs.size();
        for (int i = 1; i < size; i++)
        {
            string _new = "";
            int _size = prefix.size();
            int __size = strs[i].size();

            for (int j = 0; j < _size && j < __size; j++)
            {
                if (strs[i][j] == prefix[j])
                    _new += strs[i][j];
                else
                    break;
            }

            prefix = _new;
        }

        return prefix;
    }
};

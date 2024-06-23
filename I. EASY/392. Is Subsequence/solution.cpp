class Solution
{
public:
    bool isSubsequence(string s, string t)
    {
        const int n = t.length(), m = s.length();

        if ((!n && !m) || !m)
            return true;

        int j = 0;
        for (int i = 0; i < n; i++)
        {
            if (t[i] == s[j])
                j++;
            if (j == m)
                return true;
        }

        return false;
    }
};

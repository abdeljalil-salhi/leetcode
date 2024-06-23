class Solution
{
public:
    bool isAnagram(string s, string t)
    {
        int ascii[256];

        for (int i = 0; i < 256; i++)
            ascii[i] = 0;

        for (int i = 0; i < s.size(); i++)
            ascii[s[i]]++;

        for (int i = 0; i < t.size(); i++)
            ascii[t[i]]--;

        for (int i = 0; i < 256; i++)
            if (ascii[i] != 0)
                return false;

        return true;
    }
};

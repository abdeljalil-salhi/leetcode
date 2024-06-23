class Solution
{
public:
    int lengthOfLastWord(string s)
    {
        int length = s.length(), k = 0, space = 0;

        for (int i = 0; i < length; i++)
        {
            if (s[i] == ' ')
                space = 1;

            else if (s[i] != ' ' && space)
                space = 0, k = 1;

            else if (s[i] != ' ' && !space)
                k++;
        }

        return k;
    }
};

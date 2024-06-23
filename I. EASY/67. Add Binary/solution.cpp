class Solution
{
public:
    string addBinary(string a, string b)
    {
        string result = "";
        int i = a.length() - 1, j = b.length() - 1, rem = 0;

        while (i >= 0 || j >= 0)
        {
            int x = (i >= 0) ? a[i] - '0' : 0,
                y = (j >= 0) ? b[j] - '0' : 0;
            int sum = x + y + rem;
            result = to_string(sum % 2) + result;
            rem = sum / 2, i--, j--;
        }

        if (rem == 1)
            return "1" + result;

        return result;
    }
};

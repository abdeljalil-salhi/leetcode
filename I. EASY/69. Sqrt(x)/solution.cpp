class Solution
{
public:
    int mySqrt(int x)
    {
        if (x == 0)
            return 0;

        int l = 1, r = x, res = 0;
        while (l <= r)
        {
            int m = l + (r - l) / 2;
            if (m <= x / m)
                res = m, l = m + 1;
            else
                r = m - 1;
        }

        return res;
    }
};

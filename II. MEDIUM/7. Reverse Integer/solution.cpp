class Solution
{
public:
    int reverse(int x)
    {
        int sign = 1;

        if (x < 0 && x == INT_MIN)
            return 0;

        else if (x < 0)
            sign = -1, x = -x;

        long long reversed = 0;
        while (x != 0)
            reversed = reversed * 10 + x % 10, x /= 10;

        if (reversed > INT_MAX || reversed < INT_MIN)
            return 0;

        return static_cast<int>(reversed) * sign;
    }
};

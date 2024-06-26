class Solution
{
public:
    bool isPalindrome(int x)
    {
        if (x < 0)
            return false;

        long int y = 0, z = x;
        while (z)
            y = y * 10 + z % 10, z /= 10;

        return (x == y);
    }
};

class Solution
{
public:
    uint32_t reverseBits(uint32_t n)
    {
        char i = 32;
        uint32_t ans = 0;

        while (i > 0)
        {
            ans = ans * 2 + (n % 2);
            n /= 2;
            i--;
        }

        return ans;
    }
};

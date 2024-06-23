static const auto ZERO = []() noexcept
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    return 0;
}();

class Solution
{
public:
    void reverseString(vector<char> &s)
    {
        for (int i = 0; i < s.size() / 2; i++)
            // Speed up the swapping process by using XOR
            s[i] ^= s[s.size() - i - 1] ^= s[i] ^= s[s.size() - i - 1];
    }
};

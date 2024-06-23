class Solution
{
public:
    vector<string> simple_tokenizer(string s)
    {
        stringstream ss(s);
        string word;
        vector<string> tokens;
        while (ss >> word)
            tokens.push_back(word);
        return tokens;
    }
    string reverseWords(string s)
    {
        vector<string> tokens = simple_tokenizer(s);
        reverse(tokens.begin(), tokens.end());
        string ans = "";
        const int n = tokens.size();
        for (int i = 0; i < n; i++)
        {
            ans += tokens[i];
            if (i != n - 1)
                ans += " ";
        }
        return ans;
    }
};

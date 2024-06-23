class Solution
{
public:
    bool isValid(string s)
    {
        stack<char> st;
        unordered_map<char, char> map;
        int size = s.size();

        map[')'] = '(';
        map['}'] = '{';
        map[']'] = '[';

        for (int i = 0; i < size; i++)
        {
            if (s[i] == '(' || s[i] == '{' || s[i] == '[')
                st.push(s[i]);
            else
            {
                if (st.empty() || map[s[i]] != st.top())
                    return false;
                st.pop();
            }
        }

        return (st.empty());
    }
};

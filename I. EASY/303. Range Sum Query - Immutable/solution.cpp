class NumArray
{
private:
    vector<int> vec;

public:
    NumArray(vector<int> &nums)
    {
        this->vec = nums;
    }

    int sumRange(int left, int right)
    {
        int sum = 0;
        while (left <= right)
            sum += this->vec[left++];
        return sum;
    }
};

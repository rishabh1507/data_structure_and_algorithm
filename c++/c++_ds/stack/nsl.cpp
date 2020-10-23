// 4,5,2,10,8
//-1 4-1 2 2
// Nearer smaller to left

#include <bits/stdc++.h>
using namespace std;

vector<int> NSL(vector<int> arr)
{
    vector<int> arr1;
    stack<int> s;

    int n = arr.size();
    for (int i = 0; i < n; i++)
    {
        if (s.size() == 0)
        {
            arr1.push_back(-1);
        }
        if (s.size() > 0 && s.top() < arr[i])
        {
            arr1.push_back(s.top());
        }
        else if (s.size() > 0 && s.top() >= arr[i])
        {
            while (s.size() > 0 && s.top() >= arr[i])
            {
                s.pop();
            }
            if (s.size() == 0)
            {
                arr1.push_back(-1);
            }
            else
            {
                arr1.push_back(s.top());
            }
        }
        s.push(arr[i]);
    }
    return arr1;
}

int main()
{
    vector<int> arr = {4, 5, 2, 10, 8};
    vector<int> result;
    result = NSL(arr);
    for (int i = 0; i < result.size(); i++)
    {
        cout << result[i] << " ";
    }
    return 0;
}
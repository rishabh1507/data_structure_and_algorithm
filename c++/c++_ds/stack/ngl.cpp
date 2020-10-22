#include <bits/stdc++.h>
using namespace std;

vector<int> NGL(vector<int> arr)
{
    vector<int> arr2;
    stack<int> s;
    for (int i = 0; i < arr.size(); i++)
    {
        if (s.size() == 0)
        {
            arr2.push_back(-1);
        }
        else if (s.size() > 0 && s.top() > arr[i])
        {
            arr2.push_back(s.top());
        }
        else if (s.size() > 0 && s.top() <= arr[i])
        {
            while (s.size() > 0 && s.top() <= arr[i])
            {
                s.pop();
            }
            if (s.size() == 0)
            {
                arr2.push_back(-1);
            }
            else
            {
                arr2.push_back(s.top());
            }
        }
        s.push(arr[i]);
    }
    return arr2;
}

int main()
{
    // 1,3,0,0,1,2,4
    //-1-1 3 3 3 3 -1-1
    vector<int> arr = {1, 3, 0, 0, 1, 2, 4};
    vector<int> result;
    result = NGL(arr);
    for (int i = 0; i < result.size(); i++)
    {
        cout << result[i] << " ";
    }
    return 0;
}
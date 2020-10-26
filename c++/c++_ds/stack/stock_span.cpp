#include <bits/stdc++.h>
using namespace std;
// ngl
// 10 4 5 90 120 80
//  1 1 2 4   5   1
// -1  -1 -1  80 70 80 100

void stockSpan(vector<int> arr, int n)
{
    vector<int> v;
    stack<pair<int, int>> s;

    for (int i = 0; i < n; i++)
    {
        if (s.size() == 0)
        {
            v.push_back(-1);
        }
        else if (s.size() > 0 && s.top().first > arr[i])
        {
            v.push_back(s.top().second);
        }
        else if (s.size() > 0 && s.top().first <= arr[i])
        {
            while (s.size() > 0 && s.top().first <= arr[i])
            {
                s.pop();
            }
            if (s.size() == 0)
            {
                v.push_back(-1);
            }
            else
            {
                v.push_back(s.top().second);
            }
        }
        s.push({arr[i], i});
    }
    for (int l = 0; l < n; l++)
    {
        cout << l - v[l] << " ";
    }
    cout << "\n";
}

int main()
{
    vector<int> arr;
    vector<int> result;
    int t;
    int n;
    cin >> t;
    int temp;
    for (int i = 0; i < t; i++)
    {
        cin >> n;
        for (int j = 0; j < n; j++)
        {
            cin >> temp;
            arr.push_back(temp);
        }
        stockSpan(arr, n);
    }
    return 0;
}
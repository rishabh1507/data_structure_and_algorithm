#include <bits/stdc++.h>
using namespace std;

void rainwater(int arr[], int n)
{
    int nsl[n];
    int nsr[n];
    nsl[0] = arr[0];
    for (int i = 1; i < n - 1; i++)
    {
        nsl[i] = max(nsl[i - 1], arr[i]);
    }
    nsr[n - 1] = arr[n - 1];
    for (int i = n - 2; i >= 0; i--)
    {
        nsr[i] = max(nsr[i + 1], arr[i]);
    }
    int rain = 0;
    for (int i = 1; i < n - 1; i++)
    {
        rain += min(nsl[i], nsr[i]) - arr[i];
    }
    cout << rain << "\n";
}

int main()
{
    //code
    int t;
    int n;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        cin >> n;
        int arr[n];
        for (int j = 0; j < n; j++)
        {
            cin >> arr[j];
        }
        rainwater(arr, n);
    }
    return 0;
}

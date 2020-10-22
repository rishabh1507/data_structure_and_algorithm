// Given a sorted array find the pairs with k sum

// still incomplete
#include <bits/stdc++.h>
using namespace std;

int countpair(vector<int> arr, int k)
{
    int start = 0;
    int end = arr.size() - 1;
    int n = arr.size() - 1;
    int count = 0;
    int count1 = 0;
    int count2 = 0;
    int ans = 0;

    while (start < end)
    {
        if (arr[start] + arr[end] < k)
        {
            start++;
        }
        else if (arr[start] + arr[end] > k)
        {
            end--;
        }
        else
        {
            count++;
            if (arr[start] != arr[end])
            {
                int i = 0;
                while (i < n)
                {
                    if (arr[start] == arr[i])
                    {
                        count1++;
                    }
                    if (arr[end] == arr[i])
                    {
                        count2++;
                    }
                    i++;
                }
                ans = count + (count1 * count2);
                break;
            }
        }
    }
    return ans;
}

int main()
{
    vector<int> arr{1, 4, 4, 5, 5, 5, 6, 6, 11};
    int k = 11;
    int result;
    result = countpair(arr, k);
    cout << result;
    return 0;
}
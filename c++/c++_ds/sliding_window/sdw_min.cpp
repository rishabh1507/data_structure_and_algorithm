#include <bits/stdc++.h>
using namespace std;

// int minsubarrayK(vector<int> arr, int w)
// {
//     int left = 0;
//     int right = 0;
//     int res = 0;
//     int n = arr.size();
//     int curr;
//     while (right < n - 1 && right < w)
//     {
//         res += arr[right];
//         right++;
//     }
//     curr = res;
//     while (right < n)
//     {
//         curr += arr[right];
//         curr -= arr[left];
//         res = max(res, curr);
//         right++;
//         left++;
//     }
//     return res;
// }

// int main()
// {
//     int result;
//     vector<int> arr{2, 1, 5, 1, 3, 2};
//     int w = 7;
//     result = minsubarrayK(arr, w);
//     cout << result;
//     return 0;
// }
#include <iostream>
#include <vector>
#include <limits>
using namespace std;

class SWP_Problem03
{
public:
    static int smallestSubarrayWithGivenSum(const vector<int> &arr, int givenSum)
    {
        int minLength = numeric_limits<int>::max();
        int windowSum = 0;
        int windowStart = 0;
        for (int windowEnd = 0; windowEnd < arr.size(); windowEnd++)
        {
            windowSum += arr[windowEnd];
            while (windowSum >= givenSum)
            {
                minLength = min(minLength, windowEnd - windowStart + 1);
                windowSum -= arr[windowStart];
                windowStart++;
            }
        }

        if (minLength == numeric_limits<int>::max())
        {
            return 0;
        }

        return minLength;
    }
};

int main()
{
    int length = SWP_Problem03::smallestSubarrayWithGivenSum(vector<int>{2, 1, 5, 2, 3, 2}, 7);
    cout << length;
}
#include <bits/stdc++.h>
using namespace std;

// Problem: Given an array of positive numbers and a positive number ‘S’,
// 	find the length of the smallest contiguous subarray whose sum is greater than
// 	or equal to ‘S’. Return 0, if no such subarray exists.

// Explanation when sum becomes greater we only check window size with curr size and we update min with curr

// 	Sliding Window Pattern
// {2, 1, 5, 2, 3, 2}

// 	Output: 2

#include <bits/stdc++.h>
using namespace std;

int smallsum(vector<int> arr, int w)
{
    int left = 0;
    int right;
    int res = 100000;
    int sum1 = 0;
    // loop and do check condition when >
    for (right = 0; right < arr.size(); right++)
    {
        sum1 += arr[right];
        while (sum1 >= w)
        {
            res = min(res, right - left + 1);
            sum1 -= arr[left];
            left++;
        }
    }
    return res;
}

int main()
{
    vector<int> arr{2, 1, 5, 2, 3, 2};
    int w = 7;
    int result = smallsum(arr, w);
    cout << result;
    return 0;
}

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
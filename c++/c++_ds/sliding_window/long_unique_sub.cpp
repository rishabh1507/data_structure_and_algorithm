// Problem: Given a string, find the length of the longest substring which has no repeating characters.

// 	Example 1:
// 	Input: String="aabccbb"
// 	Output: 3
// 	Explanation: The longest substring without any repeating characters is "abc".

// 	Example 2:
// 	Input: String="abccde"
// 	Output: 3
// 	Explanation: Longest substrings without any repeating characters are "abc" & "cde".

// 	Approach:

// 	We can use a Map to remember the last index of each character we have processed.
// 	Whenever we get a repeating character we will shrink our sliding window to ensure that we
// 	always have distinct characters in the sliding window.
// 	i.e windowStart to windowEnd will always have unique characters.
// 	So, whenever I get any character which is already processed, I'll make my windowStart as
// 	the last index of the character + 1.

#include <bits/stdc++.h>
using namespace std;

int longsub(string s)
{
    unordered_map<char, int> d;
    int left = 0;
    int right;
    int res = 0;
    int n = s.size();
    for (right = 0; right < n; right++)
    {
        d[s[right]]++;

        while (d[s[right]] > 1)
        {
            d[s[left]]--;
            if (d[s[left]] <= 0)
            {
                d.erase(d[s[left]]);
            }
            left++;
            if (int(d.size()) == 0)
            {
                break;
            }
        }
        res = max(res, right - left + 1);
    }
    return res;
}

int main()
{

    string s = "abccde";
    int result;
    result = longsub(s);
    cout << result;
    return 0;
}

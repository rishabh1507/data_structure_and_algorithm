// #include <bits/stdc++.h>
// using namespace std;

// void MAH(vector<int> arr, int n)
// {
//     // 0 1 2 3 4 5 6
//     // 6 2 5 4 5 1 6
//     // 1 5 3 5 5 7 7
//     //-1-1 1 1 3-1 5
//     // 1 5 1 3 1 7 1
//     // 6,10,5,12,5,7,6
//     stack<pair<int, int>> s;
//     stack<pair<int, int>> s1;
//     // nsr
//     vector<int> nsr1;
//     // nsl
//     vector<int> nsl1;
//     vector<int> v;

//     // nsr
//     for (int i = n - 1; i >= 0; i--)
//     {
//         if (s.size() == 0)
//         {
//             nsr1.push_back(n);
//         }
//         else if (s.size() > 0 && s.top().first < arr[i])
//         {
//             nsr1.push_back(s.top().second);
//         }
//         else if (s.size() > 0 && s.top().first >= arr[i])
//         {
//             while (s.size() > 0 && s.top().first >= arr[i])
//             {
//                 s.pop();
//             }
//             if (s.size() == 0)
//             {
//                 nsr1.push_back(n);
//             }
//             else
//             {
//                 nsr1.push_back(s.top().second);
//             }
//         }
//         s.push({arr[i], i});
//     }
//     reverse(nsr1.begin(), nsr1.end());

//     // nsl
//     for (int i = 0; i < n; i++)
//     {
//         if (s1.size() == 0)
//         {
//             nsl1.push_back(-1);
//         }
//         else if (s1.size() > 0 && s1.top().first < arr[i])
//         {
//             nsl1.push_back(s1.top().second);
//         }
//         else if (s1.size() > 0 && s1.top().first >= arr[i])
//         {
//             while (s1.size() > 0 && s1.top().first >= arr[i])
//             {
//                 s1.pop();
//             }
//             if (s1.size() == 0)
//             {
//                 nsl1.push_back(-1);
//             }
//             else
//             {
//                 nsl1.push_back(s1.top().second);
//             }
//         }
//         s1.push({arr[i], i});
//     }

//     for (int l = 0; l < n; l++)
//     {
//         v.push_back((nsr1[l] - nsl1[l] - 1) * arr[l]);
//         // 	cout<<v[l]<<" ";
//     }
//     cout << *max_element(v.begin(), v.end()) << "\n";
// }

// int main()
// {
//     vector<int> arr;
//     int t;
//     int n;
//     int temp;
//     cin >> t;
//     for (int i = 0; i < t; i++)
//     {
//         cin >> n;
//         for (int j = 0; j < n; j++)
//         {
//             cin >> temp;
//             arr.push_back(temp);
//         }
//         MAH(arr, n);
//     }
//     return 0;
// }

#include <bits/stdc++.h>
using namespace std;

// 0 1 2 3 4 5 6
// 6 2 5 4 5 1 6
// 1 5 3 5 5 7 7
//-1-1 1 1 3-1 5
// 1 5 1 3 1 7 1
// 6,10,5,12,5,7,6
void fillleft(vector<int> &hist, vector<int> &left)
{

    stack<int> s;
    int extreme = -1;
    for (int i = 0; i < hist.size(); i++)
    {
        if (s.empty())
        {
            left.push_back(extreme);
        }
        else if (hist[s.top()] < hist[i])
        {
            left.push_back(s.top());
        }
        else
        {
            while (!s.empty() && hist[s.top()] >= hist[i])
            {
                s.pop();
            }
            if (s.empty())
            {
                left.push_back(extreme);
            }
            else
            {
                left.push_back(s.top());
            }
        }
        s.push(i);
    }
}

void fillright(vector<int> &hist, vector<int> &right)
{

    stack<int> s1;
    int extreme = hist.size();
    for (int i = hist.size(); i >= 0; i--)
    {
        if (s1.empty())
        {
            right.push_back(extreme);
        }
        else if (hist[s1.top()] < hist[i])
        {
            right.push_back(s1.top());
        }
        else
        {
            while (!s1.empty() && hist[s1.top()] >= hist[i])
            {
                s1.pop();
            }
            if (s1.empty())
            {
                right.push_back(extreme);
            }
            else
            {
                right.push_back(s1.top());
            }
        }
        s1.push(i);
    }
    reverse(right.begin(), right.end());
}

int main()
{
    int t;
    cin >> t;
    int n;

    while (t > 0)
    {
        cin >> n;
        vector<int> hist(n);
        vector<int> left;
        vector<int> right;
        vector<int> area;

        for (int i = 0; i < n; i++)
        {
            cin >> hist[i];
        }

        fillleft(hist, left);
        fillright(hist, right);

        for (int j = 0; j < n; j++)
        {
            int width = right[j] - left[j] - 1;
            int answer = hist[j] * width;
            area.push_back(answer);
        }
        cout << *max_element(area.begin(), area.end()) << endl;
        t--;
    }
    return 0;
}

/*
Complexity Analysis :                         Verdict : Accepted
Time Complexity: O(N). Since every bar is pushed and popped only once, the time complexity of this method is O(n).
Space Complexity: O(N). N size stack used.
*/
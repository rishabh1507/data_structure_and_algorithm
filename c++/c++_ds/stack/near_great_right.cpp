// #include <bits/stdc++.h>
// using namespace std;

// vector<int> near_great_right(int arr[], int n){
//     // make a stack and vector
//     stack<int>s;
//     vector<int>arr2;

//     for(int i=n-1;i>=0;i--){
//         if(s.size()==0){
//             arr2.push_back(-1);
//         }
//         else if (s.size() > 0 && s.top() > arr[i])
//         {
//             arr2.push_back(s.top());
//         }
//         else if (s.size() > 0 && s.top()<=arr[i])
//         {
//             while (s.size() > 0 && s.top() <= arr[i])
//             {
//                 s.pop();
//                 if(s.size()==0){
//                     arr2.push_back(-1);
//                 }
//                 else{
//                     arr2.push_back(s.top());
//                 }
//             }
//         }
//         s.push(arr[i]);
        
//     }
//     return arr2;

// }

// int main()
// {
// // 1 3 0 0 1 2 4
// // 3 4 1 1 2 4 -1

//     int n=7;
//     int arr[] = {1 ,3 ,0 ,0 ,1 ,2 ,4};
//     // cin >> n;
//     vector<int>result;
//     // for (int i =0 ;i<n;i++)
//     // {
//     //     cin>>arr[i];
//     // }
//     result = near_great_right(arr, n); 
//     for (int i = 0; i < result.size(); i++)
//     {
//         cout<< result[i]<<" ";
//     }
//     return 0;
// }
#include <bits/stdc++.h>
using namespace std;

vector<int> NGR(vector<int> arr)
{
    vector<int> arr2;
    stack<int> s;
    int n = arr.size();
    for (int i = n - 1; i > -1; i--)
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
    reverse(arr2.begin(), arr2.end());
    return arr2;
}

int main()
{
    vector<int> arr = {1, 3, 0, 0, 1, 2, 4};
    vector<int> result;
    result = NGR(arr);
    for (int i = 0; i < result.size(); i++)
    {
        cout << result[i] << " ";
    }
    return 0;
}
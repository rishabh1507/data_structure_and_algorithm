#include<bits/stdc++.h>
using namespace std;

vector<double> avg(vector<int> arr,float k)
{
    vector<double> result1;
    int left = 0;
    int right = 0;
    double res = 0;
    int n = arr.size();
    double curr;
    while(right <k && right<n){
        res += arr[right];
        right++;
    }
    result1.push_back(res/k);
    curr = res;
    while(right<n){
        curr += arr[right];
        curr -= arr[left];
        result1.push_back(curr/k);
        left ++;
        right +=k; 
    }
    return result1;
}

int main(){
    vector <int> arr{5,4,3,2,1,6,7};
    float k = 3;
    vector<double> result;
    result = avg(arr,k);
    for(auto i: result){
        cout<<i<<" ";
    }

    return 0;
}
// #include <iostream>
// #include <vector>
// using namespace std;

// class SWP_Problem01
// {
// public:
//     static vector<double> findAveragesOfSubarrays(const vector<int> &arr, int k)
//     {
//         vector<double> result(arr.size() - k + 1);
//         double windowSum = 0;
//         int windowStart = 0;
//         for (int windowEnd = 0; windowEnd < arr.size(); windowEnd++)
//         {
//             windowSum += arr[windowEnd];
//             if (windowEnd >= k - 1)
//             {
//                 result[windowStart] = windowSum / k;
//                 windowSum -= arr[windowStart];
//                 windowStart++;
//             }
//         }
//         return result;
//     }
// };

// int main(int argc, char *argv[])
// {
//     int k = 5;
//     vector<double> result = SWP_Problem01::findAveragesOfSubarrays(vector<int>{5, 4, 3, 2, 1, 6, 7}, k);
//     for (double r : result)
//     {
//         cout << r << " ";
//     }
//     cout << endl;
// }
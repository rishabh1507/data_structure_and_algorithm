#include<bits/stdc++.h>
using namespace std;

int subarrayK(vector<int> arr,int k)
{
    int left = 0;
    int right = 0;
    int res = 0;
    int n = arr.size();
    int curr;
    while(right<n-1 && right<k){
        res += arr[right];
        right++;
    }
    curr =  res;
    while(right<n){
        curr +=arr[right];
        curr -=arr[left];
        res = max(res,curr);
        right++;
        left++;
    }
    return res;
}

    int main()
{
    int result;
    vector<int>arr{2, 1, 5, 1, 3, 2};
    int k =3;
    result = subarrayK(arr,k);
    cout<<result;
    return 0;
}
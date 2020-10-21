#include<bits/stdc++.h>
using namespace std;

int substr1(string s, int k){
    unordered_map<char,int> d;
    int left =0;
    int right =0;
    int res=0;
    int n = s.size();

    // make loop
    for(int i=0;i<n;i++){
        d[s[i]]++;
        while((int)d.size()>k){
            if(d[s[left]]==0){
                d.erase(s[left]);
            }
            else{
                d[s[left]]--;
            }
            left++;
        }
        res = max(res,i-left+1); 
    }
    return res;
}


int main(){
    string s = "araaci";
    int k = 2;
    int result = substr1(s,k);
    cout<<result;

    return 0;
}
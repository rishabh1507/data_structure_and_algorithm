#include<bits/stdc++.h>
using namespace std;

vector<int> kfreq(int* arr,int n,int k){
	unordered_map<int,int> mp;
	vector<int>rest;
	priority_queue<pair<int,int>,vector<pair<int,int>>,greater<pair<int,int>>> q;
	for(int i=0;i<n;i++){
		mp[arr[i]]++;
	}
	
	for(auto m:mp){
		q.push({m.second,m.first});
		if(q.size()>k){
			q.pop();
		}
	}
	while(q.size()>0){
		rest.push_back(q.top().second);
		q.pop();
	}
	return rest;
}


int main(){
	int n;
	int k;
	int arr[10000];
	cin>>n;
	cin>>k;
	vector<int>result(k);
	for(int i=0;i<n;i++){
		cin>>arr[i];
	}
	result = kfreq(arr,n,k);
	for(auto t:result){
		cout<<t<<" ";
	}
	
	
	return 0;
}
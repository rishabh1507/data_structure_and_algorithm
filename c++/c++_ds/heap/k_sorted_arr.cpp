#include<bits/stdc++.h>
using namespace std;

int main(){
	int arr[10000];
	vector<int>res;
	int n;
	int k;
	int temp;
	cin>>n;
	cin>>k;
	for(int i=0;i<n;i++){
		cin>>arr[i];
	}
	priority_queue<int,vector<int>,greater<int>> q;
	// priority_queue<int> q;
	for(int i=0;i<n;i++){
		q.push(arr[i]);
		
		if(q.size()>k){
			temp = q.top();
			q.pop();
			res.push_back(temp);
		}
	}
	while(q.size()>0){
		temp =q.top();
		q.pop();
		res.push_back(temp);
	}
	for(int i=0;i<n;i++){
		cout<<res[i]<<" ";
	}
	
	return 0;
}
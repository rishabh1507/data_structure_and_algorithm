#include<bits/stdc++.h>
using namespace std;

int main(){
	int arr[10000];
	int n;
	int k;
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
			q.pop();
		}
	}
	while(q.size()>0){
		cout<<q.top()<<" ";
		q.pop();
	}
	
	return 0;
}
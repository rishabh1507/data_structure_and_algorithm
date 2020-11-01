#include<bits/stdc++.h>
using namespace std;

int main(){
	int arr[10000];
	vector<int>res;
	int n;
	int k;
	int k1;
	int temp;
	int key;
	cin>>n;
	cin>>k;
	cin>>k1;
	for(int i=0;i<n;i++){
		cin>>arr[i];
	}
	// priority_queue<int,vector<int>,greater<int>> q;
	priority_queue<pair<int,int>> q;
	for(int i=0;i<n;i++){
		key = abs(k-arr[i]);
		q.push({key,arr[i]});
		
		if(q.size()>k1){
			q.pop();
		}
	}
	while(q.size()>0){
		temp=q.top().second;
		cout<<temp<<" ";
		q.pop();
	}
	return 0;
}
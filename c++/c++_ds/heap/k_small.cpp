#include<bits/stdc++.h>
using namespace std;



int main(){
	int arr[1000];
	int n;
	int k;
	cin>>n;
	cin>>k;
	
	priority_queue <int> q;
	for(int i=0;i<n;i++){
		cin>>arr[i];	
	}
	
	for(int i=0;i<n;i++){
		q.push(arr[i]);
		
		if(q.size()>k){
			q.pop();
		}
	}
	cout<<q.top();
	
	
	
	return 0;
}
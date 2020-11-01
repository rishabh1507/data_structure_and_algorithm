#include<bits/stdc++.h>
using namespace std;

int main(){
	int n;
	cin>>n;
	int arr[10000];
	int temp1;
	int temp2;
	int sum1;
	int total =0;
	for(int i=0;i<n;i++){
		cin>>arr[i];
	}
	priority_queue<int,vector<int>,greater<int>> q;
	for(int i=0;i<n;i++){
		q.push(arr[i]);
	}
	while(q.size()>=2){
		temp1=q.top();
		q.pop();
		temp2=q.top();
		q.pop();
		sum1 = temp1 + temp2;
		q.push(sum1);
		total +=sum1;
	}
	cout<<total;
	return 0;
}
#include<bits/stdc++.h>
using namespace std;

int elem(int *arr,int num,int n){
	priority_queue<int>q;
	int temp1;
	for(int i=0;i<n;i++){
		q.push(arr[i]);
		if(q.size()>num){
			q.pop();
		}
	}
	temp1 = q.top();
	return temp1;
}

int main(){
	int n;
	int num1;
	int num2;
	int arr[10000];
	cin>>n;
	cin>>num1;
	cin>>num2;
	int result1;
	int result2;
	int sum1;
	for(int i=0;i<n;i++){
		cin>>arr[i];
	}
	
	result1 = elem(arr,num1,n); 
	result2 = elem(arr,num2,n);
	for(int i=0;i<n;i++){
		if(arr[i]>result1 && arr[i]<result2)
		{
			sum1 +=arr[i];
		}
	}
	cout<<result1<<" "<<result2;
	return 0;
}
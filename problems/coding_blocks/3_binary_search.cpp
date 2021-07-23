#include <bits/stdc++.h>
using namespace std;


int binary_search(int key,int arr[],int n){
	int start = 0;
	int end = n-1;
	
	while(start<=end){
		int mid;
		mid = (start + end)/2;
		
		if(arr[mid]<key){
			start = mid+1;
		}
		if(arr[mid]>key){
			end = mid-1;
		}
		if(arr[mid] == key){
			return arr[mid];
		}	
		
	}
	return 0;
	
	
}

int main()
{
	int n;
	cin>>n;

	int arr[1000];

	for(int i=0;i<n;i++) {
		cin>>arr[i];
	}
	
	int key;
	cin>>key;
	cout<<binary_search(key,arr,n);
	
	
	return 0;
}

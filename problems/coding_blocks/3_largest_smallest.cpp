#include <bits/stdc++.h>
using namespace std;


int main()
{
	int n;
	cin>>n;
	
	int arr[1000];

	for(int i=0;i<n;i++) {
		cin>>arr[i];
	}
	
	int largest = INT_MIN;
	int smallest = INT_MAX;
	
	for(int i=0;i<n;i++) {
		if(arr[i]>largest){
			largest = arr[i]; 
		}
		if(arr[i]<smallest){
			smallest = arr[i]; 
		}
		// Can also be unsigned
		//largest = max(largest,a[i]);
		//smallest = min(smallest,a[i]);
	}
	
	cout<<largest<<" "<<smallest;
	
	
	return 0;
}

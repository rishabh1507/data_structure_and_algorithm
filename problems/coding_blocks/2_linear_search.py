#include <bits/stdc++.h>
using namespace std;


int main()
{
	int n;
	cin>>n;
	int key;
	cin>>key;
	int arr[1000];
	int i;
	for(i=0;i<n;i++) {
		cin>>arr[i];
	}
	
	for(i=0;i<=n-1;i++){
		if(arr[i]==key){
			cout<<key;
			break;
		}
	}
	if(i==n) {
		cout<< "Not Found";
	}
	
	return 0;
}

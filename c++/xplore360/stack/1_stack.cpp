#include <bits/stdc++.h>
using namespace std ;
    void push(int &top,int val,int n,int arr[]){
    	if(top >= n-1){
    		cout<<"overflow";
    	}
    	else{
    		top++;
    		arr[top] = val;
    	}
	}
	void pop(int &top){
		if(top <= -1){
			cout<<"underflow";
		}
		else{
			top--;
		}

	}
	void top1(int arr[],int &top){
		cout<<arr[top];
	}
	void empty(int arr[], int &top){
		if(top==-1){
			cout<<"empty"<<"true";
		}
		else{
			cout<<"false";
		}
	}
	void size1(int &top){
		cout<<top;
	}


int main(){
	#ifndef ONLINE_JUDGE
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	#endif

	
	int n=100;
	int arr[100];
	int top = -1;
	push(top,5,n,arr);
	pop(top);
	top1(arr,top);
	empty(arr,top);
	size1(top);
	cout<<arr[0];
	cout<<"end";
}
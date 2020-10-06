#include<bits/stdc++.h>
using namespace std;

void showstack(stack <int> s){

	cout<<s.top()<<endl;
	s.pop();
	cout<<s.size()<<endl;
	cout<<s.empty()<<endl;

	while(!s.empty()){
		cout<<s.top()<<endl;
		s.pop();
	}
} 
int main()
{

	stack <int> s;
	s.push(10);
	s.push(20);
	s.push(30);
	s.push(40);
	s.push(50);
	s.push(60);
	s.push(70);
	s.push(80);

	showstack(s);
	return 0;
}
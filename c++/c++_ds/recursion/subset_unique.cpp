#include<bits/stdc++.h>
using namespace std;
vector<string> st;
void solve(string ip,string op){
	if(ip.length()==0){
		st.push_back(op);
		return ;
	}
	string op1 = op;
	string op2 = op;
	op2.push_back(ip[0]);
	ip.erase(ip.begin()+0);
	
	solve(ip,op1);
	solve(ip,op2);
}

int main(){
	string ip;
	cin>>ip;
	string op="";
	solve(ip,op);
	map<string,int> mp;
	vector<string> st2;
	map<string, int>::iterator it ; 
	for(int i=0;i<st.size();i++){
		it = mp.find(st[i]); 
      
    	if(it == mp.end()){
    		mp[st[i]]++;
    		st2.push_back(st[i]);
    	}
	}
	for(int i=0;i<st2.size();i++){
		cout<<st2[i]<<" ";
	}
	
}
#include <bits/stdc++.h>
using namespace std;

vector <int> near_great_left(stack <int> s,vector<int> v){
	if(v.empty()){
		return {};
	}
	else{
		vector<int> v2;
		// s.push(v[v.size()-1]);
		// cout<<s.top()<<"1--";
		for (int i =v.size()-1;i>=0;i--){
			if(s.size() ==0){
				v2.push_back(-1);
				// s.push_back(v[i]);
			}
			if(s.size()>0 && s.top()>=v[i]){
				v2.push_back(s.top());
				s.push(v[i]);	
			}
			else if(s.size()>0 && s.top()<=v[i]){
				while(s.size()>0 && s.top()<=v[i]){
					s.pop();
					if(s.size()==0){
						v2.push_back(-1);
					}
					else{
						v2.push_back(s.top());
					}
				}
			}
			v2.push_back(v[i]);
		}
		for (int i =v2.size()-1;i>0;i--){
			cout<<v2[i]<<"\n";
		}
		return v2;
	}
}

int main(){
	#ifndef ONLINE_JUDGE
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	#endif
	
	stack <int> s;
	vector<int> v;
	int n; cin>>n;
	int val;
	for (int i=0;i<n;i++){
		cin>>val;
		v.push_back(val);
	}
	near_great_left(s,v);
	return 0;
}
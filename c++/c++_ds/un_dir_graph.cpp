#include<bits/stdc++.h>
using namespace std;
// add edjes 
// print graph
void add_edges(vector<int> adj [],int u,int v){
    adj[u].push_back(v);
    adj[v].push_back(u);
}
void printGraph(vector<int> adj[],int V){
    // itterate V
    for(int i=0;i<V;i++){
        for(auto x: adj[i]){
            cout<<x<<" ";
        }
        cout<<"\n";
    }
}

    int main()
{

    int V = 5;
    vector<int> adj[V];
    add_edges(adj,0,1);
    add_edges(adj,0,4);
    add_edges(adj,1,2);
    add_edges(adj,1,3);
    add_edges(adj,1,4);
    add_edges(adj, 2, 3);
    add_edges(adj, 3, 4);
    printGraph(adj,V);
}

#include<bits/stdc++.h>
using namespace std;
struct Edge{
    int src;
    int dsc;
};
class Graph{
    public:
    vector<vector<int>> adjList;
    Graph(vector<Edge>&edges,int N){
        adjList.resize(N);
        for (auto &edge : edges){
            adjList[edge.src].push_back(edge.dsc);
        }
    }
};
void printGraph(Graph &graph,int N){
    for(int i=0;i<N;i++){
        cout<<i<<"-->";
        for(auto v: graph.adjList[i]){
            cout<<v<<" ";
        }
        cout<<"\n";
    }
}
int main(){
    vector<Edge> edges;
    int N = 4;
    edges ={{0,1},{1,2},{2,1},{2,0},{3,2}};
    Graph graph(edges,N);
    printGraph(graph,N);
    return 0;
}
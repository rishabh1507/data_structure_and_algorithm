#include<bits/stdc++.h>
using namespace std;

struct Edge {
    int src;
    int dsc;
    int weight;
};
typedef pair<int, int> Pair;
    
class Graph {
    public:
        vector<vector<Pair>> adjList;
        Graph(vector<Edge>&edges,int N){
            adjList.resize(N);
            for(auto &edge:edges){
                adjList[edge.src].push_back(make_pair(edge.dsc, edge.weight));
            }
        }
};

void printGraph(Graph &graph,int N){
    for(int i=0;i<N;i++){
        cout<<i<<"-->";
        for(Pair v: graph.adjList[i]){
            cout<<i<<" "<<v.first<<" "<<v.second<<" ";
        }
        cout<<"/n";
    }
}

int main() {
    int N = 5;

    vector<Edge> edges;
    edges ={{0,1,6},{1,2,7},{2,0,5},{2,1,4},{3,2,10},{4,5,3},{5,4,1}};
    Graph graph(edges,N);
    printGraph(graph,N);
    return 0;
}
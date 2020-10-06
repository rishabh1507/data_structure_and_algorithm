#include<bits/stdc++.h>
using namespace std;
// make a basic binary tree
// 1 make a node
struct Node{
    int data;
    struct Node *left;
    struct Node *right;

    Node(int val){
        data = val;
        left = NULL;
        right = NULL;


    }
};
// make a preorder to print values
void preOrder(struct Node *root){
    // ro lr
    if(root ==nullptr){
        return ;
    }
    cout<<root->data<<" ";
    preOrder(root->left);
    preOrder(root->right);
}
void inOrder(struct Node *root){
    if (root == nullptr)
    {
        return;
    }
    inOrder(root->left);
    cout << root->data << " ";
    inOrder(root->right);
}

void postOrder(struct Node *root){
    if(root ==nullptr){
        return;
    }
    postOrder(root->left);
    postOrder(root->right);
    cout<<root->data<<" ";
}

int main(){
    // make object and insert values
    struct Node *root = new Node(1);
    root->left = new Node(2);
    root->right = new Node(3);
    root->left->left = new Node(4);
    root->left->right = new Node(5);
    root->right->right = new Node(7);
    root->right->left = new Node(6);
    preOrder(root);
    cout<<"\n";
    inOrder(root);
    cout << "\n";
    postOrder(root);
}
#include <bits/stdc++.h>
using namespace std;

struct Node{
    int data;
    struct Node* left;
    struct Node* right;

    Node(int val){
        data = val;
        left = NULL;
        right = NULL;
    }
};
// make a dummy (curr) if not null push left and if null start print top value and pop
void inOrder(struct Node* root){
    // make a stack
    stack<Node*>s;
    struct Node* current = root;
    // if(current == nullptr){
    //     return ;
    // }
    //make a while loop
    while(!s.empty() || current!= nullptr){
        while(current!=nullptr){
            s.push(current);
            current=current->left;
        }
        current =s.top();
        s.pop();
        cout<<current->data<<" ";
        current=current->right;
    }
}
// make a stack insert root and check while 
// stack not empty store top in node and push is right and left
void preOrder(struct Node* root){
    // make a empty stack and push root  if stack not empty push left and right
    stack<Node*> st;
    st.push(root);
    // if(root == nullptr){
    //     return nullptr;
    // }

    while(!st.empty()){
        struct Node* current = st.top();
        cout<<current->data<<" ";
        st.pop();

        if (current->right != nullptr)
        {
            st.push(current->right);
        }
        if(current->left !=nullptr){
            st.push(current->left);
        }
        
    }   
}

Node* insertNode(struct Node*root,int data){
    if(root==nullptr){
        root = new Node(data);
        return root;
    }
    else{
        queue<Node*>q;
        q.push(root);

        while(!q.empty()){
            struct Node* current = q.front();
            q.pop();
            if(current->left !=nullptr){
                q.push(current->left);
            }
            else{
                current->left = new Node(data);
                return root;
            }

            if (current->right != nullptr)
            {
                q.push(current->right);
            }
            else
            {
                current->right = new Node(data);
                return root;
            }
        }
    }
}
// left right root => root right left same procedure as preorder
void postOrder(struct Node* root){
    stack<Node*> st1;
    st1.push(root);
    stack<Node*> st2;

    if(root == nullptr){
        return ;
    }
    // root left right
    // left right root = root right left
    while(!st1.empty()){
        struct Node* current = st1.top();
        st1.pop();
        st2.push(current);
        
        if(current->left != nullptr){
            st1.push(current->left);
        }

        if (current->right != nullptr)
        {
            st1.push(current->right);
        }
    }

    while(!st2.empty()){
        cout<<st2.top()->data<<" ";
        st2.pop();
    }



}

int main()
{
    struct Node *root = new Node(1);

    root->left = new Node(2);
    root->right = new Node(3);
    root->left->left = new Node(4);
    root->left->right = new Node(5);
    root->right->left = new Node(6);
    root->right->right = new Node(7);
    postOrder(root);

    return 0;
}
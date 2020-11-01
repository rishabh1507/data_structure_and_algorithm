// #include <bits/stdc++.h>
// using namespace std;

// struct Node{
// 	int data;
// 	struct Node* left;
// 	struct Node* right;
	
// 	Node(int val){
// 		data = val;
// 		left = NULL;
// 		right = NULL;
// 	}
// };
// void display( struct Node* head){
// 	struct Node* temp = head;
// 	if (temp == NULL) 
//         return; 
//     cout << temp->data << " "; 
  
//     display(temp->left);  
//     display(temp->right);
	
// }

// int main(){
// 	struct Node* head;
// 	struct Node* root = new Node(1);
// 	root->left = new Node(2);
// 	root->right= new Node(3);
// 	root->left->left = new Node(4);
// 	root->left->right = new Node(5);
// 	root->right->left = new Node(6);
// 	root->right->right = new Node(7);
// 	head = root;
// 	display(head);
// 	return 0;
// }
#include <bits/stdc++.h>
using namespace std;

struct Node
{
	int data;
	Node *left;
	Node *right;

	Node(int val)
	{
		data = val;
		left = NULL;
		right = NULL;
	}
};

void display(Node *root)
{
	if (root == NULL)
	{
		return;
	}
	cout << root->data;
	display(root->left);
	display(root->right);
}

int main()
{
	Node *root = new Node(1);
	root->left = new Node(2);
	root->right = new Node(3);
	root->left->left = new Node(4);
	root->left->right = new Node(5);
	root->right->left = new Node(6);
	root->right->right = new Node(7);
	display(root);
	return 0;
}
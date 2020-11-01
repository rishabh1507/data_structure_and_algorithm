#include<bits/stdc++.h>
using namespace std;

struct Node{
	int data;
	Node* next;
};

class LinkedList{
	Node *head;
	
	public:
		LinkedList(){
			head = NULL;	
		}
	
	void insert(int a){
		Node* newNode = new Node;
		newNode->data = a;
		newNode->next = NULL;
		
		if(head==NULL){
			head = newNode;
		}
		else{
			newNode->next = head;
			head = newNode;
			
		}
	}
	void remove(int a){
		if(head->data==a){
			delete head;
			head = head->next;
		}
		if(head->next == NULL){
			if(head->data == a){
				delete head;
				head = NULL;
				return ;
			}
		}
		Node* temp = head;
		while(temp->next != NULL){
			if(temp->next->data == a){
				Node* temp_ptr = temp->next->next;
				delete temp->next;
				temp->next = temp_ptr;
				return;
			}
			temp = temp->next;
		}
		
		
	}

	void display(){
		while(head!= NULL){
			cout<<head->data<<" ";
			head = head->next;
		}
	}
};


int main(){
	LinkedList l;
	l.insert(1);
	l.insert(2);
	l.insert(3);
	l.insert(4);
	l.insert(5);
	l.insert(6);
	l.insert(7);
	l.insert(8);
	// l.insert(9);
	// l.insert(10);
	l.remove(2);
	l.display();
	
	return 0;
	
}
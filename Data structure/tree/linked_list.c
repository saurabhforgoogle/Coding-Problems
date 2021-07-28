// A simple C program for traversal of a linked list 
#include <stdio.h> 
#include <stdlib.h> 

struct Node { 
	int data; 
	struct Node* next; 
};

int main(){

struct Node* A;
A=NULL;

int n;
printf("How many more you want to add");
scanf("%d",&n);
while(n>0){
    n=n-1;
    int value;
    printf("\n");
    printf("Enter Next Digit");
    scanf("%d",&value);
    struct Node* temp=(struct Node*)malloc(sizeof(struct Node));
    temp->data=value;
    temp->next=NULL;

    struct Node* temp1;
    temp1=A;
    if(A==NULL){
        A=temp;
    }
    else{
        while(temp1->next!=NULL){
            temp1=temp1->next;
        }
        temp1->next=temp;
    }
    
}
struct Node* temp1;
temp1=A;
printf(" %d",temp1->data);
while(temp1->next!=NULL){
    
    temp1=temp1->next;
    printf(" %d",temp1->data);
    }

return 0;
}

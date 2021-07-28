#include <stdio.h> 
#include <stdlib.h> 
#include<time.h>
struct Node { 
	int data; 
	struct Node* next; 
};

int main(){

struct Node* A;
A=NULL;

int n;

printf("\n How many more you want to add(Under 50);Else REDUCED TO 50 \n");
scanf("%d",&n);
if(n>50){
    n=50;
}
srand(time(0));
while(n>0){
    n=n-1;
    int value;
    //printf("\n");
    //printf("Enter Next Digit");
    //scanf("%d",&value);
    //Random Value Taken
    value=rand()%501;
    printf("Adding %d to linked list \n",value);

    struct Node* temp=(struct Node*)malloc(sizeof(struct Node));
    temp->data=value;
    temp->next=NULL;

    struct Node* temp1;
    
    if(A==NULL){
        A=temp;
    }
    else{
        temp1=A;
        struct Node* prev;
        while((temp1->data<=value)&(temp1->next!=NULL)){
            prev=temp1;
            temp1=temp1->next;
        }
        if(temp1==A){
            if(temp1->data<=value){
                temp1->next=temp;
            }
            else{
                temp->next=temp1;
                A=temp;
            }
        }
        else if(temp1->data>value){
            prev->next=temp;
            temp->next=temp1;
        }
        else{
            temp1->next=temp;
        }
        
    }
    
}
printf("Linked List: \n");
struct Node* temp1;
temp1=A;
printf(" %d",temp1->data);
while(temp1->next!=NULL){
    
    temp1=temp1->next;
    printf(" %d",temp1->data);
    }

return 0;
}

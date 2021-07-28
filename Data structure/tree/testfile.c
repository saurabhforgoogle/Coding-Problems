// A simple C program for traversal of a linked list 
#include <stdio.h> 
#include <stdlib.h> 


int main() 
{ 
    int *p;
    //p=(int*)malloc(sizeof(int));
    //p=4;

    p=(int*)malloc(5*sizeof(int));
    p[0]=5;
    for(int i=0;i<=5;i++){
        p[i]=3;
        printf(" %d",p[i]);
    }
    
	return 0; 
}



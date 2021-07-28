#include <stdio.h>
int main() {
   int x=0,y=1,z,n;
    printf("Fibbonacci Number Sequence till:");
    scanf("%d",&n);
    while(x<n){
        printf(" %d",x);
        z=x+y;
        x=y;
        y=z;
    }
   return 0;
}

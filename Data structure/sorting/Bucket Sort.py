def BUCKET_SORT(A):
    largest=max(A)+1
    n=len(A)
    for i  in range(n):
        A[i]=A[i]/largest
    
    B=[[0] for i in range(n)]
    for i in range(0,n):
        B[int(n*A[i])].append(A[i])
    for i in range(0,n):
        B[i]=Insertion(B[i])
    A=[]
    for i in range(0,n):
        A.extend([x*largest for x in B[i][1:]])
    return A

def Insertion(list1):
    m=len(list1)
    for j in range(1,m):
        key=list1[j]
        i=j-1
        while i>=0 and list1[i]>key:
            list1[i+1]=list1[i]
            i=i-1
        list1[i+1]=key
    return list1

import random
A=[random.randint(1,1000) for i in range(1000)]
print(BUCKET_SORT(A))
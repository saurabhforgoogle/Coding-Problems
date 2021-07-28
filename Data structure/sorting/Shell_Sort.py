
import random 
def ShellSort(A):
    n=len(A)
    gaps=[]
    gaps.append(n//2)
    while(gaps[-1]!=1):
        gaps.append(gaps[-1]//2)
    for gap in gaps:
        for i in range(0,n-gap):
            if A[i]>A[i+gap]:
                A[i],A[i+gap]=A[i+gap],A[i]
    return A

A=[random.randint(1,10) for i in range(10)]
print(A)
print(ShellSort(A))

'''
import random 
def ShellSort(A):
    n=len(A)
    gaps=[]
    gaps.append(n//2)
    while(gaps[-1]!=1):
        gaps.append(gaps[-1]//2)
    for gap in gaps:
        for i in range(gap,n):
            temp=A[i]
            for j in range(i,gap,-1):
                if A[j-gap]>temp:
                    A[j]=A[j-gap]
                else: break
                A[j]=temp
    return A

     

A=[random.randint(1,10) for i in range(10)]
print(A)
print(ShellSort(A))

'''
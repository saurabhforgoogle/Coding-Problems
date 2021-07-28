import matplotlib.pyplot as plt   
import time  
import numpy as np
datas=[]
for n in [100,1000,2500,5000,7500,10000]:
    datas.append([x for x in range(n,0,-1)])
results=[[0],[0],[0]]

def Insertion(list1):

    for j in range(1,len(list1)):
        key=list1[j]
        i=j-1
        while i>=0 and list1[i]>key:
            list1[i+1]=list1[i]
            i=i-1
        list1[i+1]=key
def merge(list1,p,q,r):
    n1=q-p+1
    n2=r-q
    L=[]
    R=[]
    for i in range(0,n1):
        L.append(list1[p+i])
    for j in range(0,n2):
        R.append(list1[q+j+1])
    #L.append(10000000)
    #R.append(10000000)
    i=j=0
    k=p

    while i<n1 and j<n2:
        if L[i]<=R[j]:
            list1[k]=L[i]
            i+=1
        else:
            list1[k]=R[j]
            j+=1
        k+=1


    while i < n1: 
        list1[k] = L[i] 
        i += 1
        k += 1
        
    while j < n2: 
        list1[k] = R[j] 
        j += 1
        k += 1
def merge_sort(list1,p,r):
    if p<r:
        q=int((p+r)//2)
        merge_sort(list1,p,q)
        merge_sort(list1,q+1,r)
        merge(list1,p,q,r)
    #return list1
def countingsort(arr):
    k=max(arr)
    c=[0 for i in range(k+1)]

    for j in range(0,len(arr)):
        c[arr[j]]=c[arr[j]]+1

    for i in range(1,k+1):
        c[i]=c[i]+c[i-1]

    b=[0 for i in range(n)]
    for element in reversed(arr):
        b[c[element]-1]=element
        c[element]=c[element]-1
    return b



for data in datas:
    for loop in range(3):
        t1=time.time()
        Insertion(data)
        t2=time.time()
        merge_sort(data,0,len(data)-1)
        t3=time.time()
        countingsort(data)
        t4=time.time()
        results[0][-1]+=(t2-t1)
        results[1][-1]+=(t3-t2)
        results[2][-1]+=(t4-t3)

    results[0].append(0)
    results[1].append(0)
    results[2].append(0)
results=np.array(results)
results=results/3.00
plt.plot([100,1000,2500,5000,7500,10000],results[0][:-1],label='Insertion Sort')
plt.plot([100,1000,2500,5000,7500,10000],results[1][:-1],label='Merge Sort')
plt.plot([100,1000,2500,5000,7500,10000],results[2][:-1],label='Counting Sort')
plt.legend()
plt.show()
#c lang linked list and tree easy using llist
n=int(input("enter no of digits"))
list1=[]
list1.append(0)
for i in range(n):
    m=int(input("enter next digit"))
    list1.append(m)
i=1
left=2*i
right=2*i+1
def maxheaphy(list1,i):
    l=2*i
    r=2*i+1
    if l<=n and list1[l]>list1[i]:
        largest=l
        print("hell1o",l,r,i,largest)
    else:
        largest=i
        print("hell2o",l,r,i,largest)
    if r<=n and list1[r]>list1[largest]:
        largest=r
        print("hell3o",l,r,i,largest)
    if largest!=i:
        temp=list1[i]
        list1[i]=list1[largest]
        list1[largest]=temp
        print("hello4",l,r,i,largest)
        if largest<=int(n/2):#not in the leaves
            maxheaphy(list1,largest)#i have checked print situations for debugging. at last,one more def  to confirm
            #pass
        #maxheaphy(list1,1) no need since maxheaphy only at one position.
    #for k in range(1,n+1):
        #print(list1[k])
        return list1
#maxheaphy(list1,1)
#for k in range(1,n+1):
    #print(list1[k])

global n
n=int(input("enter no of digits"))
list1=[]
list1.append(0)
for i in range(n):
    m=int(input("enter next digit"))
    list1.append(m)
i=1
left=2*i
right=2*i+1
t=n
list2=[]
def maxheaphy(list1,i):
    global n
    l=2*i
    r=2*i+1
    if l<=n and list1[l]>list1[i]:
        largest=l
    else:
        largest=i
    if r<=n and list1[r]>list1[largest]:
        largest=r
    if largest!=i:
        temp=list1[i]
        list1[i]=list1[largest]
        list1[largest]=temp
        if largest<=int(n/2):#not in the leaves
            maxheaphy(list1,largest)
        return list1
def build_max_heap(list1):
    global n
    for i in range(n//2,0,-1):
        maxheaphy(list1,i)
    return list1
def heapsort(list1):
    global n
    build_max_heap(list1)
    for i in range(t,1,-1):
        temp=list1[1]
        list1[1]=list1[i]
        list1[i]=temp
        list2.append(list1[i])
        n=n-1
        maxheaphy(list1,1)
    list2.append(list1[1])
    return list2
heapsort(list1)
print("The sorted list in descending order using heap is:")
for k in range(t):
    print(list2[k])
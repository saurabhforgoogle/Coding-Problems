n=int(input("enter no of digits"))
list1=[]
#m=n+1
for i in range(n):
    m=int(input("enter next digit"))
    list1.append(m)
    #m=m-1
for j in range(1,n):
    key=list1[j]
    i=j-1
    while i>=0 and list1[i]>key:
        list1[i+1]=list1[i]
        i=i-1
    list1[i+1]=key
#for i in range(n):
    #print(list1[i])
print(list1)
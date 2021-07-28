arr=[]
n=int(input("Enter nos. in total"))
#m=n+1
for i in range(n):
    m=int(input("enter ext no."))
    arr.append(m)
    #m=m-1
for i in range(n-1):
    min=i
    for j in range(i,n):
        if arr[j]<arr[i]:
            min=j
    if min!=i:
        temp=arr[min]
        arr[min]=arr[i]
        arr[i]=temp

print(arr)
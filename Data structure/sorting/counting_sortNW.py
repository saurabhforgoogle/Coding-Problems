n = int(input("enter no of digits"))
import random
arr = []
for i in range(n):
    arr.append(random.randint(1,2*n))
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
print(b)


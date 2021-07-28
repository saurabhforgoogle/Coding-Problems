#import random
#Not using random since it can have any sequence of best to worst, so we take descending nos,
#WORST CASE
import time
for k in range(100,2101,500):
    start = time.process_time()
    #n=int(input("enter no of digits"))
    list1=[]
    n=k
    m=k+1
    for i in range(n):
        #m=int(input("enter next digit"))
        #m=random.randint(1,10000)
        list1.append(m)
        m=m-1
    for j in range(1,n):
        key=list1[j]
        i=j-1
        while i>=0 and list1[i]>key:
            list1[i+1]=list1[i]
            i=i-1
        list1[i+1]=key
        end=time.process_time()
#for i in range(n):
    #print(list1[i])
#print(list1)
    t=(k*k)/10000
    t=t/10000
    print((end - start)/t)
    #actually we are finding constant from it by time/o(n^2)
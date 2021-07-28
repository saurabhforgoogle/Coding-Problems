A=[]
B=[]
import random
p=random.randint(2,6)
q=random.randint(2,6)
r=random.randint(2,6)
for i in range(p):
        A.append([random.randint(1,20) for j in range(q)])
for i in range(q):
        B.append([random.randint(1,20) for j in range(r)])

C=[]
for i in range(len(A)):
    C.append([0 for j in range(len(B[0]))])
if len(A[0])==len(B):
    for i in range(len(A)):
        for j in range(len(B[0])):#Iterate Over B Columns
            for k in range(len(A[0])):#Iterate Over q
                C[i][j] += A[i][k] * B[k][j]
    for x in range(len(C)):
        for y in range(len(C[0])):
            print(C[x][y],end=' ')
        print('\n')

else:
    print('Matrix Not same Size')

                

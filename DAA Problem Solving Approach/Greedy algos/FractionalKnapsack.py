N=int(input('Enter Number Of Items\n'))
Arr=[]
for i in range(N):
    Weight,Value=map(int,input('Enter Naxt W and V\n').split())
    Arr.append([Weight,Value,Value/Weight])
W=int(input('Enter Maximum Weight:\t'))
Arr=sorted(Arr,key=lambda x:x[2],reverse=True)
left_weight=W
total_value=0
for item in Arr:
    if item[0]<=left_weight:
        total_value+=item[1]
        left_weight-=item[0]
    else:
        total_value+=item[2]*left_weight
        break
print('Max Value:{}'.format(total_value))
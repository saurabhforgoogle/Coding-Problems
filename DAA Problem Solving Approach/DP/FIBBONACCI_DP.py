'''
def fibbo(n):
    if n==1 or n==2:
        return 1
    return fibbo(n-1)+fibbo(n-2)

print(fibbo(25))
'''
'''
def fibbo_Memoization(n,data={}):
    if n==1 or n==2:
        return 1
    if n not in data:
        data[n]=fibbo_Memoization(n-1)+fibbo_Memoization(n-2)
    return data[n]

print(fibbo_Memoization(500))

'''
def fibbo_Down2Top(n):
    data=[0,1,1]
    for i in range(3,n+1):
        data.append(data[-1]+data[-2])
    return data[-1]

print(fibbo_Down2Top(50000))
    


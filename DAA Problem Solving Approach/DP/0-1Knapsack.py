#0-1 Knapsack
#recursively take [:-1]elent with or withot taking [-1]th
#memoize same recursion
def Knapsack(W,weight,value,n):
    if (W,n) in memo.keys():
        return memo[(W,n)]
    if W==0 or n==0:
        return 0
    if weight[n-1]>W:
        return Knapsack(W,weight,value,n-1)
    
    calculated=max((value[n-1]+Knapsack(W-weight[n-1],weight,value,n-1)),Knapsack(W,weight,value,n-1))
    memo[W,n]=calculated
    return calculated
import random
memo={}
value = [random.randint(10,100) for x in range(10000)]
weight = [random.randint(10,100) for x in range(10000)]
W = 500
n = len(value)
print(Knapsack(W, weight, value, n))
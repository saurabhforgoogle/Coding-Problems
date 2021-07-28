import sys 
def MatrixChainOrder(p, i, j): 

	if i == j: 
		return 0 #Last when No k in between 

	minimum = sys.maxsize  #Big Value
	for k in range(i, j): #Between a subsequence

		count = (MatrixChainOrder(p, i, k) 
				+ MatrixChainOrder(p, k + 1, j) 
				+ p[i-1] * p[k] * p[j]) #first and k as 1st matrix and k ,end as 2nd matrix taking k as whole in Betwwen calling Recursively

		if count < minimum: 
			minimum = count 
	return minimum

A = [1, 2, 3, 4, 30] #Array of Size of every Matrix A[i-1]*A[i]
n = len(A) 

print("Minimum number of multiplications is ", 
	MatrixChainOrder(A, 1, n-1)) 



###Matrix failed DP
'''

A = [1, 2, 3,4] #Array of Size of every Matrix A[i-1]*A[i]
n = len(A) 
def MatrixChainOrder(p, i, j,table={}): 
    if i == j: 
        return 0 
    minimum = sys.maxsize  
    for k in range(i,j): 
        
        if (i,j) not in table:
            count = (MatrixChainOrder(p, i, k) + MatrixChainOrder(p, k + 1, j) + p[i-1] * p[k] * p[j]) 
            
        #print(table)

        if count < minimum: 
            table[(i,j)]=count 
            minimum = count 
    return minimum



print("Minimum number of multiplications is ", 
	MatrixChainOrder(A, 1, n-1)) 

'''


#DYNAMIC PROGRAMMING 
'''
# This function returns the number of
# arrangements to form 'n'

# lookup dictionary/hashmap is initialized
def solve(n, lookup = {}):
	
	# Base cases
	# negative number can't be 
	# produced, return 0
	if n < 1:
		return 0

	# 0 can be produced by not 
	# taking any number whereas 
	# 1 can be produced by just taking 1
	if n == 0 or n == 1:
		return 1

	# Checking if number of way for
	# producing n is already calculated 
	# or not if calculated, return that,
	# otherwise calulcate and then return
	if n not in lookup:
		lookup[n] = (solve(n - 1) +
					solve(n - 3) +
					solve(n - 5))
					
	return lookup[n]

# This code is contributed by GauriShankarBadola
'''
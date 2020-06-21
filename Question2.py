## creating dummy matrix

A=[[1,11,12],[10,8,3],[7,9,2],[5,4,6]]

## getting the shape of matrix
n,m=len(A),len(A[0])

k=4
'''
Initialize DP table. Note that we only need two rows or two column of size k or n respectively if we just want to get the maximum value. But to reconstruct the indices we need full DP table
'''
x=[[0]*(k+1) for _ in range(n)]
'''
We use the recurrence relation like this.Suppose we have optimal answer for $i-1$ rows picking up j entries. Then for row i, we choose p elements starting from first column and find optimal j-p elements in i-1 rows. We brute-force all possiblities for row i and select the one yielding maximum value. we iterate i from (1,n) and j from (0,k). If j=0, the answer will be zero as we are choosing zero elements.
'''
for i in range(n):
    for p in range(k+1):
            for o in range(p+1):
                x[i][p]=max(x[i-1][p-min(o,m)]+sum(A[i][:min(o,m)]),x[i][p])
print(x[-1][-1])
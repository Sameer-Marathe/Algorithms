import random
## Generate random integers to check the correctness
w= [random.randint(1,20) for _ in range(10)]
n=len(w)
## Calculate mean
mu=sum(w)/n
##bruteforce to check that we are getting the right answer using DP
brute=-float('inf')
for i in range(n):
    for j in range(i,n):
        brute=max(brute,mu*(j-i+1)-sum(w[i:j+1]))
print(brute)
## DP solution 
'''
solution until day j must include day j(to have contiguous intervals). Now there are only two possiblities
- Either day j provides the max deficit
- Day j adds up to maximum deficit of j-1 days.
We take max out of these possibilties.
'''
out=[0]*n
for i in range(n):
    out[i]=max(mu-w[i],mu-w[i]+out[i-1])

'''
Finally day j might not be in the maximum deficit interval. So we linearly scan the array and take maximum deficit as the answer.
'''
print(max(out))

# DynamicProgramming
Answers to some questions in dynamic programming

## Question 1
Being the chief climatologist of your city, you have been given the rainfall data for each day forthe last 100 years in your city. So you have an array <img src="https://render.githubusercontent.com/render/math?math=R[1,...,n]"> where R[i] lists the amount of rainmeasured in your city on the i-th day (from some starting point).Let <img src="https://render.githubusercontent.com/render/math?math=\mu%3D(\sum_%7B1 \leq i \leq n%7D R %5Bi%5D)"> denote the average rainfall in R. For an interval I[l,r], 1≤l≤r≤n. , we define the deficit of I to be <img src="https://render.githubusercontent.com/render/math?math=\mu (r-\ell%2B 1) - ( \sum_ %7B \ell \leq i \leq r%7D R %5Bi %5D )">. That is, the deficit of I is the difference between the total amount of rain expected inIand the total amount of rain that actually fell in I.(Note that the deficit of an interval can be negative.) For a new climate study, you have been asked to find an interval I that has the largest deficit. Find the value of the deficit of the largest interval. 

Follow-up: find the interval which gives the maximum interval using the DP table alone.

### Answer
Note that the naive brute force will take <img src="https://render.githubusercontent.com/render/math?math=O(n%5E 3) "> time. After smart ordering the best worst case time bound on brute-force will be <img src="https://render.githubusercontent.com/render/math?math=O(n%5E 2) ">. Can we do better than brute force?. We certainly can using dynamic programming with memoization. The solution is given in [Question1.py](https://github.com/Sameer-Marathe/DynamicProgramming/blob/master/Question1.py).

## Question 2

Let A be a n×m matrix of positive integers. A has n rows and m columns.You are asked to pick a total of k entries from the matrix that yield the maximum sum, under the following constraint: the entries that you pick in any row have to start from the first column and be contiguous. That is,your problem is to determine <img src="https://render.githubusercontent.com/render/math?math=k_1,k_2,\dots,k_n"> such that <img src="https://render.githubusercontent.com/render/math?math=k_1%2B k_2%2B \dots %2B k_n %3D k"> ,and  <img src="https://render.githubusercontent.com/render/math?math=\sum^n_%7B i%3D 1%7D \sum_ %7B j%3D1 %7D^%7B k_n %7D A%5B i%2C j %5D"> is maximized.

Follow-up: can you get the indices <img src="https://render.githubusercontent.com/render/math?math=k_1, k_2,\dots ,k_n"> from DP table.

### Answer
Naive brute force will take exponential time in worst case. We can do polynomial time using the appproach given in [Question2.py](https://github.com/Sameer-Marathe/DynamicProgramming/blob/master/Question2.py). The time complexity of our approach is <img src="https://render.githubusercontent.com/render/math?math=O(nk%5E 2) ">.

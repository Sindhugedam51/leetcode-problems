''' you are given an array of integers arr and an intergerd.your task is  to count the no of 
ways to partition the array into two subsets such that the difference of their sums is equal to d.
Since the answer can be large,return the result modulo 10*9 + 7
Write a function ece(arr, d, n) that returns this count'''

'''
def min_diff_tab(arr):
    totalsum=sum(arr)
    n=len(arr)
    halfsum=totalsum//2
    dp=[[False]*(halfsum+1) for i in range(n+1)]
    for i in range(n+1):
        dp[i][0]=True
    for i in range(1,n+1):
        for j in range(1,halfsum+1):
            if arr[i-1]<=j:
                dp[i][j]=dp[i-1][j] + dp[i-1][j-arr[i-1]]
            else:
                dp[i][j]=dp[i-1][j]
    for j in range(halfsum,-1,-1):
        if dp[n][j]:
            return totalsum-2*j
arr=[1,6,11,5]

print(min_diff_tab(arr))

'''
'''
def cs(arr,d):
    totalsum=sum(arr)
    n=len(arr)
    if (totalsum+d)%2!=0:
        return False
    targetsum=(totalsum+d)//2
    dp=[0]*(targetsum+1)
    dp[0]=True
    for num in arr:
        for j in range(targetsum,num-1,-1):
            dp[j]=dp[j]+dp[j-num]
    return dp[targetsum]
arr=[1,6,11,5]
d=1
print(cs(arr,d))
'''


def findTargetSumWays
def canPartition(nums):
        totalsum=sum(nums)
        if totalsum%2!=0:
            return False
        targetsum =totalsum//2
        dp=[False]*(targetsum+1)
        dp[0]=True
        for num in nums:
            for j in range(targetsum,num-1,-1):
                dp[j]=dp[j-num] or dp[j]
         dp[targetsum]  
nums=[1,2,2,1] 
print(canPartition(nums))   
def is_subset_sum_tab(arr, n, target):
    if not dp[n][target]:
        return []
    subset=[]
    i,j=n,target
    while i>0 and j>0:
        if dp[i][j] and dp[i-1][j]:
            subset.append(arr[i-1])
            j-=arr[i-1]
            
        i-=1
    return subset
arr=[2,3,7,8,10]
target=10
n=len(arr)
result = is_subset_sum_tab(arr, n, target)
print(result)
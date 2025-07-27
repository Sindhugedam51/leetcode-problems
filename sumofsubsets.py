""" Given  an array nums,return true if you can partition the array into two subsets 
such that the sum of the elements in the both 
subsets is equal or false otherwise 
input : nums=[1,5,11,5]
output:true """

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
        return dp[targetsum]  
nums=[1,2,2,1] 
print(canPartition(nums))    
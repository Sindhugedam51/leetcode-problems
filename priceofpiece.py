'''  given a rod of length n inches and an array price [].price[i] denotes the value of a piece of length
i.The task is to determine the maximum value obtained by cutting up the rod and selling the pieces
Note: price[] is 1-indexed array.
input price[]=[1,5,8,9,10,17,17,20]
output=22
input:price[]=[3,5,8,9,10,17,17,20] 10+9+5
output=24
''' '''
def cutRodRecur(i,price):
    if i == 0:
        return 0
    ans=0
    for j in range(1,i+1):
        ans=max(ans,price[j-1]+cutRodRecur(i-j,price))
    return ans
def cutRod(price):
    n=len(price)
    return cutRodRecur(n,price)
price=[1,5,8,9,10,17,17,20]
print(cutRod(price))
'''
'''
#memoization
def cutRodRecur(i,price,memo):
    if i == 0:
        return 0
    if memo[i-1] !=-1:
        return memo[i-1]
    ans=0
    for j in range(1, i + 1):
        ans=max(ans,price[j-1]+cutRodRecur(i-j,price,memo))
    memo[i-1]=ans
    return ans
def rodcut(price):
    n=len(price)
    memo=[-1]*n
    return cutRodRecur(n,price,memo)
price=[1,5,8,9,10,17,17,20]
print(rodcut(price))
'''

#tabulation
def cutRod(price):
    n=len(price)
    dp=[0]*(n+1)
    for i in range(1,n+1):
        for j in range(1,i+1):
            dp[i]=max(dp[i],price[j-1]+dp[i-j])
    return dp[n]
price=[1,5,8,9,10,17,17,20]
print(cutRod(price))

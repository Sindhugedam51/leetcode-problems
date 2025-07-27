''' you are given an integer array coins representing coins of different denominations and an
integer amount representing a total amount of money.
Return the fewwest number of coins that you need to makeup that amount.If that amount 
Input=coins = [1,2,5]
output= 3
'''



def coinCharge(coins, amount):
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    
    return dp[amount] if dp[amount] != amount + 1 else -1


coins = [1, 2, 5]
amount = 11
print(coinCharge(coins, amount))  

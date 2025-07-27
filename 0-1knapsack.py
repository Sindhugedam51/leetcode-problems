def knapsack(wt,prof,w,n):
    if n== 0 or w== 0:
        return 0
    if wt[n-1]>w:
        return knapsack(wt,prof,w,n-1)
    else:
        include=(prof[n-1]+knapsack(wt,prof,w,n-1))
        exclude=knapsack(wt,prof,w,n-1)
        return max(include,exclude)
wt=[3,4,6,5]
prof=[2,3,1,4]
w=8
n=4
print(knapsack(wt,prof,w,n-1))
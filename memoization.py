#memoization
def find_min_diff_memo(arr,n, sum_calculated, sum_total,memo):
    if n==0:
        return abs((sum_total - sum_calculated)- sum_calculated)
    if (n, sum_calculated) in memo:
        return memo[(n,sum_calculated)]
    include=find_min_diff_memo(arr, n-1, sum_calculated + arr[n-1], sum_total,memo)
    exclude=find_min_diff_memo(arr, n-1, sum_calculated,sum_total,memo)
    memo[(n,sum_calculated)]=min(include,exclude)
    return memo[(n,sum_calculated)]
def find_min_diff_memo(arr):
    sum_total  = sum(arr)
    memo = {}
    return find_min_diff_memo(arr,len(arr),0,sum_total,memo)
arr = [1, 6, 11, 5]
print(find_min_diff_memo(arr))
def remove(nums, k):
    stack =[]
    for i in nums:
        while stack and k >0 and stack[-1]>i:
            stack.pop()
            k -= 1
        stack.append(i)
    if k>0:
        stack = stack[:k] 
    result = ''.join(stack)
    i = 0
    while i < len(result) and result [i] == '0':
        i += 1
    result = result[i:]
    return result if result else "0"
nums = input()
k = int(input())
output = remove(nums, k)
print(output)

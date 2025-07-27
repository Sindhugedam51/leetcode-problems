'''
write a program to check whether the given number is perfect number or not.
'''
n=int(input())
sum=0
for i in range(1,n):
    if n%i==0:
        sum+=i
if n==sum:
    print('prefect')
else:
    print('no')
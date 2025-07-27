'''yu are given an integer n your task is to print the minimum number of operations required to reduce 
n to 1.you can perform only 2 operations in any order and any number of times 
1st n/x where x should be lessthan n and n%x=0
you can subtract 1 from  n.'''
n=int(input())
if n%2==0:
    print(2)
else:
    print(3)
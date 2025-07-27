''' write a program to check wether a given number is harshad number 
the given number is divisible by sum of its digits.'''
num=int(input())
temp=num
sum=0
while num!=0:
    digit=num%10
    sum+=digit
    num//=10
if temp%sum==0:
    print('harshad')
else:
    print('no')
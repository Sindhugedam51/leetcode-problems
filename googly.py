''' write a program to check whether the given number is googly or not????? sum of digits and then check it is prime or not??
ex: 25-googly
    27- not googly
    34 - googly'''
n=50
sum=0
while n!=0:
    digit=n%10
    sum+=digit
    n//=10
if prime(sum):
    print('googly')
else:
    print('not googly')

'''
write a program to print prime numbers in a given range '''
n=70
def prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
start=40
for i in range(start,n):
    if prime(i):
        print(i)
from time import *
n=int(input("Enter Last Number:\n"))

def iter(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact

def recursive(n):
    if n==0 or n==1:
        return 1
    else:
        return n*recursive(n-1)
        
print(":::::::::::::Enter a Choice:::::::::::::")
x=int(input("1.For Iterative\n2.For Recursive:"))

if x==1:
    a=time()
    iter(n)
    print(iter(n))
    b=time()
    print("Time Taken By Iterative Method:",b-a)
elif x==2:
    a=time()
    recursive(n)
    b=time()
    print("Time Taken By Recursive Method:",b-a)
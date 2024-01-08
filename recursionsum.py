
"""n=int(input())
def sum(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return n+sum(n-1)
print("sum of first "+str(n)+" whole number is "+ str(sum(n)))"""
"""s=input()
def length(s):
    return(len(max([i for i in s.split('1')])))
print(length(s))"""
"""a=[int(i) for i in input().split()]
b=[int(i) for i in input().split()]
def cross(a,b):
    return(sum([a[i]*b[i] for i in range(len(a))]))
print(cross(a,b))
"""
N=int(input())
L=[int(i) for i in input().split()]
K=int(input())
print(sorted(L).index(L[K-1])+1)
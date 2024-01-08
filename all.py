"""list=[1,2,4,5]
print(list)
list.append(6)
print(list)
list.insert(2,3)
print(list)
list.clear()
print(list)
#print(dir(list))
print(list[::-1])
print(list[1:4])"""
#names=("ram","shyam","kishan","radha","ram")
#print(names.index("shyam"))
#print(names.count("Dhanlal"))
#names={"ram","shyam","kishan","radha","ram"}
#print(names)
"""details={"ram":"kailash","shyam":"satyajith"}
print(details["ram"])
"""
"""x,y=2,3
print(x,y)
x,y=y,x
print(x,y)"""
#a=int(input())
#b=int(input())
#print(a+b,end=" ")
"""num = int(input())
for a in range(num+1):
	if a==num:
	  print(a,end="")
	else:
	  print(a)"""
"""n=int(input())
for i in range(n+1):
   print(i*"*")"""
"""n=int(input())
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return (fib(n-1)+fib(n-2))
for i in range(n):
    print(fib(i))
"""
"""n=int(input())
L=[0,1]
if n==0:
    print(0)
elif n==1:
    print(0)
    print(1)
else:
    for i in range(n-2):
         L.append(L[:n-i-1]+L[:n-i-2])
       
    for i in L:
        print(i)
    """
"""b=int(input())
h=int(input())
for i in range(h):
    for j in range(b):
        print("*",end=" ")
    print()"""
"""n=int(input())
sum=0
for i in range(1,n+1):
    sum=sum+(i**2)
print(sum)
print(2**(n))"""       
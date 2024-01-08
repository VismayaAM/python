n=int(input("enter the number of rows you want "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print('*',end="")
    print()

a=int(input("enter the breadth "))
b=int(input("enter the height "))
for i in range(1,b+1):
    for j in range(1,a+1):
        print('*',end="")
    print()
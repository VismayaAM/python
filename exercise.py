#print( "Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are")
"""
import sys
print("python version")
print(sys.version)
print("pyhton version info")
print(sys.version_info)"""
"""import datetime
now=datetime.datetime.now()
print("current date and time")
print(now.strftime("%Y-%m-%d %H-%M-%S"))"""
"""import math
r=float(input("Enter the radius"))
a=math.pi*r**2
print("area of circle ",a)"""
#first=input("enter the first name")
#second=input("enter the last name")
#print(second+" "+first)
"""values=input("enter the numbers")
list=values.split()
tuple=tuple(list)
print("list",list)
print("tuple",tuple)"""
"""num1=int(input("enter the number 1"))
num2=int(input("enter the number 2"))
def maximum(n1,n2):
    return(max(num1,num2))
a=maximum(num1,num2)
print(a)"""
"""n=int(input("enter the number"))
def fizz_buzz(num):
    if num%3==0 and num%5==0:
        return("FizzBuzz")
    elif num%3==0:
        return("Fizz")
    elif num%5==0:
        return("Buzz")
    else:
        return(num)
p=fizz_buzz(n)
print(p)
"""
flag=0
s=int(input("enter the speed "))
def checking(speed):
    if speed<70:
        print("ok")
    elif speed>130:
        print("licence cancelled")
    else:
        for speed in range(130):
            if(speed>=70):
                flag=flag+1
                speed=speed+5
        print(speed)
checking(s)

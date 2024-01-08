"""
import turtle
t=turtle.Turtle()
side=100
for i in range(4):
    t.forward(side)
    t.left(90)
r=50
t.circle(r)
a=25
for i in range(6):
    t.forward(a)
    t.left(300)
"""
import math
print("hello world".split())
print("hello world")
a=int(input("enter the number 1"))
b=int(input("enter the number 2"))
print("sum",a+b)
print("difference",a-b)
print("product",a*b)
print("quotient",a/b)
print("remainder",a%b)
a=float(input("enter the breadth of triangle"))
b=float(input("enter the height of triangle"))
print("area of triangle",a*b*.5)
s1=int(input("enter the side1 of the triangle"))
s2=int(input("enter the side2 of the triangle"))
s3=int(input("enter the side3 of the triangle"))
s=(s1+s2+s3)/2
a=math.sqrt(s*(s-s1)*(s-s2)*(s-s3))
print("area of triangle",a)
a=int(input('enter the value of a'))
b=int(input('enter the value of b'))
temp=a
a=b
b=temp
print("value of a ",a)
print("value of b",b)
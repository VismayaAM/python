def foo(l):
    a=l[0]
    for i in l:
        if i<a:
            a=i
    return a
print(foo([2,3,5,1,7,6]))
#annonymous functions are
'''def f(x):
    print(2*x+5)
f(5)'''

'''def f(x):
    return(2*x+5)
print(f(5))'''

'''def f():
    x=int(input("enter the value:"))
    print(2*x+5)
f()'''    
#syntax
#a=lambda arg:expr
'''a=lambda x:2*x+5
print(a(5))'''

'''a=int(input("a value"))
b=lambda x:2*x+5
print(b(a))'''

#print((lamda x,y:x+y)(3,5))
'''a=lambda x,y:x+y
print(a(3,5))'''
'''a=codegnan
b=lambda a:a.upper()
print(b(a))

a=lambda a:a.upper()
print(a("codegnan"))

a=input("data")
b=lambda a:a.upper()
print(b(a))'''

#a=pythoncourse
'''b=lambda a:a.title()
print(b("python course"))'''
'''a=input("f name")
b=input("l name")
c=lambda a,b:a+b
print(c(a,b))'''

'''fname,lname=input("enter the names:").split(',')
fullname=lambda fname,lname:(fname+" "+lname).title()
print(fullname(fname,lname))'''


'''a=input("fname")
b=input("lname")
c=lambda a,b:(a+" "+b).title()
print(c(a,b))'''

'''a,b=[input(str(x)) for x in input("enter the names:").split(',')]
c=lambda a,b:(a+" "+b).title()
print(c(a,b))'''
#filter
'''a=[10,20,17,40,60,80,35,67]
if a%2==0:
    print(a)'''
'''a=[10,20,17,40,60,80,35,67]
for i in a:
    if i%2==0:
        print(i)'''
'''a=[10,20,17,40,60,80,35,67]
b=list(filter(lambda a:a%2==0,a))
print(b)'''
'''b=tuple(filter(lambda i:i%2!=0,[10,20,17,40,60,80,35,67]))
print(b)'''

'''a=[[],(),set(),{},None,"",4,6.7,"python",5+9j,True,False]
b=list(filter(None,a))
print(b)'''
'''a=int(input("a value"))
b=int(input("b value"))
c=lambda a,b:(a+b,a-b,a*b)
print(c(a,b))'''


b=100
c=lambda b=b%1==0,b
print(c(b))

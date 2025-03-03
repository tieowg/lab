b= int(input("b= "))
a = int(input("a= "))
c=int(input("c=  "))
x=0
while x<=1:
    if a*x>=4:
        print(9*(x**2)+3*a*b)
    else:
        print(8*a*x-2*b*c)
    x+=0.1

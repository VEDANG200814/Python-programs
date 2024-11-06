a,b,c=0,1,1
d=a+b+c
for i in range(1,11,1):
    print(a,end=", ")
    a=b
    b=c
    c=d
    d=a+b+c
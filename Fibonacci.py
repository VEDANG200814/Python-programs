a=0
b=1
c=a+b
for i in range(1,11,1):
    print(a, end=", ")
    a=b
    b=c
    c=a+b

n=n1=int(input("Enter a number\n"))
d=f=0
while n1!=0:
    d=n1%10
    if d==0:
        f=1
        break
    n1//=10    
if f==1:
    print(n," is a Duck number")
else:
    print(n," is not a Duck number")
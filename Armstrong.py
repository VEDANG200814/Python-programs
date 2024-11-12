n=n1=int(input("Enter a number\n"))
c=0
while n1!=0:
    n1//=10
    c+=1
n1=n
s=0
while n1!=0:
    s+=pow(n1%10,c)
    n1//=10
if s==n:
    print(n,"is an Armstrong number")
else:
    print(n,"is not an Armstrong number")
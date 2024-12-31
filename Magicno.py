def magico(n):
    i=0
    while n>0:
        i+=n%10
        n//=10
        if i>9:
            i=magico(i)
    return i

n=int(input("Enter a number\n"))
i=magico(n)
if(i==1):
    print(n,"is a Magic number")
else:
    print(n,"is not a Magic number")
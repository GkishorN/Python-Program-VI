n=int(input("Enther the number of terms:"))
a=0
b=1
if(n==1):
    print(a)
elif(n==2):
    print(a,end=' ')
    print(b)
else:
    print(a,end=' ')
    print(b,end=' ')
    for i in range(3,n+1):
        temp=a+b
        a=b
        b=temp
        print(temp,end=' ')
        

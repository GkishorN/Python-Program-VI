n=int(input("Enter the number:"))
a=0
b=1
sum=0
flag=0
while(a<=n):
    if(a==n):
        print("Number is fibbinoci number")
        flag=1
    sum=a+b
    a=b
    b=sum
if(flag==0):
    print("Number is not fibbinoci number")

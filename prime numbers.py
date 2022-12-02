#prime numbers
flag=0
i=2
num=int(input())
if(num<2):
    print("invalid input")
while(i<num):
    if(num%i==0):
        flag=1
        break
    i=i+1
if(flag==1):
    print("not a prime number")
else:
    print("prime number")

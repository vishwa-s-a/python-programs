#armstrong numbers
num=int(input())
num1=num
sum1=0
while(num1>0):
    rem=num1%10
    num1=num1//10
    sum1=sum1+pow(rem,3)
if(num==sum1):
    print("Armstrong Numbers")
else:
    print("not a armstrong number")

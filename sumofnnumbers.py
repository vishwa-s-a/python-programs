#sum of n numbers
n=0
i=1
sum1=0
num=0
n=int(input("enter the total number of inputs to give"))
while i <= n:
    num=int(input("enter the value of number"))
    sum1=sum1+num
    i=i+1
print("the sum of numbers is=",sum1)
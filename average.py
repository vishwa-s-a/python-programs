#average of the numbers
num=0
i=1
n=0
sum1=0
avg=0
n=int(input("enter the total numbers to be used for calculation "))
while i<= n:
      num=int(input("enter the value of the number"))
      sum1=sum1+num
      avg=sum1/n
      i=i+1
print("the average of the numbers is =",avg)

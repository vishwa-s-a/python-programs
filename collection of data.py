#using list function
#sum of n numbers
n=int(input())
l1=[]
sum=0
for i in range(0,n,1):
    val=int(input())
    l1.append(val)
for i in range(0,n,1):
    sum=sum+l1[i]
print('sum',sum)
print(l1)
for i in range(0,n,1):
    print("l1 [",i,"]",l1[i ])

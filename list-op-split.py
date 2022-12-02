l1=[]
l1=input().split('/')#delimiter here we can give anything in this bracket 
sum=0
for i in range(0,len(l1),1):
    sum=sum+int(l1[i])
print(sum)

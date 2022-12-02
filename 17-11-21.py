#summing two matrices
a=[]
b=[]
c=[]
n=int(input())
m=int(input())
for  i in range(0,n):
    temp=[]
    for j in range(0,m):
        temp.append(int(input()))
    a.append(temp)
#print(a)
for i in range(0,n):
    temp=[]
    for j in range(0,m):
        temp.append(int(input()))
    b.append(temp)
#print(b)
sum=0
for  i in range(0,n):
    temp=[]
    for j in range(0,m):
        sum=a[i][j]+b[i][j]
        temp.append(sum)
    c.append(temp)
print(a)
print(b)
print(c)

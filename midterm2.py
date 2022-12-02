n=int(input())# to take the inputs
m=int(input())
l=[]
l1=[]
sum1=0
sum2=0
z=0
for i in range(0,n):# adding the elements to list
    temp=[]
    for j in range(0,m):
        val=int(input())
        temp.append(val)
    l.append(temp)
for i in range(0,n):
    vish=[]
    for j in range(0,m):
        app=0
        vish.append(app)
    l1.append(vish)
#print(l1)
for i in range(0,n):
    for j in range(0,m):
        l1[i][j]=l[j][i]
#print(l1)
for i in range(0,n): # for summing of diagonal elements(left)
    for j in range(0,m):
        if i==j:
            sum1=sum1+l[i][j]
print(sum1)
for i in range(0,n):# for summing elements of right elements
    for j in range(0,m):
        if (j==m-1) and (i==z):
            sum2=sum2+l[i][j]
            m=j
            z=i+1
print(sum2)
diff=abs(sum1-sum2)# finding the absolute difference of sum1 and sum2
print(diff)
for i in range(0,n):
    for j in range(0,m):
        print(l1[i][j])

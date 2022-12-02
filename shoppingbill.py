son=[]
daughter=[]
father=[]
bill=[]
total_pay=0
items={'pencil':1,'pen':2,'chocolate':3}
d={0:10,1:50,2:5}
d1={0:'pencil',1:'pen',2:'chocolate'}
print('items present in the shop are ',list(items.keys()))
n=int(input())
for i in range(0,n):
    son.append(d1[i])
    son.append(int(input()))
print('sons shopping cart',son)
for i in range(0,n):
    daughter.append(d1[i])
    daughter.append(int(input()))
print('daughters shopping cart',daughter)
for i in range(0,n):
    sum=son[2*i+1]+daughter[2*i+1]
    father.append(d1[i])
    father.append(sum)
print('fathers shopping cart',father)
for i in range(0,n):
    bill.append(d1[i])
    sum=father[2*i+1]*d[i]
    bill.append(sum)
print('bill =',bill)
for i in range(0,n):
    total_pay=total_pay+bill[2*i+1]
print('total to be paid is=',total_pay)

#23 and 24/11/21
'''d1={}
d1[1]='21bce0001'
d1['course']='bcse101'
d1['names']=['ram','sita','ganesh']
print(d1)
for i in d1.values():
    if i=='ram':
        print('hi')
    else:
        print("bye")
'''

#program to fill the dictionary taking the values from keyboard/test case
'''d1={}
print('total number of items')
n=int(input())
for i in range(0,n):
    print('enter the key')
    k=int(input())
    print('enter the value')
    v=input()
    d1[k]=v
print(d1)

#if 'sita' in d1:
    #print('sita is present')


for k,v in d1.items():
    if (v=='sita'):
        print('sita is associated with a key =',k)
'''

#nested dictionary opertions
d1={}
print('total number of items')
n=int(input())
for i in range(0,n):
    print('enter the key')
    k=input()
    #print('enter the value')
    l1=[]
    cap=input('enter the capital :')
    l1.append(cap)
    pop=int(input('enter the population :'))
    l1.append(pop)
    area=float(input('enter the area :'))
    l1.append(area)
    temp=float(input('enter the temp :'))
    l1.append(temp)
    d1[k]=l1
print(d1)

# logic to find the state with highest pop,temp,area; and to print them
d2={}
for k,v in d1.items():
    print('population in ',k,'=',v[1])
    d2[k]=v[1]
print(d2)

'''[M4_CSQ1]
l1=[] # to create a empty list
n=int(input()) # to take the input of number of elements in list
''' to take the values of list in the form of string and using split
function for providing the space between the inputs and avoid the
 space inbetween the numbers, getting a index'''
l1=str(input()).split()
'''now to extract each element from list and make it as reference then
to add all elements left of reference and create a variable as the
sum then again create a new variable and to store the sum of elements
 right to the reference'''
for i in range(0,n):
    left_sum=0
    right_sum=0
    for j in range(0,i):
        left_sum=left_sum+int(l1[j])
    #print('left_sum= ' ,left_sum)
    for k in range(i+1,n):
        right_sum=right_sum+int(l1[k])
    #print('right_sum = ',right_sum)
    if left_sum==right_sum:# here verifying whether sums are equal or not
        print(i)
        break
    if i==n-1: # if all numbers in list are not satisfying the above condition then to display 0
        print('0')'''


#[M4_CSQ2]
l1=[2,3,4,12,'*','/',3,'+']
d1={}
for i in range(0,len(l1)):
    try:
        if l1[i]>0:
            xi=l1[i]
            d1[i]=l1[i]
    except:
        xi=l1[i]
        d1[i]=l1[i]
print(d1)
for i in range(0,len(l1)):
    if d1[i]=='*' or d1[i]=='+' or d1[i]=='-' or d1[i]=='/':
        y=d1[i]
        z=d1[i-1]
        d1[i-1]=y
        d1[i]=z
        d1[i-2]=d1[i-2]
print(d1)

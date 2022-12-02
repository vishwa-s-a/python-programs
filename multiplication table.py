#multiplication table
n=0
m=0
n=int(input())
m=int(input())
if(n>0 and m>0):
    i=1
    while(i<=m):
        ans=i*n
        print(n,"*",i,"=",ans)
        i=i+1
else:
    print("invalid entry")
    
        

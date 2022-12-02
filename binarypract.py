n=int(input("enter the number to be converted"))
binary=""
while(n>0):
    rem=n%2
    n=n//2
    binary=str(rem)+binary
print(binary)

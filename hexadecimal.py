#binary numbers
binary=''
num=int(input())
while num>0:
    rem=num%10
    num=num//10
    binary=str(rem)+binary
print(binary)

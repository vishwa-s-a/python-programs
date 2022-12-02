#binary conversion
n=int(input())
bin_num=""

while n>0:
    rem=n%2
    n=n//2
    bin_num=str(rem)+bin_num

print(bin_num)

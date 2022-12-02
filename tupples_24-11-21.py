#tupples application
# hospital problem ( blood testing unit)
lab_reading={}
n=int(input('enter the number of tests :'))
for i in range(0,n):
    test=input('enter the test : ')
    min=float(input())
    max=float(input())
    lab_reading[test]=(max,min)
print(lab_reading)
check_test=input()
value=float(input())
range=lab_reading[check_test]
min=range[1]
max=range[0]
if min<value<max:
    print('normal')
else:
    print('abnormal')

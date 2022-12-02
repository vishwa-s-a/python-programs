def is_leap(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                print(True)
        print(True)
    else:
        print(False)
n=int(input())
print(is_leap(n))

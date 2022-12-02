#integers to roman numbers(2 digits integers)
roman={1:'I',4:'IV',5:'V',9:'IX',10:'X',40:'XL',50:'L',90:'XC'}
order=[90,50,40,10,9,5,4,1]
n=int(input('enter the number'))
for x in order:
    if n != 0:
        quotient=n//x
        if quotient !=0:
            for y in range(quotient):
                print(roman[x],end='')
        n=n%x

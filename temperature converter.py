#celsius to fahrenhit scale
#c = celsius scale reading
# f = fahrenhit scale reading
'''print('calculator to convert celsius to fahrenhit\n')
c=float(input("enter the reading to be converted: "))
f=((180*c)/100)+32
print('the converted value is: ',f)
print('\n')


#fahrenhit to celsius scale
print('calculator to convert fahrenhit to celsius\n')
f=float(input("enter the reading to be converted: "))
c=(5*(f-32))/9
print(c)'''

f=float(input())
c=lambda f:(5*(f-32))/9
a=c(f)
a=round(a,2)
print(a)

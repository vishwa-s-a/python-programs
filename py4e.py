largest=-1
smallest=None
while True:
    value=input('enter the value ')
    if value=='done':
        break
    try:
        value=int(value)
    except:
        print('Invalid input')
        continue
    if int(value)>largest:
        largest=int(value)
    if smallest is None:
        smallest=int(value)
    elif int(value)<smallest:
        smallest=int(value)
print('Maximum is ',largest)
print('Minimum is ',smallest)

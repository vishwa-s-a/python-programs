#checking validity of mobile number
import re
num=input()
if re.match('^[^a e i o u]* $',num):
    print('Valid entry')
else:
    print('invalid')

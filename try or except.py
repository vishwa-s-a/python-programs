#try and except statements
'''name='bob'
#meme=int(name)
try:
    meme=int(name)
except:
    meme=-1
print('first',meme)'''
#if in the try statement if there are any thing that can get a traceback then simply the program exits immidiately and goes to except statements like in this statements
'''astr='bob'
try:
     print("hello")
     istr=int(astr)
     print('there')
except:
    istr=-1
print('done',istr)

if x==6:
    print('is 6')
    print('is still 6')
    print('third 6')
'''
'''x=0
if x < 2 :
    print('Below 2')
elif x >= 2 :

     print('Two or more')
else :
    print('Something else')'''

while True:
    num=input()
    if num=='done':
        break
    try:
        num=int(num)
    except:
        print("Invalid")
    num=int(num)+123
print('hello',num)

# basics of read
'''
fh is file handler, it stores how much data is present, who created it, who is
the owner all these data is called Meta data'''
"""fh=open("f1.txt","r")
#print(fh.read())
#print(fh.readlines())
print(fh.readline())
print(fh.readline())
print(fh.readline())
# it bettter to close the file after operation
fh.close()"""

"""# now to check number of lines
fh=open("f1.txt","r")
print(fh.readlines())
no=len(fh.readlines())
print(no)
fh.close()"""

# here to remove \n in the output we can use rstrip

'''fh=open("f1.txt","r")
l1=fh.readlines()
print(l1)
no=len(l1)
print(no)
for i in range(no):
    l2=l1[i].split(' ')
    #print(l2)
    if int(l2[2])>=18:
        print(l2)
fh.close()
'''

fh1=open('f1.txt','r')
l1=fh1.readlines()
print(l1)
fh2=open('fa.txt','w')
for i in range(len(l1)):
    fh2.write(l1[i])
    #fh2.write(',')
    #words=l1[i].split()
    #fh2.write(str(len(words)))
    #fh2.write('\n')
fh1.close()
fh2.close()

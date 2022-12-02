'''fh=open('fa.txt','w')
l1=['3','34','56','12']
fh.writelines(l1)
#for i in range(len(l1)):
    #fh.write(str(l1[i]))
fh.write('god is great!!!')
fh.close()'''

# if append is used then we just addon the given information without erasing the existing data
#write mode will erase all data and then addon the given fresh data
fh=open('fa.txt','a')
l1=[[101,'ram',18],[102,'sita',18],[103,'ganesh',17]]
for i in range(len(l1)):
    for j in range(len(l1[i])):
        fh.write(str(l1[i][j]))
        if (j<len(l1[i])-1):
            fh.write(',')
        else:
            fh.write('.')
    fh.write('\n')
fh.close()

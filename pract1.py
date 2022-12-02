l=[['vishwa',21,98],['vishnu',20,99]]
fh=open('fa.txt','a')
for i in range(len(l)):
    for j in range(len(l[i])):
        fh.write(str(l[i][j]))
        if (j<len(l[i])-1):
            fh.write(',')
        else:
            fh.write('.')
    fh.write('\n')
fh.close()

import operator# to import the required package
# to create a dictionary having all mathematical operators
ops={'+':operator.add,'-':operator.sub,'*':operator.mul,'/':operator.truediv,'%':operator.mod,'^':operator.xor}
l=['+','-','*','/','%','^']
n=int(input())# to take the input of number of entries
eqn=str(input()).split()# to take the input of the testcase
i=0
while(i>=0):# to create a loop for evaluation of the test case
    if len(eqn)==1:# this is the final step of loop, and to print the output and exit the program
        print(int(float(eqn[0])))
        exit()
    if eqn[i].isnumeric():# to check whether the element is number or not
        i=i+1
        continue# if true then to head again back to the start of the loop
    elif eqn[i] in l:# if the element is a operator after verifying then proceed with further code
        L1=(ops[eqn[i]](float(eqn[i-2]),float(eqn[i-1])))
        del(eqn[i])
        del(eqn[i-1])
        eqn[i-2]=str(float(L1))
        print(eqn)
        i=i-2
    else:# again to head back to start of the loop
        i=i+1
        continue

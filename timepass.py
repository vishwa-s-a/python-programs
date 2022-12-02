#for and while loops and uses
'''for i in [5,4,3,2,1]:
    print(i)
print('blastoff')'''

'''friends=['parle-g','sunfeast','marie gold']
for friend in friends:
    print('happy new year ',friend)
print('done')'''


#to find the largest so far
'''largest_so_far=-1
for num in [9,41,12,45,95,23]:
    if largest_so_far<num:
        largest_so_far=num
print('the largest number so far is = ',largest_so_far)'''

#count the number of the things
'''count=0
print('before ',count)
for thing in [9,8,76,55,44,332,234,567,897]:
    count=count+1
    print(count,thing)
print('after',count)'''

'''#suming of the values in the []
total=0
for thing in [23,45,67,89,90,12,34,]:
    total=total+thing
print(total)'''

#finding the smallest number
'''smallest=None
for value in [12,34,56,78,90,2,3,1]:
    if smallest is None:
        smallest=value
    elif value<smallest:
        smallest=value
print(smallest)'''

tot = 0
for i in [5, 4, 3, 2, 1] :
    tot = tot + 1
print(tot)

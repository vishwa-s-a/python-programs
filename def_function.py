#types of different functions
#below we have discussed the uses of def keyword and imp point is it does not get
#executed and we have to invoke it when it is necessary

'''def thing():
    print('hello')
    print('fun')
    print('goodbye')
thing()
print('zipcode')
thing()'''

#we can also use some parameters in the parenthesis of the def function as lets
#see in the below example

'''def greet(lang):
    if lang=='es':
        print('hello')
    elif lang=='fr':
        print('Hola')
    else:
        print('bonjoure')
greet('es')
greet('fr')
greet('')'''

# and to use a return functions( here the return func either stops the function
# or returns a value)

'''def greet():
    return "hello"
    print(greet(),"glenn")
    print(greet(),"maxwell")'''


#we can also use 2 parameters in the def function ex
def addtwo(a,b):
    added=a+b
    return added
x=addtwo(45,54)
print(x)


#max and min functions
#so here for max function lower case is given more preference as compared to upp
#er case
'''big=max('hello World ')
print(big)
tiny=min('Hello world')
print(tiny)'''
# after this we can see that in float and int functions if we are using both int
#and float functions then integers are explicitly converted to floating values
#example for the same is
'''print(1+2*float(3)/4-5)'''

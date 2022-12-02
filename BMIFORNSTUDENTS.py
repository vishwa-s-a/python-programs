#calculate BMI for 1 student
weight,height,BMI,i,n=0.0,0.0,0.0,1,0 
n=int(input("enter the total number of students"))
while i<=n:
    height=float(input("please enter the value of height"))
    weight=float(input("please enter the value of weight"))
    BMI=(weight/(height**2))
    print("BMI is =", BMI)
    i=i+1
print("calculation of BMI of all students is finished")
#BMI classification of the students
weight=0.0
height=0.0
BMI=0.0
weight=float(input("enter the weight of the person in kg"))
height=float(input("enter the height of the person in cm"))
height=height/100
BMI=((weight)/(height**2))
BMI=(format(BMI,".1f")) 
if(BMI<16):
   print(BMI)
   print("serious underweight")
elif(16<=BMI<18):
     print((BMI)
     print("underweight")
elif(18<=BMI<24):
     print(BMI)
     print("normal weight")
elif(24<=BMI<29):
     print(BMI)
     print("overweight")
elif(29<=BMI<35):
     print(BMI)
     print("seriouly overweight")
elif(BMI>=35):
     print(BMI)
     print("gravely overweight")

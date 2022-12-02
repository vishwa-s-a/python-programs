#BMI classification of the students
weight=0.0
height=0.0
BMI=0.0
weight=float(input("enter the weight"))
height=float(input("enter the height"))
height=height/100
BMI=((weight)/(height**2))
BMI=round(BMI,1)
if (BMI<16):
    print(BMI," ","serious underweight")
elif(16<=BMI<18):
    print(BMI," "," underweight")
elif(18<=BMI<24):
    print(BMI," ","normal weight")
elif(24<=BMI<29):
    print(BMI," ","overweight")
elif(29<=BMI<35):
    print(BMI," ","seriously overweight")
elif(BMI>=35):
    print(BMI," ","gravely overweight")

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = weight / height ** 2
if bmi < 18.5:
    bmi = round(bmi)
    print(f"Your BMI is {bmi}, you are underwight.")
elif bmi <= 25:
    bmi = round(bmi)
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi <= 30:
    bmi = round(bmi)
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi <= 35:
    bmi = round(bmi)
    print(f"Your BMI is {bmi}, you are obese.")
else:
    bmi = round(bmi)
    print(f"Your BMI is {bmi}, you are clinically obese.")
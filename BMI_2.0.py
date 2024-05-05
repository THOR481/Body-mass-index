height = float(input("what is your Height in Meters?\n"))
weight = int(input("whah is your weight in kilograms?\n"))
bmi=float(weight/height**2)
if (bmi<18.5):
  print(f"Your BMI is {(bmi)}, you are underweight.")
elif bmi<=20:
   print(f"Your BMI is  {(bmi)}, you are normal weight.")
elif bmi<=30:
   print(f"Your BMI is {(bmi)}, you are slightly over weight.")
elif bmi<=35:
  print(f"Your BMI is {(bmi)}, you are obese.")
elif bmi>=35:
   print(f"Your BMI is {(bmi)}, you are clinically obese.")
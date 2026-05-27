def bmi_category(score):
    if score<18.5:
        return "underweight"
    elif score<=24.9:
        return "Healthy"
    else:
        return "Overweight"

score=float(input (""))
print (bmi_category(score)) 
    
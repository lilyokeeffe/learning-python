score= int(input(""))
def grade(score):
    if score>=70:
        return "Pass"
    elif score >=40:
        return "Merit"
    else:
        return "failure alert!!!!"

print (grade(score))

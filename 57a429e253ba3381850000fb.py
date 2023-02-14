# =========================== 8 kyu Calculate BMI ===========================
def bmi(weight, height):
    bmi = (weight) / (height ** 2)
    if bmi <= 18.5:
        return "Underweight"
    elif bmi > 18.5 and bmi <= 25.0:
        return "Normal"
    elif bmi > 25.0 and bmi <= 30.0:
        return "Overweight"
    elif bmi > 30:
        return "Obese"

print(bmi(86, 1.80))


def print_nums(x):

  for i in range(x):

    print(i)

    return

print_nums(10)















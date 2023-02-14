# =========================== 8 kyu Simple multiplication ===========================
def simple_multiplication(number) :
    
    if number % 2 == 0 :
        return number * 8
    else:
        return number * 9
    
print(simple_multiplication(6))
print(simple_multiplication(7))
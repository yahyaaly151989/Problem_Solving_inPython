# =========================== 8 kyu Even or Odd ===========================
def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
print(even_or_odd(4))
print(even_or_odd(3))
print(even_or_odd(9))
print(even_or_odd(19))
print(even_or_odd(20))
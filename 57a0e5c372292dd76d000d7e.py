# =========================== 8 kyu String Repeat ===========================

def repeat_str(repeat, string):
    
    # return string * repeat
    repeated_string = ""
    for i in range(repeat):
        repeated_string += string
    return repeated_string


print(repeat_str(5, "I"))
print(repeat_str(6, "Hello"))
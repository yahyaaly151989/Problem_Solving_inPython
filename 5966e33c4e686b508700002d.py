# =========================== 8 kyu Sum The Strings ===========================
def sum_str(a, b):
    a = 0 if a == "" else int(a)
    b = 0 if b == "" else int(b)
    return str(a + b)

print(sum_str("4", "5"))
print(sum_str("", ""))
print(sum_str("2", ""))
print(sum_str("-7", "2"))
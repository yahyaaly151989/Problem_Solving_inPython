# =========================== 8 kyu Price of Mangoes ===========================
def mango(quantity, price):
    l = []
    for i in range(1, quantity + 1):
        if i % 3 != 0:
            l.append(i)
    return len(l) * price


print(mango(2, 3)) # ==> 6    # 2 mangoes for 3 = 6; no mango for free
print(mango(3, 3)) # ==> 6    # 2 mangoes for 3 = 6; +1 mango for free
print(mango(5, 3)) # ==> 12   # 4 mangoes for 3 = 12; +1 mango for free
print(mango(9, 5)) # ==> 30   # 6 mangoes for 5 = 30; +3 mangoes for free
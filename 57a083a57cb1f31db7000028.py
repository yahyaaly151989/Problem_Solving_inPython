# =========================== 8 kyu Powers of 2 ===========================
def powers_of_two(n):
    # result = []
    # x = 0
    # while x <= n:
    #     result.append(pow(2, x))
    #     x += 1
    # return result
    
    resuult = []
    for i in range(0, n + 1):
        resuult.append(pow(2, i))
    return resuult
    
print(powers_of_two(0))
print(powers_of_two(1))
print(powers_of_two(2))
print(powers_of_two(3))
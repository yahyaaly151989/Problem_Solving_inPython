# =========================== 8 kyu Collatz Conjecture (3n+1) ===========================
def hotpo(n):
    # count = 0
    # if n <= 0:
    #     return False
    # else:
    #     while n != 1:
    #         if n % 2 == 0:
    #             n = n / 2
    #             count += 1
    #         else:
    #             n = (3 * n) + 1
    #             count += 1
    
    
    count = 0
    while n != 1:
        n = n / 2 if n % 2 == 0 else (n * 3) + 1
        count += 1
    return count
        


print(hotpo(1)) # 0
print(hotpo(5)) # 5
print(hotpo(6)) # 8
print(hotpo(23)) # 15
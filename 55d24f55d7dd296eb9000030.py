# =========================== 8 kyu Grasshopper - Summation ===========================
def summation(num):
    # result = 0
    # for i in range(1, num + 1):
    #     result += i
    # return result
    
    return sum(range(1, num + 1))


print(summation(2))
print(summation(8))
print(summation(4))
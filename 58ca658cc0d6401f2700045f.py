# =========================== 8 kyu Find Multiples of a Number ===========================
def find_multiples(integer, limit):
    
    # result = []
    # x = 1
    # while x <= int(limit / integer):
    #     result.append(integer * x)
    #     x += 1
    
    # return result
    
    return list(range(integer, limit + 1, integer))

print(find_multiples(2, 6))
print(find_multiples(2, 7))
print(find_multiples(5, 21))
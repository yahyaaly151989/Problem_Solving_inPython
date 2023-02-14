# =========================== 8 kyu Pythagorean Triple ===========================
def pythagorean_triple(integers):
    # sorted_list = sorted(integers)
    # a = sorted_list[0]
    # b = sorted_list[1]
    # c = sorted_list[2]
    # if pow(a, 2) + pow(b, 2) == pow(c, 2):
    #     return True
    # else:
    #     return False
    
    return pow(sorted(integers)[0], 2) + pow(sorted(integers)[1], 2) == pow(sorted(integers)[2], 2)


print(pythagorean_triple([3, 4, 5]))
print(pythagorean_triple([4, 3, 5]))
print(pythagorean_triple([13, 12, 5]))
print(pythagorean_triple([100, 3, 999]))
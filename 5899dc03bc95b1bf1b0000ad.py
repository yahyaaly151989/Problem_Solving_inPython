# =========================== 8 kyu Invert values ===========================
def invert(lst):
    inverted_list = []
    for n in lst:
        inverted_list.append(-n)
    return inverted_list
    

print(invert([1,2,3,4,5]))
print(invert([1,-2,3,-4,5]))
print(invert([]))
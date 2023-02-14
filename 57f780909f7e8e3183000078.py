# =========================== 8 kyu Beginner - Reduce but Grow ===========================
def grow(arr):
    result = 1
    for n in arr:
        result *= n
    return result

print(grow([1, 2, 3, 4]))
print(grow([1, 2, 3, 4, 10]))
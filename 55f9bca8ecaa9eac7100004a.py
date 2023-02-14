# =========================== 8 kyu Beginner Series #2 Clock ===========================
def past(h, m, s):
    return 1000 * ((3600 * h) + (60 * m) + (s))

print(past(0, 1, 1))
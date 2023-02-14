# =========================== 8 kyu Localize The Barycenter of a Triangle ===========================
def bar_triang(point_a, point_b, point_c): 
    x0 = (point_a[0] + point_b[0] + point_c[0]) / (3)
    y0 = (point_a[1] + point_b[1] + point_c[1]) / (3)
    return [round(x0, 4), round(y0, 4)]

print(bar_triang([4, 6], [12, 4], [10, 10]))
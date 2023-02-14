# =========================== 8 kyu Find Maximum and Minimum Values of a List ===========================
from functools import reduce


def minimum(arr):
    # return min(arr)
    # def m(a, b):
    #     return a if a < b else b
    # result = reduce(m, arr)
    # return result
    
    return sorted(arr)[0]

def maximum(arr):
    # return max(arr)
    # def m(a, b):
    #     return a if a > b else b
    # result = reduce(m, arr)
    # return result
    return sorted(arr)[-1]

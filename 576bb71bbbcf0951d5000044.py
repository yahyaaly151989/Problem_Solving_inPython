# =========================== 8 kyu Count of positives / sum of negatives ===========================
def count_positives_sum_negatives(arr):
    positives = []
    negatives = []
    if len(arr) == 0:
        return []
    for number in arr:
        if number > 0:
            positives.append(number)
        elif number < 0:
            negatives.append(number)
    return [len(positives), sum(negatives)]

print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))
print(count_positives_sum_negatives([0, 0]))
print(count_positives_sum_negatives([]))
# =========================== 8 kyu Add Length ===========================
def add_length(str_):
    result = []
    for word in str_.split():
        result.append(word + ' ' + str(len(word)) )
    return result


print(add_length("apple ban"))
print(add_length("you will win"))


# =========================== 8 kyu Reversed Words ===========================

def reverse_words(s):

    # my_list = s.split(' ')
    # my_reversed_list = my_list[::-1]
    # my_reversed_text = " ".join(my_reversed_list)
    # return my_reversed_text

    return " ".join(s.split(' ')[::-1])

print(reverse_words("The greatest victory is that which requires no battle"))

# Example:

# Input:  "The greatest victory is that which requires no battle"
# Output: "battle no requires which that is victory greatest The"

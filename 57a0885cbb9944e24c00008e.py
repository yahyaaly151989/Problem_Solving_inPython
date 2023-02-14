# =========================== 8 kyu Squaring an Argument ===========================
def remove_exclamation_marks(s):
    
    # return s.replace('!', '')
    return "".join( [x for x in s if x != '!'] )


print(remove_exclamation_marks("yehya!ali!yehya!ali!"))
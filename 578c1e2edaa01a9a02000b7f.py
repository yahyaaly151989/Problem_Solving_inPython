# =========================== 8 kyu Crash Override ===========================
def alias_gen(f_name, l_name):
    FIRST_NAME = {'A': 'Alpha', 'B': 'Beta', 'C': 'Cache'}
    SURNAME = {'A': 'Analogue', 'B': 'Bomb', 'C': 'Catalyst'}
    if f_name[0] not in FIRST_NAME or l_name[0] not in SURNAME:
        return 'Your name must start with a letter from A - Z.'
    else:
        return FIRST_NAME[f_name[0]] + " " + SURNAME[l_name[0]]
    


print(alias_gen('Aarry', 'Brentwood')) # == 'Logic Bomb'
print(alias_gen('123abc', 'Petrovic')) # == 'Your name must start with a letter from A - Z.'
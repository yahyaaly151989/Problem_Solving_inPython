# =========================== 8 kyu Abbreviate a Two Word Name ===========================
def abbrev_name(name):
    abbs = []
    name_list = name.split()
    for abb in name_list:
        abbs.append(abb[0].upper())
    return ".".join(abbs)

print(abbrev_name("Yehya Ali"))
print(abbrev_name("alaa mohamed"))
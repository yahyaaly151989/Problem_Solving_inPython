# =========================== 8 kyu How many lightsabers do you own? ===========================
def how_many_light_sabers_do_you_own(name = "Anyone else"):
    if name == "Zach":
        return 18
    else:
        return 0


    
print(how_many_light_sabers_do_you_own("Maher"))
print(how_many_light_sabers_do_you_own())
print(how_many_light_sabers_do_you_own("Zach"))
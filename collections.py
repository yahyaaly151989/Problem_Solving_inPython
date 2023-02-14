# # =========================== 8 kyu Collections ===========================
# # def remove_char(s):
# #     ls = list(s)
# #     ls[0] = ""
# #     ls[-1] = ""
# #     return "".join(ls)

# # print(remove_char("yehya"))

# # def get_average(marks):

# #     return int(sum(marks) / len(marks))

# # print(get_average([1, 2, 3, 4]))

# def greet(language):
#     langs = {
#         'english': 'Welcome',
#         'czech': 'Vitejte',
#         'danish': 'Velkomst',
#         'dutch': 'Welkom',
#         'estonian': 'Tere tulemast',
#         'finnish': 'Tervetuloa',
#         'flemish': 'Welgekomen',
#         'french': 'Bienvenue',
#         'german': 'Willkommen',
#         'irish': 'Failte',
#         'italian': 'Benvenuto',
#         'latvian': 'Gaidits',
#         'lithuanian': 'Laukiamas',
#         'polish': 'Witamy',
#         'spanish': 'Bienvenido',
#         'swedish': 'Valkommen',
#         'welsh': 'Croeso'
#     }
    
#     if language not in langs:
#         return "Welcome"
#     else:
#         return langs[language]
    
# def are_you_playing_banjo(name):
#     if name.startswith("R") or name.startswith("r"):
#         return name + " plays banjo"
#     else:
#         return name + " does not play banjo"
    
# def problem(a):
#     if type(a) == str:
#         return "Error"
#     else:
#         return (a * 50) + 6






class Python:
    def __init__(self, name):
        self.name = name
bubba = Python("Bubba")
print(bubba.name)

import random

class Ghost(object):
    def __init__(self):
        colors = ["white", "yellow", "purple", "red"]
        self.color = random.choice(colors)
ghost = Ghost()    
print(ghost.color)
    
    


def list_animals(animals):
    list = ''
    for i in range(len(animals)):
        list += str(i + 1) + '. ' + animals[i] + '\n'
    return list


print(list_animals([ 'dog', 'cat', 'elephant' ]))


def lowercase_count(strng):
    ls = []
    a = "abcdefghijklmnopqrstuvwxyz"
    for l in strng:
        if l.lower() in a and l.lower() == l:
            ls.append(l)
    return len(ls)

print(lowercase_count("abcdefghijklmnopqrstuvwxyz"))
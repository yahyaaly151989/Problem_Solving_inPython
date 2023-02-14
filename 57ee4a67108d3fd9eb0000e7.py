# =========================== 8 kyu Filter out the geese ===========================

geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    filtered_words = []
    for word in birds:
        if word not in geese:
            filtered_words.append(word)
    return filtered_words    
    
    
    
    


print(goose_filter( ["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"] ))
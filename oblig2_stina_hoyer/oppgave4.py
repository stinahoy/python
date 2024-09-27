tolkenboker= ["The Hobbit", "Frmer Giles of Ham", "The Fellowship of the Ring", "The Two Towers", "The Return of the King", "The Adventures of Tom Bombadil", "Tree anf Leaf"]
lotr_boker = []

for boker in tolkenboker:
    if boker in ["The Fellowship of the Ring", "The Two Towers", "The Return of the King"]:
        lotr_boker.append(boker)

for boker in lotr_boker:
    print(boker)

    

lotr_boker = [boker for boker in boker if boker in["The Fellowship of the Ring", "The Two Towers", "The Return of the King"]]

for boker in lotr_boker:
    print(boker)
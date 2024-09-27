tolkenboker= ["The Hobbit", "Frmer Giles of Ham", "The Fellowship of the Ring", "The two Towers", "The Return of the King", "The Adventures of Tom Bombadil", "Tree anf Leaf"]

print("De to første bøkene:", tolkenboker[:2])
print("De to siste bøkene:", tolkenboker[-2:])

tolkenboker += ["The Silmarillion", "Unfinished Tales"]

tolkenboker[2:5] = [f"Lord of the rings: {title}" for title in tolkenboker[2:5]]

print(sorted(tolkenboker))
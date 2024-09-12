
planeter = ["Merkur", "Venus", "Jorden", "Saturn", "Uranus"]
print(planeter)

print(planeter,[2])

planeter[3] = "Mars"
print(planeter)

planeter.append("Neptun")
print(planeter)
planeter.append("Pluto")
print(planeter)



random_list = ["Europe", 7, ["Ny liste", 23, "Med nye elementer"], "Bil"]

print(random_list[2])
print(random_list[2][2])
random_list[2][2] = "Forelesning"
print(random_list[2])

random_list[2].insert(_index 1, _object: "Spørsmål i timen") # type: ignore
print(random_list)
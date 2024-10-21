def write_filmer_to_file(filmer, filename):
    with open(filename, 'w') as file:
        for film in filmer:
            navn, år, rating = film
            file.write(f"{navn} - {år} har rating {rating}\n")

filmer_liste = [
    ("The Lion King", 1994, 8.5),
    ("Inception", 2010, 8.8),
    ("The Matrix", 1999, 8.7)
]
write_filmer_to_file(filmer_liste, "filmer.txt")

def read_filmer_from_file(filename):
    with open(filename, 'r') as file:
        content = file.readlines()
        for line in content:
            print(line.strip())

read_filmer_from_file("filmer.txt")
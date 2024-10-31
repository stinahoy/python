filmer = [
    {"navn": "Inception", "år": 2010, "rating": 8.7},
    {"navn": "Inside Out", "år": 2015, "rating": 8.1},
    {"navn": "Con Air", "år": 1997, "rating": 6.9}
]

for film in filmer:
    print(f"navn: {film['navn']}, år: {film['år']}, rating: {film['rating']}")

def average_rating(filmer):
    total_rating = sum(film['rating'] for film in filmer)
    return total_rating / len(filmer) if filmer else 0

avg_rating = average_rating(filmer)
print(f"Gjennomsnitt ratingen er: {avg_rating:.2f}")

def filter_filmer_by_år(filmer, år):
    return [film for film in filmer if film['år'] >= år] 

filtered_films = filter_filmer_by_år(filmer, 2000)
for film in filtered_films:
    print(f"Filtered film: {film['navn']}, år: {film['år']}, rating: {film['rating']}")

def write_filmer_to_file(filmer, filename):
    with open(filename, 'w') as file:
        for film in filmer:
            navn, år, rating = film
            file.write(f"{navn} - {år} har rating {rating}\n")

filmer_liste = [
    ("Inception", 2010, 8.7),
    ("Inside out", 2015, 8.1),
    ("con air", 1997, 6.9)
]
write_filmer_to_file(filmer_liste, "filmer.txt")

def read_filmer_from_file(filename):
    with open(filename, 'r') as file:
        content = file.readlines()
        for line in content:
            print(line.strip())

read_filmer_from_file("filmer.txt")
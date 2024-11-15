class film:
    def __init__(self, title, year, score):
        self.title = title
        self.year = year
        self.score = score

    def info (self):
        return f"{self.title} was realised in {self.year} and has a score of {self.score}"

inception = film("Inception", 2010, 8.8)
the_marian = film("The Martian", 2015, 8.0)
joker = film("joker", 2019, 8.4)

print(inception.info())
print(the_marian.info())
print(joker.info())


import random

def print_random_nummer():
    nummer = random.randrange(0,100)
    print("********")
    print(f"***{nummer}***")
    print("********")

for _ in range(2):
    print_random_nummer()

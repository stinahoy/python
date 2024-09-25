import random

def dartspill():
    totalscore = 0
    for _ in range(3):
        score = random.randrange(0, 61)
        totalscore += score
    return totalscore

if __name__ == "__main__":
    finalscore = dartspill()
    print("{final_score}")

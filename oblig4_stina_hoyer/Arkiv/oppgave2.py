import random

full_deck = {
    "Two of clubs": 2, "Three of clubs": 3, "Four of clubs": 4, "Five of clubs": 5,
    "Six of clubs": 6, "Seven of clubs": 7, "Eight of clubs": 8, "Nine of clubs": 9,
    "Ten of clubs": 10, "Jack of clubs": 10, "Queen of clubs": 10, "King of clubs": 10,
    "Ace of clubs": 11, "Two of diamonds": 2, "Three of diamonds": 3, "Four of diamonds": 4,
    "Five of diamonds": 5, "Six of diamonds": 6, "Seven of diamonds": 7, "Eight of diamonds": 8,
    "Nine of diamonds": 9, "Ten of diamonds": 10, "Jack of diamonds": 10, "Queen of diamonds": 10,
    "King of diamonds": 10, "Ace of diamonds": 11, "Two of hearts": 2, "Three of hearts": 3,
    "Four of hearts": 4, "Five of hearts": 5, "Six of hearts": 6, "Seven of hearts": 7,
    "Eight of hearts": 8, "Nine of hearts": 9, "Ten of hearts": 10, "Jack of hearts": 10,
    "Queen of hearts": 10, "King of hearts": 10, "Ace of hearts": 11, "Two of spades": 2,
    "Three of spades": 3, "Four of spades": 4, "Five of spades": 5, "Six of spades": 6,
    "Seven of spades": 7, "Eight of spades": 8, "Nine of spades": 9, "Ten of spades": 10,
    "Jack of spades": 10, "Queen of spades": 10, "King of spades": 10, "Ace of spades": 11,
}

def get_ny_suffled_deck():
    deck = list(full_deck.keys())
    random.shuffle(deck)
    return deck

def get_card_verdi(card):
    return full_deck[card]

def kalkuler_hand_verdi(hand):
    hand_verdi = sum(get_card_verdi(card) for card in hand)
    aces = hand.count("Ace of clubs") + hand.count("Ace of diamonds") + hand.count("Ace of heart") + hand.count("Ace of spades")
    while hand_verdi > 21 and aces:
        hand_verdi -= 10
        aces -= 1
    return hand_verdi

def deal_opening_cards(deck):
    spiller_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    return spiller_hand, dealer_hand

def print_resultat(spiller_value, dealer_value, chips, bet):
    if dealer_value > 21:
        print("Dealer busts! You win!")
        return chips + bet
    elif spiller_value > dealer_value:
        print("You win!")
        return chips + bet
    else:
        print("Its a tie")
        return chips
    
def get_bet(chips):
    while True:
        try:
            bet = int(input(f"You have {chips} chips. Enter your bet: "))
            if 1 <= bet <= chips:
                return bet
            else:
                print("Invalid bet. Try again.")
        except ValueError:
            print("Please enter a valid number.")

def play_blackjack():
    chips = 7
    while chips > 0:
        deck = get_ny_suffled_deck()
        spiller_hand, dealer_hand = deal_opening_cards(deck)

        print(f"You have {spiller_hand}, total value: {kalkuler_hand_verdi(spiller_hand)}")
        print(f"Dealers visible card: {dealer_hand[0]}")

        bet = get_bet(chips)

        if kalkuler_hand_verdi(spiller_hand) == 21:
            print("Blackjack! You win!")
            chips += bet
            continue

        while True:
            choice = input("Choose: 1 - Hit, 2 - Stand: ")
            if choice == '1':
                spiller_hand.append(deck.pop())
                print(f"Your hand: {spiller_hand}, tottal value: {kalkuler_hand_verdi(spiller_hand)}")
                if kalkuler_hand_verdi(spiller_hand) > 21:
                    print("You bust! Dealer wins.")
                    chips -= bet
                    break
                elif choice == '2':
                    break

            dealer_value = kalkuler_hand_verdi(dealer_hand)
            while dealer_value < 17:
                dealer_hand.append(deck.pop())
                dealer_value = kalkuler_hand_verdi(dealer_hand)

            print(f"Dealers hand: {dealer_hand}, total value: {dealer_value}")
            chips = print_resultat(kalkuler_hand_verdi(spiller_hand), dealer_value, chips, bet)

            if chips <= 0:
                print("You have no chips left. Game over!")
                break
            else:
                print(f"You have {chips} chips left.")
            if input("Play another round?: ").lower() != 'y':
                break


play_blackjack()



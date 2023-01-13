#Blackjack
from art import logo
import random
import os
clear = lambda : os.system('cls')

def my_cards(cards):
    """Function to get first two user cards from cards list"""
    u_first_cards.append(random.choice(cards))
    u_first_cards.append(random.choice(cards))
    return u_first_cards

def computer_cards(cards):
    """Function to get first two computer cards from cards list"""
    c_first_cards.append(random.choice(cards))
    c_first_cards.append(random.choice(cards))
    return c_first_cards

def add_card(cards):
    """Function to add a card to user list of cards"""
    u_first_cards.append(random.choice(cards))
    return u_first_cards

def c_add_card(cards):
    """Function to add a card to computer list of cards"""
    c_first_cards.append(random.choice(cards))
    return c_first_cards

def grand_total(first_cards):
    return sum(first_cards)

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

# u_total = sum(u_first_cards)
# c_total = sum(c_first_cards)
# print(my_cards(cards))
# print(computer_cards(cards))
# print(add_card(cards))
should_continue = True
u_game = True
c_game = True
game_on=True

print("Lets play a game of Blackjack 🃏")
while should_continue == True:
    game = input("Type Y for yes and N for no : ").lower()
    if game == 'y':
        clear()
        print(logo)
        u_first_cards = []
        c_first_cards = []
        my_cards(cards)
        computer_cards(cards)
        u_total=grand_total(u_first_cards)
        c_total=grand_total(c_first_cards)
        
        print(f"Your Cards: {u_first_cards}, current score : {u_total}")
    
        print(f"Computer's first card: {c_first_cards[0]}")
        while game_on == True:
            if u_total == 21 and c_total == 21:
                print("Its was a Draw")
                game_on = False
            elif u_total < 21 and c_total == 21:
                print("You Lose. It was a black jack for Dealer")
                game_on = False
            elif u_total == 21 and c_total < 21:
                print("You win. It was a Black jack")
                game_on = False
            else:
                while u_game == True:
                    u_add_card = input("Type y to get another card, type n to pass: ").lower()
                    if u_add_card == 'y':
                        add_card(cards)
                        u_total=grand_total(u_first_cards)
                        print(f"Your hand : {u_first_cards}, score : {u_total}.")
                        if u_total > 21:
                            print(f"Your final hand : {u_first_cards}, score : {u_total}. Its a bust .You Lose")
                            u_game = False
                            game_on = False
                            break
                    elif u_add_card == 'n':
                        print(f"Your final hand : {u_first_cards}, score : {u_total}.")
                        u_game = False
                        while c_game == True:
                            if c_total < 17:
                                c_add_card(cards)
                                c_total=grand_total(c_first_cards)
                            else:
                                c_game = False
                        print(f"Computer Cards: {c_first_cards}, current score : {c_total}")
                        if c_total > 21:
                            print("Computer Bust. You win")
                            u_game = False
                            game_on = False
                            break
                    elif u_total < c_total:
                        print("You lose")
                        u_game = False
                        game_on = False
                    elif c_total < u_total:
                        print("You Win")
                        u_game = False
                        game_on = False
                    elif c_total == u_total:
                        print("Draw")
                        u_game = False
                        game_on = False
    else:
        print("Good choice! Program has bugs...🪲")
        should_continue = False
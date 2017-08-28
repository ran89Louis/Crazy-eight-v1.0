#-*- coding: utf-8 -*-
from cards import Card
import random

def computer_turn():
    global c_hand, deck, up_card, active_suit, blocked
    options = []
    for card in c_hand:
        if card.rank == '8':
            c_hand.remove(card)
            up_card = card
            print "  Computer played ", card.short_name,"and changed suit is", card.suit
            #suit totals: [diamonds, hearts, spades, clubs]

            suit_totals = [0, 0, 0, 0]
            for suit in range(1, 5):
                for card in c_hand:
                    if card.suit_id == suit:
                        suit_totals[suit-1] += 1
            long_suit = 0
            for i in range(4):
                if suit_totals[i] > long_suit:
                    long_suit = i
            if long_suit == 0:  active_suit = "Diamonds"
            if long_suit == 1:  active_suit = "Hearts"
            if long_suit == 2:  active_suit = "Spades"
            if long_suit == 3:  active_suit = "Clubs"
            break
        else:
            if card.suit == active_suit:
                options.append(card)
            elif card.rank == up_card.rank:
                options.append(card)

    if len(options) > 0:
        best_play = options[0]
        for card in options:
            if card.value > best_play.value:
                best_play = card
        c_hand.remove(best_play)
        up_card = best_play
        active_suit = up_card.suit
        print "  Computer played ", best_play.short_name

    else:
        if len(deck)> 0:
            next_card = random.choice(deck)
            c_hand.append(next_card)
            deck.remove(next_card)
            print "   Computer drew a card:", next_card
        else:
            print "Computer is blocked"
            blocked += 1
    print "Computer has %i cards left"  %(len(c_hand))


def player_turn():
    global deck, p_hand, blocked, up_card, active_suit
    print "What would you like to do? ",
    response = raw_input("Type a card name to play or 'Draw' to take a card: ")
    valid_play = False
    is_eight = False
    p_hand = []
    while not valid_play:
        selected_card = None
        while selected_card == None:
            if response.lower() == 'draw':
                valid_play = True
                if len(deck) > 0:
                    card = random.choice(deck)
                    p_hand.append(card)
                    deck.remove(card)
                    print "You drew", card.short_name
                else:
                    print "There are no cards left in the deck"
                    blocked += 1
                    break

            else:
                for card in p_hand:
                    if response.upper() == card.short_name:
                        selected_card = card
                        if selected_card.suit == active_suit:
                            valid_play = True
                            p_hand.remove(selected_card)
                            selected_card = up_card
                            print "  Player played ", selected_card.short_name
                        elif selected_card.rank == up_card.rank:
                            valid_play = True
                            p_hand.remove(selected_card)
                            selected_card = up_card
                            active_suit = selected_card.suit
                            print "  Player played ", selected_card.short_name
                        elif selected_card.rank == '8':
                            valid_play = True
                            is_eight = True
                            p_hand.remove(selected_card)
                            get_new_suit()
                            print"   Suit is", active_suit

                        

                    if selected_card == None:
                        response = raw_input("You don't have that card. Try again:")

                    if not valid_play:
                        response = raw_input("That's not a legal play. Try again: ")


                
                    

                
                    
                    

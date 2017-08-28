##Crazyeight main programming
#-*- coding: utf-8 -*-
import random
from cards import Card
import method 
#其实更好的方法是，import method ，然后通过method.XXX()去调用函数呢
p_hand = []
c_hand = []
deck = []
for suit_id in range(1, 5):
    for rank_id in range(1, 14):
        new_card = Card(suit_id, rank_id)
        if new_card.rank_id == 8:
            new_card.value = 50
        deck.append(new_card)
print "Crazy Eights"        
for card in range(0, 5):
    card = random.choice(deck)
    p_hand.append(card)
    deck.remove(card)        
print "\nYour hand:"
for card in p_hand:
    print card.short_name,
    
up_card = random.choice(deck)
deck.remove(up_card)
active_suit = up_card.suit   
print "  Up card: ", up_card.short_name
print "active_suit: ", active_suit

done = False
p_total = c_total = 0
while not done:
    game_done = False
    #init_()cards
    while not game_done:
        blocked = 0
        print blocked
        method.player_turn()
    
        if len(p_hand) == 0:
            game_done = True
            print
            print "You won !"
        if not game_done:
           method.computer_turn()
            
        if len(c_hand) == 0:
            game_done = True
            print
            print "Computer won! "
            #display the game score here
        c_points = 0
        for card in p_hand:
             c_points += card.value
        c_total += c_points
        print "Computer got %i points for your hand" % c_points
    if blocked >= 2:
        game_done = True
        print "Both player blocked, GAME OVER."
        player_points = 0
        for card in c_hand:
            p_points += card.value
        p_total += p_points
        c_points = 0
        for card in p_hand:
            c_point += card.value
        c_total += c_points
        print "You got %i points for computer's hand" % p_points
        print "Computer got %i points for your hand" % c_points


    play_again = raw_input("play again (Y/N)? ")
    if play_again.lower().startswith('y'):
        done = False
        print "\nSo far,you have %i points" % p_total
        print "and the computer has %i points.\n" % c_total
    else:
        done = True
print "\n Final Score:"
print "You: %i       Computer: %i" %(p_total, c_total)




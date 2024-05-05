# -*- coding: utf-8 -*-
"""
Created on Sun May  5 15:13:30 2024

@author: patel
"""

import random



def make_deck(num_cards, num_true):
    deck = []
    for i in range(num_true):
        deck.append(True)
    for i in range(num_cards-num_true):
        deck.append(False)
    random.shuffle(deck)
    return deck


def sim_round(self_total, other_total, deck):
    next_card = deck.pop()
    print(f'Next Card: {next_card}')
    trues = deck.count(True)
    falses = deck.count(False)
    if trues > falses:
        give_other = True
    elif trues == falses:
        give_other = random.choice([True, False])
    else:
        give_other = False
    print(f'Give Other: {give_other}')
    if give_other and next_card:
        # give to other and card is true
        other_total = other_total - 1
    elif not give_other and next_card:
        # give to self and card is true
        self_total = self_total - 1
    else:
        # give to self and card is false
        # give to other and card is false
        pass
    return self_total, other_total, deck


def sim_game(player_total, dealer_total, deck):
    
    round_count = 1
    
    while player_total != 0 and dealer_total != 0: 
        print(f'Round: {round_count}')
        if round_count % 2 == 1:
            player_total, dealer_total, deck = sim_round(player_total,
                                                         dealer_total, 
                                                         deck)
        else:
            dealer_total, player_total, deck = sim_round(dealer_total, 
                                                         player_total,
                                                         deck)
        print(f'Player: {player_total}; Dealer: {dealer_total}')
        if len(deck) == 0:
            deck = get_rand_deck()
        round_count = round_count + 1
    
    if player_total > dealer_total:
        winner = True
    else:
        winner = False
        
    return winner


def get_rand_deck():
    num_card_options = [2, 3, 4, 5, 6, 7, 8]
    num_cards = random.choice(num_card_options)   
    num_true_options = list(range(1, num_cards))
    num_true = random.choice(num_true_options)
    deck = make_deck(num_cards, num_true)
    return deck


if __name__ == '__main__':
    
    deck = [True, False, True, False]
    outcome = sim_game(2, 2, deck)
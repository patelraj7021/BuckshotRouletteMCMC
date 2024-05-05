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


def sim_game(player_total, dealer_total, num_cards, num_true):
    
    deck = make_deck(num_cards, num_true)
    
    while player_total != 0 or dealer_total != 0:
        # do rounds
    
    if player_total > dealer_total:
        winner = True
    else:
        winner = False
    return


def get_rand_deck():
    num_card_options = [2, 3, 4, 5, 6, 7, 8]
    num_cards = random.choice(num_card_options)   
    num_true_options = list(range(1, num_cards))
    num_true = random.choice(num_true_options)
    deck = make_deck(num_cards, num_true)


if name == '__main__':
    
    
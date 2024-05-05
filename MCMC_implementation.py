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



print(make_deck(4, 1))
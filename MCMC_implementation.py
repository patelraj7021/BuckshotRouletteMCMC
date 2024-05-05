# -*- coding: utf-8 -*-
"""
Created on Sun May  5 15:13:30 2024

@author: patel
"""

import random
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
plt.rcParams.update({'font.size': 18})



def make_deck(num_cards, num_true):
    deck = []
    for i in range(num_true):
        deck.append(True)
    for i in range(num_cards-num_true):
        deck.append(False)
    random.shuffle(deck)
    return deck


def get_rand_deck():
    num_card_options = [2, 3, 4, 5, 6, 7, 8]
    num_cards = random.choice(num_card_options)   
    num_true_options = list(range(1, min(num_cards, 4)))
    num_true = random.choice(num_true_options)
    deck = make_deck(num_cards, num_true)
    return deck


def sim_round(self_total, other_total, deck, player_active, force_fifties):
    trues = deck.count(True)
    falses = deck.count(False)
    next_card = deck.pop()
    
    # logic for action based on knowledge of deck
    if trues > falses:
        give_other = True
    elif trues == falses:
        # for simulation purposes
        # see the outcome of player always forcing 50-50s
        if force_fifties is not None and player_active:
            give_other = force_fifties            
        else:
            give_other = random.choice([True, False])
    else:
        give_other = False
    
    # logic for action outcomes
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
    return self_total, other_total, give_other, next_card, deck


def sim_game(player_total, dealer_total, deck, 
             force_fifties=None):
    
    # starts as player turn
    player_active = True
    
    while player_total != 0 and dealer_total != 0: 
        if player_active:
            player_total, dealer_total, give_other, card, deck = sim_round(
                                                         player_total,
                                                         dealer_total, 
                                                         deck,
                                                         player_active,
                                                         force_fifties)
        else:
            dealer_total, player_total, give_other, card, deck = sim_round(
                                                         dealer_total, 
                                                         player_total,
                                                         deck,
                                                         player_active,
                                                         force_fifties)
        if len(deck) == 0:
            deck = get_rand_deck()       
        if not card and player_active and not give_other:
            # if card was false and it was player turn and player dealt to self
            # stay player turn
            player_active = True
        else:
            # switch 
            player_active = not player_active
        # forced action will only happen for first action
        # change to None after first round is done
    
    if player_total > dealer_total:
        winner = True
    else:
        winner = False
        
    return winner


def run_sim(sim_num, fifties_option, 
            num_cards=4, num_trues=2, player_total=2, dealer_total=2):
    outcomes = []
    perc_wins = []   
    for i in range(sim_num):
        deck = make_deck(num_cards, num_trues)
        outcome = sim_game(player_total, dealer_total, deck, 
                           force_fifties=fifties_option)
        outcomes.append(outcome)        
        perc_win = 100* outcomes.count(True) / len(outcomes)
        perc_wins.append(perc_win)
    return perc_wins


if __name__ == '__main__':
    
    sim_num = 50000
    force_fifties = [None, True, False]
    labels = ['50/50', 'Give', 'Keep']
    
    fig, ax = plt.subplots(1,figsize=(1.33*9, 9))
    fig.subplots_adjust(right=0.95, top=0.95)
    
    for i, force_option in enumerate(force_fifties):
        option_perc_wins = run_sim(sim_num, force_option)
        ax.plot(range(1, sim_num+1), option_perc_wins, 
                label=labels[i])
       
    ax.set_xlabel('Simulation Number', fontsize=22)
    ax.set_ylabel('Win Percentage [%]', fontsize=22)
    ax.tick_params(bottom=True, left=True, right=True, top=True)
    ax.xaxis.set_minor_locator(AutoMinorLocator(4))
    ax.yaxis.set_minor_locator(AutoMinorLocator(4))
    ax.yaxis.set_ticks_position('both')
    ax.xaxis.set_ticks_position('both')
    ax.legend(loc='upper right')
    ax.set_ylim(34, 69)
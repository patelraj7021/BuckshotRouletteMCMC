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
    num_true_options = list(range(1, num_cards))
    num_true = random.choice(num_true_options)
    deck = make_deck(num_cards, num_true)
    return deck


def sim_round(self_total, other_total, deck, force_first, force_fifties):
    next_card = deck.pop()
    trues = deck.count(True)
    falses = deck.count(False)
    # logic for action based on knowledge of deck
    if trues > falses:
        give_other = True
    elif trues == falses:
        if force_fifties is not None:
            give_other = random.choice([True, False])
        else:
            give_other = force_fifties
    else:
        give_other = False
    # for simulation purposes, need to see outcome of a forced first action
    if force_first is not None:
        give_other = force_first
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


def sim_game(player_total, dealer_total, deck, 
             force_first=None, force_fifties=None):
    
    round_count = 1
    
    while player_total != 0 and dealer_total != 0: 
        if round_count % 2 == 1:
            player_total, dealer_total, deck = sim_round(player_total,
                                                         dealer_total, 
                                                         deck,
                                                         force_first,
                                                         force_fifties)
        else:
            dealer_total, player_total, deck = sim_round(dealer_total, 
                                                         player_total,
                                                         deck,
                                                         force_first,
                                                         force_fifties)
        if len(deck) == 0:
            deck = get_rand_deck()
        round_count = round_count + 1
        # forced action will only happen for first action
        # change to None after first round is done
        if round_count == 2:
            force_first = None
    
    if player_total > dealer_total:
        winner = True
    else:
        winner = False
        
    return winner


def run_sim(sim_num, fifties_option):
    outcomes = []
    perc_wins = []   
    for i in range(sim_num):
        deck = make_deck(4, 2)
        outcome = sim_game(2, 2, deck, force_fifties=fifties_option)
        outcomes.append(outcome)        
        perc_win = 100* outcomes.count(True) / len(outcomes)
        perc_wins.append(perc_win)
    return perc_wins


if __name__ == '__main__':
    
    sim_num = 10000
    force_fifties = [None, True, False]
    
    fig, ax = plt.subplots(1,figsize=(1.33*9, 9))
    fig.subplots_adjust(right=0.95, top=0.95)
    
    for force_option in force_fifties:
        option_perc_wins = run_sim(sim_num, force_option)
        ax.plot(range(1, sim_num+1), option_perc_wins, label=str(force_option))
       
    ax.set_xlabel('Simulation Number', fontsize=22)
    ax.set_ylabel('Win Percentage [%]', fontsize=22)
    ax.tick_params(bottom=True, left=True, right=True, top=True)
    ax.xaxis.set_minor_locator(AutoMinorLocator(4))
    ax.yaxis.set_minor_locator(AutoMinorLocator(4))
    ax.yaxis.set_ticks_position('both')
    ax.xaxis.set_ticks_position('both')
    ax.legend(loc='upper right')
### Markov Chain Monte Carlo Simulation for Buckshot Roulette

This project provides MCMC simulation code for an optimal strategy for the popular game [Buckshot Roulette](https://store.steampowered.com/app/2835570/Buckshot_Roulette/). 
The base rules of the game are presented below, modified in their presentation to be a card game:
* Set up
  * There are two actors in the game, a player and a dealer, and both start with a balance of $200. 
  * From a standard deck of cards, 2 red and 2 black cards are taken, shuffled, and placed facedown in a pile.
* Player's goal
  * Reduce the dealer's total to $0.
  * If the player's total reaches $0, they lose.
* Turn gameplay (player has first turn)
  * Without looking, the active actor can deal one card from the facedown pile to either themselves or their opponent.
  * The card is revealed.
  * If it is red:
    * Whoever the card was dealt to loses $100.
    * It is the other actor's turn.
  * If it is black:
    * No changes to either balance.
    * If it was the player's turn, they can take another turn.
    * If it was the dealer's turn, the turn goes to the player.
* Notes
  * If the facedown pile runs out of cards, a new pile is made such that:
    * The total number of cards is between 2 and 8 (inclusive).
    * The total number of red cards is between 1 and 4 (inclusive).
    * There is at least 1 black card.
  * If there are an equal number of red and black cards in the pile, the dealer will randomly decide whether to give or keep a card on their turn.
   
#### Hypothesis
The best action to take when the number of red vs. black cards is unbalanced in the pile is unambiguous.
If there are more red cards in the pile, the actor should deal a card to their opponent, and vice versa.
However, the best action to take when the pile has an equal number of red and black cards is less obvious.
There is a common belief in the game's community that, as the player, giving the card to the dealer maximizes your likelihood of winning the game.
This simulation tests this belief by comparing win percentages for the player when they use a strategy on 50/50 scenarios of 
(a) always giving the dealer a card,
(b) always keeping a card, or
(c) randomly choosing (50/50 chance either way).

#### Results
The win percentage as a function of simulation runs is shown in this repository in results.png.
There is a clear advantage when using the ''always give'' strategy, confirming the hypothesis of the game's community.
Surprisingly, the ''always keep'' strategy is less beneficial than even the ''random choice'' strategy.

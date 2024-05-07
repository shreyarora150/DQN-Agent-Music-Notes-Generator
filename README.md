### run DQNMusic.ipynb to generate music 

INFO 557 Artificial Inteliigence final project 

A dqn agent to produce musical sequnece of notes. 
Created a music environment with current state holding previously 4 played notes in memory and action space consisting of 12 notes from C to B in order.

Reward function promotes notes that match a paricular musical scale. Similarity scores are caluctated for each major and minor scale and the one with highest score is chosen as final scale.

The Agent consists of a neural network with two hidden states of 24 units each and last layer of 12 units. It is trained for 50 episodes.



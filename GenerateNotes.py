from MusicEnv import MusicEnvironment
from DQNAgent import DQNAgent
import numpy as np
import pygame


def play_piano_note():

    """
    Play piano note.
    """
    env = MusicEnvironment()
    state_size = 4
    action_size = len(env.action_space)
    agent = DQNAgent(state_size, action_size)

    # Train the agent for 500 steps
    batch_size = 32
    episodes = 50
    for e in range(episodes):
        state = env.reset()
        if len(agent.memory) > batch_size:
            agent.replay(batch_size)
        action = agent.act(state)
        next_state, reward = env.step(action)
        state = state[0:agent.state_size]
        agent.remember(state, action, reward, next_state)
        state = next_state
        print("episode: {}/{}, score: {}".format(e, episodes, reward))
        
    state = env.reset()
    if not state:  # Check if state is empty
        state = [0] * state_size  # Set state to a default value
    else:
        state = np.reshape(state, [1, state_size])

    output = []
    for i in range(30):
        action = agent.act(state)
        next_state, reward = env.step(action)
        next_state = np.reshape(next_state, [1, state_size])
        state = next_state
        output.append(env.action_space[action])

    action_space_dict = {0.0:'C4', 1.0:'C4#', 2.0:'D4', 3.0:'D4#', 4.0:'E4', 5.0:'F4', 6.0:'F4#', 7.0:'G4', 8.0:'G4#', 9.0:'A4', 10.0:'A4#', 11.0:'B4'}
    output = [action_space_dict[index] for index in output]
    print("Generated output:", output)

    pygame.mixer.init()
    pygame.init()
    for note in output:
    
        pygame.mixer.music.load(f"piano_notes/{note}.wav")
        pygame.mixer.music.play()
        pygame.time.wait(500) 
        
        pygame.mixer.music.load(f"misc/drum_kick.wav")
        pygame.mixer.music.play()
        pygame.time.wait(500) 
        
        pygame.mixer.music.load(f"piano_notes/{note}.wav")
        pygame.mixer.music.play()
        pygame.time.wait(500)   
        
        pygame.mixer.music.load(f"misc/drum_snare.wav")
        pygame.mixer.music.play()
        pygame.time.wait(500)  
    # Quit pygame
    pygame.quit()
       
def stop():
    pygame.quit()
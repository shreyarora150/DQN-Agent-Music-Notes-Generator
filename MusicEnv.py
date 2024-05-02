import random

class MusicEnvironment:
    def __init__(self):
        self.state = [0.0,0.0,1.0,2.0]
        self.action_space = [0.0,  1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0]
        #self.action_space = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

    def reset(self):
        self.state = [0.0,0.0,1.0,2.0]
        return self.state

    def step(self, action_index):
        if action_index < 0 or action_index >= len(self.action_space):
            raise ValueError("Invalid action index")
        
        note = self.action_space[action_index]
        self.state.append(note)
        self.state = self.state[1:5]
        
        # Calculate reward
        reward = self.calculate_reward()
        return self.state, reward

    def calculate_reward(self):
        major_patterns_scores =[]
        minor_patterns_scores =[]
        for note in self.state:
            major_pattern = [note+2,note+4,note+5,note+7,note+9,note+11,note+12] 
            major_pattern = [x if x<11 else x-11 for x in  major_pattern]

            minor_pattern = [note+2,note+3,note+5,note+7,note+8,note+10,note+12]
            minor_pattern = [x if x<11 else x-11 for x in  minor_pattern]

            major_patterns_scores.append(sum(1 if note in major_pattern else 0 for note in self.state))
            minor_patterns_scores.append(sum(1 if note in minor_pattern else 0 for note in self.state))

        return max([max(minor_patterns_scores),max(major_patterns_scores)]) # Random reward for demonstration purposes

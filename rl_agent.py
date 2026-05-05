import numpy as np
import random

ACTIONS = [
    "Breathing Exercise",
    "Journaling Prompt",
    "Listen to Music",
    "Take a Walk",
    "Gratitude Practice",
    "Cold Water Splash",
    "Muscle Relaxation",
    "Positive Affirmation"
]

class RLAgent:
    def __init__(self):
        self.q_table = np.zeros((54, len(ACTIONS)))
        self.alpha = 0.1   # learning rate
        self.gamma = 0.9   # discount factor
        self.epsilon = 0.2 # exploration rate

    def choose_action(self, state):
        if random.random() < self.epsilon:
            return random.randint(0, len(ACTIONS) - 1)
        return np.argmax(self.q_table[state])

    def update(self, state, action, reward, next_state):
        best_next = np.max(self.q_table[next_state])

        self.q_table[state][action] += self.alpha * (
            reward + self.gamma * best_next - self.q_table[state][action]
        )
        
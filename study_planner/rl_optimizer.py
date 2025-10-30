# rl_optimizer.py
import numpy as np
import json
import os
from typing import Dict, List, Tuple

class QLearningOptimizer:
    def __init__(self, subjects: List[str], state_size: int = 10, action_size: int = 5, lr: float = 0.1, gamma: float = 0.9, epsilon: float = 0.1):
        """
        Initialize Q-Learning optimizer for study planning
        :param subjects: List of subjects in the study plan
        :param state_size: Size of the state space
        :param action_size: Size of the action space
        :param lr: Learning rate
        :param gamma: Discount factor
        :param epsilon: Exploration rate
        """
        self.subjects = subjects
        self.state_size = state_size
        self.action_size = action_size
        self.lr = lr
        self.gamma = gamma
        self.epsilon = epsilon
        self.q_table = np.zeros((state_size, action_size))
        
        # Subject to index mapping for actions
        self.subject_to_idx = {subject: idx for idx, subject in enumerate(subjects)}
        self.idx_to_subject = {idx: subject for subject, idx in self.subject_to_idx.items()}

    def get_action(self, state: int) -> int:
        """
        Choose an action based on current state using epsilon-greedy policy
        :param state: Current state
        :return: Action index
        """
        if np.random.random() < self.epsilon:
            # Explore: random action
            return np.random.choice(self.action_size)
        else:
            # Exploit: best known action
            return np.argmax(self.q_table[state])

    def update(self, state: int, action: int, reward: float, next_state: int):
        """
        Update Q-table based on experience
        :param state: Current state
        :param action: Action taken
        :param reward: Reward received
        :param next_state: Next state
        """
        predict = self.q_table[state, action]
        target = reward + self.gamma * np.max(self.q_table[next_state])
        self.q_table[state, action] += self.lr * (target - predict)

    def get_subject_from_action(self, action_idx: int) -> str:
        """
        Convert action index to subject name
        :param action_idx: Index of the action
        :return: Subject name
        """
        return self.idx_to_subject.get(action_idx, self.subjects[0])

    def save(self, path: str):
        """
        Save the Q-table to a file
        :param path: Path to save the file
        """
        # Prepare data dictionary with all necessary information
        data = {
            'q_table': self.q_table.tolist(),
            'state_size': self.state_size,
            'action_size': self.action_size,
            'lr': self.lr,
            'gamma': self.gamma,
            'epsilon': self.epsilon,
            'subjects': self.subjects,
            'subject_to_idx': self.subject_to_idx,
            'idx_to_subject': self.idx_to_subject
        }
        
        with open(path, 'w') as f:
            json.dump(data, f)

    def load(self, path: str):
        """
        Load the Q-table from a file
        :param path: Path to load the file from
        """
        if os.path.exists(path):
            with open(path, 'r') as f:
                data = json.load(f)
                
            self.q_table = np.array(data['q_table'])
            self.state_size = data['state_size']
            self.action_size = data['action_size']
            self.lr = data['lr']
            self.gamma = data['gamma']
            self.epsilon = data['epsilon']
            self.subjects = data['subjects']
            self.subject_to_idx = data['subject_to_idx']
            self.idx_to_subject = data['idx_to_subject']

    def get_optimized_schedule(self, schedule: Dict[str, List[str]], feedback: Dict[str, str]) -> Dict[str, List[str]]:
        """
        Optimize the schedule based on user feedback using Q-learning
        :param schedule: Original schedule
        :param feedback: User feedback about the schedule
        :return: Optimized schedule
        """
        # Convert feedback to rewards
        reward_map = {
            'excellent': 1.0,
            'good': 0.5,
            'fair': 0.0,
            'poor': -0.5,
            'very_poor': -1.0
        }
        
        optimized_schedule = {}
        
        for day, subjects in schedule.items():
            day_schedule = []
            for idx, subject in enumerate(subjects):
                # Create a state based on the position in the schedule
                state = (idx + hash(day)) % self.state_size
                
                # Get action from Q-table
                action = self.get_action(state)
                
                # Apply feedback to update Q-table if available for this subject
                if subject in feedback:
                    next_state = (idx + 1 + hash(day)) % self.state_size
                    reward = reward_map.get(feedback[subject], 0.0)
                    self.update(state, action, reward, next_state)
                
                # Choose subject based on action
                new_subject = self.get_subject_from_action(action)
                day_schedule.append(new_subject)
            
            optimized_schedule[day] = day_schedule
        
        return optimized_schedule


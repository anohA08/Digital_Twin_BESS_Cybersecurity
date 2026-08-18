from collections import deque
import random


class ReplayAttack:

    def __init__(self,
                 probability=0.15,
                 replay_length=5):

        self.probability = probability
        self.replay_length = replay_length

        self.buffer = deque(maxlen=replay_length)

    def attack(self, measurement):

        # Always record the newest measurement
        self.buffer.append(measurement)

        attack_active = random.random() < self.probability

        if attack_active and len(self.buffer) == self.replay_length:

            replayed_value = self.buffer[0]

            return replayed_value, True

        return measurement, False
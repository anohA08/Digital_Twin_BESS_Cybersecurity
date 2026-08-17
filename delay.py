from collections import deque


class DelayBuffer:

    def __init__(self, delay_steps=5):
        """
        delay_steps:
        Number of simulation steps to delay the measurements.
        """

        self.delay_steps = delay_steps
        self.buffer = deque()

    def update(self, measurement):
        """
        Store a new measurement and return a delayed measurement.
        """

        self.buffer.append(measurement)

        if len(self.buffer) <= self.delay_steps:
            return measurement

        return self.buffer.popleft()
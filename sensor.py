import random


class Sensor:

    def __init__(self, noise_std=0.5):
        """
        noise_std = standard deviation of measurement noise (in % SOC)
        """
        self.noise_std = noise_std

    def measure_soc(self, true_soc):
        """
        Return a noisy SOC measurement.
        """
        noise = random.gauss(0, self.noise_std)
        return true_soc + noise
import random


class SensorSpoofingAttack:
    """
    Simulates a sensor spoofing attack.
    """

    def __init__(self, attack_probability=0.2, spoof_amount=20):
        self.attack_probability = attack_probability
        self.spoof_amount = spoof_amount

    def attack(self, measured_soc):
        """
        Modify the measured SOC with a certain probability.
        """

        if random.random() < self.attack_probability:

            attacked_soc = measured_soc + self.spoof_amount

            attacked_soc = max(0, min(100, attacked_soc))

            return attacked_soc, True

        return measured_soc, False
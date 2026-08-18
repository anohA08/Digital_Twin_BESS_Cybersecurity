import pandas as pd

import config
from battery import Battery
from sensor import Sensor
from delay import DelayBuffer
from attack import SensorSpoofingAttack
from detector import AttackDetector
from replay_attack import ReplayAttack


class Simulation:

    def __init__(self, battery,digital_twin,data):
        self.battery = battery
        self.digital_twin = digital_twin
        self.data = data
        self.results = []
        self.sensor =Sensor()
        self.delay = DelayBuffer(delay_steps=config.DELAY_STEPS)
        self.attacker = SensorSpoofingAttack(attack_probability=0.20,
    spoof_amount=20)
        self.detector = AttackDetector(threshold=15)
        self.replay_attack = ReplayAttack(
    probability=0.15,
    replay_length=5
)

    def run(self):
        for _, row in self.data.iterrows():
            hour = row["Hour"]
            solar = row["Solar"]
            demand = row["Demand"]

            net_power = solar - demand

            if net_power > 0:
                charge_power = min(net_power, config.MAX_CHARGE_POWER)
                self.battery.charge(charge_power, config.TIME_STEP)
                battery_power = charge_power

            elif net_power < 0:
                discharge_power = min(
                    abs(net_power), config.MAX_DISCHARGE_POWER
                )
                self.battery.discharge(discharge_power, config.TIME_STEP)
                battery_power = -discharge_power

            else:
                battery_power = 0

            #update the digital twin and calculate the synchronization error

            true_soc = self.battery.get_soc()

            measured_soc = self.sensor.measure_soc(true_soc)

            spoofed_soc, spoof_attack = self.attacker.attack(measured_soc)

            replayed_soc, replay_attack = self.replay_attack.attack(spoofed_soc)

            delayed_soc = self.delay.update(replayed_soc)

            self.digital_twin.update(delayed_soc)

            sync_error = self.digital_twin.calculate_error(self.battery)

            
            self.detector.detect(sync_error)

            attack_detected = self.detector.attack_detected

            

            self.results.append(
                {
                    "Hour": hour,
                    "Solar": solar,
                    "Demand": demand,
                    "Net Power": net_power,
                    "Battery Power": battery_power,
                    "Energy": self.battery.energy,
                    "SOC": self.battery.get_soc(),
                    "Sync_Error": sync_error,
                    "Delay Steps": self.delay.delay_steps,
                    "Attack": spoof_attack,
                    "Attack_Detected": attack_detected,
                    "Spoofed_SOC": spoofed_soc,
                    "Replay Attack": replay_attack,
                    "Replay_SOC": replayed_soc,
                }
            )

        return pd.DataFrame(self.results)